from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Atividade
from .forms import AtividadeForm
from django.urls import reverse
# Create your views here.

def atividades(request):
    atividades = Atividade.objects.all()
    return render(request, 'atividades.html',{'atividades':atividades} )

def atividade(request, atividade_id):
    atividade = get_object_or_404(Atividade, pk=atividade_id)
    return render(request,'atividade.html',{'atividade':atividade})

def atividade_edit(request, atividade_id):
    atividade = get_object_or_404(Atividade, pk=atividade_id)
    if request.method =='POST':
        form = AtividadeForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('atividades'))
    else:
        form = AtividadeForm(instance=atividade)
    return render(request,'atividade_form.html',{'form': form})

