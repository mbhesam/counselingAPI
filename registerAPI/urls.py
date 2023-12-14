from django.urls import path
from .views import RegisterView,ShowRegisteration

urlpatterns = [
    path('submmit/', RegisterView.as_view()),
    path('show_registeration',ShowRegisteration.as_view())
]