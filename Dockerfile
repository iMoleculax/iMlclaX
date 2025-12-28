#--------------------------------------------------------------------------------------------------
# Projeto.......: iBlogX - Blog para um clínica veterinária.
# File..........: Dockerfile : Gera, Constroi nossa imagem, conforme a configuração abaixo.
# Author........: Macedo, Glener Diniz - Engenheiro de Software - Developer Full Stack
# Data Inicial..: 2025, Dezembro, 23 - Última Alteração: 2025-12-23
#--------------------------------------------------------------------------------------------------

FROM python:3.14.2-alpine3.23
LABEL mantainer="gdmacedo@hotmail.com"

# Essa variável de ambiente é usada para controlar se o Python deve 
# gravar arquivos de bytecode (.pyc) no disco. 1 = Não, 0 = Sim
ENV PYTHONDONTWRITEBYTECODE 1

# Define que a saída do Python será exibida imediatamente no console ou em 
# outros dispositivos de saída, sem ser armazenada em buffer.
# Em resumo, você verá os outputs do Python em tempo real.
ENV PYTHONUNBUFFERED 1


# Cria usuário antes de mexer em permissões 
RUN adduser --disabled-password --no-create-home duser

# Copia a pasta "iBlogX" e "scripts" para dentro do container.
COPY iBlogX /iBlogX
RUN chown -R duser:duser /iBlogX

# Copia scripts
COPY scripts/ /scripts/

# Ajusta permissões
RUN chmod -R +x /scripts && \
    chown -R duser:duser /scripts


# Entra na pasta djangoapp no container
WORKDIR /iBlogX

# A porta 8000 estará disponível para conexões externas ao container
# É a porta que vamos usar para o Django.
#EXPOSE 8000

# No caso de querer rodar na porta 8888
EXPOSE 8888

# RUN executa comandos em um shell dentro do container para construir a imagem. 
# O resultado da execução do comando é armazenado no sistema de arquivos da 
# imagem como uma nova camada.
# Agrupar os comandos em um único RUN pode reduzir a quantidade de camadas da 
# imagem e torná-la mais eficiente.
RUN python -m venv /_iBlogXW 
#  /iBlogX/bin/pip install --upgrade pip && \
RUN  /_iBlogXW/bin/python -m pip install --upgrade pip 
RUN  /_iBlogXW/bin/pip install -r /iBlogX/requirements.txt

# Estava assim. Mas para achar o erro foi realizado linha por linha, conforme acima.
#   RUN python -m venv /_iBlogXW && \
#  /iBlogX/bin/pip install --upgrade pip && \
#  /_iBlogXW/Scripts/python -m pip install --upgrade pip && \
#  /_iBlogXW/Scripts/pip install -r /iBlogX/_iBlogXApp/requirements.txt && \

#RUN adduser --disabled-password --no-create-home duser && \
RUN mkdir -p /data/web/static && \
    mkdir -p /data/web/media && \
    mkdir -p /data/web/static /data/web/media && \
    chown -R duser:duser /data/web/static /data/web/media && \
    chown -R duser:duser /_iBlogXW && \
    chown -R duser:duser /data/web/static && \
    chown -R duser:duser /data/web/media && \
    chmod -R 755 /data/web/static /data/web/media && \
    chmod -R 755 /data/web/static && \
    chmod -R 755 /data/web/media 
  # chmod -R +x /scripts

RUN mkdir -p /data/web/static /data/web/media && \
    chown -R duser:duser /data/web/static /data/web/media && \
    chmod -R 755 /data/web/static /data/web/media

# Adiciona a pasta scripts e iBlogX/bin 
# no $PATH do container.
ENV PATH="/scripts:/iBlogX/bin:$PATH"

# Muda o usuário para duser
USER duser

# Executa o arquivo scripts/commands.sh
CMD ["/scripts/commands.sh"]