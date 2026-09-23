# Auditoria integral de conformidade

## Objetivo do documento

Este documento registra, para cada seção e subseção numerada de `regrasDev.md`, `regrasUxUi.md` e `regrasProjeto.md`, o status de conformidade e a evidência correspondente no estado auditado, conforme a regra de auditoria integral de conformidade de `regrasDev.md`.

As linhas deste template constituem o conteúdo mínimo obrigatório e não podem ser removidas. O status `Descritiva` é atribuído exclusivamente pelo template.

## Regras de preenchimento

- Preencher o status de toda linha; linha sem status impede a conclusão da alteração.
- Utilizar somente os status `Conforme`, `Exceção autorizada`, `N/A`, `Descritiva` e `Não conforme`, este último somente em commit intermediário.
- `N/A` exige justificativa verificável na coluna de justificativa.
- `Exceção autorizada` exige, na coluna de justificativa, referência ao registro de exceções de `regrasProjeto.md`.
- A evidência de cada linha deve permitir localizar a demonstração da regra específica; código de catálogo amplo deve ser complementado com referência específica, no formato `CÓDIGO · referência`.
- Para seções de `regrasProjeto.md`, `Conforme` significa que os campos da seção estão preenchidos, ou declarados `Não se aplica.` com justificativa, e que a implementação corresponde às decisões registradas.
- Utilizar `—` nas colunas sem conteúdo aplicável.

## Referências

Data:

Commit do `base` adotado:

Estado auditado: o do commit que contém este documento.

## Catálogo de evidências

O tipo é `automatizada`, `inspeção` ou `automatizada e inspeção`. A reprodução é o comando exato ou, para inspeção, o critério verificado.

| Código | Artefatos | Tipo | Reprodução |
|---|---|---|---|

## `regrasDev.md`

