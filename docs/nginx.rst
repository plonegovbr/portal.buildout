nginx
=====

O nginx é um servidor proxy reverso de código aberto para protocolos HTTP, HTTPS, SMTP, POP3 e IMAP, assim como um balanceador de carga, cache HTTP e servidor web.
O projeto nginx começou fortemente focado em alta simultaneidade, alta performance e baixo consumo de memória.

Instalação
----------

A instalação do nginx em ambientes Debian/Ubuntu é muito simples:

.. code-block:: console

    $ sudo apt install -y nginx

Configuração básica
-------------------

Normalmente as configurações do nginx ficam armazenadas na pasta ``/etc/nginx/sites-available/`` e de ai se faz um link simbólico do arquivo à pasta ``/etc/nginx/sites-enabled/``.

A configuração básica mais simples e a seguinte:

::

    server {
        listen 80;
        server_name www.orgao.gov.br;
        location / {
            proxy_pass http://127.0.0.1/VirtualHostBase/http/www.orgao.gov.br:80/portal/VirtualHostRoot/;
        }

Habilitar compressão
--------------------

O módulo `ngx_http_gzip_module <http://nginx.org/en/docs/http/ngx_http_gzip_module.html>`_ do nginx é um filtro que comprime as respostas usando o método ``gzip``.
Isso ajuda a reduzir a quantidade de informação transmitida entre e servidor e os clientes.

Para habilitar a compressão usamos as seguintes diretivas:

::

    server {
        ...
        gzip on;
        gzip_disable "MSIE [1-6]\.(?!.*SV1)";
        ...
    }

A diretiva ``gzip_disable`` se usa para inabilitar a compressão caso o usuário final esteja usando uma versão antiga do IE.

Endereço canónico
-----------------

::

    server {
        listen 80;
        server_name orgao.gov.br;
        rewrite ^/(.*) http://www.orgao.gov.br/$1 permanent;
    }

Balanceador de carga
--------------------

O módulo `ngx_http_upstream_module <http://nginx.org/en/docs/http/ngx_http_upstream_module.html>`_ é usado para definir grupos de servidores que podem ser referenciados pela diretiva ``proxy_pass``.

::

    upstream plone {
        server 127.0.0.1:8081;
        server 127.0.0.1:8082;
    }

    server {
        listen 80;
        server_name www.orgao.gov.br;
        location / {
            proxy_pass http://plone/VirtualHostBase/http/www.orgao.gov.br:80/portal/VirtualHostRoot/;
        }

O nginx utiliza por padrão o método round robin para definir o servidor que vai ser utilizado.

Implementação do suporte SSL
----------------------------

O módulo `ngx_http_ssl_module <http://nginx.org/en/docs/http/ngx_http_ssl_module.html>`_ fornece o suporte para o HTTPS.
Para abilitar o suporte HTTPS precisa duma chave e um certificado SSL.

::

    server {
        listen 80;
        server_name orgao.gov.br;
        rewrite ^/(.*) https://orgao.gov.br/$1 permanent;
    }

    server {
        listen 443 ssl;
        server_name www.orgao.gov.br;

        ssl on;
        ssl_certificate /etc/nginx/ssl/www.orgao.gov.br/server.crt;
        ssl_certificate_key /etc/nginx/ssl/www.orgao.gov.br/server.key;
        ssl_trusted_certificate /etc/nginx/ssl/www.orgao.gov.br/ca-certs.pem;

        location / {
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
            proxy_pass http://plone/VirtualHostBase/https/www.orgao.gov.br:443/portal/VirtualHostRoot/;
        }
    }

Caso estiver usando um certificado auto-assinado não precisa da diretiva ``ssl_trusted_certificate``.
