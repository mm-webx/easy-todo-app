from rest_framework import serializers

from todo.models import Todo


class TodoSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Todo
        fields = ('id', 'title', 'is_completed')