from django.db import models
from ckeditor.fields import RichTextField
from googletrans import Translator


class FAQ(models.Model):
    question = models.TextField()
    answer = RichTextField()

    # Translations for Hindi and Bengali
    question_hi = models.TextField(null=True, blank=True)
    answer_hi = RichTextField(null=True, blank=True)

    question_bn = models.TextField(null=True, blank=True)
    answer_bn = RichTextField(null=True, blank=True)

    def translate_text(self):
        """Automatically translate question and answer to Hindi and Bengali if missing."""
        translator = Translator()

        if not self.question_hi:
            self.question_hi = translator.translate(self.question, src='en', dest='hi').text
        if not self.answer_hi:
            self.answer_hi = translator.translate(self.answer, src='en', dest='hi').text

        if not self.question_bn:
            self.question_bn = translator.translate(self.question, src='en', dest='bn').text
        if not self.answer_bn:
            self.answer_bn = translator.translate(self.answer, src='en', dest='bn').text

    def save(self, *args, **kwargs):
        """Translate text before saving if missing."""
        self.translate_text()
        super().save(*args, **kwargs)

    def get_translated_text(self, lang='en'):
        """Return translated question & answer based on the requested language."""
        if lang == 'hi':
            return {
                'question': self.question_hi or self.question,
                'answer': self.answer_hi or self.answer
            }
        elif lang == 'bn':
            return {
                'question': self.question_bn or self.question,
                'answer': self.answer_bn or self.answer
            }
        return {
            'question': self.question,
            'answer': self.answer
        }

    def __str__(self):
        return self.question
