from django.shortcuts import render, get_object_or_404, redirect
from .models import Equipamento
from .forms import EquipamentoForm



def loja_dinamica(request):
    
    equipamento_real = Equipamento.objects.all()

    bandeja = {
        # Passamos os produtos reais para o HTML
        'chave_estoque': equipamento_real, 
        # A função len() do Python não funciona muito bem com bancos de dados,
        # então o Django tem o método .count() para contar os itens!
        'total_itens': equipamento_real.count() 
    }

    # 4. Entregamos para o mesmo template de antes
    return render(request, 'meu_app/vitrine_inteligente.html', bandeja)

def painel_dashboard(request):
    todos_equipamentos = Equipamento.objects.all()
    
    # Podemos enviar mais dados estatísticos depois, por enquanto mandamos a lista
    bandeja = {
        'equipamentos': todos_equipamentos,
        'total': todos_equipamentos.count()
    }
    return render(request, 'meu_app/dashboard.html', bandeja)

def detalhe_equipamento(request, id):
    # O Django vai no banco e procura o Produto com o ID que veio na URL.
    # Se alguém digitar um ID que não existe (ex: /produto/999/), ele mostra a tela de Erro 404 em vez de quebrar o site!
    equipamento_escolhido = get_object_or_404(Equipamento, id=id)
    
    # Colocamos apenas ESSE produto na bandeja
    bandeja = {
        'equipamento': equipamento_escolhido
    }
    
    return render(request, 'meu_app/detalhe_equipamento.html', bandeja)




    # Adicione 'redirect' na primeira linha de importações do seu views.py


def cadastrar_equipamento(request):
    # Se o usuário clicou no botão "Salvar" (Enviou os dados)
    if request.method == 'POST':
        form = EquipamentoForm(request.POST)
        if form.is_valid():
            form.save() # Salva direto no banco de dados!
            return redirect('/loja-inteligente/') # Manda de volta pra vitrine
            
    # Se o usuário só acessou a página (Quer ver o formulário vazio)
    else:
        form = EquipamentoForm()

    # Manda o formulário para o HTML desenhar
    return render(request, 'meu_app/cadastrar_equipamento.html', {'form': form})

def editar_equipamento(request, id):
    # 1. Busca o produto no banco
    equipamento = get_object_or_404(Equipamento, id=id)
    
    # 2. Se for POST, salva as alterações. O "instance=produto" avisa que é uma edição!
    if request.method == 'POST':
        form = EquipamentoForm(request.POST, instance=equipamento)
        if form.is_valid():
            form.save()
            return redirect('/dashboard/') # Volta pro painel do gerente
    
    # 3. Se for GET, mostra o formulário já preenchido com os dados do produto
    else:
        form = EquipamentoForm(instance=equipamento)
        
    # Reutilizamos a MESMA tela de cadastro!
    return render(request, 'meu_app/cadastrar_equipamento.html', {'form': form})

def deletar_equipamento(request, id):
    equipamento = get_object_or_404(Equipamento, id=id)
    equipamento.delete() # O comando SQL DELETE invisível!
    return redirect('/dashboard/')
