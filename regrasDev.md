# Regras de Desenvolvimento

## 1. Objetivo

Este documento define as normas universais de engenharia, arquitetura, organização, modularização, implementação, qualidade e validação aplicáveis a todos os projetos que o adotem.

Seu objetivo é garantir que o código e a árvore do projeto representem a menor arquitetura semanticamente suficiente para as responsabilidades reais do sistema.

As decisões concretas de cada projeto, como stack, estrutura final, bibliotecas, valores, integrações, limites e estratégias, pertencem ao `regrasProjeto.md`.

---

## 2. Natureza normativa e mutabilidade

Este documento é:

- normativo;
- universal;
- canônico;
- imutável no contexto de um projeto.

Durante a criação, manutenção ou normalização de um projeto:

- este documento não pode ser adaptado ao projeto;
- regras não aplicáveis não podem ser removidas;
- regras específicas do projeto não podem ser adicionadas localmente;
- o conteúdo deve corresponder integralmente à revisão oficial adotada do repositório `base`;
- incompatibilidades devem ser resolvidas no projeto ou registradas como não conformidades;
- uma incompatibilidade local não autoriza modificar, ignorar, reduzir ou suspender uma regra universal.

Este documento somente pode ser alterado quando o objeto da alteração for o próprio padrão universal mantido no repositório `base`.

---

## 3. Relação entre os documentos

```text
regrasDev.md + regrasUxUi.md
            ↓
       regrasProjeto.md
            ↓
         código-fonte
            ↓
          README.md
```

- `regrasDev.md` define critérios universais de engenharia e arquitetura.
- `regrasUxUi.md` define critérios universais de experiência e interface.
- `regrasProjeto.md` concretiza as normas universais para um projeto específico.
- o código-fonte implementa a concretização válida.
- o `README.md` descreve o estado efetivamente implementado.

`regrasProjeto.md` pode concretizar, restringir ou especializar decisões que os documentos universais delegarem ao projeto, mas não pode contradizê-los, dispensá-los ou reduzir seus critérios mínimos.

### Conceitos transversais

Quando um conceito produzir obrigações tanto de engenharia ou arquitetura quanto de experiência ou interface, sua definição e suas especializações devem ser distribuídas pela responsabilidade fundamental:

- quando a responsabilidade fundamental for de engenharia ou arquitetura, este documento contém a definição canônica e `regrasUxUi.md` contém somente as especializações necessárias à experiência e à interface;
- quando a responsabilidade fundamental for de experiência ou interface, `regrasUxUi.md` contém a definição canônica e este documento contém somente as especializações técnicas necessárias;
- uma especialização presente neste documento deve preservar integralmente o significado, os critérios mínimos e as restrições da definição canônica;
- uma especialização não pode redefinir o conceito, criar critério concorrente nem constituir segunda fonte canônica;
- uma obrigação transversal aplicável ao escopo deste documento deve ser explicitada aqui sempre que sua ausência puder permitir interpretação local incompleta, ainda que a definição canônica permaneça em `regrasUxUi.md`;
- essa explicitação deve identificar a dependência normativa ou especializar suas consequências técnicas sem repetir desnecessariamente a definição canônica.

---

## 4. Aplicação independente e cumulativa

Cada regra definida em `regrasDev.md`, `regrasUxUi.md` e `regrasProjeto.md` deve ser analisada, aplicada e validada independentemente das demais.

O atendimento a uma regra:

- não implica atendimento a outra;
- não substitui outra;
- não dispensa outra;
- não permite concluir conformidade integral sem avaliar todas as regras aplicáveis.

As regras são cumulativas, salvo quando o próprio texto declarar explicitamente:

- dependência;
- precedência;
- exceção;
- não aplicabilidade.

Cada regra universal deve ser:

- independente;
- objetiva;
- afirmativa;
- verificável;
- tecnologicamente neutra;
- semanticamente singular.

Uma regra não deve depender de inferência quando uma interpretação divergente já tiver sido observada.

---

## 5. Precedência e conflitos

Em caso de conflito real, aplicar a seguinte precedência:

1. exigências legais e restrições técnicas incontornáveis da plataforma;
2. `regrasDev.md` e `regrasUxUi.md`, aplicados cumulativamente;
3. `regrasProjeto.md`;
4. código-fonte e convenções já consolidadas no projeto.

A precedência deve ser aplicada somente ao escopo incompatível. Todas as regras não afetadas permanecem obrigatórias.

Um conflito normativo existe somente quando duas regras aplicáveis não podem ser satisfeitas simultaneamente no mesmo escopo.

Não constituem conflito normativo:

- preferência pessoal;
- custo evitável;
- prazo;
- hábito;
- conveniência;
- estética;
- limitação evitável da implementação;
- convenção popular sem obrigatoriedade técnica.

Quando regras universais do mesmo nível não puderem ser satisfeitas simultaneamente, deve prevalecer a solução que melhor preserve:

1. corretude;
2. segurança;
3. integridade dos dados;
4. acessibilidade;
5. comportamento observável;
6. contratos públicos.

A decisão deve ser explícita e documentada.

---

## 6. Não conformidades e exceções

Cópias locais deste documento não podem divergir da fonte canônica.

Quando o projeto não puder satisfazer uma regra universal, a situação deve ser registrada em `regrasProjeto.md` como não conformidade conhecida, contendo:

- documento e regra afetada;
- causa;
- escopo;
- impacto;
- risco;
- responsável;
- tratamento planejado;
- medida compensatória, quando aplicável;
- condição ou prazo para correção.

O registro de uma não conformidade:

- não substitui a regra;
- não modifica a regra;
- não suspende a regra;
- não transforma a violação em conformidade.

Uma exceção somente é válida quando a própria regra universal autorizar explicitamente a exceção.

