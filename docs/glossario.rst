.. _glossario:

Glossário
=========

.. glossary::
   :sorted:

   ``...``
      Prompt padrão do Python quando acessado interativamente para a inserção de
      código indentado ou dentro de delimitadores esquerdo e direito.
      (Aspas, colchetes, parênteses, chaves).

   ``>>>``
      Prompt padrão do Python quando acessado interativamente. Usualmente
      encontrado em blocos de documentação e testes de código :term:`doctest`.

   Apache
      Servidor HTTP (HTTPD) desenvolvido nos anos 90. É robusto e bastante 
      utilizado.

   Archetypes
      Sistema/Framework para desenvolvimento de tipos de conteúdo para o 
      Plone. Desde sua versão 2.1, o Plone tem seus tipos padrão de conteúdo 
      construídos sobre este framework. Sua obsolescência é planeja para um 
      futuro próximo com a introdução do :term:`Dexterity`.

   ArchGenXML
      Pacote que, a partir de um arquivo XMI, gera produtos Plone baseados no
      :term:`Archetypes`.

   BigIP
      Balanceador de carga. Normalmente utilizado como frontend para distribuir
      requisições entre *n* servidores http.

   class
      Modelo para criação de objetos. Definições de classes normalmente contêm
      definições de métodos que serão executados nas instâncias destas classes.

   cli
      Do inglês Command Line Interface. Interface de linha de comando.

   CMF
      Content Management Framework, framework desenvolvido pela Zope Corp para 
      a criação de sistemas de gestão de conteúdo sobre a plataforma Zope 2.

   Collective
      Coletivo de soluções comunitárias -- plugins, documentações -- 
      desenvolvidas para Plone. Suas atividades podem ser acompanhadas através
      do `Github <http://github.com/collective>`_

   crontab
       Tabela de trabalhos a serem executados de maneira programada pelo 
       sistema operacional. Para verificar quais os trabalhos estão agendados 
       por um usuário, utilize :command:`crontab -l -u <username>`

   Dexterity
      Sistema/Framework para desenvolvimento de tipos de conteúdo para o 
      Plone. A partir da versão 4.3, o Plone integrará o Dexterity à sua 
      instalação padrão e, posteriormente, os tipos padrão de conteúdo serão 
      implementados com este framework. É o substituto do :term:`Archetypes`.

   doctest
      Módulo da biblioteca padrão do Python que permite a criação de testes de
      maneira rápida ao utilizar os resultados obtidos através do interpretador
      interativo como forma de elaboração dos testes.

   dsn
       Acrônimo de Data Source Name, é o identificador utilizado em conexões 
       à base de dados.

   dtml
      Document Template Markup Language é uma linguagem de template que permite
      a criação de HTML e texto. Era a tecnologia de template usada pelo Zope
      até a introdução do :term:`ZPT`, atualmente seu é depreciado mas ainda
      é possível encontrar, no core do Plone, arquivos de css, javascripts e 
      templates de e-mail que utilizam esta linguagem. Outro uso do dtml é 
      com métodos :term:`ZSQL`.

   Filestorage
       Implementação de armazenamento para :term:`ZODB` que utiliza um arquivo 
       no sistema de arquivos para persistir os dados. Usualmente este arquivo 
       tem nome de Data.fs.

   Generic Setup
      Conjunto de soluções que permite a configuração de um Plone site através
      de arquivos xml distribuídos juntamente com produtos e pacotes.

   Git
      Sistema de controle de versões desenvolvido, inicialmente, por Linus 
      Torvalds para a manutenção do código fonte do Linux. Atualmente o código 
      do Plone, do Zope e de mais diversas soluções open source são mantidos 
      em repositórios Git.

   Github
      Serviço internet que permite a criação de repositórios :term:`Git` 
      gratuitamente e através da web. O código do Plone está hospedado neste 
      serviço.

   HAProxy
      Balanceador de carga open source. Pode ser usado com o protocolo HTTP 
      (camada 7) ou com outros protocolos e serviços disponíveis sobre TCP/IP.

   i18n
      i18n é um acrônimo e uma brincadeira. Seu significado é
      internationalization, ou seja, a letra i seguida por 18 letras e
      terminando com a letra n.
      Quando usamos i18n queremos expressar o esforço a ser realizado na
      tradução do código/produto/solução para outros idiomas.

   l10n
      l10n, assim como i18n é um acrônimo. Significa localization, ou a letra l
      seguida de 10 outras letras e terminando com a letra n.

   LDAP
       Acrônimo que significa **Lightweight Directory Access Protocol**, o LDAP 
       é um protocolo que define serviços de diretório. Existem várias soluções 
       que implementam este protocolo -- como ferramentas de catálogo de 
       usuários (AddressBook, MacOsX) -- e também soluções de backend, como o 
       Active Directory e o OpenLdap.

   Memcached
       Servidor de cache de informações no formato chave-valor. Este servidor 
       é utilizado para serviços distribuídos manterem uma mesma cópia de 
       cache de informações. 

   mr.developer
      Uma extensão para o :term:`zc.buildout` que facilita o desenvolvimento de
      projetos Plone com pacotes mantidos em repositórios de versionamento de
      código.
      Para saber mais, acesse 
      `Pypi <http://pypi.python.org/pypi/mr.developer/>`_

   Nginx
       Servidor HTTP desenvolvido na última década. Possui performance muito 
       superior ao do Apache devido a sua arquitetura -- baseada em eventos.

   nosql
       Base de dados não relacional. Alguns exemplos são :term:`ZODB` e MongoDB.
       Este termo refere-se ao fato que estas bases não aderem ao padrão SQL.

   OOP
      Programação orientada a objetos (POO) é um paradigma de desenvolvimento 
      de soluções.

   orm
      Mapeador Objeto Relacional. É um mecanismo de persistência de objetos em
      bases de dados relacionais. O :term:`SQLAlchemy` é um exemplo de ORM 
      implementado em Python.

   PloneGov.BR
      `Comunidade <http://colab.interlegis.leg.br/wiki/PloneGovBr>`_ 
      de instituições ligadas ao governo brasileiro que utilizam
      Python, Zope, Plone e tecnologias correlatas.

   PostgreSQL
      Base de dados relacional open source.

   RDBMS
       Sistema de gestão de base de dados relacional

   Relstorage
       Implementação de armazenamento para :term:`ZODB` que persistir os dados 
       em base de dados relacional (:term:`RDBMS`). Apesar do uso de uma base 
       SQL, os dados armazenados através do Relstorage não são acessíveis sem 
       a utilização do ZODB.

   SQLAlchemy
       Solução de mapeamento objeto relacional desenvolvida sobre Python.

   Squid
       Servidor de cache, utilizado em sites web como solução para aumento da 
       velocidade de acesso.

   storage
       Implementação de armazenamento de dados para o :term:`ZODB`. Hoje são 
       dois os storages mais utilizados: :term:`Filestorage` e 
       :term:`Relstorage`.   

   Supervisor
        Ver :term:`supervisord`.

   supervisord
      Solução cliente-servidor que permite o monitoramento e controle de
      processos em sistemas operacionais Unix-like.
      Para saber mais, acesse `Supervisord <http://supervisord.org/>`_

   Subversion
      Subversion é um sistema de gestão de versões de documentos e códigos-
      fonte. Foi o sistema utilizado para suportar o desenvolvimento do Plone 
      e de grande parte de seus  produtos. Hoje substituido pelo :term:`Git`

   Trac
      Ambiente de colaboração para o desenvolvimento de soluções. É composto por
      wiki, bug tracking e integração com respositórios de códigos-fonte.

   Varnish
      Acelerador web de altíssima performance, desenvolvido levando em
      consideração a maneira como os sistemas operacionais atuais gerenciam
      recursos.
      Para saber mais, acesse `Varnish <http://varnish.projects.linpro.no/>`_

   virtualenv
      Pacote que implementa um ambiente separado de Python, permitindo a
      instalacão de outros pacotes e a realização de configurações sem que 
      estes influenciem o Python utilizado pelo sistema.

   WSGI
      Padrão utilizado pela comunidade Python para interoperabilidade de 
      aplicações web.

   zc.buildout
      Sistema para criação, montagem e implementação de aplicações. Permite que
      sejam criados arquivos de configuração que detalham como deve se comportar
      cada instalação.
      Para saber mais, acesse `Buildout <http://www.buildout.org/>`_

   Zen do Python
      Texto descrevendo os princípios e filosofias que são essencias para o
      entendimento e uso da linguagem. Este texto pode ser encontrado a
      qualquer momento ao se digitar "``import this``" no prompt interativo.

   ZEO
      Zope Enterprise Objects é uma maneira de utilizar o Zope de maneira
      distribuída. Com o ZEO é possível contar com diversas instâncias do
      servidor de aplicações Zope conectadas a uma base de dados :term:`ZODB`
      compartilhada. A comunicação entre os servidores de aplicação e o 
      servidor ZEO é feita através de uma implementação RPC.

   ZODB
       Base de dados :term:`nosql` orientada a objetos desenvolvida pela 
       `Zope Corporation <http://www.zope.com>`_. É utilizada como base de 
       dados padrão pelo servidor de aplicações Zope -- e consequentemente 
       pelo Plone.

   Zope
       Servidor de aplicações web desenvolvido em Python e C. Oferece boa
       parte da infraestrutura utilizada pelo Plone.

   zpt
       Acrônimo para Zope Page Templates. Solução de templates que utiliza
       XML válido através da utilização de atributos às Tags utilizadas.

   ZSQL
      Ponte entre bases de dados relacionais e o servidor Zope. Através dos 
      métodos ZSQL é possível a criação de consultas SQL parametrizáveis que 
      persistidas dentro do :term:`ZODB`. Esta tecnologia está depreciada e 
      deve ser retirada das instalações padrão do Plone em um futuro próximo. 
      A alternativa mais 

