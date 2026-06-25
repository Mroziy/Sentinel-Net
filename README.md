# Sentinel-Net

Minimal scaffold for Sentinel-Net — a Python-based project.

This repository contains a small FastAPI app and Dockerfile so you can run it locally or in a container.

Getting started

- Create a virtual environment: `python -m venv .venv`
- Activate it and install dependencies: `pip install -r requirements.txt`
- Run locally: `uvicorn sentinel_net.main:app --reload --host 0.0.0.0 --port 8000`

Docker

- Build: `docker build -t sentinel-net .`
- Run: `docker run -p 8000:8000 sentinel-net`

License

This project is released under the MIT License. See LICENSE for details.
