from rest_framework import serializers
from trackmeapp.models import Task



# transforming objects to JSON and vice versa



class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('item_id', 'title', 'description', 'created_at', 'comp_date', 'status')
