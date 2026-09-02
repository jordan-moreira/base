# Regras do Projeto

## 1. Objetivo

Este documento define as decisões, restrições, convenções e concretizações próprias deste projeto.

Ele responde à pergunta:

```text
Como este projeto deve ser estruturado, implementado, validado e mantido?
```

As instruções de uso, execução, navegação, contexto e retomada pertencem ao `README.md`.

As normas universais de engenharia e arquitetura pertencem ao `regrasDev.md`.

As normas universais de experiência e interface pertencem ao `regrasUxUi.md`.

---

## 2. Natureza normativa e mutabilidade

Este documento é:

- normativo;
- específico;
- plástico.

É normativo porque define o estado válido esperado para este projeto.

É específico porque contém apenas decisões que dependem do contexto, da stack, do domínio, da infraestrutura, dos requisitos e dos limites deste projeto.

É plástico porque deve ser atualizado sempre que mudar uma decisão válida do projeto.

Este documento deve acompanhar mudanças em:

- objetivo;
- escopo;
- arquitetura;
- stack;
- estrutura de diretórios;
- contratos;
- integrações;
- compatibilidade;
- valores;
- estratégias;
- restrições;
- critérios de validação;
- exceções autorizadas;
- não conformidades.

Este documento não pode:

- modificar `regrasDev.md` ou `regrasUxUi.md`;
- dispensar regra universal;
- reduzir critério mínimo universal;
- repetir norma universal como se fosse decisão local;
- transformar uma violação em exceção válida sem autorização explícita da própria norma universal;
- documentar como válida uma implementação acidental apenas porque ela existe no código.

---

## 3. Relação com os demais documentos

```text
regrasDev.md + regrasUxUi.md
            ↓
       regrasProjeto.md
            ↓
         código-fonte
            ↓
          README.md
```

- As regras universais definem critérios e resultados obrigatórios.
- Este documento concretiza esses critérios para o projeto.
- O código implementa as decisões concretas.
- O `README.md` descreve o estado implementado.

Em caso de divergência entre este documento e o código, não presumir automaticamente que um dos dois está correto.

Deve-se verificar:

- se o código ainda não implementou uma decisão válida;
- se a decisão ficou obsoleta;
- se houve alteração deliberada não documentada;
- se existe defeito em ambos.

Após a análise:

- se a decisão continuar válida, corrigir o código;
- se o estado implementado for o novo estado válido, atualizar este documento;
- se nenhum estiver adequado, corrigir ambos.

---

## 4. Regras de preenchimento

- Preencher do geral para o específico.
- Cada campo deve representar uma decisão principal.
- Cada decisão deve existir em apenas uma seção.
- Campos aplicáveis não devem permanecer vazios.
- Usar `Pendente.` quando a decisão ainda não tiver sido tomada.
- Usar `Não se aplica.` quando o campo não pertencer à natureza ou ao escopo do projeto.
- `Não se aplica.` exige justificativa verificável.
- Campos pendentes bloqueiam somente os ramos que dependem deles.
- Exemplos devem ser removidos após preenchimento definitivo.
- Justificativas históricas e contexto de decisões pertencem ao `README.md` ou a registro específico de decisão.
- Novas seções somente devem existir quando representarem decisão independente não acomodável nas seções existentes.
- Regras devem ser objetivas, afirmativas e verificáveis.
- Proibições devem impedir violações concretas, não preferências pessoais.

### 4.1 Árvores e hierarquias

Diretórios terminam com `/`.

Arquivos não terminam com `/`.

Cada sequência adicional de `--` representa um nível inferior.

Exemplo:

```text
src/
--app/
----router/
------router.ts
--features/
----featureName/
------index.ts
```

---

# Parte I — Governança documental

## 5. Identificação do projeto

Nome:

Descrição curta:

Tipo de projeto:

Responsável principal:

Repositório principal:

Branch estável:

Branch de integração:

Estado atual:

Versão atual:

## 6. Revisões universais adotadas

Revisão de `regrasDev.md`:

Revisão de `regrasUxUi.md`:

Aplicabilidade de `regrasUxUi.md`:

Data da última sincronização:

Método utilizado para confirmar integridade das cópias locais:

