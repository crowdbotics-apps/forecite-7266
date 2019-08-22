from django.contrib import admin
from .models import Submission, Review, Interview, Rating, Recommend
from .forms import AdminSubmissionChangeForm, AdminSubmissionCreationForm, \
                   AdminReviewChangeForm, AdminReviewCreationForm, \
                   AdminInterviewChangeForm, AdminInterviewCreationForm, \
                   AdminRatingChangeForm, AdminRatingCreationForm, \
                   AdminRecommendChangeForm, AdminRecommendCreationForm

class SubmissionAdmin(admin.ModelAdmin):
  form = AdminSubmissionChangeForm
  add_form = AdminSubmissionCreationForm

class ReviewAdmin(admin.ModelAdmin):
  form = AdminRecommendChangeForm
  add_form = AdminReviewCreationForm

class InterviewAdmin(admin.ModelAdmin):
  form = AdminInterviewChangeForm
  add_form = AdminInterviewCreationForm

class RatingAdmin(admin.ModelAdmin):
  form = AdminRatingChangeForm
  add_form = AdminRatingCreationForm

class RecommendAdmin(admin.ModelAdmin):
  form = AdminRecommendChangeForm
  add_form = AdminRecommendCreationForm

admin.site.register(Submission, SubmissionAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Interview, InterviewAdmin)
admin.site.register(Rating, RatingAdmin)
admin.site.register(Recommend, RecommendAdmin)