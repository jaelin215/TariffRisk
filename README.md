# TariffRisk

## Scalable Machine Learning Service (with Docker, CI/CD, and planned support for Optuna + Airflow)

This project demonstrates **ONE core capability**:
> I can build, optimize, test, and deploy production-ready ML services that are scalable, modular, cloud-native, and collaborative.

Built as a technical showcase for roles like **Senior Data Scientist / ML Engineer**. This repo integrates everything needed to move fast, ship weekly, and handle complexity.

---

### ⚙️ Data & Motivation

This project uses a publicly available dataset sourced from **Kaggle** (https://www.kaggle.com/datasets/mesumraza/trump-tarrif-data).  
The core motivation is to preprocess and transform this data to build a reliable predictive model for **tariff risk scoring**—helping merchants who sell their merchandise globally through platforms like **Shopify, Amazon**, and other e-commerce marketplaces assess and manage the risk of tariffs.

Beyond just modeling, this repo serves as a template for developing production-ready, scalable ML pipelines around complex, real-world trade compliance challenges faced by online merchants.
*Note: The prediction of the tariff risk score is not implemented yet and remains a key upcoming milestone for this project.*

---

### ❓ Problem This Project Solves
Real-world ML system fail when they lack:
- Reproducibility (unclear training/testing bounaries)
- Optimization (manual hyperparameter tuning or guesswork)
- Scalability (not containerized or cloud deployable)
- Team collaboration (no tests, no CI/CD, messy structure)

This repo fixes that. It's a blueprint for building and collaborating on real-world ML systems.

---

### ✅ Tech Overview

| Feature | Status |
|--------|--------|
| **FastAPI** (API backend) | ✅ Integrated |
| **Pytest** (unit tests) | ✅ Integrated |
| **Docker** (containerization) | ✅ Integrated |
| **GitHub Actions** (CI/CD) | ✅ Integrated |
| **Optuna** (hyperparameter tuning) | 🔜 *Planned* |
| **Airflow** (scheduled retraining) | 🔜 *Planned* |

---

### 🧱 Project Structure
- app/ - Logical sepearation of all core logic (i.e. models, routes, services, and config). Promotes modularity and ease of onboarding for other team members
- airflow/ - Embedded inside the app/. Realistic for small-to-mid ML projects that don't need a separate Airflow repo. Keeps retraining logic tightly coupled with the prediction logic, improving traceability.
- tests/ - Clean and organized. Unit tests per service/module file (i.e. test_predict.py, test_optuna.py). Easy plug-in for CI with pytest.
- github/workflows/ci.yml - Clean adn minimal. It shows DevOps maturity: CI/CD with GitHub Actions. Makes the project team- and cloud- ready.
- Dockerfile, .dockerignore, .gitignore - Full containerization, cloud-deployability, and local development efficiency.
- Makefile - Developer friendliness (make test, make buid, make run)
- pyproject.toml - Care about formatting, linting, and build config. Using modern Python tooling (black, isort, pytest, etc.) 


⚠️ Note: airflow/ and optuna/ are scaffolded but not yet functional. They will be integrated in the next release to support full retraining workflows and search optimization pipelines.

🧪 Testing & CI/CD
	•	pytest for local + CI test runs
	•	make test to run tests locally
	•	GitHub Actions triggers CI on push/pull

⸻

🐳 Containerization
	•	Full Docker setup with Dockerfile and .dockerignore
	•	Easily deployable on GCP, AWS, or Azure
	•	Lightweight dev experience via GitHub Codespaces

⸻

🛠 Dev UX
	•	Makefile for fast local commands (make run, make test, etc.)
	•	pyproject.toml to manage formatting (black, isort) and linting in one place

⸻

📌 Coming Soon
	•	Optuna integration for clean, modular hyperparameter search
	•	Airflow DAG for scheduled retraining + monitoring
	•	Looker dashboard template + auto-publishing
	•	GitHub Codespace one-click launch config

⸻

💬 Why This Matters

You’re not just showing that you can build ML models.
You’re showing that you can ship ML products—with reliability, traceability, and confidence.

⸻

🚀 Use This If…
	•	You’re a solo builder or early team setting up ML ops from scratch
	•	You want to showcase your ML engineering capability beyond notebooks
	•	You’re interviewing and want a sharp, practical project to discuss

⸻
