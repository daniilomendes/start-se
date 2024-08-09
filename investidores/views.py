from django.shortcuts import render, redirect
from empresarios.models import Empresas, Documento, Metricas

def sugestao(request):
    if not request.user.is_authenticated:
        return redirect('/usuarios/logar')

    areas = Empresas.area_choices
    if request.method == 'GET':
        return render(request, 'sugestao.html', {'areas': areas})
    elif request.method == 'POST':
        tipo = request.POST.get('tipo')
        area = request.POST.getlist('area')
        valor = request.POST.get('valor')

        if tipo == 'C':
            empresas = Empresas.objects.filter(tempo_existencia='+5').filter(estagio="E")
        elif tipo == 'D':
            empresas = Empresas.objects.filter(tempo_existencia__in=['-6', '+6', '+1']).exclude(estagio="E")
        
        empresas = empresas.filter(area__in=area)

        empresas_selecionadas = []
        for empresa in empresas:
            percentual = float(valor) * 100 / float(empresa.valuation)

            if percentual >= 1:
                empresas_selecionadas.append(empresa)

        return render(request, 'sugestao.html', {'areas': areas, 'empresas': empresas_selecionadas})

def ver_empresa(request, id):
    empresa = Empresas.objects.get(id=id)
    documentos = Documento.objects.filter(empresa=empresa)
    metricas = Metricas.objects.filter(empresa=empresa)
    return render(request, 'ver_empresa.html', {'empresa': empresa, 'documentos': documentos, 'metricas': metricas})
