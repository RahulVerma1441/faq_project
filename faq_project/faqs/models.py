from django.db import models
from ckeditor.fields import RichTextField
from .utils import translate_text

class FAQ(models.Model):
    question = models.TextField()
    answer = RichTextField()  # WYSIWYG editor field
    question_hi = models.TextField(blank=True, null=True)  # Hindi translation
    question_bn = models.TextField(blank=True, null=True)  # Bengali translation
    answer_hi = RichTextField(blank=True, null=True)  # Hindi translation
    answer_bn = RichTextField(blank=True, null=True)  # Bengali translation

    def get_translated_question(self, lang='en'):
        translations = {
            'hi': self.question_hi,
            'bn': self.question_bn,
        }
        return translations.get(lang, self.question)

    def get_translated_answer(self, lang='en'):
        translations = {
            'hi': self.answer_hi,
            'bn': self.answer_bn,
        }
        return translations.get(lang, self.answer)
    
    def save(self, *args, **kwargs):
        if not self.question_hi:
            self.question_hi = translate_text(self.question, 'hi')
        if not self.question_bn:
            self.question_bn = translate_text(self.question, 'bn')
        if not self.answer_hi:
            self.answer_hi = translate_text(self.answer, 'hi')
        if not self.answer_bn:
            self.answer_bn = translate_text(self.answer, 'bn')
        super().save(*args, **kwargs)