# Regras do Projeto

Este documento define as decisões específicas deste projeto e orienta como novas funcionalidades devem ser desenvolvidas.

Ele deve ser preenchido de cima para baixo, pois as decisões das seções posteriores dependem das definições anteriores.

O `README.md` deve concentrar instruções de uso, primeiros passos, contexto, histórico e diário de bordo.

O `regrasDev.md` deve concentrar regras gerais e reutilizáveis de desenvolvimento.

Este arquivo deve conter apenas definições, convenções, restrições e decisões próprias deste projeto.

## Regras de preenchimento

- Cada campo deve representar uma única decisão.
- Cada decisão deve existir em apenas uma seção.
- Campos aplicáveis não devem permanecer vazios.
- Use `Pendente.` quando a decisão ainda não tiver sido tomada.
- Use `Não se aplica.` quando o campo não pertencer ao projeto.
- Os exemplos servem apenas para indicar o tipo e o formato da informação esperada.
- Justificativas, histórico e contexto das decisões devem ser registrados no `README.md`.
- Seções posteriores devem respeitar todas as definições anteriores.
- Novas seções devem ser criadas apenas quando representarem uma decisão independente que não pertença às seções existentes.
- Regras devem ser escritas de forma objetiva, afirmativa e verificável.
- Proibições devem ser usadas apenas quando forem necessárias para impedir uma violação concreta da arquitetura ou do comportamento do projeto.

### Padrão para árvores e hierarquias

Diretórios devem terminar com `/`.

Arquivos não devem terminar com `/`.

Cada sequência adicional de `--` representa um nível abaixo na hierarquia.

Ex.:

```text
src/
--app/
----router/
------router.ts
--pages/
----home/
------components/
------HomePage.tsx
--shared/
----components/
```

### Estados permitidos para campos não definidos

```text
Pendente.
```

```text
Não se aplica.
```

# Parte I — Definição do projeto

## 1. Identificação

Nome do projeto:

Ex.: Gerador de Arquivos MAC

Descrição curta:

Ex.: Aplicação web para configurar, visualizar e gerar documentos em PDF a partir de modelos editáveis.

Tipo de projeto:

Ex.: Aplicação web front-end.

Responsável principal:

Ex.: Nome da pessoa, equipe ou organização responsável.

Repositório principal:

Ex.: `owner/repository`

Estado atual do projeto:

Ex.: Planejamento, protótipo, desenvolvimento, manutenção ou produção.

## 2. Objetivo

Problema principal que o projeto resolve:

Ex.: Automatizar a criação de documentos padronizados que atualmente são preenchidos manualmente.

Resultado principal entregue ao usuário:

Ex.: Arquivo PDF gerado a partir de dados informados na interface.

Usuários ou consumidores principais:

Ex.:

- operadores administrativos;
- gestores;
- sistemas integrados.

Critério principal de sucesso:

Ex.: Permitir a criação correta de um documento completo sem edição manual posterior.

## 3. Escopo funcional

Funcionalidades incluídas no projeto:

Ex.:

- criação de documentos;
- edição de campos;
- visualização prévia;
- exportação em PDF.

Funcionalidades explicitamente excluídas:

Ex.:

- assinatura digital;
- envio automático por e-mail;
- armazenamento em nuvem.

Limites de responsabilidade do sistema:

Ex.: O sistema gera o documento, mas não controla sua distribuição, assinatura ou arquivamento externo.

Entidades ou conceitos centrais do domínio:

Ex.:

- documento;
- modelo;
- campo;
- arquivo gerado.

## 4. Requisitos e características do sistema

Plataformas em que o sistema deve funcionar:

Ex.:

- navegador desktop;
- navegador mobile;
- servidor Linux.

Modo de funcionamento:

Ex.: Aplicação online com execução principal no navegador.

Necessidade de funcionamento offline:

Ex.: Não se aplica.

Necessidade de múltiplos usuários simultâneos:

Ex.: Sim, sem compartilhamento de sessão entre usuários.

Necessidade de autenticação:

Ex.: Não se aplica.

Necessidade de autorização por papéis ou permissões:

Ex.: Não se aplica.

Necessidade de persistência de dados:

Ex.: Armazenamento local das preferências do usuário.

Necessidade de comunicação em tempo real:

Ex.: Não se aplica.

Necessidade de consumir serviços externos:

Ex.: API de consulta de endereços por CEP.

Necessidade de importar arquivos:

Ex.: Importação de arquivos JSON com configurações de modelos.

Necessidade de gerar arquivos:

Ex.: Geração de arquivos PDF.

Necessidade de processamento assíncrono:

Ex.: Geração de arquivos executada sem bloquear a interface.

Necessidade de responsividade:

Ex.: A interface deve permanecer utilizável em telas a partir de 768 px.

Necessidade de acessibilidade:

Ex.: Navegação por teclado e associação correta entre labels e campos.

Volume esperado de dados:

Ex.: Até 100 modelos locais e documentos com até 50 páginas.

Requisitos de desempenho relevantes:

