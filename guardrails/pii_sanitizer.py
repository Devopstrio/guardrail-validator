from typing import Dict, Any, List, Optional, Union
import re

class PIISanitizerEngine:
    """
    PII (Personally Identifiable Information) Redaction Engine.
    Detects and sanitizes Email Addresses, Phone Numbers, Social Security Numbers, and API Keys.
    """

    PATTERNS = {
        "email": r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
        "ssn": r"\b\d{3}-\d{2}-\d{4}\b",
        "api_key": r"sk-[a-zA-Z0-9]{32,}"
    }

    def sanitize_text(self, text: str) -> Dict[str, Any]:
        sanitized = text
        detected_types = []

        for pii_type, pattern in self.PATTERNS.items():
            matches = re.findall(pattern, sanitized)
            if matches:
                detected_types.append(pii_type)
                sanitized = re.sub(pattern, f"[REDACTED_{pii_type.upper()}]", sanitized)

        return {
            "original_text": text,
            "sanitized_text": sanitized,
            "has_pii": len(detected_types) > 0,
            "redacted_types": detected_types
        }
