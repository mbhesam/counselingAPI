from django.urls import path
from .views import get_signup_info
from django.views.generic.base import TemplateView

urlpatterns = [
    path('registerinformation/<str:platform>/<str:username>', get_signup_info),
    path('thanks',TemplateView.as_view(template_name="thankyou.html"))
]