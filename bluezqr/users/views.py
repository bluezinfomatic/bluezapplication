from rest_framework import viewsets
from .models import Student, Candidate
from .serializers import StudentSerializer, CandidateSerializer

# Extra imports for backup
from django.core.management import call_command
from django.http import HttpResponse
from io import StringIO

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

from django.contrib.auth import get_user_model
import os

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

from cloudinary.utils import cloudinary_url
from django.shortcuts import redirect
from django.http import HttpResponse
from .models import Student

def download_resume(request, student_id):
    try:
        student = Student.objects.get(id=student_id)
        if student.resume:
            # Generate the proper Cloudinary URL for raw file (pdf)
            url, options = cloudinary_url(
                student.resume.public_id,
                resource_type="raw",
                format="pdf"
            )
            return redirect(url)
        else:
            return HttpResponse("No resume uploaded", status=404)
    except Student.DoesNotExist:
        return HttpResponse("Student not found", status=404)

