=======================================
Boas práticas
=======================================

Visando compartilhar experiências adquiridas com estes e outros projetos, elaboramos uma 
lista de boas práticas por áreas específicas:

* na área de infraestrutura, desligar o modo *debug* antes de colocar o site em produção;

* na área de infraestrutura, configurar uma instância pra cada core do servidor para ter 
  melhor performance e nunca deixar de configurar ZEO com ao menos duas instâncias em 
  ambientes de produção;

* na área de desenvolvimento, evitar customizar no *portal_view_customization* da ZMI. 
  Existe um problema de verificação de permissionamento que ocorre com alguns *templates* 
  customizados lá;

* se for desenvolver algo novo, é indicado gerar um **buildout** próprio (não usar o 
  padrão disponível no :term:`GitHub` (*portal.buildout*), apenas usá-lo como referência) 
  e criar um **policy** (produto específico com os desenvolvimentos do seu site). Para 
  criação destes produtos é preciso ter um perfil de desenvolvimento e gestão de 
  configuração. O produto **bobtemplates** pode auxiliá-lo na criação da estrutura base 
  do seu *policy*:  https://github.com/plonegovbr/bobtemplates.plonegovbr;

* na área de infraestrutura, agendar **pack** na base de dados com resguardo de histórico 
  de *UNDO*. Este resguardo pode ser de 7 a *n* dias, dependendo do volume de conteúdo e 
  frequência de atualização do seu portal;

* na área de infraestrutura, disponibilizar o formulário de login em modo seguro (HTTPS);

* na área de infraestrutura, é indicado sempre usar um servidor de cache cem produção e 
  adaptar às suas necessidades específicas (exemplo: em portais noticiosos, ter expiração 
  de capa curta, como  15 minutos);

* na área de configuração, nunca atribuir permissão a um usuário. É indicado e mais 
  prático gerir permissões à grupos de usuários;

* na área de desenvolvimento, evitar desenvolver coisas específicas. Sempre que possível 
  contribuir com projetos *open source* existentes e se possível com cobertura de testes;

* sempre que encontrar erros ou identificar melhorias, verificar os *tickets* existentes 
  ou criar nova *issue* no produto específico do GitHub (https://github.com/plonegovbr). 
  Se não tiver certeza sobre qual produto se trata o ajuste ou melhoria, reportar no 
  produto *brasil.gov.portal* (que é mais genérico).

