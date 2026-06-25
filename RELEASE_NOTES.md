# Release Notes — v0.1.0

**Release Date:** June 25, 2026  
**Status:** Initial Release (Alpha)

---

## 🎉 Welcome to Sentinel-Net v0.1.0

Sentinel-Net is an open-source, privacy-preserving **Web Application Firewall (WAF)** and **Network Anomaly Detector** designed to protect at-risk organizations, NGOs, journalists, and digital rights defenders from sophisticated cyberattacks.

This inaugural release introduces the core security architecture with two complementary defense mechanisms:

---

## ✨ What's Included

### 1. **Regex-Based WAF (Web Application Firewall)**
- ✅ Real-time HTTP/HTTPS traffic filtering
- ✅ OWASP Top 10 attack blocking (SQLi, XSS, Path Traversal, Command Injection, etc.)
- ✅ FastAPI + Python 3.8+ framework
- ✅ Customizable rule sets for organization-specific threats
- ✅ Low-latency request inspection
- ✅ Docker containerized deployment

### 2. **AI-Driven Anomaly Detection**
- ✅ Isolation Forest (unsupervised machine learning)
- ✅ Zero-day attack identification without labeled training data
- ✅ Network baseline learning and behavioral analysis
- ✅ Real-time threat alerting to Admin Dashboard
- ✅ scikit-learn + NumPy implementation

### 3. **Deployment & DevOps**
- ✅ Docker Compose for one-command deployment
- ✅ Self-hosted, cloud-agnostic architecture
- ✅ No external dependencies or cloud lock-in
- ✅ MIT Licensed (completely free and open-source)

### 4. **Documentation & Community**
- ✅ Comprehensive README with architecture diagram (Mermaid)
- ✅ [CONTRIBUTING.md](CONTRIBUTING.md) — Contributing guidelines
- ✅ [SECURITY.md](SECURITY.md) — Responsible disclosure policy
- ✅ [GitHub Issue Templates](.github/ISSUE_TEMPLATE/) — Bug reports & feature requests

---

## 🎯 Why Sentinel-Net Exists

Digital rights defenders, journalists, and activists—especially across the ECOWAS region (West Africa)—face:
- **State-sponsored surveillance and censorship**
- **DDoS attacks from state and non-state actors**
- **Limited access to affordable, international cybersecurity services**
- **Currency constraints making SaaS unaffordable**
- **Need for local data retention and digital sovereignty**

Sentinel-Net provides a **free, self-hosted alternative** to expensive commercial WAFs like Cloudflare, AWS WAF, or Akamai.

---

## 🌍 Alignment with Values

### Internet Freedom (OTF Principles)
Sentinel-Net ensures data never leaves your organization. No cloud dependency. No vendor lock-in. Your security, your infrastructure, your data.

### AI for Social Good
Demonstrates practical unsupervised learning for real-time threat hunting in resource-constrained environments.

### ECOWAS Regional Focus
Built specifically for Nigeria, Ghana, Cameroon, and other West African organizations facing unique cybersecurity challenges.

---

## 🚀 Quick Start

### Deploy the WAF
```bash
cd infrastructure
docker-compose up --build
# WAF listening on http://localhost:8000
```

### Run the Anomaly Detector
```bash
pip install scikit-learn numpy joblib
python ml/anomaly_detector.py
```

---

## 📋 Known Limitations (Alpha Release)

This is an **alpha release**. Expect:
- Limited production hardening
- Ongoing performance optimization
- Additional test coverage in upcoming releases
- Community feedback driving feature prioritization

---

## 🤝 How to Contribute

We welcome:
- Security researchers (responsible disclosure via [SECURITY.md](SECURITY.md))
- ML engineers (improving anomaly detection models)
- DevOps engineers (Kubernetes, cloud deployment examples)
- Documentation writers (regional language translations)
- Journalists & NGOs (real-world deployment feedback)

**See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.**

---

## 📜 License

MIT License — completely free and open-source.

---

## 🙏 Acknowledgments

Built for digital rights defenders, journalists, and NGOs across Africa with the belief that **security tools for at-risk communities should be free and accessible**.

**Made with ❤️ for digital rights defenders.**

---

## 📞 Support & Questions

- **Security Issues:** [SECURITY.md](SECURITY.md)
- **Bug Reports:** [GitHub Issues](https://github.com/Mroziy/Sentinel-Net/issues)
- **Feature Requests:** [GitHub Discussions](https://github.com/Mroziy/Sentinel-Net/discussions)
