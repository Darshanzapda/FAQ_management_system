import os
import django
# Import third-party and local application libraries after standard libraries
from django.test import TestCase
from django.core.cache import cache
from faq.models import FAQ

# Set up Django settings for testing
os.environ['DJANGO_SETTINGS_MODULE'] = 'faq_project.settings'
django.setup()


class FAQModelTest(TestCase):
    def test_translation_fallback(self):
        faq = FAQ.objects.create(
            question='What is Django?',
            answer='Django is a Python web framework.',
            question_hi='Django kya hai?',
            answer_hi='Django ek Python web framework hai.'
        )
        self.assertEqual(faq.get_translated_text('hi')['question'], 'Django kya hai?')
        self.assertEqual(faq.get_translated_text('hi')['answer'], 'Django ek Python web framework hai.')

        bengali_question_translation = faq.get_translated_text('bn')['question']
        expected_bengali_question_translation = 'জ্যাঙ্গো কী?'
        self.assertEqual(bengali_question_translation, expected_bengali_question_translation)

        bengali_answer_translation = faq.get_translated_text('bn')['answer']
        expected_bengali_answer_translation = 'জ্যাঙ্গো একটি পাইথন ওয়েব ফ্রেমওয়ার্ক।'
        self.assertEqual(bengali_answer_translation, expected_bengali_answer_translation)

    def test_cache_behavior_on_update(self):
        faq = FAQ.objects.create(
            question='What is Django?',
            answer='Django is a Python web framework.',
            question_hi='Django kya hai?',
            answer_hi='Django ek Python web framework hai.'
        )

        # Set cache manually
        cache.set(f"faq_{faq.id}", faq.get_translated_text('hi'))
        self.assertIsNotNone(cache.get(f"faq_{faq.id}"))  # Ensure cache is set initially

        # Update the FAQ and check cache clearing
        faq.answer = 'Updated answer for Django'
        faq.save()

        # Ensure that the cache is cleared after the update
        self.assertIsNone(cache.get(f"faq_{faq.id}"))  # Cache should be cleared after save
