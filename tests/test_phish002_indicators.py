import unittest
from pathlib import Path


class TestPHISH002Indicators(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.path = Path("analysis/PHISH-002/indicator-register.md")
        cls.content = cls.path.read_text(encoding="utf-8").lower()

    def test_indicator_register_exists(self):
        self.assertTrue(self.path.is_file())

    def test_case_id_is_present(self):
        self.assertIn("phish-002", self.content)

    def test_authentication_results_are_documented(self):
        for result in ("spf", "dkim", "dmarc"):
            with self.subTest(result=result):
                self.assertIn(result, self.content)

    def test_domain_age_is_not_proof_of_maliciousness(self):
        self.assertIn("does not prove maliciousness", self.content)
        self.assertIn("not proof of fraud", self.content)

    def test_unverified_indicators_are_not_labelled_confirmed_malicious(self):
        self.assertIn("not confirmed malicious", self.content)
        self.assertIn("remain unverified", self.content)

    def test_payment_request_is_recorded(self):
        self.assertIn("r310", self.content)
        self.assertIn("payment request", self.content)


if __name__ == "__main__":
    unittest.main(verbosity=2)
