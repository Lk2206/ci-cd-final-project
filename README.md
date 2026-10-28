# ci-cd-final-project

A Flask-based product service demonstrating CI/CD practices with GitHub Actions and Tekton.

## Features
- Flask health endpoint
- Automated linting with Flake8
- Unit tests with nose
- Tekton tasks for cleanup and testing

## Run locally
```bash
python -m pip install -r requirements.txt
python server.py
```

## Run checks
```bash
flake8 .
nosetests
```
