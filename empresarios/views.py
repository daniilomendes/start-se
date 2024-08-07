from django.shortcuts import render, redirect
from .models import Empresas
from django.contrib import messages
from django.contrib.messages import constants

def cadastrar_empresa(request):
    if request.method == "GET":
        return render(request, 'cadastrar_empresa.html', {'tempo_existencia': Empresas.tempo_existencia_choices, 
                                                          'area': Empresas.area_choices})
    elif request.method == "POST":
        nome = request.POST.get('nome')
        cnpj = request.POST.get('cnpj')
        site = request.POST.get('site')
        tempo_existencia = request.POST.get('tempo_existencia')
        descricao = request.POST.get('descricao')
        data_final = request.POST.get('data_final')
        percentual_equity = request.POST.get('percentual_equity')
        estagio = request.POST.get('estagio')
        area = request.POST.get('area')
        publico_alvo = request.POST.get('publico_alvo')
        valor = request.POST.get('valor')
        pitch = request.FILES.get('pitch')
        logo = request.FILES.get('logo')

        if nome == '' or cnpj == '' or site == '' or tempo_existencia == '' or descricao == '' or data_final == '' or percentual_equity == 0 or valor == 0:
            messages.add_message(request, constants.ERROR, 'Preencha todos os campos!')
            return redirect('/empresarios/cadastrar_empresa')

        try:
            empresa = Empresas(
                user=request.user,
                nome=nome,
                cnpj=cnpj,
                site=site,
                tempo_existencia=tempo_existencia,
                descricao=descricao,
                data_final_captacao=data_final,
                percentual_equity=percentual_equity,
                estagio=estagio,
                area=area,
                publico_alvo=publico_alvo,
                valor=valor,
                pitch=pitch,
                logo=logo
            )
            
            empresa.save()
        except:
            messages.add_message(request, constants.ERROR, 'Erro interno do servidor.')
            return redirect('/empresarios/cadastrar_empresa')

        messages.add_message(request, constants.SUCCESS, 'Empresa criada com sucesso')
        return redirect('/empresarios/cadastrar_empresa')