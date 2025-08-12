from rest_framework import viewsets
from .models import Student, Candidate
from .serializers import StudentSerializer, CandidateSerializer

# Needed imports for backup_view
from django.core.serializers import serialize
from django.http import JsonResponse, HttpResponse
from django.shortcuts import redirect

# For creating admin user
from django.contrib.auth import get_user_model
import os

# For generating Cloudinary URLs
from cloudinary.utils import cloudinary_url


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class CandidateViewSet(viewsets.ModelViewSet):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer


# ---- Temporary backup view ----
def backup_view(request):
    students_json = serialize('json', Student.objects.all())
    candidates_json = serialize('json', Candidate.objects.all())

    return JsonResponse({
        "students": students_json,
        "candidates": candidates_json
    }, safe=False)


def create_admin_user():
    User = get_user_model()
    if not User.objects.filter(username="admin").exists():
        User.objects.create_superuser(
            username="admin",
            email="bluezinfomaticsolutions@gmail.com",
            password="Bluez@.1A"
        )
        print("✅ Superuser created: admin / yourpassword123")


create_admin_user()


def download_resume(request, student_id):
    try:
        student = Student.objects.get(id=student_id)
        if student.resume:
            return redirect(student.resume.url)  # Cloudinary URL-க்கு redirect செய்யும்
        else:
            return HttpResponse("Resume not found", status=404)
    except Student.DoesNotExist:
        return HttpResponse("Student not found", status=404)
