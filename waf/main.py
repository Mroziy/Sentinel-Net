import re
import httpx
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, Response
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("SentinelWAF")

app = FastAPI(title="Sentinel-Net WAF")

# Target backend server (the app we are protecting)
TARGET_BACKEND = "http://localhost:8001"

# Regex rules for common attacks (SQLi, XSS, Path Traversal)
WAF_RULES = {
    "SQL Injection": re.compile(r"(\b(union\s+select|drop\s+table|insert\s+into|delete\s+from|exec\s+xp_)\b|('|\"|;|--|\bOR\b\s+\d+=\d+)", re.IGNORECASE),
    "Cross-Site Scripting (XSS)": re.compile(r"(<script|javascript:|on\w+\s*=|alert\s*\()", re.IGNORECASE),
    "Path Traversal": re.compile(r"(\.\./|\.\.\\|%2e%2e%2f|%2e%2e/)", re.IGNORECASE)
}

async def inspect_payload(payload: str, rule_name: str, pattern: re.Pattern) -> bool:
    if pattern.search(payload):
        logger.warning(f"[BLOCKED] {rule_name} detected in payload: {payload[:50]}...")
        return True
    return False

@app.middleware("http")
async def waf_middleware(request: Request, call_next):
    # 1. Inspect Query Parameters
    query_params = str(request.query_params)
    for rule_name, pattern in WAF_RULES.items():
        if await inspect_payload(query_params, rule_name, pattern):
            return JSONResponse(status_code=403, content={"error": f"Access Denied: {rule_name} detected by Sentinel-Net"})

    # 2. Inspect Request Body (if applicable)
    if request.method in ["POST", "PUT", "PATCH"]:
        body = await request.body()
        body_str = body.decode('utf-8', errors='ignore')
        for rule_name, pattern in WAF_RULES.items():
            if await inspect_payload(body_str, rule_name, pattern):
                return JSONResponse(status_code=403, content={"error": f"Access Denied: {rule_name} detected by Sentinel-Net"})

    # 3. If clean, forward to backend (Reverse Proxy behavior)
    try:
        async with httpx.AsyncClient() as client:
            # Forward the request to the protected backend
            backend_url = f"{TARGET_BACKEND}{request.url.path}"
            resp = await client.request(
                method=request.method,
                url=backend_url,
                params=request.query_params,
                content=body if request.method in ["POST", "PUT", "PATCH"] else None,
                headers=dict(request.headers)
            )
            
            # Return the backend's response to the user
            return Response(
                content=resp.content,
                status_code=resp.status_code,
                headers=dict(resp.headers)
            )
    except httpx.ConnectError:
        return JSONResponse(status_code=502, content={"error": "Backend server unreachable"})
