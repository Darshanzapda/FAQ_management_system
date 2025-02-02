import os
import django
# Import third-party and local application libraries after standard libraries
from django.test import TestCase
from django.core.cache import cache
from faq.models import FAQ

# Set up Django settings for testing
os.environ['DJANGO_SETTINGS_MODULE'] = 'faq_project.settings'
django.setup()


class FAQApiTest(TestCase):
    def test_get_faqs_in_english(self):
        response = self.client.get('/api/faqs/')
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertIn('What is Django?', response_data[0]['question'])

    def test_get_faqs_in_hindi(self):
        response = self.client.get('/api/faqs/?lang=hi')
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertIn('Django क्या है?', response_data[0]['question'])

    def test_get_faqs_in_bengali(self):
        response = self.client.get('/api/faqs/?lang=bn')
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertIn('জ্যাঙ্গো কী?', response_data[0]['question'])

    def test_cache_clear_on_faq_update(self):
        faq = FAQ.objects.create(
            question='What is Django?',
            answer='Django is a Python web framework.',
            question_hi='Django kya hai?',
            answer_hi='Django ek Python web framework hai.'
        )

        # Initial cache set
        cache.set(f"faq_{faq.id}", faq.get_translated_text('hi'))
        self.assertIsNotNone(cache.get(f"faq_{faq.id}"))

        # Update FAQ and check if cache is cleared
        faq.answer = 'Updated answer for Django'
        faq.save()

        # Ensure that the cache is cleared
        self.assertIsNone(cache.get(f"faq_{faq.id}"))
