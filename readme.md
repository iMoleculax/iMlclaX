# iMoleculaX
Este projeto tem o objetivo de desenvolvimento de um Sistema de Gerenciamento de Sequenciamento Genético.

O projeto inicial foi desenvolvido em Docker com Django, Biopython e PostgreSQL para seu ambiente de desenvolvimento em Python.

### Author: Macedo, Glener Diniz - Desenvolvedor Full Stack
### Data.: 29 de dezembro de 2025.

<p align="center">
  <img src="https://raw.githubusercontent.com/gdmacedo/Glener-Talk/main/developer-MacedoGDiniz.jpg" alt="Macedo, Glener Diniz">
</p>

### DESCRIÇÃO
A missão é desenvolver uma solução de software e infraestrutura, baseada na web, que organiza, armazena, processa e analisa a enorme quantidade de dados gerados pelo sequenciamento de DNA/RNA (NGS), permitindo o acompanhamento de projetos, a gestão de amostras biológicas (DNA/RNA) e a conversão de formatos de arquivo genéticos (GBK, FASTA), facilitando a identificação de variantes genéticas para diagnósticos médicos, pesquisa e medicina de precisão. 

<p align="center">
  <img src="https://raw.githubusercontent.com/gdmacedo/iBlogX/refs/heads/main/iBlogX/iClynikaX/templates/img/Contate-Nos.jpg" alt="configurar o Docker com Django e PostgreSQL para seu ambiente de desenvolvimento em Python">
</p>

### Componentes e Funcionalidades Principais:
- Gerenciamento de Amostras: Rastreamento de amostras biológicas (sangue, saliva) desde a coleta até a análise, incluindo seu armazenamento e metadados.
- Processamento de Dados (Bioinformática): Ferramentas para alinhar, montar e analisar os "reads" (fragmentos de DNA) gerados pelos sequenciadores (Illumina, PacBio, Nanopore).
- Armazenamento de Dados: Plataformas para guardar arquivos de sequência (como FASTQ, BAM, VCF) e anotações genéticas.
- Análise de Variantes: Identificação de mutações, SNPs e outras variações genéticas associadas a doenças ou características.
- Visualização e Relatórios: Ferramentas para visualizar genomas, transcriptomas e epigenomas, gerando relatórios compreensíveis para médicos e pesquisadores.
- Conversão de Formatos: Suporte para converter entre diferentes formatos de arquivo, como GBK para FASTA, essencial para a interoperabilidade.
- Controle de Projetos: Gerenciamento de fluxos de trabalho e permissões de usuários, facilitando a colaboração. 

## Neste projeto foi utilizado, as seguintes ferramentas:
 - Git, GitHub e .gitignore;
 - VS Code .vscode/settings.json;
 - Django com django-admin startproject;
 - Requirements.txt e .dockerignore;
 - Variáveis de ambiente com .env e o settings.py do projeto Django;
 - Dockerfile para gerar nossa imagem Docker Django;
 - Containers do Docker com Docker Compose - docker-compose.yml;
 - Comandos úteis em containers Docker.

<p align="center">
  <img src="https://raw.githubusercontent.com/iMoleculax/iMlclaX/refs/heads/main/imagens/Sequenciamento.jpeg" alt="Sistema de Gerenciamento de Sequenciamento Genético">
</p>

## Inicialização
1. Rode o script de setup, mas antes as dependencias: requirements-system.txt
   ```bash
   ./init.sh


<h3 style="margin-bottom: 0;">Créditos:</h3> 
<h5 style="margin-top: 0;">Macedo, Glener Diniz</h5>
<hr>
