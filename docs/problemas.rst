=======================================
Problemas Comuns
=======================================

Não consigo clonar o repositório
=============================================

Provavelmente seu acesso internet é feito através de algum servidor de Proxy.
Se o bloqueio acontecer apenas para a porta de **SSH** (22), altere
todas as referências a  **git@github.com:** por **https://github.com/**.

Error: Buildout now includes 'buildout-versions' (and part of the older 'buildout.dumppickedversions')
======================================================================================================

A tag `1.1.3 <https://github.com/plonegovbr/portal.buildout/releases/tag/1.1.3>`_
está causando o erro:

::

    Error: Buildout now includes 'buildout-versions' (and part of the older 'buildout.dumppickedversions').
    Remove the extension from your configuration and look at the 'show-picked-versions' option in buildout's documentation.

quando o buildout é executado. Favor utilizar uma tag maior que a 1.1.3.