from guardrails.pii_sanitizer import PIISanitizerEngine

def test_sanitize_email_and_ssn():
    sanitizer = PIISanitizerEngine()
    text = "Contact user at admin@devopstrio.co.uk with SSN 123-45-6789."
    res = sanitizer.sanitize_text(text)
    assert res["has_pii"] is True
    assert "[REDACTED_EMAIL]" in res["sanitized_text"]
    assert "[REDACTED_SSN]" in res["sanitized_text"]

def test_sanitize_clean_text():
    sanitizer = PIISanitizerEngine()
    res = sanitizer.sanitize_text("Deploy Kubernetes cluster with Terraform.")
    assert res["has_pii"] is False
    assert res["sanitized_text"] == "Deploy Kubernetes cluster with Terraform."
