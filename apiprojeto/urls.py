from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', RedirectView.as_view(url='/admin/', permanent=True)),
    path('admin/', admin.site.urls),
    path('api/', include('tarefas.urls')),
    
    path('api/token/', obtain_auth_token, name='api_token_auth'),
]