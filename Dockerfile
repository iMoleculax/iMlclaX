#--------------------------------------------------------------------------------------------------
# Projeto.......: iMoleculaX - Sistema de Gerenciamento de Sequenciamento Genético.
# File..........: Dockerfile : Gera, Constroi nossa imagem, conforme a configuração abaixo.
# Author........: Macedo, Glener Diniz - Engenheiro de Software - Developer Full Stack
# Data Inicial..: 2025, Dezembro, 29 - Última Alteração: 2025-12-29
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
RUN adduser --disabled-password --no-create-home iMlclaXUser

# Copia a pasta "iMlclaX_App" e "scripts" para dentro do container.
COPY iMlclaX_App /iMlclaX_App
RUN chown -R iMlclaXUser:iMlclaXUser /iMlclaX_App


# Copia scripts
COPY scripts/ /scripts/

# Ajusta permissões
RUN chmod -R +x /scripts && \
    chown -R iMlclaXUser:iMlclaXUser /scripts


# Entra na pasta djangoapp no container
WORKDIR /iMlclaX_App

# A porta 8000 estará disponível para conexões externas ao container
# É a porta que vamos usar para o Django.
#EXPOSE 8000

# No caso de querer rodar na porta 8989
EXPOSE 8989

# RUN executa comandos em um shell dentro do container para construir a imagem. 
# O resultado da execução do comando é armazenado no sistema de arquivos da 
# imagem como uma nova camada.
# Agrupar os comandos em um único RUN pode reduzir a quantidade de camadas da 
# imagem e torná-la mais eficiente.
RUN python -m venv /_iMlclaX_AppW && \
    /_iMlclaX_AppW/bin/python -m pip install --upgrade pip && \
    /_iMlclaX_AppW/bin/pip install -r /iMlclaX_App/requirements.txt
#   /iMlclaX_App/bin/pip install --upgrade pip && \


# Estava assim. Mas para achar o erro foi realizado linha por linha, conforme acima.
#   RUN python -m venv /_iMlclaX_AppW && \
#  /iMlclaX_App/bin/pip install --upgrade pip && \
#  /_iMlclaX_AppW/Scripts/python -m pip install --upgrade pip && \
#  /_iMlclaX_AppW/Scripts/pip install -r /iMlclaX_App/_iMlclaX_AppApp/requirements.txt && \

#RUN adiMlclaXUser --disabled-password --no-create-home iMlclaXUser && \
#RUN mkdir -p /data/web/static && \
#    mkdir -p /data/web/media && \
#    mkdir -p /data/web/static /data/web/media && \
#    chown -R iMlclaXUser:iMlclaXUser /data/web/static /data/web/media && \
#    chown -R iMlclaXUser:iMlclaXUser /_iMlclaX_AppW && \
#    chown -R iMlclaXUser:iMlclaXUser /data/web/static && \
#    chown -R iMlclaXUser:iMlclaXUser /data/web/media && \
#    chmod -R 755 /data/web/static /data/web/media && \
#    chmod -R 755 /data/web/static && \
#    chmod -R 755 /data/web/media 
    # chmod -R +x /scripts

# Todas do útlimo RUN, trocadas pelas de baixo:

# Cria diretórios de static e media e ajusta permissões
RUN mkdir -p /data/web/static /data/web/media \
    && chown -R iMlclaXUser:iMlclaXUser /data/web/static /data/web/media /_iMlclaX_AppW \
    && chmod -R 755 /data/web/static /data/web/media

RUN mkdir -p /data/web/static /data/web/media && \
    chown -R iMlclaXUser:iMlclaXUser /data/web/static /data/web/media && \
    chmod -R 755 /data/web/static /data/web/media

# Adiciona a pasta scripts e iMlclaX_App/Scritps 
# no $PATH do container.
# ENV PATH="/scripts:/iMlclaX_App/Scripts:$PATH"
ENV PATH="/_iMlclaX_AppW/bin:$PATH"


# Muda o usuário para iMlclaXUser, definidno que o container roda como esse usuário.
USER iMlclaXUser

# Executa o arquivo scripts/commands.sh
CMD ["/scripts/commands.sh"]