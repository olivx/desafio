from django.test import TestCase
from django.shortcuts import resolve_url as r


# Create your tests here.
class TestViewCore(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('home'))

    def test_get_home(self):
        """Test get status code """
        self.assertEqual(200, self.resp.status_code)

