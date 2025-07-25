from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Tarefa

class TarefaAPITests(APITestCase):

    def setUp(self):
        self.utilizador1 = User.objects.create_user(username='utilizador1', password='password123')
        Tarefa.objects.create(utilizador=self.utilizador1, titulo='Tarefa importante de hoje', concluida=False)
        Tarefa.objects.create(utilizador=self.utilizador1, titulo='Tarefa concluída', concluida=True)

        self.utilizador2 = User.objects.create_user(username='utilizador2', password='password123')
        Tarefa.objects.create(utilizador=self.utilizador2, titulo='Tarefa do outro utilizador')

    def test_utilizador_nao_autenticado_nao_pode_ver_tarefas(self):
        url = reverse('tarefa-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_utilizador_autenticado_ve_apenas_suas_tarefas(self):
        self.client.force_authenticate(user=self.utilizador1)
        url = reverse('tarefa-list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2) 
        
    def test_filtrar_tarefas_por_concluidas(self):
        self.client.force_authenticate(user=self.utilizador1)
        url = reverse('tarefa-list') + '?concluida=true'
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['titulo'], 'Tarefa concluída')

    def test_pesquisar_tarefas_por_titulo(self):
        self.client.force_authenticate(user=self.utilizador1)
        url = reverse('tarefa-list') + '?search=importante'
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['titulo'], 'Tarefa importante de hoje')