Toda exceção deve:

- permanecer restrita ao menor escopo possível;
- declarar a regra afetada;
- possuir justificativa verificável;
- registrar risco e impacto;
- possuir critério de encerramento;
- ser reavaliada quando mudar o contexto, a tecnologia, o risco ou a regra afetada.

Uma exceção local não cria convenção geral.

---

# Parte I — Princípios universais

## 7. Clareza

- O código deve priorizar legibilidade, previsibilidade e manutenção.
- Código explícito é preferível a comportamento implícito difícil de localizar.
- Nomes, contratos, efeitos e dependências devem permitir compreender a intenção sem reconstruir mentalmente detalhes dispersos.
- A solução mais simples que preserve corretude, segurança e capacidade de evolução deve ser preferida.

## 8. Responsabilidade

- Cada nó estrutural deve possuir uma responsabilidade principal identificável.
- Uma responsabilidade representa um motivo coerente para mudança.
- Quando um nó tende a mudar por motivos independentes, ele deve ser avaliado para divisão.
- Responsabilidade é o critério principal de modularização.

## 9. Coesão

- Elementos que colaboram para resolver o mesmo problema devem permanecer próximos.
- Elementos com o mesmo consumidor, contexto, finalidade e ciclo de mudança devem permanecer no mesmo módulo enquanto não possuírem independência real.
- Código não relacionado deve permanecer separado, mesmo quando possa tecnicamente compartilhar o mesmo nó.

## 10. Acoplamento

- Dependências devem ser explícitas e reduzidas ao necessário.
- Alterações internas de um nó não devem exigir mudanças indiscriminadas em outros nós.
- Um nó não deve depender de detalhes internos de outro nó fora da fronteira pública permitida.
- Dependências devem seguir direção previsível e evitar ciclos.

## 11. Arquitetura proporcional

- A arquitetura deve crescer conforme a complexidade real do projeto.
- Projetos pequenos não devem reproduzir estruturas próprias de sistemas maiores sem necessidade.
- Projetos maiores não devem permanecer em estruturas simples quando isso comprometer manutenção, testes, segurança ou evolução.
- Nenhuma camada, abstração, arquivo ou diretório deve existir apenas para satisfazer um padrão teórico ou produzir simetria visual.

## 12. Proximidade

- Código específico deve permanecer próximo do domínio, funcionalidade, página, módulo, arquivo ou função que o utiliza.
- Todo conteúdo deve começar no menor contexto semanticamente correto.
- Código só deve ser promovido para uma área compartilhada quando houver reutilização real, estável e semanticamente equivalente.

## 13. Corretude antes da simplificação

Quando não for possível satisfazer simultaneamente todos os objetivos:

- corretude prevalece sobre redução de código;
- segurança prevalece sobre conveniência;
- integridade dos dados prevalece sobre eficiência;
- contratos públicos prevalecem sobre conveniências de refatoração;
- responsabilidade e coesão prevalecem sobre tamanho físico;
- estrutura semântica prevalece sobre simetria da árvore.

---

# Parte II — Modelo universal da árvore

## 14. Projeto como árvore semântica

A estrutura completa de um projeto deve ser compreendida como uma única árvore semântica.

- A raiz é o diretório raiz do projeto.
- Os nós intermediários podem ser domínios, contextos, módulos, diretórios, arquivos, classes, componentes, funções, métodos ou blocos lógicos.
- As folhas são os menores blocos lógicos indivisíveis.

Exemplo conceitual:

```text
raiz do projeto
└── domínio
    └── módulo
        └── diretório
            └── arquivo
                └── função
                    └── bloco lógico indivisível
```

Nem todos os níveis precisam existir. Cada nível deve ser criado somente quando representar responsabilidade real.

## 15. Bloco lógico indivisível

Um bloco é indivisível quando sua separação:

- não produz responsabilidades independentes;
- não cria contrato próprio;
- não permite teste independente relevante;
- não reduz acoplamento;
- apenas aumenta navegação, nomes ou indireções.

Um bloco deixa de ser indivisível quando contém partes com:

- responsabilidades distintas;
- dependências independentes;
- ciclos de mudança distintos;
- consumidores distintos;
- contratos próprios;
- possibilidade real de teste independente.

## 16. Menor árvore semanticamente suficiente

A estrutura deve utilizar o menor número de nós, folhas e níveis capaz de preservar:

- separação clara de responsabilidades;
- localização intuitiva;
- coesão;
- isolamento entre domínios;
- manutenção independente;
- testabilidade;
- direção previsível das dependências;
- segurança;
- contratos.

A menor árvore semanticamente suficiente não é a árvore com a menor quantidade absoluta de elementos.

Redução estrutural não pode produzir:

- responsabilidades misturadas;
- arquivos genéricos;
- funções extensas com múltiplas tarefas;
- diretórios usados como depósitos;
- fronteiras implícitas;
- dependências imprevisíveis.

## 17. Balanceamento horizontal e vertical

O balanceamento horizontal controla a quantidade e a relação semântica dos filhos de um nó.

O balanceamento vertical controla a profundidade entre a raiz e as folhas.

A árvore está adequadamente balanceada quando:

- cada nó possui filhos semanticamente relacionados;
- nós sobrecarregados são subdivididos somente quando existem grupos reais;
- não existem níveis intermediários sem responsabilidade própria;
- não existem cadeias de filho único sem justificativa;
- a profundidade é proporcional à complexidade;
- a largura não impede localização direta;
- nenhuma divisão existe apenas por simetria visual.

Quantidade de filhos é indicador, não limite numérico automático.

## 18. Modularização das folhas para a raiz

Toda modularização deve ocorrer obrigatoriamente das folhas para a raiz.

Ordem de análise:

