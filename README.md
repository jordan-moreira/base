# README

## Objetivo do documento

Este documento apresenta o projeto, seu contexto, seu estado atual e orienta sua execução, navegação e continuidade do desenvolvimento.

Não deve conter regras arquiteturais, padrões gerais de desenvolvimento ou documentação detalhada da implementação.

As decisões arquiteturais específicas do projeto pertencem ao `regrasProjeto.md`.

Os padrões gerais de desenvolvimento pertencem ao `regrasDev.md`.

---

# Regras de preenchimento

- Documentar sempre o estado atual do projeto.
- Priorizar informações úteis para compreensão, execução, navegação e retomada do desenvolvimento.
- Organizar as informações do geral para o específico.
- Utilizar campos declarativos sempre que possível.
- Utilizar textos explicativos apenas quando forem necessários para evitar ambiguidades.
- Utilizar exemplos somente quando o conteúdo esperado para o campo não for evidente.
- Remover os exemplos após o preenchimento definitivo do campo.
- Não repetir decisões presentes no `regrasProjeto.md`.
- Não repetir padrões presentes no `regrasDev.md`.
- Não documentar funções, componentes ou arquivos linha a linha.
- Não utilizar o README como histórico detalhado de alterações.
- Não utilizar o README como backlog completo do projeto.
- Manter o conteúdo no nível de conceitos, fluxos e pontos de entrada.
- Representar fluxos do sistema em alto nível, sem detalhar a implementação interna.
- Utilizar caminhos relativos ao repositório ao referenciar arquivos e diretórios.
- Utilizar `Não se aplica.` quando um campo não fizer parte do projeto.
- Utilizar `Pendente.` quando uma informação ainda não estiver definida.

## Critérios de atualização

Atualizar este documento sempre que houver alteração relevante em:

- objetivo ou escopo atual do projeto;
- forma de instalação, configuração ou execução;
- pré-requisitos do ambiente;
- pontos de entrada da aplicação;
- fluxo principal do sistema;
- localização das principais responsabilidades;
- orientações para navegação no código;
- pontos críticos para manutenção;
- documentação relacionada.

## Critérios para novas seções

Uma nova seção somente deve ser criada quando:

- representar uma responsabilidade diferente das seções existentes;
- não puder ser incorporada de forma clara a outra seção;
- ajudar qualquer pessoa a compreender, executar, localizar ou continuar o projeto;
- não duplicar conteúdo do `regrasProjeto.md`, do `regrasDev.md` ou de uma documentação específica em `docs/`.

---

# PARTE I — Identificação do projeto

## Nome

Ex.:

Sistema de gerenciamento de estoque.

## Descrição

Ex.:

Aplicação web destinada ao controle de produtos, movimentações e inventário.

## Objetivo

Ex.:

Automatizar o controle de entradas, saídas e disponibilidade de produtos.

## Problema que resolve

Ex.:

Substituir controles manuais e descentralizados realizados por planilhas.

## Público-alvo

Ex.:

Empresas de pequeno e médio porte responsáveis pelo controle de estoque.

## Situação atual

Ex.:

MVP funcional em validação.

## Licença

Ex.:

MIT.

---

# PARTE II — Contexto

## Origem do projeto

Ex.:

Projeto acadêmico desenvolvido como trabalho de conclusão de curso.

## Motivação

Ex.:

Necessidade de reduzir tarefas manuais e centralizar informações operacionais.

## Escopo atual

Ex.:

Aplicação web com cadastro, consulta, atualização e remoção de registros.

## Objetivo de longo prazo

Ex.:

Evoluir o sistema para uma plataforma completa com integrações externas e automações.

## Premissas importantes

Ex.:

- O sistema será utilizado inicialmente por uma única organização.
- O acesso depende de autenticação.
- A aplicação deve funcionar em navegadores modernos.

## Limitações conhecidas

Ex.:

- Não existe suporte a múltiplos idiomas.
- Não existe sincronização com sistemas externos.

---

# PARTE III — Estado atual

## Versão atual

Ex.:

`0.1.0`

## Situação geral

Ex.:

O fluxo principal está implementado e o projeto encontra-se em fase de validação.

## Funcionalidades concluídas

Ex.:

- Cadastro de usuários.
- Autenticação.
- Cadastro de produtos.
- Consulta de movimentações.

## Funcionalidades em desenvolvimento

Ex.:

- Relatórios.
- Exportação de dados.

## Funcionalidades planejadas

Ex.:

