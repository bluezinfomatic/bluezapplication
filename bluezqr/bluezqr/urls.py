from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from users.views import StudentViewSet, CandidateViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse


router = DefaultRouter()
router.register(r'students', StudentViewSet)
router.register(r'candidates', CandidateViewSet)

def home(request):
    return HttpResponse("Welcome to Bluez Application")

urlpatterns = [
    path("", home),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