```text
blocos lógicos indivisíveis
→ funções, métodos ou componentes
→ arquivos
→ diretórios
→ módulos
→ domínios ou contextos
→ raiz do projeto
```

O nível pai só pode ser considerado conforme depois que todos os filhos relevantes estiverem conformes.

Em cada nível:

1. identificar os nós relevantes;
2. compreender suas responsabilidades;
3. organizar o conteúdo interno;
4. avaliar coesão, dependências, consumidores e ciclos de mudança;
5. dividir, agrupar ou realocar somente quando houver justificativa semântica;
6. remover duplicações, classificações concorrentes e níveis artificiais;
7. revalidar o nível;
8. avançar exatamente um nível em direção à raiz.

## 19. Ordem entre modularização e balanceamento

Para cada nó:

1. modularizar e validar o conteúdo interno e os filhos;
2. avaliar o balanceamento do nó;
3. dividir, agrupar, mover, promover, incorporar ou remover filhos somente quando necessário;
4. retornar ao menor nível afetado quando o balanceamento alterar a estrutura;
5. remodularizar e revalidar o ramo das folhas para a raiz;
6. concluir o nó somente quando modularização e balanceamento estiverem simultaneamente conformes.

Não é permitido modularizar toda a árvore e balancear toda a árvore como duas etapas globais executadas uma única vez.

## 20. Revalidação do ramo afetado

Quando uma alteração em nível superior afetar qualquer nível inferior já validado:

- identificar o menor nível afetado;
- retornar a esse nível;
- reavaliar todos os descendentes relevantes;
- subir novamente das folhas para a raiz.

Uma validação anterior deixa de ser suficiente quando suas premissas estruturais forem modificadas.

---

# Parte III — Divisão, alocação e abstração

## 21. Unidade de modularização

A unidade de modularização é a responsabilidade, não o tipo técnico nem a quantidade física de elementos.

A existência de múltiplos componentes, estilos, funções, tipos, constantes ou contratos não justifica isoladamente a criação de múltiplos arquivos, diretórios, módulos ou camadas.

Não criar automaticamente:

- um arquivo por função;
- um arquivo por componente visual;
- um arquivo por estilo;
- um diretório por arquivo;
- um módulo por tipo técnico;
- uma abstração por elemento de marcação;
- uma camada por convenção arquitetural.

A separação exige responsabilidade, contrato, consumidor, ciclo de mudança, teste ou evolução independente real.

## 22. Regra de divisão

Um nó deve ser dividido quando ocorrer pelo menos uma destas condições:

- contém responsabilidades diferentes;
- possui filhos com ciclos de mudança distintos;
- mistura fronteiras técnicas incompatíveis;
- sua responsabilidade única possui sub-responsabilidades reais e nomeáveis;
- a quantidade de filhos prejudica localização, compreensão, teste ou manutenção;
- partes internas possuem dependências ou consumidores independentes;
- a divisão reduz acoplamento relevante;
- a divisão torna contratos ou limites mais claros.

Quantidade de linhas, arquivos, funções ou diretórios nunca constitui critério isolado.

## 23. Regra de permanência

Elementos devem permanecer no mesmo nó quando:

- participam do mesmo fluxo;
- possuem o mesmo motivo de mudança;
- utilizam as mesmas dependências;
- possuem o mesmo consumidor principal;
- dependem do mesmo contexto;
- não possuem valor independente;
- sua separação apenas aumentaria navegação;
- o nó atual permanece claro, coeso e previsível.

## 24. Regra de alocação

Cada elemento deve ser alocado no menor nó semanticamente correto capaz de representá-lo.

Ao reorganizar:

- criar nós irmãos quando as responsabilidades estiverem no mesmo nível de abstração;
- criar subnós quando representarem partes internas de uma responsabilidade maior;
- realocar para outro ramo quando a responsabilidade pertencer a outro domínio;
- criar área compartilhada somente quando houver consumidores reais em ramos distintos;
- preservar uma localização canônica para cada responsabilidade.

Não criar nós apenas para distribuir visualmente a árvore.

## 25. Menor abstração semanticamente suficiente

A implementação deve utilizar a menor abstração capaz de tornar responsabilidades, estados, variantes, contratos e dependências compreensíveis, sem privilegiar apenas a menor quantidade de código.

Criar uma abstração somente quando ela reduzir pelo menos um destes custos:

- compreensão;
- localização;
- alteração;
- validação;
- reutilização;
- acoplamento;
- risco de erro.

Uma abstração pode:

- eliminar repetição relevante;
- estabilizar um contrato;
- isolar dependência variável;
- representar conceito real do domínio;
- proteger fronteira;
- simplificar consumidores.

A menor abstração não corresponde necessariamente à menor quantidade de código.

Uma abstração que apenas acrescente nomes, arquivos, níveis ou indireções sem reduzir algum custo deve ser evitada.

Não abstrair para antecipar necessidade futura sem evidência.

## 26. Compartilhamento exige equivalência semântica

Compartilhar somente quando os usos possuírem:

- mesma responsabilidade;
- mesmo significado;
- mesmo contrato;
- mesmo comportamento esperado;
- evolução previsivelmente conjunta;
- consumidores reais em mais de um contexto ou necessidade arquitetural clara.

Semelhança visual, nominal, estrutural ou técnica isolada não justifica compartilhamento.

Código compartilhado deve retornar ao contexto específico quando os consumidores deixarem de possuir equivalência semântica.

## 27. Camadas

Adicionar camada somente quando houver:

- responsabilidade distinta;
- fronteira técnica;
- regra de dependência;
- coordenação;
- proteção;
- adaptação;
- transformação.

Camadas que apenas encaminham dados sem acrescentar responsabilidade devem ser incorporadas ao nó semanticamente correto.

---

# Parte IV — Organização da árvore

## 28. Organização obrigatória