- Integração com serviços externos.
- Controle de permissões por função.

## Principais pendências

Ex.:

- Finalizar testes de integração.
- Configurar ambiente de produção.

## Débitos técnicos conhecidos

Ex.:

- Cobertura de testes insuficiente em módulos legados.
- Validações duplicadas em fluxos específicos.

---

# PARTE IV — Primeiros passos

## Pré-requisitos

Ex.:

- Node.js 22.
- Docker.
- MySQL 9.

## Clonagem

```bash
git clone <url-do-repositorio>
cd <nome-do-repositorio>
```

## Instalação

Ex.:

```bash
npm install
```

## Configuração

Descrever os arquivos, variáveis e serviços que precisam ser configurados antes da execução.

Ex.:

```bash
cp .env.example .env
```

Variáveis obrigatórias:

```env
DATABASE_URL=
PORT=
```

## Banco de dados

Descrever como criar, iniciar, migrar ou popular o banco de dados.

Ex.:

```bash
npm run database:migrate
npm run database:seed
```

## Execução em desenvolvimento

Ex.:

```bash
npm run dev
```

## Build

Ex.:

```bash
npm run build
```

## Execução da build

Ex.:

```bash
npm start
```

## Testes

Ex.:

```bash
npm test
```

## Verificação de qualidade

Ex.:

```bash
npm run lint
npm run typecheck
```

## Deploy local

Descrever apenas quando existir um fluxo local diferente da execução comum.

Ex.:

```bash
docker compose up --build
```

---

# PARTE V — Guia de navegação

## Ordem de leitura da documentação

1. `README.md`
2. `regrasProjeto.md`
3. `regrasDev.md`
4. Documentações específicas disponíveis em `docs/`

## Fluxo recomendado para conhecer o projeto

Ex.:

1. Leia este README integralmente.
2. Execute o projeto localmente.
3. Leia o `regrasProjeto.md` para compreender as decisões específicas.
4. Leia o `regrasDev.md` para compreender os padrões gerais de implementação.
5. Identifique o ponto de entrada da aplicação.
6. Acompanhe o fluxo principal até os módulos responsáveis pelas regras de negócio.
7. Navegue pela funcionalidade relacionada ao objetivo da alteração.

## Ponto de entrada da aplicação

Ex.:

`src/main.ts`

## Ponto de entrada do front-end

Ex.:

`src/app/App.tsx`

## Ponto de entrada do back-end

Ex.:

`src/server.ts`

## Localização das funcionalidades

Ex.:

`src/features/`

## Localização das regras de negócio

Ex.:

`src/domain/`

## Localização dos componentes compartilhados

Ex.:

`src/shared/components/`

## Localização dos estados compartilhados

Ex.:

`src/shared/stores/`

## Localização das integrações

Ex.:

`src/infrastructure/integrations/`

## Localização da persistência

Ex.:

`src/infrastructure/database/`

## Localização das configurações

Ex.:

`src/config/`

## Localização dos arquivos estáticos

Ex.:

`public/`

## Localização dos testes

Ex.:

`tests/`

## Localização da documentação específica

Ex.:

`docs/`

## Como localizar rapidamente uma funcionalidade

Ex.:

1. Identifique o nome funcional utilizado pela interface ou pelo domínio.
2. Localize a feature correspondente.
3. Inicie pela tela, rota, controller ou caso de uso principal.
4. Acompanhe os imports e chamadas até a regra de negócio.
5. Identifique os contratos, serviços, persistência e testes relacionados.

## Como localizar a origem de um comportamento

Ex.:

1. Identifique onde o comportamento aparece para o usuário.
2. Localize o evento que inicia o fluxo.
3. Acompanhe a chamada até o módulo responsável.
4. Verifique regras de negócio antes de alterar componentes de interface.
5. Consulte os testes existentes para confirmar o comportamento esperado.

---

# PARTE VI — Fluxos do sistema

## Fluxo principal

Descrever o caminho principal percorrido pelos dados ou pelas ações do usuário.

Ex.:

```text
Usuário
↓
Interface
↓
Validação
↓
Regra de negócio
↓
Persistência
↓
Resposta
```

## Fluxos secundários

Descrever apenas fluxos relevantes para compreensão geral do sistema.

Ex.:

- Recuperação de senha.
- Exportação de dados.
- Geração de documentos.
- Sincronização com serviço externo.

## Entrada de dados

Ex.:

- Formulários da interface.
- Arquivos importados.
- Requisições de APIs externas.

## Processamento

Ex.:

