from django.db import models

# Create your models here.

from django.db import models

class CustomText(models.Model):
    title = models.CharField(max_length=150)

    def __str__(self):
        return self.title

    @property
    def api(self):
        return f'/api/v1/customtext/{self.id}/'

    @property
    def field(self):
        return 'title'


class HomePage(models.Model):
    body = models.TextField()

    @property
    def api(self):
        return f'/api/v1/homepage/{self.id}/'

    @property
    def field(self):
        return 'body'


class Submission(models.Model):
    GENDERS = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('unsure', 'Not Sure')
    ]
    gender = models.CharField(max_length=10, choices=GENDERS)
    racial_group = models.CharField(max_length=50)
    company = models.CharField(max_length=100)
    education = models.CharField(max_length=200)
    industry = models.CharField(max_length=50)

class Review(models.Model):
    employee_type = models.CharField(max_length=20)
    employment_year = models.CharField(max_length=50)
    salary = models.IntegerField(default=0)
    submission = models.ForeignKey(Submission, related_name='review_submission', on_delete=models.CASCADE)

    def __str__(self):
        return self.employee_type

class Interview(models.Model):
    submission = models.ForeignKey(Submission, related_name='interview_submission', on_delete=models.CASCADE)
    industry = models.CharField(max_length=50)
    job_title = models.CharField(max_length=50)
    difficulty = models.CharField(max_length=50)
    questions = models.TextField()
    phone = models.CharField(max_length=20)
    offer = models.CharField(max_length=100)
    description = models.TextField()

class Rating(models.Model):
    review = models.ForeignKey(Review, related_name='rating_review', on_delete=models.CASCADE)
    score = models.IntegerField(default=1)

class Recommend(models.Model):
    interview = models.ForeignKey(Interview, related_name='recommend_interview', on_delete=models.CASCADE)
    score = models.IntegerField(default=1)
    