Ex.: A visualização prévia deve refletir alterações em até 200 ms em condições normais.

Requisitos de compatibilidade relevantes:

Ex.: Compatibilidade com as duas versões estáveis mais recentes de Chrome, Edge e Firefox.

## 5. Restrições e premissas

Tecnologias obrigatórias:

Ex.:

- TypeScript;
- React;
- Vite.

Tecnologias proibidas:

Ex.:

- dependências sem manutenção ativa;
- bibliotecas que exijam serviço externo para gerar PDF.

Ambientes obrigatoriamente suportados:

Ex.:

- desenvolvimento local em Windows;
- build de produção em Linux.

Limites de infraestrutura:

Ex.: O projeto deve funcionar sem servidor próprio.

Compatibilidades que devem ser preservadas:

Ex.:

- formato atual dos arquivos exportados;
- contratos públicos utilizados por integrações existentes.

Funcionalidades existentes que não podem mudar de comportamento:

Ex.:

- geração dos PDFs;
- visualização prévia dos modelos;
- funcionamento das stores existentes.

Restrições acadêmicas, comerciais, legais ou organizacionais:

Ex.: O projeto deve utilizar apenas dependências com licenças compatíveis com uso comercial.

Premissas adotadas:

Ex.: O usuário utilizará um navegador moderno com JavaScript habilitado.

# Parte II — Decisões técnicas

## 6. Natureza do sistema

Modelo principal da aplicação:

Ex.: Aplicação web de página única.

Componentes técnicos existentes:

Ex.:

- front-end;
- API;
- banco de dados;
- serviço assíncrono.

Modelo de execução:

Ex.: Interface executada no navegador e API executada em Node.js.

Modelo de implantação:

Ex.: Front-end estático e API em contêiner separado.

Pontos de entrada da aplicação:

Ex.:

- `src/main.tsx`;
- `src/server.ts`;
- comando de linha `generate`.

Interfaces públicas do sistema:

Ex.:

- interface gráfica;
- API REST;
- arquivos exportados.

## 7. Stack tecnológica

### 7.1 Linguagens

Linguagem principal:

Ex.: TypeScript.

Linguagens auxiliares:

Ex.:

- CSS;
- SQL;
- Python.

Versão mínima da linguagem principal:

Ex.: TypeScript 5.7.

### 7.2 Runtime e plataforma

Runtime principal:

Ex.: Node.js.

Versão mínima do runtime:

Ex.: Node.js 22.

Plataforma principal de execução:

Ex.: Navegadores modernos.

Sistemas operacionais suportados para desenvolvimento:

Ex.:

- Windows 11;
- Linux.

### 7.3 Front-end

Framework ou biblioteca principal:

Ex.: React 19.

Ferramenta de build:

Ex.: Vite.

Biblioteca de roteamento:

Ex.: React Router.

Biblioteca de gerenciamento de estado local ou global:

Ex.: Zustand.

Biblioteca para estado remoto:

Ex.: TanStack Query.

Biblioteca de formulários:

Ex.: React Hook Form.

Biblioteca de validação:

Ex.: Zod.

Estratégia de estilos:

Ex.: CSS Modules.

Biblioteca de componentes visuais:

Ex.: Não se aplica.

### 7.4 Back-end

Framework principal:

Ex.: Fastify.

Servidor ou adaptador HTTP:

Ex.: Servidor nativo do Fastify.

Biblioteca de validação:

Ex.: Zod.

Estratégia de autenticação:

Ex.: JWT com access token e refresh token.

Ferramenta de documentação da API:

Ex.: OpenAPI gerado pelo Fastify Swagger.

### 7.5 Persistência

Banco de dados principal:

Ex.: MySQL 8.

ORM, query builder ou driver:

Ex.: Prisma.

Ferramenta de migração:

Ex.: Prisma Migrate.

Solução de cache:

Ex.: Redis.

Armazenamento de arquivos:

Ex.: Sistema de arquivos local.

### 7.6 Ferramentas de desenvolvimento

Gerenciador de pacotes:

Ex.: npm.

Ferramenta de lint:

Ex.: ESLint.

Ferramenta de formatação:

Ex.: Prettier.

Framework de testes unitários:

Ex.: Vitest.

Framework de testes de interface:

Ex.: Testing Library.

Framework de testes de ponta a ponta:

Ex.: Playwright.

Ferramenta de containerização:

Ex.: Docker.

Ferramenta de integração contínua:

Ex.: GitHub Actions.

## 8. Arquitetura adotada

Modelo arquitetural principal:

Ex.: Arquitetura modular organizada por features.

Estratégia predominante de organização:

Ex.: Organização por feature, com áreas compartilhadas e infraestrutura isolada.

Camadas ou áreas arquiteturais existentes:

Ex.:

- aplicação;
- features;
- domínio;
- infraestrutura;
- compartilhado.

Responsabilidade de cada camada ou área:

Ex.:

- aplicação: composição, inicialização e roteamento;
- features: funcionalidades de negócio;
- domínio: regras e contratos independentes;
- infraestrutura: integrações e detalhes técnicos;
- compartilhado: elementos reutilizados por múltiplas features.

