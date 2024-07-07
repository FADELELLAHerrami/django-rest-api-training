from django.urls import path
from .views import get_all_courses, get_one_course

urlpatterns = [
    path('courses/', get_all_courses, name = "course-list"),
    path('course/<int:pk>', get_one_course, name = "course")
]
