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
    out = StringIO()
    call_command('dumpdata', stdout=out)  # dumps all data from the DB
    response = HttpResponse(out.getvalue(), content_type='application/json')
    response['Content-Disposition'] = 'attachment; filename=backup.json'
    return response
