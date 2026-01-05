"""
===========================================================
Sistema de Gerenciamento de Sequenciamento Genético
Arquivo.: ./projetos/models.py
Módulo..: Aplicação Django - Modelos de Dados

Propósito:
    Definir as classes de modelo que representam as tabelas
    do sistema de gerenciamento de sequenciamento genético.

Contexto Scrum:
    Épico: Cadastro e Gestão de Projetos de Sequenciamento
    História de Usuário: #US-101 - Como pesquisador, quero
    registrar projetos de sequenciamento para organizar dados.
    Sprint: Sprint 3 (Jan/2026)

Responsável:
    Desenvolvedor: Macedo, Glener Diniz
    Revisão: Time de Desenvolvimento
    Product Owner: [Nome do PO]

Última atualização: 02/01/2026
===========================================================
"""
from django.db import models
from django.contrib.auth.models import User


class PrjetSqncmnto(models.Model):
    """
    Representa um projeto de sequenciamento genético dentro do sistema.
    """

    # Informações básicas
    descricao = models.CharField(
        max_length=200, unique=True, verbose_name="Descrição do Projeto")
    detalhe = models.TextField(blank=True, verbose_name="Detalhe")

    # Datas importantes
    dt_Criacao = models.DateTimeField(
        auto_now_add=True, verbose_name="Data de Criação")
    dt_Atualizacao = models.DateTimeField(
        auto_now=True, verbose_name="Última Atualização")
    dt_Inicio = models.DateField(
        null=True, blank=True, verbose_name="Data de Início")
    dt_Fim = models.DateField(null=True, blank=True,
                              verbose_name="Data de Conclusão")

    # Relacionamentos
    responsavel = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name="projetos_responsaveis",
        verbose_name="Responsável"
    )

    # Status do projeto
    STATUS_CHOICES = [
        ("Plnjdo", "Planejado"),
        ("EAndmnto", "Em andamento"),
        ("Concldo", "Concluído"),
        ("Cancldo", "Cancelado"),
    ]
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Plnjdo",
        verbose_name="Status"
    )

    # ✅ Novo campo para classificar o tipo de projeto
    TIPO_CHOICES = [
        ("TCC", "Trabalho de Conclusão de Curso"),
        ("Artigo", "Artigo Científico"),
        ("Dissertacao", "Dissertação"),
        ("Tese", "Tese"),
        ("Estudo", "Estudo"),
    ]
    tipo_projeto = models.CharField(
        max_length=20,
        choices=TIPO_CHOICES,
        default="Estudo",
        verbose_name="Tipo de Projeto"
    )

    # Metadados
    class Meta:
        db_table = "Projeto_Sequenciamento"
        ordering = ["-dt_Criacao"]
        verbose_name = "Projeto de Sequenciamento"
        verbose_name_plural = "Projetos de Sequenciamento"

    def __str__(self):
        return f"{self.descricao} ({self.status})"