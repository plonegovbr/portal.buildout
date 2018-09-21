=====================
Configurações Básicas
=====================

Pré-Requisitos
==============

Para ambientes de desenvolvimento sugerimos:

* Sistema Operacional: Debian 9.0 / Ubuntu 18.04 LTS
* Memória Mínima: 2GB

Para ambientes de produção sugerimos:

* Sistema Operacional: Ubuntu 18.04 LTS
* Memória Mínima: 4GB

Preparação do ambiente
======================

Acesso internet
---------------

Tanto para o ambiente de desenvolvimento como o de produção, é necessário
que o computador onde será realizada a instalação tenha acesso à Internet.

Teste o acesso internet utilizando a ferramenta :command:`wget` no terminal do Linux:

.. code-block:: console

	$ wget --server-response --delete-after https://plone.org/

Configurando proxy
~~~~~~~~~~~~~~~~~~

Para acesso à internet, caso seja necessário configurar servidores de proxy, digite no terminal:

.. code-block:: console

	$ export http_proxy=http://<endereco>:<porta>
	$ export https_proxy=http://<endereco>:<porta>
	$ export ftp_proxy=http://<endereco>:<porta>

.. hint::
    Para servidores que necessitam de autenticação,
    substitua *<endereco>:<porta>* por *<nome_usuario>:<senha>@<endereco>:<porta>*.

Pacotes do sistema
------------------

Primeiramente atualizar os pacotes existentes e depois instalar os pacotes base.

No Ubuntu 18.04 LTS:

.. code-block:: console

    $ sudo apt update && sudo apt upgrade -y
    $ sudo apt install -y build-essential libssl-dev libxml2-dev libxslt1-dev libbz2-dev zlib1g-dev python-setuptools python-dev python-virtualenv libjpeg62-dev libreadline-gplv2-dev python-pil wv poppler-utils git

No Ubuntu 16.04 LTS:

.. code-block:: console

    $ sudo apt update && sudo apt upgrade -y
    $ sudo apt install -y build-essential libssl-dev libxml2-dev libxslt1-dev libbz2-dev zlib1g-dev python-setuptools python-dev python-virtualenv libjpeg62-dev libreadline-gplv2-dev python-imaging python-pip wv poppler-utils git libldap2-dev libsasl2-dev libssl-dev

No Debian 9:

.. code-block:: console

    $ sudo apt update && sudo apt upgrade -y
    $ sudo apt install -y build-essential libssl-dev libxml2-dev libxslt1-dev libbz2-dev zlib1g-dev python-setuptools python-dev python-virtualenv libjpeg62-turbo-dev libreadline-gplv2-dev python-imaging python-pip wv poppler-utils git

No CentOS 7:

.. code-block:: console

    $ sudo yum install -y epel-release && sudo yum update -y
    $ sudo yum install -y gcc gcc-g++ make tar bzip2 gzip openssl-devel libxml2-devel libxml2 libxslt-devel bzip2-libs zlib-devel python-setuptools python-devel python-virtualenv libjpeg-turbo-devel readline-devel python-imaging python-pip poppler-utils git openldap-devel

Recomendamos fortemente que instale o pacote wv usando o gerenciador de pacotes/EPEL;
caso não seja possível você pode instalar manualmente pela URL:

.. code-block:: console

    $ sudo yum install -y https://kojipkgs.fedoraproject.org//packages/wv/1.2.7/2.el6/x86_64/wv-1.2.7-2.el6.x86_64.rpm
