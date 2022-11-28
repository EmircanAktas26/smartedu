from django.shortcuts import render
from . models import Course

# Create your views here.

def course_list(request):
    courses = Course.objects.all().order_by('-created')

    context = {
        'courses': courses
    }



    return render(request, 'courses.html',context)