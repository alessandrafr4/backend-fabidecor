from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from usuario.router import router as usuario_router
from django.conf import settings
from django.conf.urls.static import static

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from fabidecor.views import  CategoriaViewSet, TemasViewSet, ProdutoViewSet
from usuario.router import router as usuario_router
from uploader.router import router as uploader_router



router = DefaultRouter()
router.register(r"categorias", CategoriaViewSet)
router.register(r"temas", TemasViewSet)
router.register(r"produtos", ProdutoViewSet)



urlpatterns = [

    # OpenAPI 3
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/swagger/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "api/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    # path("api/usuario/", include(usuario_router.urls)),
    path("admin/", admin.site.urls),
    # path("api/media/", include(uploader_router.urls)),
    # path("", include(router.urls)),
    path("api/", include(router.urls)),
    path("api/usuario/", include(usuario_router.urls)),
    path("api/media/", include(uploader_router.urls)),


]

urlpatterns += static(settings.MEDIA_ENDPOINT, document_root=settings.MEDIA_ROOT)
