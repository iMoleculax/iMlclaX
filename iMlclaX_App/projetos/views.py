from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from usuarios.models import Perfil

# ============================================================================================
# Acessa todos os projetos
# ============================================================================================


@login_required
def fnct_prjtsAll(request):
    if request.method == "GET":
        parmetros = {
            'slctPrfl_User': Perfil.objects.get(user=request.user),
        }

        return render(request, 'Projetos.html', parmetros)


# ============================================================================================
# Acessa todos os projetos
# ============================================================================================
@login_required
def fnct_Prjtos(request):
    if request.method == "GET":
        parmetros = {
            'slctPrfl_User': Perfil.objects.get(user=request.user),
        }

        return render(request, 'Projetos.html', parmetros)


# ============================================================================================
# Acessa todos os projetos do usuário que esteja logado.
# ============================================================================================
@login_required
def fnct_mPrjtos(request):
    if request.method == "GET":
        parmetros = {
            'slctPrfl_User': Perfil.objects.get(user=request.user.id)
        }

        return render(request, 'meusProjetos.html', parmetros)


# ============================================================================================
# Acessa todos as analises do usuário que esteja logado.
# ============================================================================================
@login_required
def fnct_mAnalises(request):
    if request.method == "GET":
        parmetros = {
            'slctPrfl_User': Perfil.objects.get(user=request.user.id)
        }

        return render(request, 'mAnalises.html', parmetros)


# ============================================================================================
# Acessa todos as analises do usuário que esteja logado.
# ============================================================================================
@login_required
def fnct_Clbracoes(request):
    if request.method == "GET":
        slctUser_Prfil = Perfil.objects.get(user=request.user.id)
        parmetros = {
            'slctPrfl_User': slctUser_Prfil,
        }

        return render(request, 'Colaboracoes.html', parmetros)