- A estrutura deve ser organizada por responsabilidade, domínio ou funcionalidade conforme a natureza do projeto.
- Cada nó deve possuir propósito claro e nome semanticamente coerente.
- A árvore deve permitir localizar código sem conhecer previamente toda a implementação.
- Elementos relacionados devem permanecer próximos.
- Código compartilhado deve ser distinguido de código específico.
- Não manter árvores concorrentes para a mesma responsabilidade.
- Não preservar estrutura antiga após migração concluída.
- Fronteiras entre módulos devem ser explícitas.

A estrutura concreta pertence ao `regrasProjeto.md`.

## 29. Modelo abstrato

```text
projeto/
├── documentação e regras
├── configurações
├── scripts e automações
├── código-fonte/
│   ├── inicialização e composição
│   ├── domínios ou funcionalidades
│   ├── compartilhado
│   └── infraestrutura global
├── recursos estáticos
└── testes externos, quando aplicável
```

O modelo é conceitual. Nenhum diretório ou nível é obrigatório sem responsabilidade real.

## 30. Profundidade

Criar novo nível somente quando ele:

- representar responsabilidade própria;
- agrupar múltiplos elementos relacionados;
- separar conteúdo de natureza distinta;
- reduzir sobrecarga real;
- tornar localização mais previsível.

Não criar nível que:

- repita o nome do pai;
- contenha um único filho sem justificativa;
- represente categoria técnica desnecessária;
- aumente navegação sem melhorar entendimento.

## 31. Largura

Não existe quantidade máxima fixa de filhos por nó.

Avaliar subdivisão quando:

- elementos forem difíceis de localizar;
- prefixos repetidos simularem agrupamentos;
- grupos semanticamente distintos estiverem misturados;
- novos elementos não possuírem posição previsível;
- manutenção exigir busca frequente.

Não subdividir apenas para reduzir visualmente a quantidade de filhos.

## 32. Diretórios genéricos

Diretórios como `components`, `utils`, `services`, `helpers`, `common`, `shared`, `types` e `hooks` devem possuir escopo claro.

Não devem funcionar como depósitos classificados apenas por tipo técnico.

## 33. Promoção progressiva

A promoção estrutural deve seguir, quando necessária:

```text
bloco lógico
→ função, método ou componente
→ arquivo
→ diretório
→ módulo
→ domínio
→ estrutura global
```

Um elemento só deve subir de nível quando adquirir responsabilidade, dependências, consumidores, contrato ou ciclo de mudança próprios.

---

# Parte V — Código interno

## 34. Funções, métodos e componentes

Cada função, método ou componente deve:

- executar uma responsabilidade principal;
- possuir nome que descreva intenção;
- receber apenas dados necessários;
- tornar efeitos externos explícitos;
- retornar resultado previsível;
- evitar misturar validação, transformação, persistência e apresentação sem coordenação justificável;
- delegar etapas independentes;
- evitar aninhamento excessivo;
- tratar erros na fronteira adequada.

Uma função coordenadora pode representar fluxo composto, desde que delegue etapas independentes.

## 35. Arquivos

Cada arquivo deve possuir responsabilidade principal identificável pelo nome e pela posição.

Criar arquivo quando o conteúdo:

- representar conceito próprio;
- possuir motivo de mudança diferente;
- depender de recursos distintos;
- puder ser testado isoladamente;
- possuir reutilização real;
- implementar fronteira ou contrato;
- comprometer a coesão do arquivo atual.

Não criar arquivo apenas para:

- reduzir linhas;
- armazenar constante local sem contexto próprio;
- separar função privada inseparável;
- criar wrapper sem responsabilidade;
- antecipar reutilização;
- reproduzir convenção externa.

## 36. Diretórios

Criar diretório somente quando houver conjunto coeso de arquivos ou subdiretórios que:

- represente responsabilidade identificável;
- forme domínio, funcionalidade ou fronteira;
- torne o pai realmente sobrecarregado;
- precise ser localizado como grupo.

Diretório com único filho exige justificativa arquitetural ou técnica explícita.

## 37. Módulos e domínios

Criar módulo quando um conjunto possuir:

- responsabilidade funcional ou de negócio própria;
- contratos próprios;
- dependências próprias;
- ciclo de vida relativamente independente;
- fronteira clara.

Módulos devem expor interface pública intencional e proteger detalhes internos.

## 38. Ordem interna de arquivos

Quando aplicável, utilizar ordem previsível:

1. imports;
2. tipos e contratos locais;
3. constantes locais;
4. validações;
5. funções auxiliares privadas;
6. implementação principal;
7. composição ou coordenação;
8. exports.

A ordem pode ser adaptada à tecnologia, mas deve permanecer consistente no projeto.

## 39. Duplicação

- Duplicação pequena e ocasional pode ser preferível a abstração incorreta.
- Extrair quando a repetição representar o mesmo conceito e possuir manutenção conjunta.
- Não unificar comportamentos apenas semelhantes.

---

# Parte VI — Nomenclatura, tipagem e contratos

## 40. Nomenclatura semântica

Todo nó deve possuir nome que represente sua responsabilidade real dentro do contexto dos nós superiores.

A leitura do caminho da raiz até a folha deve permitir compreender progressivamente a finalidade.

Os nomes devem:

- representar conteúdo ou comportamento real;
- distinguir responsabilidades diferentes;
- utilizar vocabulário consistente do domínio;
- conter somente contexto necessário;
- evitar termos genéricos, históricos ou baseados apenas na implementação;
- ser reavaliados quando a responsabilidade mudar.

A responsabilidade deve ser identificada antes da escolha do nome.

Convenções de linguagem definem a forma, não o significado.

Quando aplicável:

