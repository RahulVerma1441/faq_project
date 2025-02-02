from django.urls import path
from .views import FAQListView, faq_frontend

urlpatterns = [
    path('', faq_frontend, name='faq-frontend'),
    path('api/faqs/', FAQListView.as_view(), name='faq-list'),
]