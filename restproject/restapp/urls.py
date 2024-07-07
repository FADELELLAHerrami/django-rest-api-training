from django.urls import path
from .views import get_all_courses

urlpatterns = [
    path('courses/', get_all_courses, name = "course-list"),
]
