from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from funcionarios.serializers import FuncionarioSerializer
from funcionarios.models import Funcionario

class FuncionarioApiView(viewsets.ViewSet):
    #Método Post
    def create(self, request):
        salario = 0
        queryset = ""
        for request in request.data:
            funcionario = Funcionario.objects.create(
                matricula=request["matricula"],
                nome=request["nome"],
                salario=request["salario"]
            )

            if funcionario.salario > salario:
                salario = funcionario.salario
                queryset = funcionario

        serializer = FuncionarioSerializer(queryset)
        return Response(serializer.data)



