from django.db import models
from students.models import Student
from teachers.models import Teacher

class Class(models.Model):
    SUBJECT_CHOICES = [
        ('MATH', 'Mathematics'),
        ('SCI', 'Science'),
        ('ENG', 'English'),
        ('HIST', 'History'),
        ('ART', 'Art'),
        ('PE', 'Physical Education'),
    ]

    name = models.CharField(max_length=100)  # e.g. "Grade 5 - Math"
    subject = models.CharField(max_length=4, choices=SUBJECT_CHOICES)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, related_name='classes')
    students = models.ManyToManyField(Student, related_name='classes', blank=True)
    room_number = models.CharField(max_length=10, blank=True)
    schedule = models.CharField(max_length=100, blank=True)  # e.g. "Mon/Wed 10-11am"
    start_date = models.DateField()

    def __str__(self):
        return self.name

# Create your models here.
