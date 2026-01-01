from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from usuarios.models import Perfil, UfEstados


@login_required
def fnct_dashboard(request):
    if request.method == "GET":
        slctPrfl_User = Perfil.objects.get(user=request.user)

        return render(request, 'usuarios/dashboard.html', {'Perfil_User': slctPrfl_User})

    elif request.method == "POST":
        slctPrfl_User = Perfil.objects.get(user=request.user)
        return render(request, 'usuarios/dashboard.html', {'Perfil_User': slctPrfl_User})