| Regra | Título | Status | Evidência | Justificativa |
|---|---|---|---|---|
| 1 | Objetivo | Descritiva | — | — |
| 2 | Natureza normativa e mutabilidade |  |  |  |
| 3 | Relação entre os documentos |  |  |  |
| 4 | Aplicação independente e cumulativa |  |  |  |
| 5 | Precedência e conflitos |  |  |  |
| 6 | Não conformidades e exceções |  |  |  |
| 7 | Clareza |  |  |  |
| 8 | Responsabilidade |  |  |  |
| 8.1 | Elementos sem responsabilidade vigente |  |  |  |
| 9 | Coesão |  |  |  |
| 10 | Acoplamento |  |  |  |
| 11 | Arquitetura proporcional |  |  |  |
| 12 | Proximidade |  |  |  |
| 13 | Corretude antes da simplificação |  |  |  |
| 13.1 | Eficiência computacional proporcional |  |  |  |
| 13.2 | Trabalho computacional redundante |  |  |  |
| 13.3 | Caminho crítico, concorrência e paralelismo |  |  |  |
| 13.4 | Medição de desempenho |  |  |  |
| 13.5 | Ciclo de vida de recursos |  |  |  |
| 13.6 | Volumes sem limite |  |  |  |
| 14 | Projeto como árvore semântica |  |  |  |
| 15 | Bloco lógico indivisível |  |  |  |
| 16 | Menor árvore semanticamente suficiente |  |  |  |
| 17 | Balanceamento horizontal e vertical |  |  |  |
| 18 | Modularização das folhas para a raiz |  |  |  |
| 19 | Ordem entre modularização e balanceamento |  |  |  |
| 20 | Revalidação do ramo afetado |  |  |  |
| 21 | Unidade de modularização |  |  |  |
| 22 | Regra de divisão |  |  |  |
| 23 | Regra de permanência |  |  |  |
| 24 | Regra de alocação |  |  |  |
| 25 | Menor abstração semanticamente suficiente |  |  |  |
| 26 | Compartilhamento exige equivalência semântica |  |  |  |
| 27 | Camadas |  |  |  |
| 28 | Organização obrigatória |  |  |  |
| 29 | Modelo abstrato | Descritiva | — | — |
| 30 | Profundidade |  |  |  |
| 31 | Largura |  |  |  |
| 32 | Diretórios genéricos |  |  |  |
| 33 | Promoção progressiva |  |  |  |
| 34 | Funções, métodos e componentes |  |  |  |
| 35 | Arquivos |  |  |  |
| 36 | Diretórios |  |  |  |
| 37 | Módulos e domínios |  |  |  |
| 38 | Ordem interna de arquivos |  |  |  |
| 39 | Duplicação |  |  |  |
| 40 | Nomenclatura semântica |  |  |  |
| 41 | Convenções tecnológicas |  |  |  |
| 42 | Tipagem |  |  |  |
| 42.1 | Coerência semântica de validações |  |  |  |
| 43 | Contratos |  |  |  |
| 44 | Semântica e contratos nativos da plataforma |  |  |  |
| 45 | Comentários e documentação |  |  |  |
| 46 | Dependências |  |  |  |
| 47 | Imports |  |  |  |
| 48 | Configuração |  |  |  |
| 49 | Erros |  |  |  |
| 49.1 | Semântica do erro e estado da operação |  |  |  |
| 49.2 | Cancelamento, reversão e compensação |  |  |  |
| 50 | Segurança |  |  |  |
| 50.1 | Autoridade de autorização |  |  |  |
| 51 | Observabilidade |  |  |  |
| 52 | Integridade e persistência |  |  |  |
| 53 | Integrações externas |  |  |  |
| 54 | Organização do front-end |  |  |  |
| 55 | Normalização global de estilos |  |  |  |
| 56 | Responsabilidades estruturais e visuais |  |  |  |
| 57 | Componentes |  |  |  |
| 58 | Páginas e telas |  |  |  |
| 59 | Fonte canônica de estados semânticos |  |  |  |
| 60 | Condições no nível responsável |  |  |  |
| 61 | Contratos de variantes |  |  |  |
| 62 | Estado local e compartilhado |  |  |  |
| 63 | Engines e templates |  |  |  |
| 64 | Assets |  |  |  |
| 65 | Organização do back-end |  |  |  |
| 66 | Domínio antes da categoria técnica |  |  |  |
| 67 | Camadas proporcionais |  |  |  |
| 68 | Grafo comportamental e casos de uso |  |  |  |
| 68.1 | Modelo comportamental |  |  |  |
| 68.2 | Estados semanticamente distintos |  |  |  |
| 68.3 | Estados de encerramento |  |  |  |
| 68.4 | Completude do grafo comportamental |  |  |  |
| 68.5 | Conformidade entre modelo e implementação |  |  |  |
| 68.6 | Completude e cobertura |  |  |  |
| 68.7 | Transições isoladas e sequências comportamentais |  |  |  |
| 68.8 | Rastreabilidade entre modelo e validação |  |  |  |
| 68.9 | Operações assíncronas, concorrência e respostas obsoletas |  |  |  |
| 68.10 | Execução única da intenção de domínio |  |  |  |
| 68.11 | Sensibilidade das evidências e testes de mutação |  |  |  |
| 69 | Níveis de teste |  |  |  |
| 70 | Comportamento e permanência |  |  |  |
| 71 | Automação e evidências |  |  |  |
| 71.1 | Eficiência da execução das evidências |  |  |  |
| 72 | Branches |  |  |  |
| 73 | Commit de conclusão |  |  |  |
| 74 | Promoção |  |  |  |
| 75 | Declaração de conformidade |  |  |  |
| 76 | Auditoria integral de conformidade |  |  |  |
| 77 | Artefatos temporários |  |  |  |
| 78 | Baseline obrigatória |  |  |  |
| 79 | Planejamento antes da migração |  |  |  |
| 80 | Ordem da refatoração |  |  |  |
| 81 | Preservação de contratos observáveis |  |  |  |
| 82 | Migração e poda |  |  |  |
| 83 | Regra de parada |  |  |  |

