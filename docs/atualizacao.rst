==========================================
Atualização de *release*
==========================================

Toda vez que uma nova *release* (pacote de atualização **estável**) do Portal 
Institucional Padrão em Plone for lançada no :term:`PyPI`, a Comunidade avisará 
na lista de discussões :term:`PloneGov-BR`. 

.. note :: Atualmente não há uma frequência estabelecida para criação de 
           *releases* do produto principal *brasil.gov.portal*.

Para atualizar um portal existente, basta alterar a versão do *buildout* para o 
número de versão mais atual, conforme o *buildout* base 
(https://github.com/plonegovbr/portal.buildout/blob/master/buildout.d/base.cfg#L5), 
rodar o *buildout* e reiniciar a(s) instância(s).

Encontrando incorreções, colabore com melhorias. Se não se sentir seguro(a) para 
corrigir o código fonte de um produto, verifique os *tickets* existentes no 
:term:`GitHub` ou faça novo reporte (*New issue*) no produto específico do GitHub 
(https://github.com/plonegovbr) – com o maior número de detalhes que puder informar. 
Reportar problemas é um trabalho nobre. :)

.. note :: A partir da versão 1.0.1 do Portal Institucional Padrão em Plone, o 
           *buildout* passou a depender de um arquivo único de versões. Essa é uma 
           melhoria que faz o Portal Padrão funcionar como o Plone (por padrão). 
           Esta foi a modificação realizada para trazer esta melhoria na atualização 
           do produto: 
           https://github.com/plonegovbr/portal.buildout/blob/master/buildout.d/base.cfg#L5