- `camelCase` para variáveis, funções, métodos e propriedades;
- `PascalCase` para componentes, classes, tipos, interfaces e enums;
- `UPPER_SNAKE_CASE` apenas para constantes globais convencionais;
- funções indicam ação;
- booleanos indicam condição, preferencialmente com `is`, `has`, `can` ou `should`;
- coleções usam plural;
- abreviações não consolidadas devem ser evitadas.

## 41. Convenções tecnológicas

Uma convenção pode prevalecer quando:

- for obrigatória para linguagem, framework ou ferramenta;
- permitir descoberta automática;
- reduzir configuração relevante;
- for consolidada e previsível no ecossistema;
- melhorar interoperabilidade.

Não aplicar convenção apenas por hábito quando ela prejudicar a semântica.

## 42. Tipagem

- Contratos públicos devem possuir tipos explícitos.
- Preferir `unknown` a `any` quando o dado precisar de validação.
- Evitar casts para silenciar erros.
- Dados externos devem ser validados em runtime quando necessário.
- Tipos devem impedir estados inválidos quando viável.
- Tipos locais permanecem próximos ao uso.
- Tipos compartilhados representam contratos realmente compartilhados.

## 43. Contratos

Contrato é qualquer interface estável entre módulos, processos ou sistemas.

- Contratos devem ser explícitos e previsíveis.
- Contratos públicos devem ser definidos antes das implementações concretas que os satisfazem.
- Mudanças incompatíveis devem ser tratadas deliberadamente.
- Implementações internas não devem vazar.
- Campos opcionais, valores nulos e estados de erro devem ser intencionais.

## 44. Semântica e contratos nativos da plataforma

Abstrações, wrappers e componentes devem preservar a semântica, os contratos e os comportamentos nativos adequados da linguagem, plataforma ou ambiente.

Não substituir recurso nativo adequado por abstração genérica que exija reconstrução manual de:

- comportamento;
- integração;
- estado;
- valor;
- foco;
- teclado;
- acessibilidade;
- ciclo de vida;
- compatibilidade com ferramentas.

Quando uma abstração for necessária, ela deve preservar os contratos observáveis e acrescentar responsabilidade real.

## 45. Comentários e documentação

- Comentários explicam intenção, restrição, decisão ou motivo não evidente.
- Não comentar linha a linha comportamento já claro.
- Comentários devem permanecer sincronizados.
- Código desativado não deve permanecer comentado.
- Documentação afetada deve ser atualizada junto com o código.
- Evidências temporárias devem permanecer em logs ou artefatos apropriados.

---

# Parte VII — Dependências, configuração, erros e segurança

## 46. Dependências

Antes de adicionar dependência, verificar se:

- resolve problema real;
- não existe solução adequada já disponível;
- reduz mais complexidade do que adiciona;
- possui manutenção, documentação e licença compatíveis;
- impacto em segurança, tamanho e desempenho é aceitável.

Dependências não utilizadas devem ser removidas.

## 47. Imports

- Remover imports não utilizados.
- Evitar ciclos.
- Preferir caminhos estáveis.
- Não acessar detalhes internos de outros módulos.
- Evitar reexports em cadeia.

## 48. Configuração

- Configurações variáveis devem ser centralizadas.
- Valores de ambiente devem ser validados na inicialização.
- Configurações obrigatórias ausentes devem produzir erro claro.
- Segredos nunca devem ser versionados.
- Valores específicos de ambiente não pertencem à regra de negócio.

## 49. Erros

- Erros não devem ser ignorados silenciosamente.
- Erros esperados devem possuir representação previsível.
- Falhas inesperadas devem preservar contexto para diagnóstico.
- Mensagens externas não devem expor detalhes internos.
- Recuperação automática só deve ocorrer quando for segura.
- A taxonomia interna de erros deve ser definida antes da conversão para transporte, interface, logs ou métricas.

## 50. Segurança

- Toda entrada externa é não confiável.
- Validação, autenticação e autorização devem ocorrer na fronteira adequada.
- Aplicar menor privilégio.
- Dados sensíveis devem ser protegidos em armazenamento, transporte e logs.
- Não confiar no cliente para decisões de segurança.
- Requisitos de segurança e privacidade devem anteceder decisões sobre logs, persistência e preenchimento automático.

## 51. Observabilidade

- Logs devem possuir contexto suficiente.
- Não registrar segredos ou dados sensíveis sem necessidade explícita.
- Mensagens devem ser consistentes e acionáveis.
- Métricas e rastreamento devem existir quando houver necessidade operacional real.

---

# Parte VIII — Regras de front-end

## 52. Organização do front-end

A árvore deve representar responsabilidades reais da interface e dos fluxos.

Quando existirem, distinguir:

- inicialização e composição;
- páginas, telas ou rotas;
- funcionalidades ou domínios;
- componentes compartilhados;
- componentes específicos;
- estado compartilhado e local;
- engines e transformações;
- templates;
- integrações;
- assets;
- contratos.

Nenhuma divisão é criada automaticamente.

## 53. Normalização global de estilos

Todo front-end web deve possuir base global de estilos carregada na inicialização para neutralizar diferenças desnecessárias entre navegadores suportados.

Reset mínimo:

```css
*,
*::before,
*::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}
```

Quando aplicável, a base global deve:

- fazer controles herdarem tipografia e cor;
- impedir mídia de ultrapassar o contêiner;
- definir comportamento previsível para conteúdo substituído;
- normalizar diferenças relevantes dos navegadores.

A base global não deve:

- remover foco visível sem substituição equivalente;
- eliminar semântica ou comportamento nativo necessário;
- remover sinais de interação sem alternativa clara;
- introduzir regras específicas de componentes.

## 54. Responsabilidades estruturais e visuais

Elementos estruturais ou visuais com responsabilidade identificável podem possuir representação nomeada no código, mesmo sem comportamento próprio.

