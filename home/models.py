from django.db import models

# Create your models here.

from django.db import models


class Review(models.Model):
    employee_type = models.CharField(max_length=20)
    employment_year = models.CharField(max_length=50)
    salary = models.IntegerField(default=0)
    submission = models.ForeignKey(Demograph, related_name='submission', on_delete=models.CASCADE)

    def __str__(self):
        return self.employee_type

class Demograph(models.Model):
    gender = models.CharField(max_length=10)
    racial_group = models.CharField(max_length=50)

class Interview(models.Model):
    submission = models.ForeignKey(Demograph, related_name='submission', on_delete=models.CASCADE)

class Rating(models.Model):
    review = models.ForeignKey(Review, related_name='review', on_delete=models.CASCADE)

class Recommend(models.Model):
    interview = models.ForeignKey(Interview, related_name='interview', on_delete=models.CASCADE)

class InterviewFormat(models.Model):
    interview = models.ForeignKey(Interview, related_name='interview', on_delete=models.CASCADE)

class Specialization(models.Model):
    review = models.ForeignKey(Review, related_name='review', on_delete=models.CASCADE)
    job = models.CharField(max_length=50)
