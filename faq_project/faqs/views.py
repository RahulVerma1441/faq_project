from rest_framework.views import APIView
from rest_framework.response import Response
from .models import FAQ
from .serializers import FAQSerializer
from django.core.cache import cache
from django.http import JsonResponse
from django.shortcuts import render

def home(request):
        return JsonResponse({"message": "Welcome to the FAQ API!"})

def faq_frontend(request):
    return render(request, 'faqs.html')

class FAQListView(APIView):
    def get(self, request):
        lang = request.query_params.get('lang', 'en')
        cache_key = f'faqs_{lang}'
        cached_data = cache.get(cache_key)

        if cached_data:
            return Response(cached_data)

        faqs = FAQ.objects.all()
        data = []
        for faq in faqs:
            data.append({
                'question': faq.get_translated_question(lang),
                'answer': faq.get_translated_answer(lang),
            })

        cache.set(cache_key, data, timeout=3600)  
        return Response(data)
    
    