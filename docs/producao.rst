=======================================
Ambiente de produção
=======================================

Criar Usuário 
===============

Vamos criar um usuário para rodarmos o Plone.::

    adduser --system --shell /bin/bash plone
    addgroup plone
    adduser plone plone

A partir de agora usaremos o usuário **plone**:
::

    su - plone


Instalando o Portal
==============================

Usando repositório
---------------------

Inicialmente é feito o clone deste buildout:
::

    cd /opt/
    git clone git@github.com:plonegovbr/portal.buildout.git portal.buildout


.. note :: Caso o comando acima apresente problemas -- provavelmente devido ao
           bloqueio da porta de ssh (22) na sua rede interna -- altere 
           **git@github.com:** por **https://github.com/**.


Ajuste as permissões::

	chown -R plone:plone portal.buildout

Para evitar conflitos com o Python utilizado pelo sistema operacional, cria-se
um virtualenv apartado do restante do sistema.
::

    cd /opt/portal.buildout
    virtualenv py27
    source py27/bin/activate
    
.. note :: Apesar das instruções de instalação de bibliotecas e execução
           do virtualenv sobre o python da máquina para menor complexidade
           do procedimento, é recomendado o uso de uma nova instalação de
           Python 2.7, efetuando sobre ela esses procedimentos de
           instalação de bibliotecas e virtualenv.

Criamos um novo arquivo de configuração *buildout.cfg*, que extende o 
**production.cfg** para definir variáveis deste ambiente::

    [buildout]
    extends =
        production.cfg

    [hosts]
    instance = 172.30.20.12

    [ports]
    instance = 9080

    [users]
    os = plone

.. note :: Na configuração acima definimos o endereço do servidor como
           *172.30.20.12*, a porta base como *9080* e o usuário do sistema
           como *plone*.

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

O controle de inicialização e parada do backend é feita através do daemon
:term:`Supervisor`. Esta ferramenta é instalada automaticamente pela
configuração de produção do buildout.

O :term:`Supervisor` disponibiliza dois scripts no ambiente de produção do portal
::

    bin/supervisord
    bin/supervisorctl

O primeiro script, :command:`bin/supervisord`, é utilizado para inicialização do
daemon do :term:`Supervisor`. O segundo script, :command:`bin/supervisorctl` é
o controlador dos serviços e interface padrão para o administrador

A inicialização do :term:`Supervisor` é feita ao se executar:
::

    cd /opt/portal.buildout/
    ./bin/supervisord

Para avaliarmos se o ambiente foi iniciado corretamente, utilizamos o
:command:`bin/supervisorctl`:
::

    ./bin/supervisorctl status

Que deverá produzir um resultado semelhante ao exibido a seguir:
::

    zeo                              RUNNING    pid 24546, uptime 20 days, 19:08:25
    haproxy                          RUNNING    pid 34254, uptime 20 days, 19:08:25
    instance1                        RUNNING    pid 18731, uptime 19 days, 7:01:22
    instance2                        RUNNING    pid 18731, uptime 19 days, 7:01:22

Indicando que os 4 serviços -- base de dados (zeo), redirecionador web e duas
instâncias do servidor de aplicação (instance1 e instance2) -- estão ativos.

Para parar um dos serviços também utilizamos o :command:`bin/supervisorctl`:
::

    ./bin/supervisorctl stop instance1

Assim como iniciar e reiniciar os serviços:
::

    ./bin/supervisorctl start instance1
    ./bin/supervisorctl restart instance1 instance2

Para parar o daemon do :term:`Supervisor` o comando é:
::

    ./bin/supervisorctl shutdown

.. note:: Após um **shutdown** é necessário executar, novamente o
          :command:`bin/supervisord`

Manutenção do ambiente
========================

Backup da base de dados
--------------------------

O servidor de aplicação Zope utiliza, primariamente, o :term:`ZODB` como
base de dados. O ZODB é uma base de dados não relacional (:term:`nosql`),
hierárquica e orientada a objetos.

