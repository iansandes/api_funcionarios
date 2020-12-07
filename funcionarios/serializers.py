from funcionarios.models import Funcionario
from rest_framework.serializers import ModelSerializer

class FuncionarioSerializer(ModelSerializer):
    class Meta:
        model = Funcionario
        fields = ["matricula", "nome", "salario"]