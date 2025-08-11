from django.contrib import admin
from django.http import HttpResponse
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from users.views import StudentViewSet, CandidateViewSet, backup_view
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.conf import settings
from django.conf.urls.static import static

router = DefaultRouter()
router.register(r'students', StudentViewSet)
router.register(r'candidates', CandidateViewSet)

def candidates_page(request):
    return HttpResponse("<h1>Candidate Registration Page</h1><p>This is the candidates page.</p>")

def students_page(request):
    return HttpResponse("<h1>Student Registration Page</h1><p>This is the students page.</p>")

urlpatterns = [
    path("", lambda request: HttpResponse("Welcome to Bluez Application")),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Static pages
    path('candidates/', candidates_page, name='candidates_page'),
    path('students/', students_page, name='students_page'),

    # Backup route
    path('backup/', backup_view, name='backup'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