Direção obrigatória das dependências:

Ex.:

```text
a aplicação
--pode depender de features
----podem depender do domínio
------pode depender de contratos compartilhados

a infraestrutura
--pode implementar contratos do domínio
```

Dependências proibidas entre camadas ou áreas:

Ex.:

- domínio não depende da interface;
- compartilhado não depende de features;
- infraestrutura não contém regras de apresentação.

Critério para criação de uma nova camada ou área arquitetural:

Ex.: Somente quando existir uma responsabilidade independente que não possa ser acomodada sem violar as fronteiras existentes.

## 9. Módulos e fronteiras

Módulos principais do sistema:

Ex.:

- documentGeneration;
- templateManagement;
- fileImport;
- applicationSettings.

Responsabilidade de cada módulo:

Ex.:

- `documentGeneration`: preparar e gerar documentos finais;
- `templateManagement`: criar e editar modelos;
- `fileImport`: validar e importar arquivos externos;
- `applicationSettings`: manter preferências da aplicação.

Dados pertencentes a cada módulo:

Ex.:

- modelos pertencem a `templateManagement`;
- documentos gerados pertencem a `documentGeneration`;
- preferências pertencem a `applicationSettings`.

Interfaces públicas de cada módulo:

Ex.:

- cada módulo expõe apenas seu arquivo `index.ts`;
- arquivos internos não podem ser importados externamente.

Dependências permitidas entre módulos:

Ex.:

- `documentGeneration` pode consumir contratos públicos de `templateManagement`.

Dependências proibidas entre módulos:

Ex.:

- `templateManagement` não pode acessar internals de `documentGeneration`.

Critério para criação de um novo módulo:

Ex.: Criar um novo módulo quando surgir uma capacidade de negócio com dados, regras e ciclo de evolução próprios.

## 10. Fluxos técnicos principais

Fluxo de inicialização da aplicação:

Ex.:

```text
main.tsx
--App
----providers
------router
--------pages
```

Fluxo principal de leitura de dados:

Ex.:

```text
Page
--Hook
----Service
------Repository
--------Database
```

Fluxo principal de escrita de dados:

Ex.:

```text
Form
--UseCase
----Service
------Repository
--------Database
```

Fluxo de autenticação:

Ex.:

```text
LoginPage
--authenticationService
----authenticationApi
------sessionStore
```

Fluxo de geração de arquivos:

Ex.:

```text
Page
--documentGenerationUseCase
----documentEngine
------fileOutput
```

Fluxo de integração externa:

Ex.:

```text
Feature
--Service
----IntegrationClient
------ExternalApi
```

Fluxo de tratamento de falhas:

Ex.:

```text
Origem da falha
--erro técnico
----erro de aplicação
------mensagem segura para a interface
```

# Parte III — Organização do código

## 11. Estrutura de diretórios

Diretório raiz do código-fonte:

Ex.: `src/`

Estrutura principal de diretórios:

Ex.:

```text
src/
--app/
----providers/
----router/
--features/
----documentGeneration/
----templateManagement/
--shared/
----components/
----hooks/
----types/
----utils/
--infrastructure/
----api/
----storage/
--main.tsx
```

Diretórios obrigatórios:

Ex.:

- `src/app/`;
- `src/features/`;
- `src/shared/`.

Diretórios opcionais:

Ex.:

- `src/infrastructure/`;
- `src/domain/`;
- `src/assets/`.

Diretórios proibidos:

Ex.:

- diretórios genéricos duplicados na raiz e em `shared`;
- diretórios sem responsabilidade definida.

Critério para criar um novo diretório:

Ex.: Criar apenas quando houver um agrupamento coerente de arquivos com a mesma responsabilidade.

## 12. Responsabilidade dos diretórios

Responsabilidade de `app/`:

Ex.: Compor a aplicação, registrar providers, configurar rotas e inicializar dependências.

Conteúdo permitido em `app/`:

Ex.:

- providers;
- roteamento;
- layouts globais;
- composição da aplicação.

Conteúdo proibido em `app/`:

Ex.:

- regras específicas de uma feature;
- componentes reutilizáveis de domínio;
- acesso direto ao banco de dados.

Responsabilidade de `features/`:

Ex.: Concentrar cada capacidade funcional do sistema e seus elementos específicos.

Conteúdo permitido em `features/`:

Ex.:

- componentes específicos;
- hooks específicos;
- serviços da feature;
- tipos da feature;
- stores da feature.

Conteúdo proibido em `features/`:

Ex.:

- elementos reutilizáveis sem vínculo com uma feature;
- implementações de infraestrutura compartilhada.

Responsabilidade de `shared/`:

Ex.: Concentrar apenas elementos estáveis e reutilizados por múltiplas features.

Conteúdo permitido em `shared/`:

Ex.:

- componentes genéricos;
- hooks genéricos;
- utilitários puros;
- tipos compartilhados;
- contratos comuns.

Conteúdo proibido em `shared/`:

Ex.:

