from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('data-sets/',include("datastore.urls",namespace="datastore")),
    path('data-models/',include("modelstore.urls",namespace="modelstore")),
    path('ml/',include('core.urls',namespace='core')),
    path('api-auth/', include('rest_framework.urls'))
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)