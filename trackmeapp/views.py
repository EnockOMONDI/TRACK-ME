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


# get all items
@api_view(['GET', 'POST'])
def get_post_items(request):
    if request.method == 'GET':
        puppies = Task.objects.all()
        serializer = TaskSerializer(puppies, many=True)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    # create a new item
    elif request.method == 'POST':
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

