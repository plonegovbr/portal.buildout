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

    $ cd ~/portal.buildout
    $ virtualenv py27
    $ source py27/bin/activate

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

    $ pip install -U setuptools==42.0.2
    $ python bootstrap.py
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
    .
    daemon process started, pid=3834

Porém isto não significa que o ambiente está pronto.
Para validar se o ambiente está pronto, utilize o comando :command:`tail` para listar as últimas linhas do log:

.. code-block:: console

    $ tail -f var/log/instance.log
    ...
    2018-08-31T12:13:30 INFO Zope Ready to handle requests

Se você fechar a janela do terminal, o processo continuará ativo.

Rodando o buildout de uma tag antiga de um pacote
=================================================

Para atender ao relato de `ter vários jobs de integração contínua em pacotes do IDG <https://github.com/plonegovbr/portalpadrao.release/issues/11>`_,
no fim da seção extends do buildout.cfg de todos os pacotes temos a seguinte linha:

.. code-block:: cfg

    https://raw.githubusercontent.com/plonegovbr/portal.buildout/master/buildout.d/versions.cfg

Hoje esse arquivo contém sempre as versões pinadas de um release a ser lançado (``master``).
Por esse motivo, quando é feito o checkout de uma tag mais antiga provavelmente você não conseguirá rodar o buildout.
Dessa forma, após fazer o checkout de uma tag antiga, recomendamos que adicione, na última linha do extends, o arquivo de versões do IDG compatível com aquela tag, presente no repositório `portalpadrao.release <https://github.com/plonegovbr/portalpadrao.release>`_.

Exemplo: você clonou o repositório do brasil.gov.portal na sua máquina, e deu checkout na tag 1.0.5.
Ao editar o buildout.cfg, ficaria dessa forma, já com a última linha adicionada:

.. code-block:: cfg

    extends =
        https://raw.github.com/collective/buildout.plonetest/master/test-4.3.x.cfg
        https://raw.github.com/collective/buildout.plonetest/master/qa.cfg
        http://downloads.plone.org.br/release/1.0.4/versions.cfg
        https://raw.githubusercontent.com/plonegovbr/portal.buildout/master/buildout.d/versions.cfg
        https://raw.githubusercontent.com/plone/plone.app.robotframework/master/versions.cfg
        https://raw.githubusercontent.com/plonegovbr/portalpadrao.release/master/1.0.5/versions.cfg

Para saber qual arquivo de versões é compatível, no caso do brasil.gov.portal, é simples pois é a mesma versão (no máximo um bug fix, por exemplo, brasil.gov.portal é 1.1.3 e o arquivo de versão é 1.1.3.1).

Para os demais pacotes, recomendamos comparar a data da tag do pacote e a data nos changelog entre uma versão e outra para adivinhar a versão compatível.
