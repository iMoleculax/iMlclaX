from django.urls import path
from . import views


urlpatterns = [
    path('', views.fnct_Prjtos, name='url_Prjtos'),
    path('all/', views.fnct_prjtsAll, name='url_prjtsAll'),
    path('mAnalises/', views.fnct_mAnalises, name='url_mAnalises'),
    path('meusProjetos/', views.fnct_mPrjtos, name='url_mPrjtos'),
    path('Colaboracoes/', views.fnct_Clbracoes, name='url_Clbrcoes'),
]
