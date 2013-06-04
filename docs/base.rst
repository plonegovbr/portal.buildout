==========================
Configurações Básicas
==========================

Pré-Requisitos
================

Para ambientes de desenvolvimento sugerimos:

    * Sistema Operacional: Debian 7.0 / Ubuntu 12.10
    * Memória Mínima: 1GB


Para ambientes de produção sugerimos:

    * Sistema Operacional: Debian 7.0 / Ubuntu 12.10
    * Memória Mínima: 2GB


Preparação do ambiente
==========================

Acesso internet
----------------------

Tanto para o ambiente de desenvolvimento como o de produção é necessário
que o computador onde será realizada a instalação deve ter acesso à Internet.

Teste o acesso internet utilizando a ferramenta **wget** no terminal do Linux:
::

	wget -S --delete-after http://www.plone.org/


.. note :: O *-S* indica que o wget deverá retornar os cabeçalhos de
           conexão. 


Configurando proxy
~~~~~~~~~~~~~~~~~~~~

Caso, para acesso à internet, seja necessário configurar servidores de Proxy,
no terminal digite:
::

	export http_proxy=http://<endereco>:<porta>
	export https_proxy=http://<endereco>:<porta>
	export ftp_proxy=http://<endereco>:<porta>

.. note :: Para servidores que necessitam de autenticação,
           substitua *<endereco>:<porta>* por 
           *<nome_usuario>:<senha>@<endereco>:<porta>*.


Pacotes do sistema
----------------------

Primeiramente atualizar os pacotes existentes::

    aptitude update && aptitude upgrade


Depois instalar os pacotes base::

    sudo aptitude install build-essential libssl-dev libxml2-dev libxslt1-dev libbz2-dev zlib1g-dev python-setuptools python-dev python-virtualenv libjpeg62-dev libreadline-gplv2-dev python-imaging wv poppler-utils git -y

