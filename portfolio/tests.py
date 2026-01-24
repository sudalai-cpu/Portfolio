from django.test import TestCase, Client
from django.urls import reverse
from .models import Contact

class ContactTest(TestCase):
    def test_contact_page_loads(self):
        client = Client()
        response = client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Get in Touch")

    def test_contact_form_submission(self):
        client = Client()
        data = {
            'name': 'Test User',
            'email': 'test@example.com',
            'message': 'This is a test message.'
        }
        response = client.post(reverse('contact'), data)
        # Check redirection after success
        self.assertEqual(response.status_code, 302)
        # Verify message is saved
        self.assertEqual(Contact.objects.count(), 1)
        self.assertEqual(Contact.objects.first().name, 'Test User')
