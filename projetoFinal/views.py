from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . import models, forms 

# @login_required
def pagina(request):
    filme= models.Filme.objects.all()
    return render(request, 'paginainicial.html', {'filme':filme}) 

def resenha(request):
    resenha= models.Comentarios.objects.all()
    return render(request, 'resenha.html', {'resenha':resenha}) 

def conteudo(request):
    return render(request, 'conteudo.html') 

def cadastro(request):
    return render(request, 'cadastro.html') 

@login_required
def formulario(request):
    form= forms.Filmeform(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()

        return redirect('pagina')
    else:
        return render(request, 'form.html', {'Filme':form})

    
def comentarios(request):
    coment= forms.Coment(request.POST or None, request.FILES or None)

    if coment.is_valid():
        coment.save()

        return redirect('pagina')
    else:
        return render(request, 'comentarios.html', {'Comentarios':coment})   
    
def remove(request, id):
    remove = models.Comentarios.objects.get(id=id)
    remove.delete()
    return redirect('resenha')    