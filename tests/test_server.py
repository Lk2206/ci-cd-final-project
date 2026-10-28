import unittest
from server import app


class ServerTests(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_root_returns_running_status(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["status"], "SERVICERUNNING")

    def test_health_endpoint(self):
        response = self.client.get("/health")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["status"], "ok")


if __name__ == "__main__":
    unittest.main()
