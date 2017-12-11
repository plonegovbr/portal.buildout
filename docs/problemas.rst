================
Problemas comuns
================

.. contents:: Índice
   :depth: 1


Não consigo clonar o repositório
================================

Provavelmente seu acesso internet é feito através de algum servidor de Proxy.
Se o bloqueio acontecer apenas para a porta de **SSH** (22), altere
todas as referências a  **git@github.com:** por **https://github.com/**.


Error: Wheels are not supported
===============================

Você está usando uma combinação de setuptools e zc.buildout não suportada.
A partir da versão 38.2.0 o setuptools começou suportar e descarregar `wheels <https://pythonwheels.com/>`_ (um novo padrão para distribuir módulos que tenta substituir os eggs),
mas essa versão ocasionou um `problema <https://github.com/buildout/buildout/issues/425>`_ no zc.buildout.

Tem duas formas de solucionar esse problema:

* fazer downgrade do setuptools no virtualenv:

.. code-block:: console

    $ pip install -U setuptools==33.1.1

* atualizar a versão do zc.buildout:

.. code-block:: ini

    [versions]
    zc.buildout = 2.10.0


Error: Buildout now includes 'buildout-versions' (and part of the older 'buildout.dumppickedversions')
======================================================================================================

A tag `1.1.3 <https://github.com/plonegovbr/portal.buildout/releases/tag/1.1.3>`_ está causando o erro:

.. code-block:: console

    Error: Buildout now includes 'buildout-versions' (and part of the older 'buildout.dumppickedversions').
    Remove the extension from your configuration and look at the 'show-picked-versions' option in buildout's documentation.

quando o buildout é executado. Favor utilizar uma tag maior que a 1.1.3.