O ZODB pode armazenar seus dados de algumas maneiras, sendo que o
:term:`storage` mais utilizado é o :term:`FileStorage`, que armazena as
informações de maneira incremental[#]_ em um único arquivo no file system.

No ambiente do portal o ZODB está configurado para que conteúdos e metadados,
armazenados em um FileStorage, utilizem o arquivo.
::

    /opt/portal.buildout/var/filestorage/Data.fs

Enquanto conteúdos de arquivos e imagens sejam armazenados como blobs, na pasta
::

    /opt/portal.buildout/var/blobstorage/

O backup dos dados pode ser feito, sem parar o ambiente, copiando-se o arquivo
Data.fs e o conteúdo da pasta de blobstorage para algum outro local.

Porém é possível realizar o backup diferencial do arquivo Data.fs, permitindo
uma transferência mais rápido dos arquivos.

Isto é feito com o script :command:`bin/backup` que, pelos valores padrão,
armazenará os dados na pasta
::

    /opt/portal.buildout/var/backup/


Além disto, teremos o backup dos arquivos blob na pasta:
::

    /opt/portal.buildout/var/blobstoragebackups

Na instalação realizada no portal, conforme documentado no **producao.cfg**,
foi inserida uma entrada no :term:`crontab` do usuário **root** para a
realização diária deste backup de base de dados
::

    crontab -l -u plone
    0 3 * * 0-6 /opt/portal.buildout/bin/backup


Neste cenário, backup incremental do FileStorage e completo do blobstorage,
deve-se copiar apenas estas pastas para outro local no disco. Isto pode ser
realizado com os comandos a seguir:
::

    rsync -auv /opt/portal.buildout/var/backup/ /opt/bkp/filestorage/
    rsync -auv /opt/portal.buildout/var/blobstorage/ /opt/bkp/blobstorage/

.. warning:: Esta configuração não foi realizada no ambiente de produção

Purga da base de dados
--------------------------

A abordagem incremental do FileStorage é positiva pois permite a realização
de *undo* e manutenção do histórico de cada uma das transações. Por outro lado,
esta característica implica que o arquivo de base de dados cresce rapidamente,
conforme o número de transações realizadas.

É recomendado, então, realizar a purga do histórico de transações da base de
dados, de maneira periódica.

Em um ambiente que utilize a separação entre servidores de aplicação e
servidor de base de dados, como é o caso do portal, esta purga pode ser realizada
sem que nenhuma dos servidores de aplicação seja comprometido [#]_

A configuração **producao.cfg**, utilizada para o ambiente de backend, provê
um script específico para a realização da purga do ZODB. Este script é utilizado
da maneira a seguir.
::

    cd /opt/portal.buildout/
    ./bin/zeopack -p 8100 -d 1


Onde :option:`-p 8100` indica que o servidor de base de dados está ouvindo na
porta 8100 e a opção :option:`-d 1` indica que manteremos o histórico de
transações realizadas no último dia.

Na instalação realizada no portal, conforme documentado no **producao.cfg**,
foi inserida uma entrada no :term:`crontab` do usuário **root** para a
realização semanal da purga da base de dados -- e imediado backup
::

    crontab -l -u plone
    0 3 * * 7  /opt/portal.buildout/bin/zeopack -p 8100 -d 1 && /opt/portal.buildout/bin/backup

Logrotate
--------------------------

Cada instância do servidor de aplicação cria, por padrão, dois arquivos de log:

    * Log de ocorrências (<nome_da_instancia>.log)

    * Log de acessos (<nome_da_instancia>-Z2.log)

Além disto o servidor de base de dados cria um log:

    * Log de ocorrências (zeo.log)

O Supervisor cria seu próprio log:

    * Log de ocorrências (supervisord.log)

E ao menos mais dos logs por processo configurado:

    * Log de erro de processo (<nome_do_processo>-stderr---supervisor-<seq>.log)

    * Log de saída de processo (<nome_do_processo>-stdout---supervisor-<seq>.log)

Se os logs do Supervisor são pequenos e podem ser ignorados [#]_, os logs dos
servidores de aplicação e base de dados devem ser rotacionados.

Na instalação realizada no portal, conforme documentado no **producao.cfg**,
foi inserida uma entrada no :term:`crontab` do usuário **root** para a
o rotacionamento dos logs
::

    crontab -l -u plone
    0 3 * * 7  /usr/sbin/logrotate --state /opt/portal.buildout/var/logrotate.status /opt/portal.buildout/etc/logrotate.conf

.. note:: Conforme o indicado acima, o arquivo de configuração do logrotate se
          encontra em */opt/portal.buildout/etc/logrotate.conf*


.. [#] Ou seja, transações com as alterações aos conteúdos existentes são
       anexadas ao final do arquivo de base de dados.

.. [#] Comprometido aqui significa ter seus recursos direcionados à tarefa de
       purga da base de dados.

.. [#] Os logs de processo, por exemplo, existem apenas durante o ciclo de vida
       deste processo, sendo apagados em seguida.