## `regrasUxUi.md`

| Regra | Título | Status | Evidência | Justificativa |
|---|---|---|---|---|
| 1 | Objetivo | Descritiva | — | — |
| 2 | Natureza normativa e mutabilidade |  |  |  |
| 3 | Relação entre os documentos |  |  |  |
| 4 | Aplicação independente e cumulativa |  |  |  |
| 5 | Precedência e conflitos |  |  |  |
| 6 | Não conformidades e exceções |  |  |  |
| 7 | Clareza |  |  |  |
| 8 | Simplicidade |  |  |  |
| 9 | Consistência |  |  |  |
| 10 | Previsibilidade |  |  |  |
| 11 | Eficiência |  |  |  |
| 12 | Reconhecimento antes de memorização |  |  |  |
| 13 | Tolerância a erros |  |  |  |
| 14 | Controle do usuário |  |  |  |
| 15 | Proporcionalidade |  |  |  |
| 16 | Inclusão |  |  |  |
| 17 | Organização semântica |  |  |  |
| 18 | Hierarquia informacional |  |  |  |
| 19 | Menor estrutura informacional suficiente |  |  |  |
| 20 | Agrupamento perceptível |  |  |  |
| 21 | Nomenclatura |  |  |  |
| 22 | Localização previsível |  |  |  |
| 23 | Divulgação progressiva |  |  |  |
| 24 | Ordem do conteúdo |  |  |  |
| 25 | Densidade informacional |  |  |  |
| 26 | Densidade conforme a natureza do conteúdo |  |  |  |
| 27 | Ordem de compactação |  |  |  |
| 28 | Informação redundante |  |  |  |
| 29 | Informação essencial |  |  |  |
| 30 | Menor estrutura visual suficiente |  |  |  |
| 31 | Função dos contêineres visuais |  |  |  |
| 32 | Prioridade visual |  |  |  |
| 33 | Tipografia |  |  |  |
| 34 | Espaçamento |  |  |  |
| 35 | Alinhamento |  |  |  |
| 36 | Cor e contraste |  |  |  |
| 37 | Ícones |  |  |  |
| 38 | Ruído visual |  |  |  |
| 39 | Identidade visual |  |  |  |
| 40 | Responsabilidade do componente |  |  |  |
| 41 | Reutilização semântica |  |  |  |
| 42 | Variantes |  |  |  |
| 43 | Estados obrigatórios |  |  |  |
| 43.1 | Estados e transições de interface |  |  |  |
| 43.2 | Consistência semântica do estado |  |  |  |
| 44 | Elementos nativos |  |  |  |
| 45 | Área de interação |  |  |  |
| 46 | Indicação de interação |  |  |  |
| 47 | Design system |  |  |  |
| 48 | Localização atual |  |  |  |
| 49 | Estrutura de navegação |  |  |  |
| 50 | Profundidade |  |  |  |
| 51 | Continuidade |  |  |  |
| 52 | Retorno e cancelamento |  |  |  |
| 53 | Links e botões |  |  |  |
| 54 | Fluxos com etapas |  |  |  |
| 55 | Feedback imediato |  |  |  |
| 56 | Correspondência entre ação e resposta |  |  |  |
| 57 | Operações demoradas |  |  |  |
| 58 | Ações duplicadas |  |  |  |
| 58.1 | Acionamentos equivalentes e intenção única |  |  |  |
| 59 | Confirmações e desfazer |  |  |  |
| 59.1 | Cancelamento, desfazer e reversibilidade |  |  |  |
| 60 | Animações |  |  |  |
| 61 | Processos automáticos |  |  |  |
| 62 | Cobertura de estados |  |  |  |
| 63 | Estado inicial |  |  |  |
| 64 | Carregamento |  |  |  |
| 65 | Estado vazio |  |  |  |
| 66 | Estado de erro |  |  |  |
| 67 | Estado parcial |  |  |  |
| 68 | Estado desabilitado |  |  |  |
| 68.1 | Permissões e disponibilidade de ações |  |  |  |
| 69 | Estado de sucesso |  |  |  |
| 70 | Estado offline ou degradado |  |  |  |
| 71 | Necessidade dos campos |  |  |  |
| 72 | Rótulos |  |  |  |
| 73 | Formato esperado |  |  |  |
| 74 | Tipo de controle |  |  |  |
| 75 | Ordem de preenchimento |  |  |  |
| 76 | Obrigatoriedade |  |  |  |
| 77 | Validação |  |  |  |
| 78 | Mensagens de erro |  |  |  |
| 79 | Preservação de dados |  |  |  |
| 80 | Ações do formulário |  |  |  |
| 81 | Formulários extensos |  |  |  |
| 82 | Prevenção |  |  |  |
| 83 | Valores padrão |  |  |  |
| 84 | Ações destrutivas |  |  |  |
| 85 | Recuperação |  |  |  |
| 86 | Erros locais e globais |  |  |  |
| 87 | Mensagens técnicas |  |  |  |
| 88 | Princípio geral |  |  |  |
| 89 | Estrutura semântica |  |  |  |
| 90 | Teclado |  |  |  |
| 91 | Foco |  |  |  |
| 92 | Tecnologias assistivas |  |  |  |
| 93 | Contraste e cor |  |  |  |
| 94 | Texto alternativo e mídia |  |  |  |
| 95 | Movimento e tempo |  |  |  |
| 96 | Ampliação e redimensionamento |  |  |  |
| 97 | Contexto responsável pela adaptação |  |  |  |
| 98 | Conteúdo antes do dispositivo |  |  |  |
| 99 | Breakpoints justificados |  |  |  |
| 100 | Adaptação contínua e discreta |  |  |  |
| 101 | Fluxo responsivo |  |  |  |
| 102 | Prioridade de conteúdo |  |  |  |
| 103 | Toque e ponteiro |  |  |  |
| 104 | Teclados móveis |  |  |  |
| 105 | Tabelas e dados densos |  |  |  |
| 106 | Orientação e métodos de entrada |  |  |  |
| 107 | Linguagem direta |  |  |  |
| 108 | Vocabulário do usuário |  |  |  |
| 109 | Consistência terminológica |  |  |  |
| 110 | Rótulos de ação |  |  |  |
| 111 | Mensagens de estado |  |  |  |
| 112 | Tom |  |  |  |
| 113 | Datas, números e unidades |  |  |  |
| 114 | Internacionalização |  |  |  |
| 115 | Resposta à interação |  |  |  |
| 116 | Carregamento progressivo |  |  |  |
| 116.1 | Caminho crítico e independência técnica |  |  |  |
| 117 | Estabilidade visual |  |  |  |
| 118 | Atualizações otimistas |  |  |  |
| 119 | Indicadores proporcionais |  |  |  |
| 119.1 | Medição do desempenho percebido |  |  |  |
| 120 | Validação funcional |  |  |  |
| 120.1 | Reentrada e sequências de fluxos temporários |  |  |  |
| 120.2 | Operações assíncronas e recuperação observável |  |  |  |
| 120.3 | Sensibilidade das evidências de interface |  |  |  |
| 121 | Inspeção heurística |  |  |  |
| 122 | Testes com usuários |  |  |  |
| 123 | Critérios de sucesso |  |  |  |
| 124 | Testes de acessibilidade |  |  |  |
| 125 | Dispositivos e contextos |  |  |  |
| 125.1 | Alternância entre métodos de entrada |  |  |  |
| 126 | Regressão visual e comportamental |  |  |  |
| 127 | Registro de problemas |  |  |  |
| 128 | Níveis de validação |  |  |  |
| 129 | Validação de densidade e responsividade |  |  |  |
| 130 | Critério de conclusão |  |  |  |
| 131 | Conformidade da alteração |  |  |  |

