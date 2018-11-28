from django.forms import ModelForm
from .models import Atividade

class AtividadeForm(ModelForm):
    class Meta:
        model = Atividade
        fields = ['autor','titulo','descricao','horario','lab']
