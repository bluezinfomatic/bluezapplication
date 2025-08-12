from rest_framework import serializers
from .models import Student, Candidate

class StudentSerializer(serializers.ModelSerializer):
    resume_url = serializers.SerializerMethodField()

    class Meta:
        model = Student
        fields = '__all__'  # or list all fields explicitly + 'resume_url'

    def get_resume_url(self, obj):
        if obj.resume:
            return obj.resume.url
        return None

class CandidateSerializer(serializers.ModelSerializer):
    resume_url = serializers.SerializerMethodField()

    class Meta:
        model = Candidate
        fields = '__all__'  # or list all fields explicitly + 'resume_url'

    def get_resume_url(self, obj):
        if obj.resume:
            return obj.resume.url
        return None
