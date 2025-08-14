from django.db import models
from cloudinary.models import CloudinaryField

class Student(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    alternate_mobile = models.CharField(max_length=15, blank=True, null=True)
    degree = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    college_name = models.CharField(max_length=200)
    area = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    passout_year = models.IntegerField()
    percentage = models.FloatField()
    resume = CloudinaryField('resume', resource_type='raw', folder='resumes/students')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Candidate(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    alternate_mobile = models.CharField(max_length=15, blank=True, null=True)
    branch = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    area = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    passout_year = models.IntegerField()
    experience_years = models.IntegerField()
    experience_details = models.TextField()
    resume = CloudinaryField('resume', resource_type='raw', folder='resumes/candidates')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
