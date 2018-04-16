from django.urls import reverse, resolve

from test_plus.test import TestCase


class TestUserURLs(TestCase):
    """Test URL patterns for users app."""

    def setUp(self):
        self.user = self.make_user()

    def test_detail_reverse(self):
        """users:detail should reverse to /testuser/."""
        self.assertEqual(
            reverse("users:detail", kwargs={"username": "testuser"}), "/testuser/"
        )

    def test_detail_resolve(self):
        """testuser/ should resolve to users:detail."""
        self.assertEqual(resolve("/testuser/").view_name, "users:detail")