## 7. Não conformidades conhecidas

Para cada não conformidade, registrar:

Regra afetada:

Causa:

Escopo:

Impacto:

Risco:

Responsável:

Medida compensatória:

Tratamento planejado:

Prazo ou condição para correção:

Estado:

Quando não existirem:

```text
Não se aplica.
```

## 8. Exceções autorizadas pelas regras universais

Para cada exceção autorizada, registrar:

Regra que autoriza a exceção:

Motivo:

Escopo mínimo:

Impacto:

Risco:

Medida compensatória:

Responsável:

Prazo ou condição de reavaliação:

Critério de encerramento:

Quando não existirem:

```text
Não se aplica.
```

---

# Parte II — Definição do produto

## 9. Objetivo

Problema principal resolvido:

Resultado principal entregue:

Público ou consumidores:

Critério principal de sucesso:

Objetivo de longo prazo:

## 10. Escopo funcional

Funcionalidades incluídas:

Funcionalidades excluídas:

Limites de responsabilidade do sistema:

Entidades e conceitos centrais:

Casos de uso principais:

Casos de uso alternativos:

Casos de uso de erro e recuperação:

## 11. Requisitos do sistema

Plataformas suportadas:

Modo de funcionamento:

Funcionamento offline:

Usuários simultâneos:

Autenticação:

Autorização:

Persistência:

Comunicação em tempo real:

Serviços externos:

Importação de arquivos:

Geração de arquivos:

Processamento assíncrono:

Responsividade:

Acessibilidade:

Internacionalização:

Volume esperado de dados:

Desempenho relevante:

Compatibilidade relevante:

### 11.1 Desempenho e capacidade

Escopos com requisitos concretos de desempenho:

Volume de dados por operação:

Volume total esperado:

Carga simultânea esperada:

Metas de latência:

Metas de resposta percebida, quando aplicáveis:

Throughput esperado:

Limites de memória:

Limites de CPU:

Limites de armazenamento:

Limites de entrada e saída:

Limites de rede:

Limites de serviços externos:

Recursos computacionais disponíveis:

Caminhos críticos de desempenho:

Conteúdos, regiões ou resultados prioritários, quando aplicáveis:

Trabalhos secundários que podem permanecer fora do caminho crítico:

Estratégia de concorrência ou paralelismo:

Limites de concorrência:

Otimizações relevantes e respectivas justificativas:

## 12. Restrições e premissas

Tecnologias obrigatórias:

Tecnologias proibidas:

Ambientes suportados:

Limites de infraestrutura:

Compatibilidades preservadas:

Comportamentos que não podem mudar:

Contratos que não podem mudar:

Restrições acadêmicas, comerciais, legais ou organizacionais:

Premissas adotadas:

---

# Parte III — Natureza técnica e stack

## 13. Natureza do sistema

Modelo principal da aplicação:

Componentes técnicos existentes:

Modelo de execução:

Modelo de implantação:

Pontos de entrada:

Interfaces públicas:

## 14. Linguagens e plataformas

Linguagem principal:

Versão mínima:

Linguagens auxiliares:

Runtime principal:

Versão mínima do runtime:

Plataforma principal:

Sistemas operacionais de desenvolvimento:

Sistemas operacionais de produção:

## 15. Front-end

Aplicabilidade:

Framework ou biblioteca:

Ferramenta de build:

Roteamento:

Estado local ou global:

Estado remoto:

Formulários:

Validação:

Estratégia de estilos:

Biblioteca visual:

Design system:

## 16. Back-end

Aplicabilidade:

Framework:

Servidor ou adaptador HTTP:

Validação:

Autenticação:

Documentação da API:

Processamento assíncrono:

## 17. Persistência

Aplicabilidade:

Banco de dados:

ORM, query builder ou driver:

Migrações:

Cache:

Armazenamento de arquivos:

Estratégia de backup:

## 18. Ferramentas de desenvolvimento

Gerenciador de pacotes:

Lint:

Formatação:

Tipagem:

Testes unitários:

Testes de integração:

Testes de interface:

Testes de ponta a ponta:

Containerização:

Integração contínua:

---

# Parte IV — Arquitetura e árvore

## 19. Arquitetura adotada

