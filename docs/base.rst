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

Tanto para o ambiente de desenvolvimento como o de produção, é necessário
que o computador onde será realizada a instalação tenha acesso à Internet.

Teste o acesso internet utilizando a ferramenta **wget** no terminal do Linux:
::

	wget -S --delete-after http://www.plone.org/


.. note :: O *-S* indica que o wget deverá retornar os cabeçalhos de
           conexão. 


Configurando proxy
~~~~~~~~~~~~~~~~~~~~

Para acesso à internet, caso seja necessário configurar servidores de Proxy,
digite no terminal:
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

Depois instalar os pacotes base (Ubuntu 12.10/Debian 7 Wheezy)::

    sudo aptitude install -y build-essential libssl-dev libxml2-dev libxslt1-dev libbz2-dev zlib1g-dev python-setuptools python-dev python-virtualenv libjpeg62-dev libreadline-gplv2-dev python-imaging wv poppler-utils git

No Debian 8 (Jessie), instalar::

    sudo apt-get install -y build-essential libssl-dev libxml2-dev libxslt1-dev libbz2-dev zlib1g-dev python-setuptools python-dev python-virtualenv libjpeg62-turbo-dev libreadline-gplv2-dev python-imaging python-pip wv poppler-utils git

No CentOS 7::

    yum install -y epel-release
    yum update -y
    yum install -y gcc gcc-g++ make tar bzip2 gzip openssl-devel libxml2-devel libxml2 libxslt-devel bzip2-libs zlib-devel python-setuptools python-devel python-virtualenv libjpeg-turbo-devel readline-devel python-imaging python-pip wv poppler-utils git
