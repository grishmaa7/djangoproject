from django.db import models

class Teacher(models.Model):
    SUBJECT_CHOICES = [
        ('MATH', 'Mathematics'),
        ('SCI', 'Science'),
        ('ENG', 'English'),
        ('HIST', 'History'),
        ('ART', 'Art'),
        ('PE', 'Physical Education'),
    ]

    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True)
    subject = models.CharField(max_length=4, choices=SUBJECT_CHOICES)
    qualification = models.CharField(max_length=100, blank=True)
    years_of_experience = models.IntegerField(default=0)
    hire_date = models.DateField()
    salary = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

# Create your models here.
