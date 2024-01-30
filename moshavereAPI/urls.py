from django.contrib import admin
from django.urls import path , include
import registerAPI.urls
import coreAPI.urls
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
import users.urls

schema_view = get_schema_view(
   openapi.Info(
      title="Test API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="testing@api.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)
urlpatterns = [
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path(r'^docs/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),
    path('register/', include(registerAPI.urls)),
    path('users/', include(users.urls)),
    path('core/', include(coreAPI.urls)),
]
