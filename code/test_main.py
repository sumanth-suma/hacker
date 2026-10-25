import csv
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from main import AuditEngine, IdentityResolver, ROOT


class AuditUnitTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.dataset = ROOT / "dataset"

    def test_historical_email_resolves_to_the_same_subject(self):
        resolver = IdentityResolver(self.dataset)
        request = next(r for r in csv.DictReader((self.dataset / "sample_deletion_requests.csv").open(encoding="utf-8")) if r["case_id"] == "case_03")
        identity = resolver.resolve(request["email"])
        self.assertIsNotNone(identity)
        self.assertIn(request["email"].casefold(), identity.identifiers)

    def test_non_deletion_request_is_not_applicable(self):
        self.assertFalse(AuditEngine.deletion_authorized("Please export my account data."))

    def test_deletion_request_is_authorized(self):
        self.assertTrue(AuditEngine.deletion_authorized("Please permanently delete my account."))


if __name__ == "__main__":
    unittest.main()
