from django.test import TestCase, SimpleTestCase
from django.urls import reverse
# Create your tests here.
class HomepageTest(SimpleTestCase):
    def test_homepage_status_code(self):
        response = selg..client.get(/)
        self.asserEqual(response.status_code,200)

    def test_homepage_status_code(self):
        response = self.client.get(reverse('index'),200)

    def test_homepage_template(self):
        response.assertTemplateUsed(response, 'index.html')
