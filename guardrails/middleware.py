from typing import Dict, Any, List, Optional, Union
from guardrails.safety_validator import SafetyGuardrailValidator

class GuardrailMiddleware:
    """
    HTTP & Gateway Guardrail Interceptor Middleware.
    Wraps API request payloads to enforce pre-LLM security validation.
    """

    def __init__(self):
        self.validator = SafetyGuardrailValidator()

    def process_incoming_payload(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        prompt = payload.get("prompt", "")
        validation = self.validator.validate_request(prompt)

        if validation["status"] == "BLOCKED":
            return {
                "allowed": False,
                "error": "Request blocked by safety guardrails",
                "details": validation
            }

        payload["prompt"] = validation["sanitized_prompt"]
        return {
            "allowed": True,
            "modified_payload": payload
        }
