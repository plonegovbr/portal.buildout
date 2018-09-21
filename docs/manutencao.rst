=====================
Manutenção de portais
=====================

O processo de manutenção dos portais deve ser realizado periodicamente é inclui, no mínimo, as seguintes operações básicas:

- monitoramento do consumo de CPU
- monitoramento do consumo de memória
- monitoramento do espaço em disco
- revisão dos logs do servidor web e de eventos do Zope
- compactação do banco de dados
- criação de backups do banco de dados
- purga de revisões do histórico de versões
- atualização de componentes

Performance
===========

Manter a performance de um servidor de produção passa por ter um número suficiente de instâncias (ou threads) e objetos cacheados no servidor Zope.
Não existe uma solução única e cada sistema vai precisar de ajustes específicos e monitoramento constante.

Como regra geral um servidor de produção deve ter um consumo baixo de CPU e alto de memória,
deixando sempre espaço livre para buffers e page cache do sistema operacional.
Um servidor de produção não deveria utilizar nunca memória swap.

Um servidor de produção deve ter também espaço livre em disco para armazenar tanto o banco de dados, quanto seus backups.

Manutenção do banco de dados
============================

A configuração de produção inclui scripts para gerenciar o processo de compactação do banco de dados e backups:

Para compactar o banco de dados utilize:

.. code-block:: console

    $ bin/zeopack

Para criar um backup utilize:

.. code-block:: console

    $ bin/backup

Em ambientes de produção é recomendado agendar backups diários e compactações semanais utilizando o comando :term:`crontab`.

Gerenciamento de versões
------------------------

O Plone suporta versionamento de conteúdo por padrão.
O versionamento armazena uma cópia adicional do conteúdo cada vez que este tem sido modificado.
O número de versões máximas armazenadas é configurável, mas por padrão é infinito e isso pode representar um problema em alguns casos.
No IDG quase todos os tipos de conteúdo tem o versionamento habilitado.

Para gerenciar o histórico de versões de forma simples é necessário instalar o complemento `collective.revisionmanager <https://pypi.python.org/pypi/collective.revisionmanager>`_.
Adicione a seguinte linha no seu buildout de produção:

.. code-block:: ini

    [buildout]
    eggs +=
        collective.revisionmanager

Na "Configuração do Site" selecione "Complementos" e instale o collective.revisionmanager.
Um novo item chamado "Gerenciar revisões" será disponibilizado.

O configlet tem duas telas: "Configurações" e "Listar históricos".

.. info::
    O processo de gerenciamento de versões pode ser demorado em dependência do tamanho do banco de dados.
    Acesse o configlet diretamente na porta de instância de Plone sem passar por servidores intermediários que possam abortar as requisições devido a timeouts.

Para gerenciar corretamente as revisões é necessário primeiramente calcular as estadísticas.
Selecione o botão "Recalcular estadísticas" e espere;
após alguns minutos as estadísticas estarão disponíveis

Ao selecionar "Listar históricos" você verá uma tabela com o histórico de todas as versões do conteúdo no site.
Ordene por tamanho para localizar conteúdo que poderia estar ocasionando problemas.

.. info::
    Versões do IDG anteriores à 1.2 apresentavam um bug que ocasionava a criação de milhões de blobs vazios no file system do ZEO Server quando o versionamento era utilizado (ver `collective.cover#532 <https://github.com/collective/collective.cover/issues/532>`_).

.. info::
    Versões do IDG anteriores à 1.5.1 apresentavam um bug que ocasionava o crescimento exponencial dos objetos e do banco de dados quando o versionamento era utilizado (ver `collective.cover#765 <https://github.com/collective/collective.cover/issues/765>`_).

.. warning::
    O tipo de conteúdo Capa (``collective.cover.content``) precisa do versionamento só quando a edição é realizada utilizando o procedimento de checkout/checkin.
    Se recomenda apagar regularmente o histórico de versões dos objetos para evitar seu crescimento desnecessário (ver `collective.cover#828 <https://github.com/collective/collective.cover/issues/828>`_).

Como último passo, selecione "Apagar órfãos" para eliminar todos os históricos sem cópia de trabalho.

Recalcule as estadísticas para comparar.

Atualização de componentes
==========================

Todo o código fonte do IDG e dos complementos utilizados se encontra disponível nos repositórios armazenados no GitHub, e foi liberado utilizando uma licencia GPLv2.

Para desenvolver novas funcionalidades ou corrigir problemas em complementos utilizados se recomenda seguir algumas boas práticas:

- consulte a `documentação para desenvolvedores Plone <http://docs.plone.org/4/en/develop/index.html>`_

- verifique se a funcionalidade que precisa adicionar não foi implementada já em algum complemento existente que possa ser utilizado diretamente ou melhorado; não tente reinventar a roda

- dentro do possível, limite o escopo da nova funcionalidade desejada para conseguir uma solução geral que possa ser utilizada fora do IDG;
isso garantirá o sucesso futuro da funcionalidade ou complemento

- verifique se o problema que precisa corrigir foi já relatado com anterioridade no issue tracker do complemento envolvido

- verifique se existe uma nova versão do complemento que está utilizando que solucione o problema que está enfrentando

- relate o problema no issue tracker do complemento com detalhe suficiente para os mantenedores do pacote poder reproduzir e ajudar na solução

- nunca resolva um problema em forks privados ou você correrá o risco de ter que manter esse fork para sempre

- utilize a `API do Plone <https://docs.plone.org/develop/plone.api/docs/index.html>`_ e as convenções de codificação da comunidade

- implemente testes unitários e de integração

- implemente integração contínua utilizando serviços como `Travis <http://travis-ci.org/>`_ ou similares

- documente seu trabalho

- dentro do possível, colabore com a solução abertamente;
não esqueça, você está utilizando software livre e o processo de manutenção é de ida e volta: desfrute e partilhe