Modelo arquitetural:

Estratégia predominante de organização:

Camadas ou áreas existentes:

Responsabilidade de cada camada ou área:

Direção obrigatória das dependências:

Dependências proibidas:

Critério para criar nova camada ou área:

## 20. Módulos e fronteiras

Módulos principais:

Responsabilidade de cada módulo:

Dados pertencentes a cada módulo:

Interface pública de cada módulo:

Dependências permitidas:

Dependências proibidas:

Critério para criar novo módulo:

## 21. Fluxos técnicos

Fluxo de inicialização:

Fluxo principal de leitura:

Fluxo principal de escrita:

Fluxo de autenticação:

Fluxo de geração de arquivos:

Fluxo de integração externa:

Fluxo de tratamento de falhas:

## 22. Estrutura de diretórios

Diretório raiz do código-fonte:

Árvore final:

```text
Pendente.
```

Diretórios obrigatórios:

Diretórios opcionais:

Diretórios proibidos:

Critério para criar diretório:

Critério para remover diretório:

## 23. Responsabilidade dos diretórios

Para cada diretório principal, registrar:

Caminho:

Responsabilidade:

Conteúdo permitido:

Conteúdo proibido:

Consumidores:

Dependências permitidas:

## 24. Organização interna dos módulos

Estrutura padrão, quando existir:

Subdiretórios obrigatórios:

Subdiretórios opcionais:

Critério para criar subdiretório:

Critério para dividir arquivo:

Critério para promover código a compartilhado:

Interface pública padrão:

## 25. Imports, exports e aliases

Aliases disponíveis:

Direção permitida dos imports:

Imports proibidos:

Política para imports relativos:

Política para reexports:

Política para dependências circulares:

Política para interfaces públicas:

---

# Parte V — Convenções de implementação

## 26. Nomenclatura

Padrão de nomes de arquivos:

Padrão de nomes de diretórios:

Vocabulário do domínio:

Abreviações permitidas:

Nomes proibidos ou reservados:

## 27. Componentes, funções e arquivos

Padrão de componentes:

Critério para dividir componente:

Padrão de funções:

Critério para extrair função:

Padrão de arquivos:

Critério para criar arquivo:

Critério para manter conteúdo no mesmo arquivo:

## 28. Abstrações e compartilhamento

Critério concreto para criar abstração:

Critério para reutilizar código:

Critério para duplicação temporária:

Critério para código compartilhado:

Critério para remover abstração:

Critério para retornar código compartilhado ao contexto específico:

## 29. Tipos e contratos

Padrão de tipos locais:

Padrão de contratos públicos:

Localização dos contratos:

Política para dados externos:

Política para estados inválidos:

Local da validação autoritativa por regra ou domínio:

Validações antecipadas ou derivadas relevantes:

Política de coerência semântica das validações entre fronteiras:

Política de compatibilidade:

## 30. Estado

Estados semânticos relevantes:

Critério para estado local:

Critério para estado de módulo ou feature:

Critério para estado global:

Critério para estado remoto:

Fonte canônica de cada estado semântico relevante:

Escopo e ciclo de vida dos estados relevantes:

Política para estados derivados:

Política de sincronização entre representações do mesmo estado:

Estratégia de persistência:

Diretório das stores:

Critério para criar store:

Conteúdo proibido nas stores:

## 31. Erros e observabilidade

Modelo interno de erros:

Categorias de erro:

Estado da operação após cada categoria de falha relevante:

Política de repetição segura:

Estratégias de recuperação por categoria de erro:

Tratamento de falhas secundárias após efeito principal concluído:

Tratamento de resultados indeterminados:

Fronteira de conversão:

Formato externo:

Biblioteca de logs:

Formato dos logs:

Campos obrigatórios:

Dados proibidos:

Correlação:

Métricas:

---

# Parte VI — Concretização de UX e UI

## 32. Aplicabilidade e contexto

Aplicabilidade de `regrasUxUi.md`:

Público principal:

Frequência de uso:

Contextos operacionais:

Dispositivos suportados:

Métodos de entrada suportados:

Tecnologias assistivas consideradas:

## 33. Arquitetura da informação

Estrutura principal de navegação:

