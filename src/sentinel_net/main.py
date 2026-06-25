from fastapi import FastAPI

app = FastAPI(title="Sentinel-Net")

@app.get("/")
async def root():
    return {"status": "ok", "service": "Sentinel-Net"}

@app.get("/health")
async def health():
    return {"status": "healthy"}
