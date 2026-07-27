from typing import Dict, Any, List, Optional, Union
from guardrails.pii_sanitizer import PIISanitizerEngine
from guardrails.prompt_injection import PromptInjectionScanner

class SafetyGuardrailValidator:
    """
    Enterprise Safety Guardrail & Sanitization Engine.
    Executes combined PII redaction and jailbreak/prompt-injection scanning.
    """

    def __init__(self):
        self.pii_engine = PIISanitizerEngine()
        self.injection_scanner = PromptInjectionScanner()

    def validate_request(self, user_prompt: str) -> Dict[str, Any]:
        injection_res = self.injection_scanner.scan_prompt(user_prompt)
        if not injection_res["is_safe"]:
            return {
                "status": "BLOCKED",
                "reason": "PROMPT_INJECTION_DETECTED",
                "details": injection_res,
                "sanitized_prompt": ""
            }

        pii_res = self.pii_engine.sanitize_text(user_prompt)
        return {
            "status": "PASSED",
            "reason": "VALIDATED_AND_SANITIZED",
            "sanitized_prompt": pii_res["sanitized_text"],
            "pii_redacted": pii_res["has_pii"]
        }