- regras específicas de uma feature;
- imports de módulos internos de features;
- código movido preventivamente sem reutilização real.

Responsabilidade de `infrastructure/`:

Ex.: Implementar detalhes técnicos, integrações externas, persistência e adaptadores.

Conteúdo permitido em `infrastructure/`:

Ex.:

- clientes HTTP;
- repositories concretos;
- armazenamento;
- adaptadores externos.

Conteúdo proibido em `infrastructure/`:

Ex.:

- componentes visuais;
- regras de apresentação;
- decisões de fluxo da interface.

## 13. Organização interna dos módulos

Estrutura padrão de uma feature:

Ex.:

```text
featureName/
--components/
--hooks/
--services/
--store/
--types/
--utils/
--index.ts
```

Subdiretórios obrigatórios em uma feature:

Ex.: Apenas `index.ts`; os demais devem existir somente quando necessários.

Subdiretórios opcionais em uma feature:

Ex.:

- `components/`;
- `hooks/`;
- `services/`;
- `store/`;
- `types/`;
- `utils/`.

Critério para criar um subdiretório interno:

Ex.: Criar quando existirem pelo menos dois arquivos da mesma responsabilidade ou quando a separação melhorar claramente a fronteira do módulo.

Critério para dividir um arquivo:

Ex.: Dividir quando o arquivo acumular responsabilidades independentes ou apresentar blocos que evoluem por motivos diferentes.

Critério para mover código específico para uma área compartilhada:

Ex.: Mover somente após reutilização real por pelo menos duas features e quando o elemento não depender do contexto interno de nenhuma delas.

Interface pública padrão dos módulos:

Ex.: O arquivo `index.ts` exporta apenas contratos e elementos permitidos para consumidores externos.

## 14. Dependências e imports

Aliases disponíveis:

Ex.:

- `@app/*` → `src/app/*`;
- `@features/*` → `src/features/*`;
- `@shared/*` → `src/shared/*`;
- `@infrastructure/*` → `src/infrastructure/*`.

Direção permitida dos imports:

Ex.:

```text
app/
--features/
----shared/

features/
--shared/

infrastructure/
--shared/
```

Imports proibidos:

Ex.:

- `shared` importando `features`;
- uma feature importando internals de outra feature;
- domínio importando interface ou infraestrutura concreta.

Política para imports relativos:

Ex.: Imports relativos podem ser usados dentro do mesmo módulo e não devem atravessar fronteiras arquiteturais.

Política para reexports:

Ex.: Reexports devem ocorrer apenas nas interfaces públicas dos módulos e não devem ocultar dependências circulares.

Política para dependências circulares:

Ex.: Dependências circulares são proibidas e devem ser eliminadas por extração de contratos ou reorganização das responsabilidades.

## 15. Convenções específicas do projeto

Padrão de nomes de arquivos:

Ex.:

- componentes: `PascalCase.tsx`;
- hooks: `useNomeDoHook.ts`;
- serviços: `nomeDoServicoService.ts`;
- tipos: `nomeDoContexto.types.ts`.

Padrão de nomes de diretórios:

Ex.: `camelCase` para features e diretórios técnicos.

Padrão de componentes:

Ex.: Um componente principal por arquivo, com tipos auxiliares locais quando não forem reutilizados.

Padrão de hooks:

Ex.: Hooks encapsulam estado ou comportamento reutilizável e começam com `use`.

Padrão de serviços:

Ex.: Serviços representam operações de aplicação ou comunicação e não contêm detalhes visuais.

Padrão de stores:

Ex.: Cada store possui responsabilidade específica e expõe apenas estado e ações necessárias.

Padrão de tipos e contratos:

Ex.: Tipos locais permanecem próximos ao uso; contratos públicos ficam na interface pública do módulo.

Padrão de arquivos de índice:

Ex.: `index.ts` define a API pública do diretório e não deve reexportar automaticamente todos os arquivos internos.

Padrão de testes:

Ex.: Arquivos de teste permanecem próximos ao código testado com sufixo `.test.ts` ou `.test.tsx`.

# Parte IV — Regras de implementação

## 16. Regras gerais de implementação

Critério para considerar uma funcionalidade pertencente ao projeto:

Ex.: A funcionalidade deve estar dentro do escopo definido e possuir módulo responsável identificado.

Critério para alterar uma funcionalidade existente:

Ex.: A alteração deve preservar contratos, restrições e comportamentos marcados como obrigatórios.

Critério para criar uma nova abstração:

Ex.: Criar somente quando houver responsabilidade estável, reutilização real ou necessidade de isolar uma dependência variável.

Critério para reutilizar código existente:

Ex.: Reutilizar quando o contrato e a responsabilidade forem equivalentes, sem introduzir condicionais específicas de consumidores distintos.

Critério para duplicação temporária:

Ex.: Permitida apenas quando uma abstração comum criaria acoplamento incorreto; a decisão deve ser registrada no README.

Critério para criação de código compartilhado:

Ex.: O código deve ser reutilizado por múltiplos módulos e não pode depender de um contexto específico.