A nomeação é justificável quando reduz o custo de compreender:

- composição;
- hierarquia;
- estados;
- variantes;
- relações visuais.

A existência de responsabilidade visual identificável não exige isoladamente:

- novo componente;
- novo arquivo;
- novo diretório;
- API pública;
- abstração reutilizável.

Elementos incidentais usados apenas como marcação, texto ou agrupamento circunstancial devem permanecer locais quando a abstração apenas aumentar vocabulário ou navegação.

São decisões independentes:

1. nomear uma responsabilidade;
2. extrair abstração;
3. separar em arquivo;
4. promover para compartilhado.

Cada decisão deve satisfazer seus próprios critérios.

## 55. Componentes

- Componentes específicos permanecem próximos à página ou funcionalidade.
- Mover para compartilhado somente com equivalência semântica e contrato estável.
- Não manter árvores concorrentes como `src/components` e `src/shared/components` quando representarem a mesma responsabilidade.

## 56. Páginas e telas

Páginas e telas coordenam interface e fluxos de alto nível.

Não devem concentrar:

- transformações complexas;
- geração de arquivos;
- regras de negócio independentes;
- persistência;
- integrações detalhadas.

## 57. Fonte canônica de estados semânticos

Cada estado semântico deve possuir uma representação canônica.

Lógica, apresentação, comportamento e acessibilidade devem derivar da mesma representação sempre que possível.

Representações derivadas do mesmo estado devem permanecer semanticamente equivalentes em todo instante observável.

Uma alteração de estado não pode produzir divergência persistente entre comportamento, apresentação, conteúdo ou acessibilidade. Quando houver estado intermediário observável, ele deve possuir significado próprio e integrar o modelo comportamental aplicável.

Não manter fontes independentes equivalentes, como:

- `selected`;
- `active`;
- classe selecionada;
- prop visual selecionada;
- atributo acessível selecionado.

Quando a plataforma exigir duplicação, a derivação e sincronização devem ser explícitas, determinísticas e testáveis.

## 58. Condições no nível responsável

Toda condição deve ser representada no menor nível com responsabilidade e informação suficientes.

- condições de negócio pertencem ao domínio ou caso de uso;
- condições derivadas de dados pertencem à transformação ou contrato responsável;
- estados funcionais pertencem ao componente ou módulo controlador;
- condições exclusivamente apresentacionais pertencem à camada visual;
- características do ambiente pertencem aos mecanismos da plataforma.

Condições apresentacionais não devem introduzir estado de aplicação, eventos, listeners ou processamento de runtime quando o mecanismo visual for suficiente.

A camada visual não deve reconstruir decisões de negócio a partir de sinais indiretos de apresentação.

## 59. Contratos de variantes

Parâmetros de componentes devem representar conceitos coerentes, como:

- tamanho;
- densidade;
- ênfase;
- intenção;
- orientação;
- estado;
- variante.

Parâmetros públicos não devem transportar detalhes visuais arbitrários, como margens, paddings, cores e posicionamentos.

Detalhes concretos de apresentação permanecem na camada visual ou no sistema de estilos.

Uma exceção exige que o valor seja parte real e estável do contrato público.

## 60. Estado local e compartilhado

- Estado local permanece próximo ao consumidor.
- Promover para store, contexto ou equivalente somente com múltiplos consumidores, sobrevivência necessária ou atualização coordenada.
- Dados derivados devem ser calculados a partir da fonte canônica quando possível.
- A localização técnica do estado não pode reduzir o ciclo de vida exigido pelo comportamento que ele representa.
- Quando a sobrevivência além do consumidor atual fizer parte do comportamento, o estado deve permanecer no menor escopo capaz de preservá-la corretamente.

## 61. Engines e templates

Transformações complexas, cálculos, serialização e geração de arquivos permanecem fora de componentes visuais quando possuírem responsabilidade própria.

Preview e exportação não devem depender de fontes de verdade divergentes.

## 62. Assets

Assets devem ser organizados por finalidade ou domínio.

Não criar subdiretório por asset isolado sem fronteira real.

---

# Parte IX — Regras de back-end

## 63. Organização do back-end

A árvore deve ser organizada prioritariamente por domínio ou funcionalidade.

Quando existirem, distinguir:

- inicialização e composição;
- casos de uso;
- regras de negócio;
- persistência;
- integrações externas;
- transporte;
- contratos;
- configuração;
- infraestrutura compartilhada.

Nenhuma subdivisão é automática.

## 64. Domínio antes da categoria técnica

Evitar diretórios globais como `controllers`, `services`, `repositories` e `models` quando dispersarem uma funcionalidade por toda a árvore.

Preferir proximidade dos elementos do mesmo domínio.

## 65. Camadas proporcionais

Não criar controller, service, use case, repository, gateway e adapter para todo fluxo automaticamente.

Cada camada deve possuir responsabilidade real.

Camadas que apenas encaminham argumentos devem ser removidas ou incorporadas.

---

# Parte X — Testes e validação

## 66. Grafo comportamental e casos de uso

A estratégia de testes deve mapear o grafo de casos de uso e o grafo comportamental necessário para representar integralmente os comportamentos relevantes do projeto.

O grafo deve incluir, conforme aplicável:

- casos de uso;
- estados semanticamente distintos;
- transições entre estados;
- conexões relevantes;
- fluxos principais;
- fluxos alternativos;
- erros;
- recuperação;
- limites;
- estados de encerramento.

Cobertura de linhas, funções, branches ou instruções não substitui a completude nem a cobertura do grafo comportamental.

### 66.1 Modelo comportamental

Quando um comportamento possuir estado ou evolução entre condições semanticamente distintas, o modelo deve representar explicitamente:

