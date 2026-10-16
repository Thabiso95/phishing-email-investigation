
import re
from email import message_from_string
from email.utils import parseaddr
from urllib.parse import urlparse


def analyze_email(email_text):
    message = message_from_string(email_text)

    sender_name, sender_address = parseaddr(
        message.get("From", "")
    )
    subject = message.get("Subject", "")

    body = message.get_payload()
    if not isinstance(body, str):
        body = ""

    findings = []

    # 1. Extract the sender's domain.
    sender_domain = (
        sender_address.rsplit("@", 1)[-1].lower()
        if "@" in sender_address
        else ""
    )

    # 2. Extract URLs from the message body.
    urls = re.findall(
        r"https?://[^\s<>'\"]+",
        body,
        flags=re.IGNORECASE
    )

    # 3. Inspect sender and URL hostnames.
    hosts = [sender_domain]

    for url in urls:
        hostname = urlparse(url).hostname
        if hostname:
            hosts.append(hostname.lower())

    if any("micros0ft" in host for host in hosts):
        findings.append("Possible brand impersonation")

    # 4. Check for urgency indicators.
    combined_text = f"{subject} {body}".lower()

    urgency_phrases = [
        "within 24 hours",
        "immediately",
        "urgent",
        "suspended"
    ]

    if any(
        phrase in combined_text
        for phrase in urgency_phrases
    ):
        findings.append("Urgency or pressure tactic")

    # 5. Flag links requesting verification.
    if urls and "verify" in combined_text:
        findings.append(
            "Verification link requires investigation"
        )

    return findings


if __name__ == "__main__":
    from pathlib import Path

    email_file = Path("evidence/phishing-email-001.eml")
    email_text = email_file.read_text(encoding="utf-8")

    findings = analyze_email(email_text)

    print("PHISH-001: Email Indicator Analysis")
    print("-" * 40)

    for finding in findings:
        print(f"[!] {finding}")

    print(f"\nIndicators identified: {len(findings)}")
