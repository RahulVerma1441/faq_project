from django.test import TestCase
from .models import FAQ

class FAQModelTest(TestCase):
    def test_translation(self):
        faq = FAQ.objects.create(
            question="What is Django?",
            answer="Django is a web framework."
        )
        self.assertEqual(faq.get_translated_question('hi'), "Django क्या है?")