- estado de origem;
- evento, condição ou causa da transição;
- precondições aplicáveis;
- efeitos produzidos;
- propriedades que devem permanecer invariantes quando sua preservação fizer parte do comportamento;
- estado de destino;
- falhas aplicáveis;
- possibilidades de recuperação;
- encerramento, quando aplicável.

Uma transição representa a mudança semanticamente relevante entre estados provocada por evento, condição ou resultado definido.

Uma transição somente pode alterar propriedades cuja alteração esteja definida entre seus efeitos. As demais propriedades semanticamente relevantes devem preservar seu valor válido; invalidação, reinicialização ou descarte também constituem efeitos e devem ser explícitos.

O ciclo de vida da representação técnica de um estado deve ser suficiente para o ciclo de vida do comportamento que ele representa. Recriação, recomposição, remontagem, troca de contexto técnico ou outra mudança de implementação não pode descartar estado ainda semanticamente válido sem transição que defina esse efeito.

### 66.2 Estados semanticamente distintos

Um estado deve ser catalogado separadamente quando sua existência alterar pelo menos um aspecto semanticamente relevante do comportamento, como:

- transições permitidas;
- precondições;
- invariantes;
- efeitos possíveis;
- ações disponíveis;
- comportamento observável;
- tratamento de erro;
- possibilidades de recuperação ou encerramento.

Combinações arbitrárias de valores não constituem estados distintos quando não alterarem comportamento semanticamente relevante.

### 66.3 Estados de encerramento

Estados que representem encerramento de fluxo devem declarar explicitamente quais transições de saída, se houver, permanecem permitidas.

Não devem existir transições implícitas a partir de estado de encerramento.

Quando o encerramento for definitivo no escopo modelado, nenhuma transição de saída deve ser permitida.

### 66.4 Completude do grafo comportamental

O grafo comportamental somente pode ser declarado completo quando todos os estados semanticamente possíveis e alcançáveis no escopo modelado e todas as transições válidas entre eles estiverem catalogados.

A análise de completude deve considerar, quando aplicável:

- estados iniciais;
- estados intermediários;
- permanência no mesmo estado quando possuir significado comportamental;
- sucesso;
- erro;
- espera;
- ausência;
- parcialidade;
- degradação;
- recuperação;
- limites;
- encerramento.

Todo estado catalogado deve possuir tratamento explícito para entrada, permanência, saída, erro, recuperação e encerramento quando cada uma dessas possibilidades for aplicável.

Estado ou transição cuja existência permaneça desconhecida, indefinida ou apenas presumida impede declarar o grafo completo.

### 66.5 Conformidade entre modelo e implementação

A implementação não pode produzir estado semanticamente alcançável ausente do grafo comportamental nem permitir transição alcançável não catalogada.

Quando a análise, execução ou teste revelar estado ou transição alcançável ausente do modelo:

1. o grafo deve ser atualizado para representar o comportamento válido, quando esse comportamento for intencional; ou
2. a implementação deve ser corrigida, quando o comportamento não for válido.

Enquanto a divergência existir, o comportamento afetado não pode ser considerado conforme.

### 66.6 Completude e cobertura

Completude do grafo e cobertura do grafo são critérios independentes e cumulativos.

- completude demonstra que o modelo contém todos os estados e transições semanticamente possíveis e alcançáveis no escopo definido;
- cobertura demonstra que os elementos aplicáveis do modelo possuem tratamento e evidência de validação adequados.

Cobertura integral não pode ser declarada para grafo cuja completude não tenha sido estabelecida.

O grafo deve estar formalizado e sua completude deve ser estabelecida antes de declarar cobertura integral.

## 67. Níveis de teste

A cobertura deve combinar, conforme necessidade real:

- testes unitários;
- testes de integração;
- testes de ponta a ponta.

Cada comportamento deve ser validado no nível mais adequado.

Uma categoria não deve ser exigida quando não agregar proteção, mas sua omissão deve registrar:

- qual proteção não agregaria;
- quais comportamentos permanecem cobertos;
- por quais níveis de teste.

## 68. Comportamento e permanência

- Testes verificam comportamento observável.
- Regras de negócio relevantes e estáveis devem possuir testes.
- Refatorações devem preservar contratos e comportamento.
- Testes quebrados não podem ser ignorados ou removidos para permitir integração.
- Cenários de erro e limite devem ser testados quando fizerem parte do comportamento.
- Testes permanentes permanecem versionados.
- Testes temporários só podem ser removidos quando não protegerem comportamento permanente.

## 69. Automação e evidências

- Integração contínua deve executar validações aplicáveis quando utilizada.
- Validações essenciais devem possuir forma documentada de execução local ou equivalente.
- Ausência de execução ou resultado desconhecido não equivale a aprovação.
- Declarações de validação devem identificar escopo, revisão, procedimentos, resultados e limitações.

---

# Parte XI — Versionamento e integração

## 70. Branches

- Projetos devem identificar branches estáveis, de integração e de trabalho quando existirem.
- Alterações devem ocorrer fora da branch estável quando houver fluxo de integração.
- Nomes e exceções pertencem ao `regrasProjeto.md`.
- Atualizações forçadas devem ser evitadas e somente podem ocorrer com autorização explícita e sem perda de histórico relevante.

## 71. Promoção

Uma alteração só pode ser promovida quando:

- o diff corresponder ao escopo autorizado;
- build, testes e validações aplicáveis estiverem aprovados;
- contratos e comportamentos protegidos estiverem preservados;
- documentação afetada estiver atualizada;
- não existirem resíduos ou implementações concorrentes;
- limitações e não conformidades estiverem registradas;
- a branch de destino não possuir alterações incompatíveis.

## 72. Artefatos temporários

