from rest_framework import serializers
from .models import Student, Candidate

class StudentSerializer(serializers.ModelSerializer):
    resume_url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Student
        fields = '__all__'  # includes 'resume' so upload works

    def get_resume_url(self, obj):
        return obj.resume.url if obj.resume else None


class CandidateSerializer(serializers.ModelSerializer):
    resume_url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Candidate
        fields = '__all__'  # includes 'resume' so upload works

    def get_resume_url(self, obj):
        return obj.resume.url if obj.resume else None
