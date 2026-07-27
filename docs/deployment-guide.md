# Developer & Deployment Guide: Guardrail Validator

This guide details installation, API middleware integration, and automated testing.

## 1. Installation

```bash
git clone https://github.com/Devopstrio/guardrail-validator.git
cd guardrail-validator

# Install in developer mode
pip install -e .
```

## 2. API Gateway Integration Example

```python
from guardrails.middleware import GuardrailMiddleware

middleware = GuardrailMiddleware()

# Incoming HTTP request payload
incoming_request = {
    "prompt": "Send cloud report to security@devopstrio.co.uk"
}

response = middleware.process_incoming_payload(incoming_request)

if response["allowed"]:
    print("Sanitized Payload ready for LLM:", response["modified_payload"])
else:
    print("Request Blocked:", response["error"])
```

## 3. Running Pytest Suite

```bash
python -m pytest -v tests/
```
