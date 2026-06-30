from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    
    path('api/', include('characters.urls', namespace="characters")),
    path('api/doc/', SpectacularAPIView.as_view(), name='schema'),
    path('api/doc/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('admin/', admin.site.urls),
]