Vocabulário adotado:

Conteúdo essencial por contexto:

Conteúdo secundário por contexto:

Estratégia de divulgação progressiva:

Critério para criar página, etapa, seção ou grupo:

## 34. Densidade

Densidades adotadas:

Exemplo de preenchimento:

```text
- compacta em tabelas e painéis operacionais;
- normal em formulários;
- ampliada em onboarding e avisos críticos.
```

Critério para escolher densidade:

Áreas em que compactação é permitida:

Áreas em que compactação é restrita:

Dimensões mínimas de interação:

## 35. Responsividade

Estratégia global:

Estratégia local:

Mecanismo para condições de viewport:

Mecanismo para condições do contêiner:

Mecanismo para preferências do usuário:

Comportamentos fluidos adotados:

Breakpoints ou limiares:

Para cada breakpoint, registrar:

Valor:

Mudança observável que o justifica:

Componentes ou fluxos afetados:

## 36. Sistema visual

Identidade visual:

Paleta:

Tipografia:

Escala de espaçamento:

Tokens:

Bordas, raios e sombras:

Critério para uso de contêineres:

Critério para ação principal, secundária e destrutiva:

Política de disponibilidade de ações conforme permissões conhecidas:

Política para ações canceláveis, reversíveis ou compensáveis:

Comunicação de limitações de reversibilidade:

## 37. Componentes visuais

Biblioteca ou design system:

Critério para componente compartilhado:

Variantes permitidas:

Estados obrigatórios:

Política para elementos nativos:

Política de foco:

Política de ícones:

## 38. Formulários e conteúdo

Padrão de rótulos:

Padrão de obrigatoriedade:

Momento da validação:

Padrão de mensagens de erro:

Padrão de ações:

Padrão de datas, números e unidades:

Tom de voz:

Internacionalização:

## 39. Acessibilidade

Padrão ou nível exigido:

Critérios de contraste:

Ampliação suportada:

Navegação por teclado:

Leitores de tela:

Redução de movimento:

Alternativas de mídia:

Exceções autorizadas:

## 40. Condições limite de validação

Largura mínima:

Largura máxima relevante:

Ampliação máxima exigida:

Conteúdo mínimo:

Conteúdo máximo:

Textos extensos:

Idiomas ou traduções:

Estados vazios:

Estados de erro:

Estados selecionados:

Orientações:

Toque:

Teclado:

Mudanças dinâmicas de conteúdo:

Nível de validação UX/UI exigido:

---

# Parte VII — Back-end, persistência e integrações

## 41. Transporte e API

Aplicabilidade:

Diretório das rotas:

Responsabilidade das rotas:

Diretório dos handlers:

Responsabilidade dos handlers:

Formato de sucesso:

Formato de erro:

Versionamento:

Paginação:

Filtros e ordenação:

## 42. Aplicação e domínio

Diretório dos casos de uso:

Responsabilidade dos casos de uso:

Serviços de aplicação:

Limite transacional:

Idempotência:

Concorrência:

Dependências de ordem:

Tratamento de operações assíncronas ou sobrepostas:

Tratamento de resultados obsoletos:

Operações canceláveis e semântica de cancelamento:

Operações reversíveis:

Operações compensáveis e estratégia de compensação:

Efeitos irrevogáveis ou parcialmente reversíveis:

Diretório do domínio:

Entidades:

Objetos de valor:

Invariantes:

Dependências permitidas no domínio:

Dependências proibidas no domínio:

## 43. Persistência

Responsabilidade:

Diretório dos modelos ou schemas:

Diretório das migrações:

Diretório das seeds:

Acessos diretos permitidos:

Acessos diretos proibidos:

Integridade dos dados:

Estratégia de migração:

Backup:

Dados de teste:

## 44. Integrações externas

Para cada integração, registrar:

Nome:

Finalidade:

Módulo responsável:

Cliente ou adaptador:

Diretório:

Contrato interno:

Autenticação:

Timeout:

Repetição:

Backoff:

Fallback:

Tratamento de erros:

Limites de uso:

## 45. Autenticação e autorização

Aplicabilidade:

Modelo de autenticação:

Modelo de autorização:

Papéis:

Permissões:

Local da autenticação:

