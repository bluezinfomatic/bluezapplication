from rest_framework import viewsets
from .models import Student, Candidate
from .serializers import StudentSerializer, CandidateSerializer
from rest_framework.views import exception_handler

# Extra imports for backup
from django.core.management import call_command
from django.http import HttpResponse, HttpResponseForbidden
from io import StringIO

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class CandidateViewSet(viewsets.ModelViewSet):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer

# ---- Temporary backup view ----
def backup_view(request):
    # Optional: restrict to admin users only
    # if not request.user.is_authenticated or not request.user.is_staff:
    #     return HttpResponseForbidden("Forbidden")

    out = StringIO()
    call_command('dumpdata', stdout=out)
    response = HttpResponse(out.getvalue(), content_type='application/json')
    response['Content-Disposition'] = 'attachment; filename=backup.json'
    return response
