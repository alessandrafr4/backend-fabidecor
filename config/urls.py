from django.contrib import admin
from django.urls import path,include

from rest_framework.routers import DefaultRouter

from fabidecor.views import CategoriaViewSet

router  = DefaultRouter()
router.register(r'categorias', CategoriaViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]
