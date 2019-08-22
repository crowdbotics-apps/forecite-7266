from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django import forms
from .models import Submission, Review, Interview, Rating, Recommend

class AdminSubmissionChangeForm(forms.ModelForm):
  class Meta:
    model = Submission
    fields = ('gender', 'company',)
class AdminSubmissionCreationForm(forms.ModelForm):
  class Meta:
    model = Submission
    fields = ('gender', 'company',)

class AdminReviewChangeForm(forms.ModelForm):
  class Meta:
    model = Review
    fields = ('submission', 'employee_type', 'employment_year', 'salary',)
class AdminReviewCreationForm(forms.ModelForm):
  class Meta:
    model = Review
    fields = ('submission', 'employee_type', 'employment_year', 'salary',)

class AdminInterviewChangeForm(forms.ModelForm):
  class Meta:
    model = Interview
    fields = ('submission', 'phone', 'description',)
class AdminInterviewCreationForm(forms.ModelForm):
  class Meta:
    model = Interview
    fields = ('submission', 'industry', 'job_title', 'phone', 'description',)

class AdminRatingChangeForm(forms.ModelForm):
  class Meta:
    model = Rating
    fields = ('review', 'score',)
class AdminRatingCreationForm(forms.ModelForm):
  class Meta:
    model = Rating
    fields = ('review', 'score',)

class AdminRecommendChangeForm(forms.ModelForm):
  class Meta:
    model = Recommend
    fields = ('interview', 'score',)
class AdminRecommendCreationForm(forms.ModelForm):
  class Meta:
    model = Recommend
    fields = ('interview', 'score',)
