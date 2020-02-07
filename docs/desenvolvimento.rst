===========================
Ambiente de desenvolvimento
===========================

Instalando o código do Portal
=============================

Usando repositório
------------------

Inicialmente é feito o clone deste *buildout*:

.. code-block:: console

    $ cd ~
    $ git clone git@github.com:plonegovbr/portal.buildout.git


.. note::
    Caso o comando acima apresente problemas -- provavelmente devido ao bloqueio da porta de SSH (22) na sua rede interna -- altere **git@github.com:** por **https://github.com/**.

Virtualenv
----------

Para evitar conflitos com o Python utilizado pelo sistema operacional,
cria-se um ambiente virtual (:command:`virtualenv`) apartado do restante do sistema.
Execute:

.. code-block:: console

    $ virtualenv --version

Se a versão for menor que 1.10 (por exemplo na distribuição LTS do Ubuntu 12.04),
você precisa executar o :command:`virtualenv` da seguinte forma:

.. code-block:: console

    $ cd ~/portal.buildout
    $ virtualenv --setuptools py27
    $ source py27/bin/activate

Se for maior ou igual a 1.10,
o comando :command:`virtualenv` não necessita do parâmetro *--setuptools* como indicado acima:

.. code-block:: console

    $ cd ~/portal.buildout
    $ virtualenv py27
    $ source py27/bin/activate

Para entender a motivação dessa diferença,
leia a `documentação <https://github.com/plonegovbr/portal.buildout/issues/41>`_.

.. note::
    Apesar das instruções de instalação de bibliotecas e execução do :command:`virtualenv` sobre o Python da máquina,
    para menor complexidade do procedimento é recomendado o uso de uma nova instalação de Python 2.7,
    efetuando sobre ela esses procedimentos de instalação de bibliotecas e :command:`virtualenv`.

Criar um novo arquivo de configuração *buildout.cfg*,
que estende o **development.cfg** para definir variáveis deste ambiente

.. code-block:: ini

    [buildout]
    extends =
        development.cfg

    [remotes]
    plonegovbr = https://github.com/plonegovbr
    collective = https://github.com/collective
    plone = https://github.com/plone
    simplesconsultoria = https://github.com/simplesconsultoria

.. note::
    Na configuração garantimos que todos os códigos hospedados no :term:`GitHub` sejam baixados através de HTTPS e não de SSH -- esta alteração não é obrigatória,
    mas é comum em redes que possuam um *firewall* impedindo acesso direto à Internet.

E finalmente executa-se o :command:`buildout` com as configurações para ambiente de produção -- **buildout.cfg**

.. code-block:: console

    $ python bootstrap.py --setuptools-version=42.02 --buildout-version=2.13.2
    $ bin/buildout

.. warning::
    **Não execute** o seu buildout com :command:`sudo`:
    dessa forma, seu virtualenv será `ignorado <http://askubuntu.com/a/478001>`_ e ocorrerá todo tipo de erro de dependências da sua instância com as do Python do sistema.

Instalação com Docker
---------------------

Para instalação use o docker-compose ou crie com docker como o `manual <https://docs.plone.org/manage/docker/docs/index.html>`_.

Um exemplo de **docker-compose.yml**.

.. code-block:: yaml

    version: "2"
    services:
      haproxy:
    	 image: eeacms/haproxy
    	 ports:
    	 - 80:5000
    	 - 1936:1936
    	 depends_on:
    	 - plone
    	 environment:
    	   BACKENDS: "plone"
    	   BACKENDS_PORT: "8080"
    	   DNS_ENABLED: "True"

      plone:
    	 image: plonegovbr/plonegovbr
    	 depends_on:
    	 - zeoserver
    	 environment:
    	 - ZEO_ADDRESS=zeoserver:8100

      zeoserver:
    	 image: plonegovbr/plonegovbr
    	 command: zeoserver
    	 volumes:
    	 - data:/data

    volumes:
      data:

Com o comando:

.. code-block:: shell

    $ docker-compose up -d

Irá criar um serviço de :term:`HAProxy` que ira balancear os backends e um :term:`ZEO` server.

Inicialização e controle
========================

A configuração presente no arquivo **development.cfg** utiliza apenas uma instância -- sem configurações de :term:`ZEO` -- e ela, ao ser iniciada, ouvirá na porta **8080** da sua máquina local.

Iniciando em modo *foreground*
------------------------------

Para iniciar a instância em modo *foreground*, execute na linha de comando:

.. code-block:: console

    $ cd ~/portal.buildout
    $ bin/instance fg

O ambiente estará pronto para ser utilizado quando você visualizar a seguinte mensagem na sua janela de terminal:
**INFO Zope Ready to handle requests**.

.. note::
    Esta mensagem, será precedida pela data e hora em que o ambiente ficou ativo,
    ex: **2013-05-22 11:38:39 INFO Zope Ready to handle requests**

Se você fechar a janela do terminal, o processo não mais estará ativo.

Iniciando em modo serviço (daemon)
----------------------------------

Caso você deseje iniciar a instância e mantê-la ativa mesmo depois de fechar a janela de terminal,
execute os seguintes comandos:

.. code-block:: console

    $ cd ~/portal.buildout
    $ bin/instance start

Este comando retornará uma mensagem como **daemon process started, pid=32819**,
porém isto não significa que o ambiente está pronto.
Para validar se o ambiente está pronto, utilize o comando :command:`tail` para listar as últimas linhas do log:

.. code-block:: console

    $ tail -f var/log/instance.log

Se você fechar a janela do terminal, o processo continuará ativo.