- Arquivos, scripts, workflows, branches, pacotes e fragmentos temporários devem possuir finalidade explícita.
- Não devem tornar-se dependências da arquitetura final.
- Automações com escrita devem possuir escopo mínimo e proteção contra ciclos.
- Todo resíduo temporário deve ser removido antes da validação final.

---

# Parte XII — Refatoração e manutenção

## 73. Baseline obrigatória

Antes de normalização, migração ou refatoração estrutural, registrar baseline de:

- comportamento;
- contratos;
- formatos;
- resultados observáveis;
- casos de uso afetados.

## 74. Planejamento antes da migração

A árvore final planejada deve ser validada contra:

- responsabilidades;
- contratos;
- dependências;
- casos de uso;
- restrições do projeto.

Nenhuma migração estrutural deve começar sem plano completo.

## 75. Ordem da refatoração

Toda refatoração estrutural deve ocorrer das folhas para a raiz:

1. compreender comportamento atual;
2. identificar blocos lógicos indivisíveis;
3. organizar blocos internos;
4. modularizar funções, métodos e componentes;
5. extrair arquivos quando necessário;
6. organizar diretórios;
7. consolidar módulos e domínios;
8. validar a raiz;
9. atualizar imports, referências e contratos;
10. remover estruturas antigas;
11. validar comportamento, build e testes.

## 76. Preservação de contratos observáveis

Mudanças estruturais devem preservar, salvo alteração funcional explícita:

- conteúdo;
- ordem lógica;
- semântica;
- foco;
- navegação por teclado;
- nomes acessíveis;
- estados;
- eventos;
- valores;
- contratos públicos;
- regras de negócio;
- efeitos observáveis.

Equivalência não pode ser presumida apenas por:

- semelhança visual;
- aprovação do build;
- ausência de erro de tipagem;
- funcionamento do caminho principal isolado.

## 77. Migração e poda

Ao mover elemento:

1. confirmar que todo conteúdo necessário existe na estrutura final;
2. atualizar imports, exports, aliases e referências;
3. validar funcionamento;
4. remover versão anterior;
5. confirmar ausência de duplicações e caminhos obsoletos.

A reorganização só termina quando existir uma única árvore válida para cada responsabilidade.

---

# Parte XIII — Critério de conclusão

## 78. Regra de parada

A normalização ou modularização está concluída somente quando:

- raiz e todos os níveis foram validados das folhas para a raiz;
- cada nó representa responsabilidade clara;
- filhos são semanticamente relacionados;
- largura é administrável;
- profundidade é proporcional;
- alocação é correta;
- não existem duplicações ou classificações concorrentes;
- não existem subdivisões preventivas;
- nenhum nó pode ser dividido sem criar fragmentação artificial;
- comportamento e contratos permanecem preservados;
- documentação está atualizada.

---

# Checklist de conformidade

## Arquitetura

- [ ] A árvore representa responsabilidades reais.
- [ ] A estrutura é a menor semanticamente suficiente.
- [ ] Não existem árvores concorrentes.
- [ ] Não existem camadas artificiais.
- [ ] Dependências possuem direção previsível.

## Modularização

- [ ] A análise começou nas folhas.
- [ ] Nenhum nível pai foi validado antes dos filhos.
- [ ] A unidade de modularização foi a responsabilidade.
- [ ] Tamanho físico não foi usado como critério isolado.
- [ ] Ramos afetados foram reavaliados do menor nível até a raiz.

## Abstrações e compartilhamento

- [ ] Cada abstração reduz custo identificável.
- [ ] Não existem abstrações preventivas.
- [ ] Compartilhamento possui equivalência semântica.
- [ ] Código específico permanece próximo ao consumidor.

## Código

- [ ] Funções, componentes e arquivos possuem responsabilidade principal.
- [ ] Nomes representam responsabilidades reais.
- [ ] Contratos públicos são explícitos.
- [ ] Semântica nativa foi preservada.
- [ ] Estados semânticos possuem fonte canônica.
- [ ] Representações derivadas do mesmo estado permanecem semanticamente equivalentes.
- [ ] Transições preservam propriedades cuja alteração não esteja definida entre seus efeitos.
- [ ] O ciclo de vida técnico dos estados preserva o ciclo de vida dos comportamentos representados.
- [ ] Condições estão no nível responsável.
- [ ] Variantes representam conceitos, não propriedades arbitrárias.

## Referências

- [ ] Imports são válidos.
- [ ] Exports são válidos.
- [ ] Aliases são válidos.
- [ ] Não existem ciclos ou caminhos obsoletos.

## Testes

- [ ] O grafo de casos de uso e o grafo comportamental estão mapeados.
- [ ] Todos os estados semanticamente possíveis e alcançáveis no escopo estão catalogados.
- [ ] Todas as transições válidas e alcançáveis no escopo estão catalogadas.
- [ ] Não existem estados ou transições alcançáveis fora do modelo catalogado.
- [ ] A completude do grafo foi estabelecida antes de declarar cobertura integral.
- [ ] Fluxos principais, alternativos, erros e limites estão cobertos.
- [ ] Níveis de teste foram escolhidos conforme risco e responsabilidade.
- [ ] Testes permanentes não foram removidos.

## Refatoração

- [ ] Baseline foi registrada.
- [ ] Árvore final foi planejada antes da migração.
- [ ] Todo conteúdo foi colocado na árvore final antes da poda.
- [ ] Contratos observáveis foram revalidados.
- [ ] Não restaram resíduos temporários.

## Documentação

- [ ] `regrasDev.md` corresponde à revisão canônica.
- [ ] `regrasUxUi.md` corresponde à revisão canônica quando aplicável.
- [ ] `regrasProjeto.md` concretiza as decisões específicas.
- [ ] `README.md` descreve o estado implementado.
- [ ] Não conformidades estão explicitamente registradas.
