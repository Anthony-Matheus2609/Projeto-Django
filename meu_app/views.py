from django.shortcuts import render, get_object_or_404, redirect
from .models import Equipamento
from .forms import EquipamentoForm

def painel_dashboard(request):
    todos_equipamentos = Equipamento.objects.all()
    
    
    bandeja = {
        'equipamentos': todos_equipamentos,
        'total': todos_equipamentos.count()
    }
    return render(request, 'dashboard.html', bandeja)

def detalhe_equipamento(request, id):
    equipamento_escolhido = get_object_or_404(Equipamento, id=id)
    
    
    bandeja = {
        'equipamento': equipamento_escolhido
    }
    
    return render(request, 'meu_app/detalhe_equipamento.html', bandeja)




    


def cadastrar_equipamento(request):
    
    if request.method == 'POST':
        form = EquipamentoForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('/loja-inteligente/') 
            
    
    else:
        form = EquipamentoForm()

    
    return render(request, 'meu_app/cadastrar_equipamento.html', {'form': form})

def editar_equipamento(request, id):
    equipamento = get_object_or_404(Equipamento, id=id)
    
    
    if request.method == 'POST':
        form = EquipamentoForm(request.POST, instance=equipamento)
        if form.is_valid():
            form.save()
            return redirect('/dashboard/') 
    
    
    else:
        form = EquipamentoForm(instance=equipamento)
        
    
    return render(request, 'meu_app/cadastrar_equipamento.html', {'form': form})

def deletar_equipamento(request, id):
    equipamento = get_object_or_404(Equipamento, id=id)
    equipamento.delete() 
    return redirect('/dashboard/')