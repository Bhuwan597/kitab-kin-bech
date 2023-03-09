
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
import home
import authenticate

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls'), name='home'),
    path('authenticate', include('authenticate.urls'), name='authenticate')
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
