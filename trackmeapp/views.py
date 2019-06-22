from django.shortcuts import render
from trackmeapp.models import Task
# from trackmeapp.serializers import TaskSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


'''
handle index
'''
def index(request, template_name='index.html'):
    return render(request, template_name)


'''
handle GET and POST requests, list of available Task or creating a new Task
'''

