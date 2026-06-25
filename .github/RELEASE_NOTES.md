# Release Notes — Sentinel-Net v0.1.0

## 🛡️ Sentinel-Net v0.1.0 — Initial Public Release

**Released:** June 25, 2026

First public release of Project Sentinel-Net — an open-source, AI-powered Web Application Firewall and Network Anomaly Detector for at-risk organizations, journalists, and NGOs.

---

## ✨ What's Included

### 🔒 Regex-Based Reverse Proxy WAF
- Blocks OWASP Top 10 attacks: SQL Injection, Cross-Site Scripting (XSS), Path Traversal, and more
- Low-latency request filtering at the network edge
- Customizable rule sets for different threat profiles
- Full request/response logging for audit trails

### 🤖 AI-Powered Anomaly Detection
- **Isolation Forest** unsupervised learning model
- Detects zero-day attacks without labeled training data
- Establishes baseline of normal network behavior
- Identifies DDoS spikes, port scans, and abnormal traffic patterns
- No cloud dependency — runs locally

### 🐳 Docker Deployment
- Complete Docker Compose setup for production deployment
- Self-hosted on any Linux server (no cloud vendor lock-in)
- Minimal dependencies: Python 3.8+, Docker, scikit-learn
- MIT Licensed — free and open-source

---

## 📋 Key Features

✅ **Digital Sovereignty** — Data never leaves your infrastructure  
✅ **Cost-Effective** — Free alternative to $10K–$50K/year commercial WAFs  
✅ **No Cloud Required** — Fully self-hosted and air-gappable  
✅ **Lightweight** — Low CPU/memory footprint  
✅ **Real-Time Protection** — Blocks threats before they reach your app  
✅ **Audit Ready** — Comprehensive logging for compliance  

---

## 🚀 Quick Start

### Deploy via Docker
```bash
cd infrastructure
docker-compose up --build
```

WAF listens on `http://localhost:8000`

### Run AI Detector
```bash
pip install scikit-learn numpy joblib
python ml/anomaly_detector.py
```

---

## 📖 Documentation

- **[README.md](https://github.com/Mroziy/Sentinel-Net/blob/main/README.md)** — Overview & architecture
- **[CONTRIBUTING.md](https://github.com/Mroziy/Sentinel-Net/blob/main/CONTRIBUTING.md)** — How to contribute code & report bugs
- **[SECURITY.md](https://github.com/Mroziy/Sentinel-Net/blob/main/SECURITY.md)** — Responsible vulnerability disclosure

---

## 🌍 Who This Is For

- 🛡️ **Digital Rights Defenders** — Protect your infrastructure from state-sponsored surveillance
- 📰 **Independent Journalists & Media** — Keep your publishing platform secure
- 🤝 **NGOs & Activism Groups** — Enterprise-grade security on a nonprofit budget
- 🌍 **Organizations in Africa (ECOWAS)** — Built with West African context in mind

---

## ⚠️ Known Limitations

1. **Regex-based WAF** is a first-line defense; sophisticated obfuscated attacks may bypass it
2. **Isolation Forest** requires 24–48 hours of baseline training; early false-positive rates may be high
3. Deployment security is user's responsibility (follow [SECURITY.md](SECURITY.md) best practices)

---

## 🔐 Security

For responsible disclosure of vulnerabilities, see **[SECURITY.md](https://github.com/Mroziy/Sentinel-Net/blob/main/SECURITY.md)**.

**Do NOT** open public GitHub issues for security vulnerabilities.

---

## 📝 License

MIT License — completely free and open-source for all uses.

---

## 🙏 Thanks

Built with ❤️ for digital rights defenders, journalists, and NGOs across Africa.

**Questions?** Open a [Discussion](https://github.com/Mroziy/Sentinel-Net/discussions) or email the maintainer.