Comportamentos que toda nova implementação deve preservar:

Ex.:

- contratos públicos;
- formatos de arquivos;
- estado persistido;
- acessibilidade existente;
- fluxo atual de geração de documentos.

## 17. Front-end

Aplicabilidade da seção:

Ex.: Aplicável quando o projeto possuir interface gráfica.

### 17.1 Páginas e rotas

Diretório das páginas:

Ex.: `src/pages/`

Responsabilidade das páginas:

Ex.: Compor a interface de uma rota e coordenar componentes e hooks da funcionalidade.

Conteúdo permitido nas páginas:

Ex.:

- composição visual;
- leitura de parâmetros de rota;
- acionamento de hooks e casos de uso.

Conteúdo proibido nas páginas:

Ex.:

- acesso direto a APIs;
- regras de negócio complexas;
- implementação de persistência.

Local de definição das rotas:

Ex.: `src/app/router/`

Estratégia de proteção de rotas:

Ex.: Guards declarativos baseados no estado de autenticação.

Estratégia para parâmetros de rota:

Ex.: Parâmetros devem ser validados antes de serem utilizados pela feature.

### 17.2 Componentes

Diretório dos componentes específicos de uma feature:

Ex.: `src/features/nomeDaFeature/components/`

Diretório dos componentes compartilhados:

Ex.: `src/shared/components/`

Critério para considerar um componente compartilhado:

Ex.: Ser reutilizado por múltiplas features sem conhecer regras específicas de nenhuma delas.

Responsabilidade permitida nos componentes:

Ex.: Apresentação, interação local e delegação de eventos.

Responsabilidade proibida nos componentes:

Ex.: Acesso direto a APIs, banco de dados ou regras de negócio independentes da interface.

Critério para divisão de componentes:

Ex.: Dividir quando partes possuírem responsabilidade, estado, reutilização ou ciclo de alteração próprios.

Política de propriedades:

Ex.: Props devem representar contratos explícitos, mínimos e orientados ao comportamento do componente.

### 17.3 Estado

Critério para utilizar estado local:

Ex.: Quando o estado pertencer a um único componente ou à sua subárvore imediata.

Critério para utilizar estado da feature:

Ex.: Quando múltiplos elementos da mesma feature precisarem compartilhar estado persistente durante o fluxo.

Critério para utilizar estado global:

Ex.: Somente quando múltiplas features independentes precisarem acessar ou alterar o mesmo estado.

Critério para utilizar estado remoto:

Ex.: Quando os dados tiverem origem externa e exigirem cache, sincronização ou revalidação.

Diretório das stores globais:

Ex.: `src/shared/stores/`

Diretório das stores específicas:

Ex.: `src/features/nomeDaFeature/store/`

Critério para criar uma nova store:

Ex.: Criar apenas quando o estado não puder permanecer local e possuir responsabilidade claramente delimitada.

Conteúdo proibido nas stores:

Ex.:

- componentes;
- chamadas diretas de apresentação;
- dados derivados que possam ser calculados por seletores;
- múltiplos domínios sem relação.

Estratégia de persistência do estado:

Ex.: Persistir apenas preferências necessárias entre sessões usando adaptador de armazenamento definido.

### 17.4 Formulários e validação

Biblioteca padrão para formulários:

Ex.: React Hook Form.

Biblioteca padrão para validação:

Ex.: Zod.

Local dos schemas de validação:

Ex.: Próximos à feature ou formulário que utiliza o contrato.

Momento da validação no cliente:

Ex.: Validar na alteração para feedback simples e no envio para validação completa.

Tratamento de erros de formulário:

Ex.: Exibir mensagens próximas aos campos e manter um resumo apenas quando necessário.

Conversão entre valores da interface e domínio:

Ex.: Adaptadores devem converter strings de formulário em tipos de domínio antes do caso de uso.

### 17.5 Estilos e interface

Estratégia principal de estilos:

Ex.: CSS Modules com tokens globais.

Local dos estilos globais:

Ex.: `src/app/styles/`

Local dos estilos específicos:

Ex.: Próximos aos componentes que utilizam os estilos.

Estratégia para tokens visuais:

Ex.: Variáveis CSS centralizadas para cores, tipografia, espaçamento e bordas.

Critério para criar um componente visual compartilhado:

Ex.: Criar após recorrência real de estrutura e comportamento visual em múltiplas features.

Regras de responsividade:

Ex.: Layout fluido com pontos de quebra definidos nos tokens do projeto.

Regras de acessibilidade específicas:

Ex.:

- todos os controles possuem nome acessível;
- estados não são comunicados apenas por cor;
- foco visível deve ser preservado.

## 18. Back-end

Aplicabilidade da seção:

Ex.: Aplicável quando o projeto possuir API, servidor ou processamento no back-end.

### 18.1 Transporte e API

Diretório das rotas:

Ex.: `src/interfaces/http/routes/`

Responsabilidade das rotas:

Ex.: Declarar método, caminho, middleware e handler responsável.

Diretório dos controllers ou handlers:

Ex.: `src/interfaces/http/controllers/`

Responsabilidade dos controllers ou handlers:

Ex.: Converter transporte em entrada de aplicação e resposta de aplicação em resposta HTTP.

Formato padrão de sucesso:

Ex.:

```text
{
  "data": {},
  "meta": {}
}
```

Formato padrão de erro:

Ex.:

```text
{
  "error": {
    "code": "RESOURCE_NOT_FOUND",
    "message": "Recurso não encontrado"
  }
}
```

Estratégia de versionamento da API:

Ex.: Prefixo `/api/v1`.

Política de paginação:

Ex.: Paginação por cursor para coleções potencialmente grandes.

Política de filtros e ordenação:

Ex.: Parâmetros explícitos e validados por schema.

### 18.2 Aplicação

Diretório dos casos de uso:

Ex.: `src/application/useCases/`

Responsabilidade dos casos de uso:

Ex.: Coordenar regras, contratos e efeitos necessários para concluir uma ação do sistema.

Responsabilidade dos serviços de aplicação:

Ex.: Encapsular operações reutilizadas por múltiplos casos de uso sem assumir detalhes de transporte.

Estratégia de transação:

Ex.: O caso de uso define o limite transacional e utiliza uma abstração de unidade de trabalho.

Estratégia para idempotência:

Ex.: Operações sensíveis aceitam uma chave de idempotência persistida.

Estratégia para concorrência:

Ex.: Atualizações críticas utilizam controle otimista por versão.

### 18.3 Domínio

Diretório do domínio:

Ex.: `src/domain/`

Entidades principais:

Ex.:

- User;
- Document;
- Template.

Objetos de valor principais:

Ex.:

- Email;
- DocumentId;
- PageSize.

Invariantes obrigatórias:

Ex.: Um documento deve possuir pelo menos uma página válida antes de ser gerado.

Local das regras de negócio:

Ex.: Entidades, objetos de valor e serviços de domínio.

Dependências permitidas no domínio:

Ex.: Tipos da linguagem e contratos abstratos definidos pelo próprio domínio.

Dependências proibidas no domínio:

Ex.:

- framework HTTP;
- ORM;
- componentes de interface;
- clientes externos concretos.

### 18.4 Infraestrutura

Diretório dos repositories concretos:

Ex.: `src/infrastructure/database/repositories/`

Diretório dos clientes externos:

Ex.: `src/infrastructure/integrations/`

Diretório dos adaptadores de armazenamento:

Ex.: `src/infrastructure/storage/`

Responsabilidade da infraestrutura:

Ex.: Implementar contratos definidos pelas camadas internas usando tecnologias concretas.

Critério para substituir uma implementação de infraestrutura:

Ex.: A substituição deve preservar o contrato interno e os comportamentos observáveis definidos.

## 19. Persistência

Aplicabilidade da seção:

Ex.: Aplicável quando o projeto armazenar dados além do ciclo atual de execução.

Responsabilidade da camada de persistência:

Ex.: Armazenar e recuperar dados sem expor detalhes do banco às camadas consumidoras.

Diretório dos schemas ou modelos de persistência:

Ex.: `src/infrastructure/database/schema/`

Diretório das migrações:

Ex.: `database/migrations/`

Diretório das seeds:

Ex.: `database/seeds/`

Camadas autorizadas a acessar o banco diretamente:

Ex.: Somente repositories e ferramentas de migração.

Camadas proibidas de acessar o banco diretamente:

Ex.:

- controllers;
- componentes;
- casos de uso;
- entidades de domínio.

Estratégia de integridade dos dados:

Ex.: Restrições no banco complementadas por validações e invariantes no domínio.

Estratégia de migração:

Ex.: Migrações incrementais, versionadas e compatíveis com rollback quando tecnicamente possível.

Estratégia de backup antes de migrações críticas:

Ex.: Backup obrigatório antes de alterações destrutivas em produção.

Estratégia para dados de teste:

Ex.: Factories isoladas e banco descartável por suíte de integração.

## 20. Integrações externas

Integrações existentes:

Ex.:

- serviço de CEP;
- armazenamento de arquivos;
- provedor de e-mail.

Para cada integração, preencher os campos abaixo.

Nome da integração:

Ex.: ViaCEP.

Finalidade da integração:

Ex.: Consultar endereço a partir de um CEP informado.

Módulo responsável:

Ex.: `addressLookup`.

Cliente ou adaptador utilizado:

Ex.: `ViaCepClient`.

Diretório da implementação:

Ex.: `src/infrastructure/integrations/viaCep/`

Contrato interno exposto:

Ex.: `AddressLookupGateway`.

Estratégia de autenticação:

Ex.: Não se aplica.

Timeout definido:

Ex.: 5 segundos.

Política de repetição:

Ex.: Até duas novas tentativas para falhas transitórias.

Política de espera entre tentativas:

Ex.: Backoff exponencial com limite máximo de 2 segundos.

Estratégia de fallback:

Ex.: Permitir preenchimento manual quando a consulta falhar.

Tratamento de erros:

