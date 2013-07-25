=======================================
Máquina Virtual
=======================================

Disponibilizamos uma máquina virtual, no formato OVF, compatível com 
`VirtualBox`_.

Esta documentação espera que o VirtualBox já esteja instalado no seu
computador.

Download
------------

Faça o download da VM a partir do endereço:

	* http://downloads.plone.org.br/identidade-ubuntu-1.2a.ova


Importação
-------------

Vamos importar a imagem, clique em **Arquivo** -> **Importar Appliance**

Clique em **Abrir appliance**

.. image:: images/vm_passo_01.png

Procurar o local onde foi feito o download da imagem e clicar em 
**Abrir**

.. image:: images/vm_passo_02.png

Cliquem em **Próximo(N)**

.. image:: images/vm_passo_03.png

Clique em **Importar**

.. image:: images/vm_passo_04.png

Agora é só aguardar a importação terminar.

.. image:: images/vm_passo_05.png


Usando a VM
-------------

Para iniciar a máquina virtual, selecione a imagem e clique em 
**Iniciar (T)**

.. image:: images/vm_passo_06.png

O processo de inicialização pode levar alguns minutos

.. image:: images/vm_passo_07.png

Quando a máquina acabar o processo de inicialização, você verá a tela
a seguir

.. image:: images/vm_passo_08.png

Para saber o endereço ip de acesso a esta máquina se autentique com as
seguintes credenciais:

    * login: **plonegovbr**
    * password: **plonegovbr**

E na tela seguinte você verá o endereço para acessar este servidor

.. image:: images/vm_passo_09.png

Agora, em seu computador, inicie o seu navegador e use o endereço do passo 
anterior para acessar o site:

.. image:: images/acesso_01.png

Para se autenticar no site, acesse o mesmo endereço adicionando /login

.. image:: images/acesso_02.png

Credenciais:

    * Nome de usuário: **admin**
    * Senha: **admin**


.. _VirtualBox: https://www.virtualbox.org/
