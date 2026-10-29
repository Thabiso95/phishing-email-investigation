import unittest
from pathlib import Path


class TestPHISH002AttackAssessment(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.path = Path("analysis/PHISH-002/mitre-attack-assessment.md")
        cls.content = cls.path.read_text(encoding="utf-8").lower()

    def test_assessment_exists(self):
        self.assertTrue(self.path.is_file())

    def test_case_id_is_present(self):
        self.assertIn("phish-002", self.content)

    def test_unconfirmed_techniques_are_not_presented_as_facts(self):
        self.assertIn("not confirmed", self.content)
        self.assertIn("no mitre att&ck technique is confirmed", self.content)

    def test_sensitive_information_request_is_assessed(self):
        self.assertIn("t1598", self.content)
        self.assertIn("qualifications", self.content)

    def test_no_unsupported_system_compromise_claim(self):
        self.assertIn("does not establish malware delivery", self.content)
        self.assertIn("system compromise", self.content)

    def test_detection_opportunities_are_documented(self):
        self.assertIn("detection opportunities", self.content)
        self.assertIn("mail gateway", self.content)


if __name__ == "__main__":
    unittest.main(verbosity=2)
