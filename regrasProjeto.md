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
- exceções autorizadas.

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
- Quando um mesmo conceito possuir consequências em seções diferentes, somente a seção responsável pela decisão deve defini-la; as demais devem registrar apenas consequências específicas, referências ou evidências do próprio escopo.
- Campos com nomes semelhantes em seções diferentes não autorizam repetir a mesma decisão; o significado deve ser delimitado pela responsabilidade declarada da seção e pelo rótulo do campo.
- Campos aplicáveis não devem permanecer vazios.
- Usar `Pendente.` quando a decisão ainda não tiver sido tomada.
- Usar `Não se aplica.` quando o campo não pertencer à natureza ou ao escopo do projeto.
- `Não se aplica.` exige justificativa verificável.
- Campos pendentes bloqueiam somente os ramos que dependem deles.
- Exemplos devem ser removidos após preenchimento definitivo.
- Justificativas históricas e contexto de decisões pertencem ao `README.md` ou a registro específico de decisão.
- Fatos do estado implementado, como versão, situação atual e funcionalidades, pertencem exclusivamente ao `README.md`.
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

## 6. Adoção das regras universais

Aplicabilidade de `regrasUxUi.md`:

O commit do repositório `base` adotado é registrado na declaração de conformidade de cada commit de conclusão e de promoção, conforme `regrasDev.md`.

## 7. Exceções autorizadas pelas regras universais

Para cada exceção autorizada, registrar:

Documento e regra que autoriza a exceção:

Justificativa verificável:

Escopo mínimo:

Impacto:

Risco:

Medida compensatória:

Responsável:

Condição ou prazo de reavaliação:

Critério de encerramento:

Quando não existirem:

```text
Não se aplica.
```

## 8. Conflitos normativos resolvidos

Para cada conflito entre regras universais do mesmo nível resolvido conforme `regrasDev.md`, registrar:

Regras em conflito:

Escopo:

Solução adotada:

Critério de precedência aplicado:

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

Requisitos que possuem seção própria neste documento são definidos exclusivamente nela.

Plataformas suportadas:

Modo de funcionamento:

Funcionamento offline:

Comunicação em tempo real:

Importação de arquivos:

Geração de arquivos:

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

Limites de tamanho de entrada:

Limites de tamanho de resultado:

Recursos computacionais disponíveis:

Processos críticos:

Complexidade computacional adotada por processo crítico:

Conteúdos, regiões ou resultados prioritários, quando aplicáveis:

Trabalhos secundários que podem permanecer fora do caminho crítico:

Critério para considerar ganho de desempenho relevante:

Estratégia de concorrência ou paralelismo exclusivamente para desempenho e capacidade:

Limites de concorrência relacionados à capacidade:

Otimizações relevantes e respectivas justificativas:

Ferramenta de medição de desempenho:

Ambiente de medição:

Cenários de medição:

Tolerância de variação e de regressão:

## 12. Restrições e premissas

Tecnologias obrigatórias:

Tecnologias proibidas:

Ambientes suportados:

Limites de infraestrutura:

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

Biblioteca de validação:

Estratégia de estilos:

Biblioteca visual:

Design system:

## 16. Back-end

Aplicabilidade:

Framework:

Servidor ou adaptador HTTP:

Biblioteca de validação:

Mecanismo de autenticação:

Documentação da API:

Mecanismo de processamento assíncrono:

## 17. Persistência

Aplicabilidade:

Banco de dados:

ORM, query builder ou driver:

Ferramenta de migrações:

Cache:

Estratégia de invalidação:

Armazenamento de arquivos:

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

Ordem interna dos arquivos:

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

Estados semânticos concretizados na implementação:

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

## 32. Contexto de uso

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

## 37. Componentes visuais

Biblioteca ou design system:

Critério para componente compartilhado:

Variantes permitidas:

Estados obrigatórios:

Política para elementos nativos:

Política de foco:

Política de ícones:

## 38. Interação, formulários e conteúdo

Política de disponibilidade de ações conforme permissões conhecidas:

Política para ações canceláveis, reversíveis ou compensáveis:

Comunicação de limitações de reversibilidade:

Padrão de rótulos:

Padrão de obrigatoriedade:

Momento da validação:

Padrão de mensagens de erro:

Padrão de ações:

Padrão de datas, números e unidades:

Tom de voz:

Idiomas suportados e padrão de internacionalização:

## 39. Acessibilidade

Padrão ou nível exigido:

Critérios de contraste:

Ampliação suportada:

Navegação por teclado:

Leitores de tela:

Redução de movimento:

Alternativas de mídia:

## 40. Validação de UX e UI

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

