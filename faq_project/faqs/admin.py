from django.contrib import admin
from .models import FAQ

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'get_translated_question')
    search_fields = ('question', 'question_hi', 'question_bn')

    def get_translated_question(self, obj):
        return obj.get_translated_question('hi')  
    get_translated_question.short_description = 'Translated Question'