Local da autorização:

Política de atualização ou invalidação de permissões:

Sessão ou token:

Expiração:

Revogação:

Rotas protegidas:

## 46. Processamentos especializados

Para cada processamento, registrar:

Nome:

Responsabilidade:

Módulo responsável:

Entrada:

Saída:

Contrato:

Dependências permitidas:

Dependências proibidas:

Restrições:

Comportamentos preservados:

---

# Parte VIII — Configuração, testes e entrega

## 47. Configuração e ambientes

Ambientes:

Diretório de configuração:

Variáveis obrigatórias:

Variáveis opcionais:

Valores padrão:

Validação da configuração:

Arquivo de exemplo:

Dados proibidos no repositório:

Diferenças entre ambientes:

## 48. Grafo comportamental e testes

Local do grafo de casos de uso:

Local do grafo comportamental:

Escopo do grafo comportamental:

Local do catálogo de estados e transições:

Estados semanticamente relevantes catalogados:

Transições catalogadas:

Estados de encerramento relevantes:

Evidência de completude do grafo:

Local da rastreabilidade entre modelo e validação:

Forma de identificação de estados, transições e sequências nas evidências:

Estratégia geral de testes:

Critérios adicionais de cobertura específicos do projeto:

Critério para declarar cobertura comportamental completa:

Transições validadas isoladamente:

Sequências comportamentais sujeitas a dependência ou interferência:

Cenários de reentrada relevantes:

Cenários de alternância entre métodos de entrada:

Cenários assíncronos e concorrentes relevantes:

Cenários de respostas obsoletas:

Cenários de execução única da intenção de domínio:

Casos de uso cobertos por testes unitários:

Conexões cobertas por integração:

Fluxos cobertos por ponta a ponta:

Fluxos principais:

Fluxos alternativos:

Fluxos de erro:

Limites e transições:

Localização dos testes unitários:

Localização dos testes de integração:

Localização dos testes ponta a ponta:

Estratégia de mocks:

Banco de testes:

Fixtures e factories:

Cobertura quantitativa mínima adicional, quando aplicável:

Política de permanência:

Critério para remover teste temporário:

Omissões justificadas de categoria de teste:

## 49. Comandos de validação

Desenvolvimento:

Build:

Lint:

Tipagem:

Testes unitários:

Testes de integração:

Testes ponta a ponta:

Formatação:

Validação UX/UI:

## 50. Versionamento e integração

Branch estável:

Branch de integração:

Branches de trabalho:

Alterações diretas na branch estável:

Estratégia de integração:

Atualização forçada:

Critérios para promoção:

Relatórios permanentes:

Destino de evidências temporárias:

Política para scripts e workflows temporários:

## 51. Build e implantação

Artefato de build:

Empacotamento:

Implantação:

Rollback:

Critério técnico de conclusão:

---

# Parte IX — Controle arquitetural

## 52. Restrições obrigatórias

Arquivos ou módulos que não podem ser removidos:

Tecnologias que exigem decisão explícita para substituição:

Comportamentos protegidos:

Contratos protegidos:

Acessos diretos proibidos:

Duplicações arquiteturais proibidas:

## 53. Baseline de comportamento

Revisão usada como baseline:

Casos de uso executados:

Contratos registrados:

Formatos registrados:

Resultados observáveis registrados:

Evidências:

## 54. Planejamento estrutural

Árvore final aprovada:

Módulos finais:

Arquivos finais:

Estratégia de migração:

Estratégia de poda:

Critérios de revalidação dos ramos:

## 55. Decisões pendentes

Para cada decisão:

Descrição:

Motivo:

Impacto:

Opções consideradas:

Regra temporária:

Ramos bloqueados:

Seções afetadas:

## 56. Débitos técnicos

Para cada débito:

Descrição:

Causa:

Impacto:

Risco:

Escopo:

Tratamento planejado:

Prioridade:

---

# Checklist de conformidade

## Documentos

- [ ] A revisão de `regrasDev.md` está identificada.
- [ ] A revisão de `regrasUxUi.md` está identificada quando aplicável.
- [ ] As cópias locais correspondem às versões canônicas.
- [ ] Este documento contém somente concretizações específicas.
- [ ] O `README.md` descreve o estado implementado.

