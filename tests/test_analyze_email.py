
import unittest

from src.analyze_email import analyze_email


class TestEmailAnalysis(unittest.TestCase):

    def test_detects_three_indicators(self):
        email = """
        From: security@micros0ft-example.invalid
        Subject: Your account will be suspended within 24 hours
        Please verify your account:
        https://micros0ft-example.invalid/verify
        """

        findings = analyze_email(email)

        self.assertEqual(len(findings), 3)
        self.assertIn(
            "Possible brand impersonation", findings
        )
        self.assertIn(
            "Urgency or pressure tactic", findings
        )
        self.assertIn(
            "Verification link requires investigation", findings
        )

    def test_clean_message_returns_no_indicators(self):
        email = """
        From: colleague@example.com
        Subject: Meeting agenda
        The meeting starts at 10:00 tomorrow.
        """

        findings = analyze_email(email)

        self.assertEqual(findings, [])

    def test_indicator_matching_is_case_insensitive(self):
        email = """
        From: security@example.com
        Subject: MICRO S0FT account
        Please VERIFY at HTTPS://example.invalid/login
        """

        findings = analyze_email(email)

        self.assertIn(
            "Verification link requires investigation", findings
        )


    def test_detects_suspicious_sender_without_other_indicators(self):
        email = """From: Security Team <security@micros0ft-example.invalid>
        Subject: Account information

        Please review the account information in the attached notice.
        """

        findings = analyze_email(email)

        self.assertIn("Possible brand impersonation", findings)
        self.assertNotIn("Urgency or pressure tactic", findings)
        self.assertNotIn(
            "Verification link requires investigation", findings
        )


if __name__ == "__main__":
    unittest.main()
