from django.shortcuts import render
from .models import Course
from django.http import JsonResponse



# Create your views here.
def get_all_courses(request):
    courses = Course.objects.all()
    data = {"courses": list(courses.values())}
    return JsonResponse(data)
def get_one_course(request, pk):
    course = Course.objects.get(pk=pk)
    data = {
        'id': course.id,
        'title': course.title,
        'description': course.desc,
        'published': course.active
    }
    return JsonResponse(data)