Os dados são validados, transformados e encaminhados ao módulo responsável pela regra de negócio.

## Persistência

Ex.:

Os dados processados são armazenados no banco de dados por meio da camada de persistência.

## Saída de dados

Ex.:

- Respostas da API.
- Atualização da interface.
- Arquivos gerados.
- Notificações.

## Integrações externas

Ex.:

```text
Aplicação
↓
Serviço de integração
↓
API externa
↓
Normalização da resposta
↓
Aplicação
```

## Fluxos específicos documentados

Referenciar documentos adicionais quando um fluxo exigir detalhamento próprio.

Ex.:

- `docs/fluxoAutenticacao.md`
- `docs/fluxoGeracaoPdf.md`

---

# PARTE VII — Continuidade do desenvolvimento

## Ponto inicial recomendado

Descrever por onde uma pessoa deve começar ao retomar o projeto.

Ex.:

1. Verifique o estado atual descrito neste README.
2. Execute o projeto e valide o fluxo principal.
3. Consulte as pendências conhecidas.
4. Leia a documentação da funcionalidade que será alterada.
5. Confirme as regras aplicáveis no `regrasProjeto.md` e no `regrasDev.md`.

## Pontos críticos

Ex.:

- Alterações no mecanismo de geração de PDF afetam exportação e preview.
- Mudanças em contratos compartilhados podem afetar múltiplas funcionalidades.

## Áreas de maior impacto

Ex.:

- Autenticação.
- Persistência.
- Estado global.
- Geração de arquivos.

## Dependências importantes

Ex.:

- Banco de dados disponível para execução local.
- Serviço externo necessário para autenticação.
- Ferramenta de geração de documentos instalada.

## Cuidados antes de alterar

Ex.:

- Verificar reutilização antes de modificar código compartilhado.
- Confirmar contratos públicos existentes.
- Executar testes relacionados.
- Validar fluxos dependentes da funcionalidade alterada.

## Fluxo recomendado para implementar uma nova funcionalidade

Ex.:

1. Confirmar o escopo da funcionalidade.
2. Consultar as regras específicas no `regrasProjeto.md`.
3. Identificar a feature ou módulo responsável.
4. Reutilizar contratos e componentes existentes quando aplicável.
5. Implementar a regra de negócio.
6. Integrar a interface e a infraestrutura necessárias.
7. Adicionar ou atualizar testes.
8. Validar o fluxo completo.
9. Atualizar a documentação afetada.

## Fluxo recomendado para corrigir um problema

Ex.:

1. Reproduzir o problema.
2. Identificar o comportamento esperado.
3. Localizar a origem do comportamento.
4. Verificar testes e contratos relacionados.
5. Corrigir a causa, não apenas o efeito visível.
6. Adicionar um teste que cubra o problema.
7. Validar fluxos relacionados.
8. Atualizar a documentação quando necessário.

## Melhorias previstas

Ex.:

- Aumentar a cobertura de testes.
- Reduzir acoplamento entre módulos.
- Automatizar tarefas de configuração.

## Observações para futuras manutenções

Ex.:

- Determinados módulos ainda dependem de contratos legados.
- Alguns fluxos precisam ser validados manualmente após alterações.

## Informações que não devem ser perdidas

Registrar conhecimentos essenciais que ainda não estejam evidentes no código ou em outros documentos.

Ex.:

- Restrições externas que influenciam o comportamento do sistema.
- Dependências temporárias.
- Compatibilidades que precisam ser preservadas.

---

# PARTE VIII — Documentação relacionada

## `regrasProjeto.md`

Responsabilidade:

Define as decisões, restrições e regras específicas para construção e evolução deste projeto.

## `regrasDev.md`

Responsabilidade:

Define os padrões gerais de engenharia e desenvolvimento aplicáveis ao projeto.

## `docs/`

Responsabilidade:

Armazena documentações específicas que exigem maior detalhamento e não pertencem ao README.

## Diagramas

Ex.:

- `docs/diagramas/arquitetura.md`
- `docs/diagramas/fluxoPrincipal.md`

## Documentação de APIs

Ex.:

- `docs/api/`
- OpenAPI ou Swagger.

## Documentação do banco de dados

Ex.:

- `docs/database/`
- Diagrama entidade-relacionamento.

## Documentação externa

Ex.:

- Documentação oficial das tecnologias utilizadas.
- Documentação de serviços integrados.

## Referências técnicas

Ex.:

- Artigos.
- Normas.
- Especificações.
- Repositórios de referência.
