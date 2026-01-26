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

    def test_about_page_loads(self):
        from .models import Home, AboutSection
        Home.objects.create(name="Test User", bio="Bio summary", about_summary="About summary")
        AboutSection.objects.create(heading="Test Section", points="Point 1|Point 2")
        client = Client()
        response = client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "About summary")
        self.assertContains(response, "Test Section")
        self.assertContains(response, "Point 1")