## `regrasProjeto.md`

| Regra | Título | Status | Evidência | Justificativa |
|---|---|---|---|---|
| 1 | Objetivo | Descritiva | — | — |
| 2 | Natureza normativa e mutabilidade |  |  |  |
| 3 | Relação com os demais documentos |  |  |  |
| 4 | Regras de preenchimento |  |  |  |
| 4.1 | Árvores e hierarquias |  |  |  |
| 5 | Identificação do projeto |  |  |  |
| 6 | Adoção das regras universais |  |  |  |
| 7 | Exceções autorizadas pelas regras universais |  |  |  |
| 8 | Conflitos normativos resolvidos |  |  |  |
| 9 | Objetivo |  |  |  |
| 10 | Escopo funcional |  |  |  |
| 11 | Requisitos do sistema |  |  |  |
| 11.1 | Desempenho e capacidade |  |  |  |
| 12 | Restrições e premissas |  |  |  |
| 13 | Natureza do sistema |  |  |  |
| 14 | Linguagens e plataformas |  |  |  |
| 15 | Front-end |  |  |  |
| 16 | Back-end |  |  |  |
| 17 | Persistência |  |  |  |
| 18 | Ferramentas de desenvolvimento |  |  |  |
| 19 | Arquitetura adotada |  |  |  |
| 20 | Módulos e fronteiras |  |  |  |
| 21 | Fluxos técnicos |  |  |  |
| 22 | Estrutura de diretórios |  |  |  |
| 23 | Responsabilidade dos diretórios |  |  |  |
| 24 | Organização interna dos módulos |  |  |  |
| 25 | Imports, exports e aliases |  |  |  |
| 26 | Nomenclatura |  |  |  |
| 27 | Componentes, funções e arquivos |  |  |  |
| 28 | Abstrações e compartilhamento |  |  |  |
| 29 | Tipos e contratos |  |  |  |
| 30 | Estado |  |  |  |
| 31 | Erros e observabilidade |  |  |  |
| 32 | Contexto de uso |  |  |  |
| 33 | Arquitetura da informação |  |  |  |
| 34 | Densidade |  |  |  |
| 35 | Responsividade |  |  |  |
| 36 | Sistema visual |  |  |  |
| 37 | Componentes visuais |  |  |  |
| 38 | Interação, formulários e conteúdo |  |  |  |
| 39 | Acessibilidade |  |  |  |
| 40 | Validação de UX e UI |  |  |  |
| 41 | Transporte e API |  |  |  |
| 42 | Aplicação e domínio |  |  |  |
| 43 | Persistência |  |  |  |
| 44 | Integrações externas |  |  |  |
| 45 | Autenticação e autorização |  |  |  |
| 46 | Segurança e privacidade |  |  |  |
| 47 | Processamentos especializados |  |  |  |
| 48 | Configuração e ambientes |  |  |  |
| 49 | Grafo comportamental e testes |  |  |  |
| 50 | Comandos de validação |  |  |  |
| 51 | Versionamento e integração |  |  |  |
| 52 | Build e implantação |  |  |  |
| 53 | Restrições obrigatórias |  |  |  |
| 54 | Baseline de comportamento |  |  |  |
| 55 | Planejamento estrutural |  |  |  |
| 56 | Decisões pendentes |  |  |  |
| 57 | Débitos técnicos |  |  |  |

## Conclusão

Total de linhas: 307

Conforme:

Exceção autorizada:

N/A:

Descritiva: 4

Não conforme:

A conclusão permanece válida enquanto os documentos adotados, a matriz e as validações referenciadas no catálogo permanecerem aprovados no estado auditado.