Ex.: Converter falhas externas em erros internos estáveis sem expor detalhes do provedor.

Limites de uso:

Ex.: Até 100 requisições por minuto por instância.

## 21. Autenticação e autorização

Aplicabilidade da seção:

Ex.: Aplicável quando o sistema identificar usuários ou restringir ações.

Modelo de autenticação:

Ex.: E-mail e senha com sessão baseada em tokens.

Modelo de autorização:

Ex.: Controle de acesso baseado em papéis e permissões.

Papéis existentes:

Ex.:

- administrator;
- editor;
- viewer.

Permissões existentes:

Ex.:

- `document:create`;
- `document:update`;
- `document:delete`.

Local da validação de autenticação:

Ex.: Middleware HTTP e serviço de sessão.

Local da validação de autorização:

Ex.: Casos de uso ou política central antes da execução da ação.

Estratégia de armazenamento de sessão ou token:

Ex.: Refresh token em cookie seguro e access token mantido em memória.

Tempo de expiração:

Ex.:

- access token: 15 minutos;
- refresh token: 7 dias.

Estratégia de revogação:

Ex.: Refresh tokens versionados e revogáveis no servidor.

Regras para rotas protegidas:

Ex.: Rotas privadas exigem sessão válida e permissões explícitas quando aplicável.

## 22. Processamentos especializados

Processamentos especializados existentes:

Ex.:

- geração de PDF;
- importação de TCX;
- processamento de imagens;
- geração de relatórios;
- inteligência artificial.

Para cada processamento especializado, preencher os campos abaixo.

Nome do processamento:

Ex.: Geração de PDF.

Responsabilidade:

Ex.: Transformar um modelo e seus dados em um arquivo PDF final.

Módulo responsável:

Ex.: `documentGeneration`.

Entrada esperada:

Ex.: Modelo validado e dados normalizados.

Saída esperada:

Ex.: Arquivo PDF em memória ou stream.

Contrato interno:

Ex.: `DocumentGenerator`.

Dependências permitidas:

Ex.: Engine de PDF e contratos públicos de modelos.

Dependências proibidas:

Ex.: Componentes visuais e estado direto da interface.

Restrições obrigatórias:

Ex.:

- preservar dimensões dos templates;
- preservar quebra de páginas;
- preservar fontes incorporadas.

Comportamentos existentes que devem ser preservados:

Ex.:

- conteúdo do arquivo;
- ordem das páginas;
- visualização prévia equivalente ao documento final.

# Parte V — Configuração, qualidade e entrega

## 23. Configuração e ambientes

Ambientes existentes:

Ex.:

- development;
- test;
- staging;
- production.

Diretório ou módulo de configuração:

Ex.: `src/config/`

Variáveis de ambiente obrigatórias:

Ex.:

- `DATABASE_URL`;
- `API_BASE_URL`;
- `SESSION_SECRET`.

Variáveis de ambiente opcionais:

Ex.:

- `LOG_LEVEL`;
- `PORT`.

Valores padrão permitidos:

Ex.:

- `PORT=3000`;
- `LOG_LEVEL=info`.

Estratégia de validação da configuração:

Ex.: Validar todas as variáveis no início da aplicação com schema tipado.

Arquivo de exemplo das variáveis:

Ex.: `.env.example`

Dados que nunca podem ser versionados:

Ex.:

- segredos;
- tokens;
- credenciais;
- dados pessoais reais.

Diferenças obrigatórias entre ambientes:

Ex.: Produção utiliza logs estruturados e não exibe detalhes internos de erro.

## 24. Erros, logs e observabilidade

Modelo interno de erros:

Ex.: Classes ou objetos tipados separados por categoria de domínio, aplicação e infraestrutura.

Categorias de erro existentes:

Ex.:

- validationError;
- notFoundError;
- conflictError;
- externalServiceError;
- internalError.

Local de conversão de erros técnicos:

Ex.: Nas fronteiras entre infraestrutura, aplicação e transporte.

Formato de erro exposto externamente:

Ex.: Código estável, mensagem segura e identificador de correlação.

Biblioteca de logs:

Ex.: Pino.

Formato dos logs:

Ex.: JSON estruturado.

Campos obrigatórios nos logs:

Ex.:

- timestamp;
- level;
- message;
- correlationId;
- operation.

Dados proibidos nos logs:

Ex.:

- senhas;
- tokens;
- documentos pessoais completos;
- conteúdo sensível de arquivos.

Estratégia de correlação:

Ex.: Um `correlationId` é criado ou propagado por requisição e operação assíncrona.

Métricas obrigatórias:

Ex.:

- duração das operações críticas;
- taxa de erros;
- quantidade de arquivos gerados.

## 25. Testes

Estratégia geral de testes:

Ex.: Testes unitários para regras, integração para fronteiras e ponta a ponta para fluxos críticos.

Diretório ou localização dos testes unitários:

Ex.: Próximos aos arquivos testados.

Diretório dos testes de integração:

Ex.: `tests/integration/`

Diretório dos testes de ponta a ponta:

