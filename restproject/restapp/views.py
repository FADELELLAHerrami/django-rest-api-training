from django.shortcuts import render
from .models import Course
from django.http import JsonResponse



# Create your views here.
def get_all_courses(request):
    courses = Course.objects.all()
    data = {"courses": list(courses.values())}
    return JsonResponse(data)