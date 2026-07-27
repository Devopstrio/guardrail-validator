# Guardrail Validator Architecture

The **Guardrail Validator** provides real-time security, PII redaction, and prompt injection interception for LLM microservices and API gateways.

![Guardrail Validator Architecture](images/architecture_diagram.jpg)

## Component Sequence Diagram

```mermaid
flowchart TD
    Client[Client App / API Gateway] -->|1. Transmit Payload| Middleware[Guardrail Interceptor Middleware]
    Middleware -->|2. Scan Injection Triggers| Scanner[Prompt Injection & Jailbreak Scanner]
    Scanner --> IsSafe{Is Prompt Safe?}
    IsSafe -- Prompt Injection Detected --> Reject[Reject Request 403]
    IsSafe -- Prompt Safe --> Sanitizer[PII Redaction Engine]
    Sanitizer -->|Redact Emails/SSNs/Keys| Forward[Forward Sanitized Payload to LLM]
```

## Core Safety Modules

1. **PII Sanitizer Engine (`guardrails/pii_sanitizer.py`)**
   - Redacts Email addresses, Social Security Numbers, and API secret keys (`[REDACTED_EMAIL]`, `[REDACTED_SSN]`).

2. **Prompt Injection Scanner (`guardrails/prompt_injection.py`)**
   - Intercepts system prompt overrides, roleplay jailbreaks, and credential harvesting attempts.

3. **Safety Guardrail Validator (`guardrails/safety_validator.py`)**
   - Coordinates multi-stage input sanitization and security rule evaluation.

4. **Interceptor Middleware (`guardrails/middleware.py`)**
   - Web middleware component for wrapping incoming REST/gRPC API payloads.
