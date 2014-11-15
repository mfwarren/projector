from .models import Task

from rest_framework import serializers


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = (
            'id', 'description', 'assignee', 'project', 'is_enabled', 'group',
            'actual_duration', 'updated_at', 'created_at'
        )
        read_only_fields = ('created_at', 'updated_at')
