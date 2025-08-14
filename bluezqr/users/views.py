from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, FormParser  # ✅ added for file uploads
from .models import Student, Candidate
from .serializers import StudentSerializer, CandidateSerializer

# Needed imports for backup_view
from django.core.serializers import serialize
from django.http import JsonResponse, HttpResponse
from django.shortcuts import redirect

# For creating admin user
from django.contrib.auth import get_user_model

# For generating Cloudinary URLs
from cloudinary.utils import cloudinary_url


# -------------------------------
# ViewSets
# -------------------------------
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    parser_classes = (MultiPartParser, FormParser)  # ✅ handle file uploads

    def create(self, request, *args, **kwargs):
        # Save student data
        response = super().create(request, *args, **kwargs)
        resume_url = response.data.get('resume')
        print(f"📄 Uploaded student resume URL: {resume_url}")
        return response


class CandidateViewSet(viewsets.ModelViewSet):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer
    parser_classes = (MultiPartParser, FormParser)  # ✅ handle file uploads

    def create(self, request, *args, **kwargs):
        # Save candidate data
        response = super().create(request, *args, **kwargs)
        resume_url = response.data.get('resume')
        print(f"📄 Uploaded candidate resume URL: {resume_url}")
        return response


# -------------------------------
# Backup JSON view
# -------------------------------
def backup_view(request):
    students_json = serialize('json', Student.objects.all())
    candidates_json = serialize('json', Candidate.objects.all())

    return JsonResponse({
        "students": students_json,
        "candidates": candidates_json
    }, safe=False)


# -------------------------------
# Create superuser if not exists
# -------------------------------
def create_admin_user():
    User = get_user_model()
    if not User.objects.filter(username="admin").exists():
        User.objects.create_superuser(
            username="admin",
            email="bluezinfomaticsolutions@gmail.com",
            password="Bluez@.1A"
        )
        print("✅ Superuser created: admin / Bluez@.1A")


create_admin_user()


# -------------------------------
# Download resume by redirect
# -------------------------------
def download_resume(request, student_id):
    try:
        student = Student.objects.get(id=student_id)
        if student.resume:
            return redirect(student.resume.url)
        else:
            return HttpResponse("Resume not found", status=404)
    except Student.DoesNotExist:
        return HttpResponse("Student not found", status=404)
