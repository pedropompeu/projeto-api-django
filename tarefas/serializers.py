from rest_framework import serializers
from .models import Tarefa

class TarefaSerializer(serializers.ModelSerializer):
    utilizador = serializers.StringRelatedField(source='utilizador.username', read_only=True)
    class Meta:
        model = Tarefa
        fields = '__all__'
