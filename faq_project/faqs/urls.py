from django.urls import path
from .views import FAQListView, home  # Ensure both are imported

urlpatterns = [
    path('', home, name='home'),  # Root URL
    path('api/faqs/', FAQListView.as_view(), name='faq-list'),
]