Ex.: `tests/e2e/`

Partes que exigem testes unitários:

Ex.:

- regras de negócio;
- validações;
- transformações;
- seletores;
- utilitários não triviais.

Partes que exigem testes de integração:

Ex.:

- repositories;
- clientes externos;
- persistência;
- endpoints.

Fluxos que exigem testes de ponta a ponta:

Ex.:

- criação de documento;
- visualização prévia;
- geração do PDF.

Estratégia de mocks:

Ex.: Mockar fronteiras externas e evitar mocks de detalhes internos da unidade testada.

Estratégia para banco de testes:

Ex.: Banco isolado, descartável e migrado antes da suíte.

Estratégia para fixtures e factories:

Ex.: Factories reutilizáveis com valores válidos por padrão e sobrescritas explícitas.

Cobertura mínima obrigatória:

Ex.: Não se aplica; fluxos e regras críticas devem possuir cobertura explícita.

## 26. Build, validação e entrega

Comando de desenvolvimento:

Ex.: `npm run dev`

Comando de build:

Ex.: `npm run build`

Comando de lint:

Ex.: `npm run lint`

Comando de verificação de tipos:

Ex.: `npm run typecheck`

Comando de testes unitários:

Ex.: `npm run test`

Comando de testes de integração:

Ex.: `npm run test:integration`

Comando de testes de ponta a ponta:

Ex.: `npm run test:e2e`

Comando de formatação:

Ex.: `npm run format`

Artefato gerado pelo build:

Ex.: Diretório `dist/`.

Estratégia de empacotamento:

Ex.: Build estático produzido pelo Vite.

Estratégia de deploy:

Ex.: Publicação automática após aprovação na branch principal.

Validações obrigatórias antes de concluir uma alteração:

Ex.:

- lint;
- tipagem;
- testes afetados;
- build.

Critério técnico para considerar uma implementação concluída:

Ex.: Código integrado, validações aprovadas, contratos preservados e regras deste documento atendidas.

# Parte VI — Controle arquitetural

## 27. Restrições obrigatórias

Arquivos, módulos ou áreas que não podem ser removidos:

Ex.:

- engine atual de geração de PDF;
- contratos públicos de templates.

Tecnologias que não podem ser substituídas sem decisão explícita:

Ex.:

- Zustand;
- biblioteca de geração de PDF;
- formato de persistência local.

Comportamentos que não podem ser alterados:

Ex.:

- resultado visual dos PDFs;
- fluxo da visualização prévia;
- formato dos arquivos importados e exportados.

Contratos que devem permanecer compatíveis:

Ex.:

- propriedades públicas dos templates;
- formato dos dados persistidos;
- respostas públicas da API.

Acessos diretos proibidos:

Ex.:

- componentes acessando APIs;
- casos de uso acessando banco;
- features importando internals de outras features.

Duplicações arquiteturais proibidas:

Ex.:

- duas pastas compartilhadas com a mesma responsabilidade;
- múltiplos clientes para a mesma integração sem contrato comum;
- stores concorrentes para o mesmo estado.

## 28. Decisões pendentes

Para cada decisão ainda não tomada, preencher os campos abaixo.

Decisão pendente:

Ex.: Escolha da estratégia de autenticação.

Motivo da pendência:

Ex.: O modelo de usuários ainda não foi definido.

Impacto da decisão:

Ex.: Afeta rotas, persistência, segurança e estrutura do back-end.

Opções consideradas:

Ex.:

- sessão no servidor;
- JWT;
- provedor externo.

Regra temporária até a decisão:

Ex.: Não implementar autenticação nem criar abstrações provisórias.

Seções afetadas quando a decisão for concluída:

Ex.:

- Stack tecnológica;
- Autenticação e autorização;
- Estrutura de diretórios.

## 29. Checklist para novas implementações

- [ ] A implementação pertence ao escopo definido.
- [ ] O módulo responsável foi identificado.
- [ ] As decisões pendentes relacionadas foram verificadas.
- [ ] A implementação segue a arquitetura adotada.
- [ ] A estrutura de diretórios foi respeitada.
- [ ] A responsabilidade de cada arquivo está clara.
- [ ] A direção permitida dos imports foi respeitada.
- [ ] Nenhum módulo interno foi acessado fora de sua interface pública.
- [ ] Contratos existentes foram reutilizados quando aplicáveis.
- [ ] Nenhum estado global foi criado sem necessidade comprovada.
- [ ] Nenhum código foi movido para `shared` sem reutilização real.
- [ ] Nenhuma abstração foi criada preventivamente.
- [ ] As restrições obrigatórias foram preservadas.
- [ ] Os comportamentos existentes protegidos permanecem inalterados.
- [ ] Erros são tratados na fronteira adequada.
- [ ] Logs não expõem dados sensíveis.
- [ ] Testes necessários foram adicionados ou atualizados.
- [ ] Lint foi executado com sucesso.
- [ ] Verificação de tipos foi executada com sucesso.
- [ ] Testes afetados foram executados com sucesso.
- [ ] Build foi executado com sucesso.
