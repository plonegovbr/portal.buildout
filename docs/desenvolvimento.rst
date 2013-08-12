=======================================
Ambiente de desenvolvimento
=======================================

Instalando o código do Portal
================================

Usando repositório
---------------------

Inicialmente é feito o clone deste buildout:
::

    cd ~
    git clone git@github.com:plonegovbr/portal.buildout.git portal.buildout


.. note :: Caso o comando acima apresente problemas -- provavelmente devido ao
           bloqueio da porta de ssh (22) na sua rede interna -- altere 
           **git@github.com:** por **https://github.com/**.



Para evitar conflitos com o Python utilizado pelo sistema operacional, cria-se
um virtualenv apartado do restante do sistema.
::

    cd ~/portal.buildout
    virtualenv py27
    source py27/bin/activate
    
.. note :: Apesar das instruções de instalação de bibliotecas e execução
           do virtualenv sobre o python da máquina para menor complexidade
           do procedimento, é recomendado o uso de uma nova instalação de
           Python 2.7, efetuando sobre ela esses procedimentos de
           instalação de bibliotecas e virtualenv.

Criamos um novo arquivo de configuração *buildout.cfg*, que extende o 
**development.cfg** para definir variáveis deste ambiente::

    [buildout]
    extends =
        development.cfg

    [remotes]
    plonegovbr = https://github.com/plonegovbr
    collective = https://github.com/collective
    plone = https://github.com/plone
    simplesconsultoria = https://github.com/simplesconsultoria

.. note :: Na configuração garantimos que todos os códigos hospedados no
           Github sejam baixados através de https e não de ssh. (Esta 
           alteração não é mandatória, mas é comum em redes que possuam
           um firewall impedindo acesso direto à Internet.)

E finalmente executa-se o buildout com as configurações para ambiente de
produção -- **buildout.cfg**::

    python bootstrap.py -c buildout.cfg
    ./bin/buildout -c buildout.cfg

Instalação no CentOS
-----------------------

Para instalação do Portal Modelo no CentOS 5, devido a diferenças de versões
das bibliotecas libxml e libxslt, é recomendada a instalação das versões
corretas através do próprio buildout.

.. note :: Essas instruções só devem ser seguidas para o caso de
           instalação em CentOS 5.

No **buildout.cfg** incluir o passo **[lxml]**: 
::
    [buildout]
    extends =
        development.cfg

    [lxml]
    recipe = z3c.recipe.staticlxml
    egg = lxml
    libxml2-url = xmlsoft.org/libxml2/libxml2-2.7.8.tar.gz
    libxslt-url = xmlsoft.org/libxml2/libxslt-1.1.26.tar.gz
    static-build = true
    force = false

No **buildout.d/base.cfg** incluir o passo **[lxml]** definido acima, antes
dos já existentes: 
::
    parts =
        lxml
        instance
        mkdir-chameleon
        zopepy

Inicialização e controle
==========================

A configuração presente no arquivo **development.cfg** utiliza apenas uma
instância -- sem configurações de :term:`ZEO` -- e ela, ao ser iniciada, ouvirá na
porta **8080** da sua máquina local.

Iniciando em modo foreground
------------------------------------

Para inicia a instância execute, na linha de comando::

    cd ~/portal.buildout
    ./bin/instance fg

O ambiente estará pronto para ser utilizado quando você vir a seguinte
mensagem na sua janela de terminal: **INFO Zope Ready to handle requests**.

.. note :: Esta mensagem, será precedida pela data e hora em que o ambiente
           ficou ativo, ex: **2013-05-22 11:38:39 INFO Zope Ready to handle
           requests**

Caso você feche a janela do terminal, o processo não mais estará ativo.


Iniciando em modo serviço (daemon)
------------------------------------

Caso você deseje iniciar a instância e mantê-la ativa mesmo depois de fechar
a janela de terminal, execute os seguintes comandos::

    cd ~/portal.buildout
    ./bin/instance start

Este comando retornará uma mensagem como **daemon process started, pid=32819**,
porém isto não significa que o ambiente está pronto. Para validar se o ambiente
está pronto utilize o comando :command:`tail` para listar as últimas linhas do log::

    tail -f var/log/instance.log 

Caso você feche a janela do terminal, o processo continuará ativo.
