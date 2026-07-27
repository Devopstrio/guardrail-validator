from typing import Dict, Any, List, Optional, Union

class PromptInjectionScanner:
    """
    Prompt Injection & Jailbreak Attack Scanner Engine.
    Detects system instruction overrides, roleplay bypasses, and unauthorized system prompt leakage attempts.
    """

    INJECTION_TRIGGERS = [
        "ignore previous instructions",
        "system prompt override",
        "bypass security rules",
        "you are now DAN",
        "reveal system credentials"
    ]

    def scan_prompt(self, user_prompt: str) -> Dict[str, Any]:
        prompt_lower = user_prompt.lower()
        found_injections = [trigger for trigger in self.INJECTION_TRIGGERS if trigger in prompt_lower]

        is_safe = len(found_injections) == 0

        return {
            "prompt": user_prompt,
            "is_safe": is_safe,
            "detected_injections": found_injections,
            "action": "ALLOW" if is_safe else "BLOCK_PROMPT_INJECTION"
        }
