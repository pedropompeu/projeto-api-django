from rest_framework import viewsets
from .models import Tarefa
from .serializers import TarefaSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend


class TarefaViewSet(viewsets.ModelViewSet):
    serializer_class = TarefaSerializer
    permission_classes = [IsAuthenticated]

    filter_backends = [DjangoFilterBackend, SearchFilter]
    
    filterset_fields = ['concluida'] 
    search_fields = ['titulo', 'descricao'] 

    def get_queryset(self):
        utilizador = self.request.user
        return Tarefa.objects.filter(utilizador=utilizador).order_by('-data_criacao')

    def perform_create(self, serializer):
        serializer.save(utilizador=self.request.user)