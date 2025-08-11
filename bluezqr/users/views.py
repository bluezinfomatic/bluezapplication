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
