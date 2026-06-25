# Contributing to Sentinel-Net

Thank you for your interest in contributing to **Project Sentinel-Net**! We welcome contributions from security researchers, developers, and digital rights advocates worldwide.

## Code of Conduct

We are committed to providing a welcoming and inclusive environment. All contributors must:
- Treat each other with respect and dignity
- Welcome diverse perspectives and backgrounds
- Focus on constructive, civil communication

Violations will not be tolerated.

---

## Ways to Contribute

### 1. Report Bugs
Found a vulnerability or bug? Please:
1. **Check existing issues** — avoid duplicates
2. **Create a detailed bug report** using the [bug report template](.github/ISSUE_TEMPLATE/bug_report.md)
3. **Include:**
   - Steps to reproduce
   - Expected vs. actual behavior
   - Environment details (Python version, OS, Docker version, etc.)
   - Relevant logs or error messages

### 2. Request Features
Have an idea to improve Sentinel-Net?
1. **Check existing issues** — avoid duplicates
2. **Create a feature request** using the [feature request template](.github/ISSUE_TEMPLATE/feature_request.md)
3. **Explain:**
   - The problem it solves
   - How it benefits at-risk communities
   - Proposed implementation (if applicable)

### 3. Submit Code

#### Setup Your Development Environment
```bash
# Clone the repository
git clone https://github.com/Mroziy/Sentinel-Net.git
cd Sentinel-Net

# Create a virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
pip install -r requirements-dev.txt  # For testing, linting, etc.
```

#### Before Submitting a PR
1. **Create a feature branch:**
   ```bash
   git checkout -b feature/your-feature-name
   ```
2. **Follow coding standards:**
   - Use PEP 8 style (4 spaces, lowercase with underscores)
   - Add docstrings to functions and classes
   - Write type hints for better clarity
3. **Test your code:**
   ```bash
   pytest tests/
   ```
4. **Run linting:**
   ```bash
   black .
   flake8 .
   ```
5. **Commit with clear messages:**
   ```bash
   git commit -m "feat: add anomaly detection confidence scoring"
   ```
   Use conventional commits: `feat:`, `fix:`, `docs:`, `test:`, `refactor:`

6. **Push and open a Pull Request:**
   ```bash
   git push origin feature/your-feature-name
   ```

#### PR Requirements
Your pull request will be reviewed for:
- ✅ Code quality and adherence to standards
- ✅ Test coverage (new code should have tests)
- ✅ Documentation updates (if applicable)
- ✅ No breaking changes (or clear migration path)
- ✅ Alignment with Sentinel-Net's mission (digital sovereignty, Internet freedom)

### 4. Improve Documentation
Documentation is critical for adoption. You can:
- Fix typos or unclear explanations
- Add examples and tutorials
- Translate documentation to other languages
- Create deployment guides for specific environments

---

## Security Contributions

### Reporting Vulnerabilities
**Do not open a public issue for security vulnerabilities.** Instead:
1. **Read [SECURITY.md](SECURITY.md)** for responsible disclosure guidelines
2. **Email your findings** to the maintainer with details
3. **Allow time for a fix** before public disclosure

We take security seriously and will respond promptly.

---

## Project Structure

```
Sentinel-Net/
├── waf/                    # WAF core code (regex rules, request filtering)
├── ml/                     # AI anomaly detector (Isolation Forest)
├── infrastructure/         # Docker Compose & deployment configs
├── tests/                  # Unit and integration tests
├── docs/                   # Additional documentation
├── README.md               # Main project overview
├── CONTRIBUTING.md         # This file
├── SECURITY.md             # Security policy and vulnerability disclosure
└── requirements.txt        # Python dependencies
```

---

## Getting Help

- **Questions?** Open a [discussion](https://github.com/Mroziy/Sentinel-Net/discussions)
- **Bug reports?** Use the [bug report template](.github/ISSUE_TEMPLATE/bug_report.md)
- **Security concerns?** See [SECURITY.md](SECURITY.md)

---

## Recognition

All contributors are recognized in:
- The main repository's contributor list
- Release notes for significant contributions
- Our project's [CONTRIBUTORS.md](CONTRIBUTORS.md) file (coming soon)

Thank you for helping defend digital rights! 🛡️