## Escopo e arquitetura

- [ ] Objetivo, escopo e restrições estão definidos.
- [ ] A arquitetura emerge das responsabilidades reais.
- [ ] A árvore final está registrada.
- [ ] Fronteiras e dependências são explícitas.
- [ ] Não existem árvores concorrentes.

## Implementação

- [ ] Nomenclatura e contratos específicos estão definidos.
- [ ] A validação autoritativa e suas validações antecipadas ou derivadas permanecem semanticamente coerentes.
- [ ] Estados semânticos relevantes e suas fontes canônicas estão identificados.
- [ ] Ciclos de vida e sincronização de estados relevantes estão concretizados.
- [ ] Critérios de abstração e compartilhamento estão concretizados.
- [ ] Comportamentos e contratos protegidos estão registrados.
- [ ] Estados de operação, repetição segura e recuperação de erros relevantes estão concretizados.
- [ ] Concorrência, ordenação e tratamento de resultados obsoletos estão concretizados quando aplicáveis.
- [ ] Cancelamento, reversão, compensação e efeitos irrevogáveis estão concretizados quando aplicáveis.

## Desempenho

- [ ] Escopos com requisitos de desempenho possuem metas ou limites concretos quando aplicáveis.
- [ ] Volume, latência, throughput, concorrência e recursos disponíveis estão definidos quando relevantes.
- [ ] Metas de resposta percebida e prioridades observáveis estão definidas quando aplicáveis.
- [ ] Limites de memória, CPU, armazenamento, entrada e saída, rede e serviços externos estão registrados quando relevantes.
- [ ] Caminhos críticos e trabalhos secundários independentes estão identificados quando relevantes.
- [ ] Estratégia e limites de concorrência ou paralelismo estão concretizados quando aplicáveis.
- [ ] Otimizações que adicionam complexidade relevante possuem justificativa registrada.

## UX e UI

- [ ] A aplicabilidade de `regrasUxUi.md` está declarada.
- [ ] Densidades por contexto estão definidas.
- [ ] Estratégias global e local de responsividade estão definidas.
- [ ] Breakpoints possuem justificativas observáveis.
- [ ] Conteúdo essencial e secundário está classificado.
- [ ] Disponibilidade de ações conforme permissões conhecidas está concretizada quando aplicável.
- [ ] Cancelamento, reversibilidade e suas limitações possuem política observável compatível com as garantias técnicas.
- [ ] Condições limite de validação estão registradas.
- [ ] Nível de acessibilidade e validação está definido.

## Testes

- [ ] O grafo de casos de uso está localizado.
- [ ] O grafo comportamental e seu escopo estão localizados.
- [ ] Estados e transições relevantes estão catalogados.
- [ ] A evidência de completude do grafo está registrada.
- [ ] A rastreabilidade entre modelo e evidências está definida.
- [ ] O critério para declarar cobertura comportamental completa está definido.
- [ ] Transições isoladas e sequências sujeitas a interferência estão identificadas.
- [ ] Cenários assíncronos, concorrentes, de respostas obsoletas e de execução única estão registrados quando aplicáveis.
- [ ] Critérios adicionais de cobertura específicos do projeto estão definidos quando existirem.
- [ ] Cobertura quantitativa, quando adotada, está registrada como critério adicional e não como substituta da cobertura comportamental.
- [ ] Fluxos principais, alternativos, erros e limites estão cobertos.
- [ ] Unitários, integração e ponta a ponta são usados conforme necessidade.
- [ ] Omissões de níveis de teste estão justificadas.
- [ ] Testes permanentes permanecem versionados.

## Entrega

- [ ] Comandos de validação estão registrados.
- [ ] Estratégia de branches está definida.
- [ ] Critérios para promoção estão definidos.
- [ ] Artefatos temporários possuem política de remoção.
- [ ] Critério técnico de conclusão está definido.

## Conformidade

- [ ] Não conformidades estão registradas separadamente de exceções.
- [ ] Exceções possuem autorização universal explícita.
- [ ] Decisões pendentes bloqueiam somente ramos dependentes.
- [ ] Nenhuma implementação acidental foi transformada em regra local.
