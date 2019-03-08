from django.test import TestCase

# Create your tests here.
class TestPage(TestCase):

    """Docstring for TestPage. """

    def test_home_page_workd(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
        self.assertContains(response, 'BookTime')
