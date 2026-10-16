
from pathlib import Path

EMAIL_FILE = Path("evidence/phishing-email-001.eml")


def analyze_email(email_text):
    findings = []

    text = email_text.lower()

    if "micros0ft" in text:
        findings.append("Possible brand impersonation")

    if "suspended within 24 hours" in text:
        findings.append("Urgency or pressure tactic")

    if "verify" in text and "http" in text:
        findings.append("Verification link requires investigation")

    return findings


if __name__ == "__main__":
    email_text = EMAIL_FILE.read_text(encoding="utf-8")
    findings = analyze_email(email_text)

    print("PHISH-001: Initial Indicator Analysis")
    print("-" * 40)

    for finding in findings:
        print(f"[!] {finding}")

    print(f"\nIndicators identified: {len(findings)}")
