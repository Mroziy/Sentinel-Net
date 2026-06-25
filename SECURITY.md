# Security Policy

## Reporting Vulnerabilities

Sentinel-Net is a **security-critical tool** used by at-risk organizations, journalists, and NGOs across Africa. If you discover a security vulnerability, please report it **responsibly and privately**.

### ⚠️ DO NOT
- Open a public GitHub issue
- Post on social media
- Disclose details in public forums
- Share with third parties without permission

### ✅ DO
**Email the maintainer directly:**
```
To: [maintainer email - add your email]
Subject: SECURITY: [Brief vulnerability description]
```

**Include:**
1. Vulnerability type (e.g., SQL injection, authentication bypass, DoS)
2. Affected component (WAF, ML detector, Docker config, etc.)
3. Steps to reproduce
4. Potential impact (data breach, service disruption, etc.)
5. Suggested fix (if available)
6. Your contact information

---

## Response Timeline

We commit to:
- **Acknowledgment:** Within 48 hours
- **Investigation:** Within 1 week
- **Fix & patch:** Within 2 weeks (for critical issues)
- **Public disclosure:** After patch release + 30 days for user updates

---

## Scope

### In Scope (We'll investigate)
- Authentication/authorization bypasses
- Injection attacks (SQLi, command injection, etc.)
- Cryptographic weaknesses
- Denial of service (network, resource exhaustion)
- Information disclosure (logs, configs, credentials)
- Privilege escalation
- Remote code execution

### Out of Scope (Not security issues)
- Theoretical vulnerabilities without proof-of-concept
- Social engineering or phishing
- DDoS attacks on the repository itself
- Missing security headers (we're not a web service)
- Dependency vulnerabilities already patched in `requirements.txt`

---

## Security Best Practices for Deployment

If you deploy Sentinel-Net, follow these guidelines:

### 1. Network Security
- ✅ Run Sentinel-Net behind a firewall
- ✅ Use HTTPS/TLS for all traffic
- ✅ Restrict admin dashboard access to trusted IPs
- ❌ Don't expose admin ports to the public internet

### 2. Container Security
- ✅ Keep Docker and container images updated
- ✅ Run containers with minimal privileges (non-root user)
- ✅ Mount `/logs` on encrypted volumes
- ✅ Use network policies to isolate containers
- ❌ Don't share Docker images with sensitive logs

### 3. Configuration
- ✅ Change default passwords and API keys
- ✅ Use environment variables for secrets (not hardcoded)
- ✅ Rotate API keys regularly
- ✅ Review WAF rules periodically
- ❌ Don't expose `docker-compose.yml` with credentials

### 4. Monitoring & Logging
- ✅ Enable audit logging for all WAF decisions
- ✅ Monitor ML detector alerts in real-time
- ✅ Store logs on secure, isolated storage
- ✅ Set up alerts for suspicious activity
- ❌ Don't log sensitive user data (passwords, tokens)

### 5. Updates
- ✅ Subscribe to security updates (watch this repo)
- ✅ Test patches in a staging environment first
- ✅ Apply patches within 30 days of release
- ❌ Don't run outdated versions in production

---

## Known Limitations

Sentinel-Net is designed for **edge defense**, not a complete security solution. Be aware of:

1. **Regex-based WAF** cannot detect sophisticated, obfuscated attacks
   - Consider it a first line of defense
   - Combine with IDS/IPS for deeper protection

2. **Isolation Forest** requires baseline training
   - First 24–48 hours may have high false-positive rates
   - Tune thresholds for your environment

3. **Deployment responsibility**
   - Misconfigured Docker deployments can expose logs or configs
   - Always follow security best practices above

---

## Supported Versions

We provide security patches for:
- ✅ Latest release
- ✅ Previous major version (for 6 months)
- ❌ Older versions (end-of-life)

---

## Security Advisories

All security vulnerabilities and fixes will be published as **GitHub Security Advisories** after patches are released.

Subscribe to updates:
1. Click **Watch** → **Custom** → **Security alerts**
2. Join our [Discussions](https://github.com/Mroziy/Sentinel-Net/discussions)

---

## Contact

**Security Maintainer:**
- Email: [Add your security contact email]
- PGP Key: [Optional - add if available]

---

Thank you for helping keep Sentinel-Net secure for at-risk communities. 🛡️
