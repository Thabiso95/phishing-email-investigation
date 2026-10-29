import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

FILES = {
    "report": ROOT / "reports" / "PHISH-002-incident-report.md",
    "evidence": ROOT / "evidence" / "PHISH-002" / "evidence-register.md",
    "timeline": ROOT / "analysis" / "PHISH-002" / "timeline.md",
    "findings": ROOT / "analysis" / "PHISH-002" / "findings.md",
}


class TestPhish002Documentation(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.documents = {}
        for name, path in FILES.items():
            if path.exists():
                cls.documents[name] = path.read_text(
                    encoding="utf-8"
                ).casefold()

    def test_all_case_documents_exist(self):
        for name, path in FILES.items():
            with self.subTest(document=name):
                self.assertTrue(
                    path.is_file(),
                    f"Missing case document: {path}"
                )

    def test_documents_identify_case(self):
        for name, content in self.documents.items():
            with self.subTest(document=name):
                self.assertIn("phish-002", content)

    def test_findings_include_authentication_evidence(self):
        findings = self.documents.get("findings", "")
        self.assertIn("spf", findings)
        self.assertIn("dkim", findings)
        self.assertIn("dmarc", findings)

    def test_domain_age_is_not_treated_as_proof(self):
        findings = self.documents.get("findings", "")
        self.assertIn("not inherently malicious", findings)

    def test_case_does_not_claim_confirmed_fraud(self):
        all_text = "\n".join(self.documents.values())
        self.assertNotIn("confirmed fraud", all_text)
        self.assertIn("not conclusively established", all_text)


if __name__ == "__main__":
    unittest.main(verbosity=2)