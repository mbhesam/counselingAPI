from django.urls import path
from .views import get_signup_info
from django.views.generic.base import TemplateView

urlpatterns = [
    path('registerinformation/<str:platform>/<str:username>',get_signup_info, name='register_information'),
    path('thanks',TemplateView.as_view(template_name="thankyou.html")),
    path('alreadysubmitted', TemplateView.as_view(template_name="alreadysubmitted.html")),
]