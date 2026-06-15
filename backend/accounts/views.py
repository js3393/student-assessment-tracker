from random import randint

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'User' : 'Jose',
        'Classroom' : 'Coding 101',
        'num_students' : randint(7, 30)
    }
    return render(request, 'index.html', context=context)