Critérios de sucesso de UX e respectivos valores:

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

Semântica de concorrência das operações:

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

Compatibilidade entre versões durante a implantação:

Validação de migrações:

Backup:

Verificação de restauração:

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

Limite de tentativas:

Backoff:

Fallback:

Tratamento de erros:

Limites de uso:

Verificação de contrato:

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

## 46. Segurança e privacidade

Classificação dos dados sensíveis:

Proteção em armazenamento:

Proteção em transporte:

Proteção em logs e mensagens:

Gestão de segredos:

Retenção e descarte de dados:

Exigências legais aplicáveis:

## 47. Processamentos especializados

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

## 48. Configuração e ambientes

Ambientes:

Diretório de configuração:

Variáveis obrigatórias:

Variáveis opcionais:

Valores padrão:

Validação da configuração:

Arquivo de exemplo:

Dados proibidos no repositório:

Diferenças entre ambientes:

## 49. Grafo comportamental e testes

Local do grafo de casos de uso:

Local do grafo comportamental:

Relação e rastreabilidade entre grafo de casos de uso e grafo comportamental:

Local do catálogo de estados, transições e restrições comportamentais:

Estados catalogados no grafo comportamental:

Estados declarados inalcançáveis e respectivas justificativas:

Transições válidas catalogadas:

Transições proibidas relevantes e evidências de prevenção ou rejeição:

Estados de encerramento catalogados:

Evidência de completude do grafo:

Local do mapeamento entre transições semânticas e caminhos técnicos de implementação:

Local da rastreabilidade entre modelo e validação:

Forma de identificação de estados, transições e sequências nas evidências:

Estratégia geral de testes:

Critérios adicionais de cobertura específicos do projeto:

Procedimento e evidências usados para demonstrar o atendimento ao critério universal de cobertura comportamental completa:

Transições catalogadas validadas isoladamente:

Sequências comportamentais sujeitas a dependência ou interferência:

Cenários de reentrada relevantes:

Cenários de alternância entre métodos de entrada:

Cenários assíncronos e concorrentes relevantes:

Cenários de respostas obsoletas:

Cenários de execução única da intenção comportamental e, quando aplicável, da intenção de domínio:

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

Ferramenta de teste de mutação:

Indisponibilidade de ferramenta de mutação e justificativa:

Operadores de mutação adotados:

Momento de execução da mutação no escopo afetado e integral:

Limite de tempo da mutação:

Local do registro de mutantes equivalentes por equivalência sintática:

Estratégia de isolamento das evidências:

Estratégia de paralelização das evidências:

Estratégia de seleção de evidências por impacto:

Otimizações de mutação adotadas:

Otimizações de execução não adotadas e justificativas:

## 50. Comandos de validação

Desenvolvimento:

Build:

Lint:

Tipagem:

Testes unitários:

Testes de integração:

Testes ponta a ponta:

Formatação:

Validação UX/UI:

Mutação:

Desempenho:

Tempo máximo do portão de conclusão:

Tempo máximo da promoção:

Tolerância de regressão do tempo dos portões:

## 51. Versionamento e integração

Branch estável:

Branch de integração:

Branches de trabalho:

Estratégia de integração:

Mecanismo de verificação do commit de conclusão:

Atualização forçada:

Critérios adicionais para promoção:

Relatórios permanentes:

Destino de evidências temporárias:

Política para scripts e workflows temporários:

## 52. Build e implantação

Artefato de build:

Empacotamento:

Implantação:

Rollback:

Critério técnico de conclusão:

---

# Parte IX — Controle arquitetural

## 53. Restrições obrigatórias

Arquivos ou módulos que não podem ser removidos:

Tecnologias que exigem decisão explícita para substituição:

Comportamentos protegidos:

Contratos protegidos:

Compatibilidades protegidas:

Acessos diretos proibidos:

Duplicações arquiteturais proibidas:

## 54. Baseline de comportamento

Commit usado como baseline:

Casos de uso executados:

Contratos registrados:

Formatos registrados:

Resultados observáveis registrados:

Evidências:

## 55. Planejamento estrutural

A árvore aprovada é definida exclusivamente na seção de estrutura de diretórios.

Estratégia de migração:

Estratégia de poda:

Critérios de revalidação dos ramos:

## 56. Decisões pendentes

Para cada decisão:

Descrição:

Motivo:

Impacto:

Opções consideradas:

Regra temporária:

Ramos bloqueados:

Seções afetadas:

## 57. Débitos técnicos

Para cada débito:

Descrição:

Causa:

Impacto:

Risco:

Escopo:

Tratamento planejado:

Prioridade:
