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
- o conteúdo deve corresponder integralmente ao commit do repositório `base` adotado na última sincronização do projeto;
- incompatibilidades devem ser resolvidas no projeto e, enquanto não resolvidas, constituem não conformidades;
- uma incompatibilidade local não autoriza modificar, ignorar, reduzir ou suspender uma regra universal.

Este documento somente pode ser alterado quando o objeto da alteração for o próprio padrão universal mantido no repositório `base`.

### Sincronização com o repositório `base`

A versão vigente das regras universais no repositório `base` é o seu commit mais recente.

A sincronização de um projeto com o repositório `base` é deliberada e não ocorre automaticamente. Até a sincronização seguinte, o projeto permanece sujeito às cópias locais correspondentes ao commit do `base` adotado na última sincronização.

A conformidade de cada commit do projeto é avaliada exclusivamente contra as regras do commit do `base` registrado em sua declaração de conformidade. Alterações posteriores no repositório `base` não tornam retroativamente não conforme um commit que era conforme às regras então adotadas.

A sincronização constitui alteração do projeto. As regras modificadas desde o commit do `base` anteriormente adotado devem ser identificadas pela comparação entre os dois commits, e a sincronização somente pode ser registrada em commit de conclusão quando o projeto satisfizer as regras sincronizadas no escopo afetado por essas modificações.

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
- `modelo-comportamental.md` registra o grafo de casos de uso e o grafo comportamental do projeto.
- `auditoria-conformidade.md` registra a avaliação de cada regra aplicável no estado auditado.

`regrasProjeto.md` pode concretizar, restringir ou especializar decisões que os documentos universais delegarem ao projeto, mas não pode contradizê-los, dispensá-los ou reduzir seus critérios mínimos.

### Conceitos transversais

Quando um conceito produzir obrigações tanto de engenharia ou arquitetura quanto de experiência ou interface, sua definição e suas especializações devem ser distribuídas pela responsabilidade fundamental.

A responsabilidade fundamental deve ser identificada pelos seguintes critérios:

- um conceito possui responsabilidade fundamental de engenharia ou arquitetura quando a garantia correspondente continuar necessária para a corretude, segurança, integridade, contratos, estado, processamento ou estrutura do sistema mesmo que não exista interação humana;
- um conceito possui responsabilidade fundamental de experiência ou interface quando a obrigação existir especificamente em razão de como uma pessoa percebe, compreende, opera ou recebe resposta do sistema;
- quando o mesmo conceito possuir uma garantia sistêmica e uma consequência humana inseparáveis, a garantia sistêmica permanece canônica em `regrasDev.md` e a consequência humana é especializada em `regrasUxUi.md`;
- quando a obrigação puder ser completamente definida sem depender de comportamento técnico interno e existir exclusivamente para a experiência humana, sua definição canônica pertence a `regrasUxUi.md`.

Aplicada essa classificação:

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

### Demonstração

Um requisito está demonstrado quando existe evidência executada sobre o conteúdo exato da alteração, com resultado conhecido, reproduzível e localizável.

Afirmação, intenção, execução sobre conteúdo diferente do avaliado ou resultado desconhecido não constituem demonstração.

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

A decisão deve ser explícita e registrada em `regrasProjeto.md` como conflito normativo resolvido, identificando as regras em conflito, o escopo, a solução adotada e o critério de precedência aplicado.

---

## 6. Não conformidades e exceções

Cópias locais deste documento não podem divergir do commit do repositório `base` adotado na última sincronização.

Esta seção contém a definição canônica de não conformidade e de exceção para `regrasDev.md`, `regrasUxUi.md` e `regrasProjeto.md`.

Não conformidade é o descumprimento conhecido de regra aplicável.

Commits intermediários podem conter não conformidades, desde que as declarem conforme a seção de declaração de conformidade. Commit de conclusão e commit de promoção não podem conter não conformidade conhecida.

A declaração de uma não conformidade:

- não substitui a regra;
- não modifica a regra;
- não suspende a regra;
- não transforma a violação em conformidade.

Uma exceção somente é válida quando a própria regra universal autorizar explicitamente a exceção.

Toda exceção deve ser registrada em `regrasProjeto.md`, contendo:

- documento e regra que autoriza a exceção;
- justificativa verificável;
- escopo mínimo;
- impacto;
- risco;
- medida compensatória, quando aplicável;
- responsável;
- condição ou prazo de reavaliação;
- critério de encerramento.

Toda exceção deve permanecer restrita ao menor escopo possível e ser reavaliada quando mudar o contexto, a tecnologia, o risco ou a regra afetada.

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

### 8.1 Elementos sem responsabilidade vigente

Todo elemento do projeto, como código, arquivo, diretório, dependência, configuração, estilo, asset, documentação, comentário, teste ou flag, deve possuir responsabilidade vigente ou consumidor real.

Elemento sem responsabilidade vigente deve ser removido na mesma alteração que eliminou sua responsabilidade.

Código que não realize nem suporte comportamento catalogado no grafo comportamental não possui responsabilidade vigente.

As regras específicas sobre código comentado, documentação, dependências, imports, camadas, estruturas migradas, artefatos temporários e testes temporários constituem aplicações desta regra.

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
- A arquitetura não deve introduzir camadas, abstrações, arquivos ou diretórios cujas responsabilidades, contratos, dependências ou ciclos de mudança não existam no projeto.
- A arquitetura deve introduzir separações adicionais quando responsabilidades, contratos, dependências ou ciclos de mudança distintos fizerem a estrutura atual comprometer manutenção, testes, segurança ou evolução.
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
- estrutura semântica prevalece sobre simetria da árvore;
- a responsabilidade de uma evidência prevalece sobre a eficiência de sua execução.

As regras de eficiência deste documento aplicam-se a todo código do projeto, inclusive evidências, fixtures, automações e scripts de validação.

### 13.1 Eficiência computacional proporcional

A implementação deve utilizar complexidade computacional e consumo de recursos proporcionais aos limites reais do problema.

Devem ser evitados, quando desnecessários, custos superiores em:

- tempo de processamento;
- memória;
- armazenamento;
- operações de entrada e saída;
- serialização e desserialização;
- comunicação de rede;
- quantidade de chamadas a serviços, persistência ou recursos externos.

Processo crítico é a operação ou o fluxo essencial para o funcionamento da aplicação ou executado com alta frequência. Os processos críticos devem ser identificados em `regrasProjeto.md`.

A execução das evidências exigidas pelos portões de commit de conclusão e de promoção constitui processo crítico em todo projeto.

Em processos críticos:

- a complexidade computacional deve ser a menor conhecida para o problema;
- a complexidade adotada deve ser conhecida e declarada em `regrasProjeto.md`;
- entre complexidade de tempo e consumo de memória, deve prevalecer a menor complexidade de tempo compatível com os limites de memória definidos em `regrasProjeto.md`;
- a complexidade deve ser avaliada em relação às dimensões da entrada que não possuam limite garantido por contrato, tipo ou invariante; dimensões com limite garantido podem ser tratadas como constantes.

Fora de processos críticos:

- entre soluções que preservem igualmente corretude, segurança, integridade, contratos e comportamento, deve ser preferida aquela que reduza custo computacional ou uso de recursos relevante sem aumentar desproporcionalmente complexidade estrutural, risco ou manutenção;
- a menor complexidade assintótica possível não constitui obrigação isolada, e uma solução teoricamente mais eficiente não deve substituir solução suficientemente eficiente quando o ganho for irrelevante para os limites reais e a troca aumentar complexidade ou risco sem benefício justificável.

A relevância de custo, ganho ou economia de recursos deve ser avaliada contra os limites, metas, carga esperada e recursos concretizados em `regrasProjeto.md`. Ganho apenas teórico, sem efeito verificável nesses limites ou metas, não constitui benefício relevante por si só.

Otimizações que adicionem complexidade relevante devem possuir necessidade demonstrada conforme a regra de medição de desempenho. Limites, metas e restrições concretas de desempenho pertencem ao `regrasProjeto.md`.

### 13.2 Trabalho computacional redundante

Processamento cujo resultado válido já esteja disponível não deve ser repetido sem necessidade.

Devem ser evitadas repetições desnecessárias de:

- cálculos;
- consultas;
- transformações;
- serializações e desserializações;
- leituras e escritas;
- transferências;
- renderizações;
- conversões;
- chamadas externas.

Resultados válidos podem ser reutilizados quando isso reduzir custo relevante e puder preservar corretude, atualidade, consistência, segurança e limites de memória ou armazenamento.

Cache, memoização, materialização ou outra forma de reutilização não são obrigatórios quando invalidação, obsolescência, coordenação, consumo de recursos ou complexidade introduzida superarem o benefício esperado.

Repetição necessária para preservar segurança, integridade, idempotência, observabilidade ou validação em fronteiras independentes não constitui trabalho redundante apenas por produzir verificação semelhante.

Resultado reutilizado constitui representação derivada de sua fonte e obedece à regra de fonte canônica de estados semânticos.

Quando a obsolescência de um resultado reutilizado puder afetar comportamento observável, seus estados de validade devem integrar o grafo comportamental, e a invalidação deve constituir efeito explícito das transições que alteram a fonte.

As evidências devem demonstrar tanto a reutilização, como propriedade de custo, quanto a invalidação, como propriedade de corretude.

### 13.3 Caminho crítico, concorrência e paralelismo

O caminho crítico de uma operação é a cadeia de trabalhos dos quais depende a produção do próximo resultado necessário ou a liberação da próxima operação dependente.

Dois trabalhos são independentes entre si quando nenhum depende do resultado, efeito, estado intermediário ou ordem de execução do outro para preservar o comportamento definido, seus invariantes e seus contratos.

Trabalho que não seja necessário ao resultado ou à operação seguinte não deve permanecer artificialmente no caminho crítico quando puder ser adiado, executado incrementalmente, concorrentemente ou em paralelo com benefício relevante.

Trabalhos independentes devem utilizar execução concorrente ou paralela quando a plataforma permitir, houver ganho relevante conforme as metas e limites definidos em `regrasProjeto.md` e puderem ser preservados:

- corretude;
- segurança;
- integridade e consistência;
- invariantes;
- contratos;
- ordem realmente necessária;
- limites de recursos;
- limites de serviços externos.

Dependências reais e requisitos de ordenação devem permanecer explícitos. Trabalho com estado mutável compartilhado, efeitos concorrentes ou recursos contenciosos somente pode avançar concorrentemente quando sua coordenação preservar o comportamento definido.

Concorrência ou paralelismo não devem ser introduzidos quando custo de coordenação, sincronização, contenção, criação de tarefas, comunicação, consumo adicional de recursos, complexidade ou risco superar o benefício esperado.

Paralelização não substitui a eliminação de trabalho redundante nem a escolha de complexidade computacional proporcional.

### 13.4 Medição de desempenho

Toda decisão justificada por desempenho, toda declaração de ganho e toda meta de desempenho devem ser demonstradas por medição reproduzível.

Isso inclui, quando aplicável:

- necessidade de otimização;
- reutilização de resultados, cache ou memoização;
- concorrência ou paralelismo;
- impacto de dependências;
- metas e limites definidos em `regrasProjeto.md`.

A medição deve declarar:

- cenário;
- volume de dados representativo dos limites definidos em `regrasProjeto.md`;
- ambiente;
- quantidade de repetições suficiente para distinguir o efeito da variação.

Um ganho somente pode ser declarado pela comparação entre medições anterior e posterior à alteração, no mesmo cenário e ambiente.

As metas de desempenho do projeto devem possuir verificação automatizada quando viável.

Regressão além da tolerância definida em `regrasProjeto.md` impede a conclusão da alteração.

A complexidade computacional declarada pode ser demonstrada por análise, sem prejuízo da medição exigida para metas e ganhos.

### 13.5 Ciclo de vida de recursos

Todo recurso adquirido, como memória retida, conexão, arquivo, handle, listener, assinatura, timer, worker ou bloqueio, deve possuir responsável definido e ser liberado ao fim do ciclo de vida que justificou sua aquisição, inclusive nos caminhos de erro, cancelamento e abandono.

A liberação constitui efeito das transições de saída ou de encerramento correspondentes no grafo comportamental.

As evidências devem demonstrar que a execução repetida de um fluxo não acumula recursos além do estado anterior à sua execução.

### 13.6 Volumes sem limite

Toda operação cujo custo cresça com dimensão de dados sem limite garantido por contrato, tipo ou invariante deve possuir limite explícito, como paginação, processamento em lotes, fluxo contínuo, tamanho máximo ou limite de tempo.

Toda entrada externa deve possuir limite de tamanho verificado na fronteira de entrada antes do processamento.

Os limites concretos pertencem ao `regrasProjeto.md`.

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

Esta é a definição canônica de compartilhamento para qualquer nó, inclusive componentes de interface. `regrasUxUi.md` especializa somente suas consequências perceptíveis.

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
- delegar etapas que possuam responsabilidade própria conforme os critérios de modularização das Partes II e III;
- evitar aninhamento excessivo;
- tratar erros na fronteira adequada.

Uma função coordenadora pode representar fluxo composto, desde que delegue as etapas que possuam responsabilidade própria conforme os mesmos critérios de modularização.

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

A ordem pode ser adaptada à tecnologia, mas deve permanecer consistente no projeto e ser registrada em `regrasProjeto.md`.

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

Quando a linguagem ou o ecossistema não possuírem convenção consolidada:

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

Quando prevalecer, a convenção tecnológica especializa somente a forma, os nomes exigidos, os mecanismos de descoberta, a integração ou a interoperabilidade necessários ao ecossistema. Ela não pode reduzir semântica, responsabilidade, corretude, segurança, contratos ou comportamento exigidos por estas regras.

Não aplicar convenção apenas por hábito quando ela prejudicar a semântica.

## 42. Tipagem

- Contratos públicos devem possuir tipos explícitos.
- Dados que precisem de validação devem utilizar tipos que exijam verificação antes do uso, e não tipos que desativem a verificação, como `unknown` em vez de `any` em TypeScript.
- Evitar casts para silenciar erros.
- Dados externos devem ser validados em runtime quando necessário.
- Tipos devem impedir estados inválidos quando viável.
- Tipos locais permanecem próximos ao uso.
- Tipos compartilhados representam contratos realmente compartilhados.

### 42.1 Coerência semântica de validações

Uma mesma restrição de domínio, contrato ou regra de negócio validada em múltiplas fronteiras deve preservar o mesmo significado semântico em todas elas.

Validação antecipada em cliente, transporte, adaptador ou outra fronteira pode melhorar feedback ou rejeitar entradas inválidas mais cedo, mas não substitui a validação autoritativa na fronteira responsável pela regra.

Fronteiras diferentes não podem aceitar e rejeitar estados semanticamente contraditórios para a mesma regra. Diferenças de formato, normalização, mensagem ou mecanismo são permitidas quando preservarem o mesmo conjunto semântico de estados válidos e inválidos.

Quando fronteiras validarem responsabilidades diferentes, essa diferença deve ser explícita e não pode ser apresentada como se representasse a mesma regra.

A regra autoritativa deve permanecer localizável no domínio, contrato ou fronteira responsável, e representações derivadas devem acompanhar suas alterações.

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

Esta é a definição canônica de preservação da semântica nativa. `regrasUxUi.md` especializa somente suas consequências perceptíveis e interativas.

## 45. Comentários e documentação

- Comentários explicam intenção, restrição, decisão ou motivo não evidente.
- Não comentar linha a linha comportamento já claro.
- Comentários devem permanecer sincronizados.
- Código desativado não deve permanecer comentado.
- Documentação afetada deve ser atualizada junto com o código e removida quando perder seu objeto.
- Evidências temporárias devem permanecer em logs ou artefatos apropriados.

---

# Parte VII — Dependências, configuração, erros, segurança, persistência e integrações

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

- Configurações variáveis devem possuir fonte canônica e mecanismo coerente de acesso e validação. Centralização semântica não exige concentração física em um único arquivo quando a modularização exigir distribuição por contexto.
- Valores de ambiente devem ser validados na inicialização.
- Configurações obrigatórias ausentes devem produzir erro claro.
- Segredos nunca devem ser versionados.
- Valores específicos de ambiente não pertencem à regra de negócio.

## 49. Erros

Para esta seção:

- erro esperado é uma falha prevista pelo contrato, pelo modelo comportamental ou pela regra da operação;
- falha inesperada é uma falha não prevista para aquela operação e que, por isso, exige preservação de contexto para diagnóstico e eventual atualização do modelo ou da implementação.

- Erros não devem ser ignorados silenciosamente.
- Erros esperados devem possuir representação previsível.
- Falhas inesperadas devem preservar contexto para diagnóstico.
- Mensagens externas não devem expor detalhes internos.
- Recuperação automática só deve ocorrer quando for segura.
- A taxonomia interna de erros deve ser definida antes da conversão para transporte, interface, logs ou métricas.

### 49.1 Semântica do erro e estado da operação

Erro interno, classificação semântica e estado resultante da operação são conceitos relacionados, mas não equivalentes.

Para cada falha relevante, a fronteira responsável deve preservar informação suficiente para determinar, quando aplicável:

- qual intenção ou operação falhou;
- se seus efeitos principais não ocorreram, ocorreram parcialmente, foram concluídos ou permaneceram indeterminados;
- quais efeitos secundários, sincronizações ou comunicações falharam depois de um efeito principal já válido;
- se a repetição é segura;
- quais formas de recuperação permanecem válidas.

A conversão para transporte, interface, logs ou métricas deve preservar a semântica necessária ao consumidor sem expor detalhes internos desnecessários.

Falhas ocorridas depois de uma mutação concluída não podem ser representadas como se a mutação necessariamente não tivesse ocorrido.

Quando o resultado permanecer indeterminado, o sistema deve tratá-lo explicitamente como indeterminado e não presumir sucesso nem ausência de efeito.

### 49.2 Cancelamento, reversão e compensação

Cancelamento, reversão, compensação e repetição representam contratos distintos e não podem ser tratados como equivalentes por conveniência de implementação ou apresentação.

Uma operação somente pode expor promessa de cancelar ou desfazer quando possuir semântica técnica capaz de produzir o efeito prometido sem violar invariantes, integridade, segurança ou contratos externos.

Deve ser distinguido, quando aplicável:

- impedir que uma operação ainda não efetivada continue;
- interromper processamento futuro sem desfazer efeitos já produzidos;
- reverter diretamente efeitos produzidos;
- restaurar versão ou estado anterior válido;
- executar operação compensatória que produza resultado semanticamente equivalente ao desfazer permitido.

Quando uma operação for apenas parcialmente reversível, possuir efeitos externos irrevogáveis ou exigir compensação com resultado diferente da restauração exata, essas limitações devem permanecer explícitas no contrato.

Uma camada externa, inclusive interface, não pode prometer cancelamento, desfazer ou recuperação mais forte do que a operação subjacente consegue garantir.

## 50. Segurança

- Toda entrada externa é não confiável.
- Validação, autenticação e autorização devem ocorrer na fronteira adequada.
- Aplicar menor privilégio.
- Dados sensíveis devem ser protegidos em armazenamento, transporte e logs.
- Não confiar no cliente para decisões de segurança.
- Requisitos de segurança e privacidade devem anteceder decisões sobre logs, persistência e preenchimento automático.

A classificação dos dados sensíveis, suas formas de proteção, a gestão de segredos, a retenção de dados e as exigências legais aplicáveis pertencem ao `regrasProjeto.md`.

### 50.1 Autoridade de autorização

Autorização deve ser decidida e aplicada na fronteira que protege a operação ou o recurso correspondente.

Estado visual, ocultação, desabilitação, roteamento de cliente ou qualquer outra restrição de interface não constitui mecanismo autoritativo de autorização.

A interface pode refletir permissões conhecidas para evitar apresentar ações indevidamente disponíveis, mas essa representação não concede, revoga nem substitui a autorização técnica.

Toda operação protegida deve validar a autorização aplicável independentemente da forma como foi alcançada, inclusive por chamada direta, cliente alternativo, automação ou fluxo não visual.

Mudanças de permissão devem produzir comportamento compatível com o estado autoritativo vigente, sem depender de estado de interface previamente calculado como fonte de segurança.

## 51. Observabilidade

- Logs devem possuir contexto suficiente.
- Não registrar segredos ou dados sensíveis sem necessidade explícita.
- Mensagens devem ser consistentes e acionáveis.
- Métricas e rastreamento devem existir quando houver necessidade operacional real.

## 52. Integridade e persistência

Invariantes de dados devem ser protegidos na fronteira responsável pela persistência, independentemente do caminho de escrita.

Um conjunto de escritas que represente um único efeito de domínio deve ser atômico ou possuir compensação explícita conforme 49.2. Estado parcial não pode tornar-se observável como estado válido sem estar catalogado no grafo comportamental.

Toda alteração na estrutura dos dados persistidos deve ocorrer por migração versionada e reproduzível.

Toda correção de dados persistidos deve ocorrer por mecanismo versionado e reproduzível.

Uma migração deve preservar compatibilidade com todas as versões da aplicação que possam operar sobre os mesmos dados durante a implantação. Uma alteração incompatível deve ser decomposta em etapas sucessivas compatíveis.

Uma migração deve ser reversível ou declarada irreversível antes da aplicação, com a perda de dados explicitada.

Uma migração deve ser validada sobre dados representativos dos estados existentes, incluindo limites, antes de ser aplicada a dados reais.

Dados que não possam ser reconstruídos devem possuir backup. Backup cuja restauração não tenha sido verificada não constitui proteção.

Estratégias, ferramentas, periodicidade e valores concretos pertencem ao `regrasProjeto.md`.

## 53. Integrações externas

Toda integração deve ser acessada por adaptador com contrato interno. Tipos, formatos e erros externos não devem ultrapassar o adaptador.

Dados externos devem ser validados e normalizados na fronteira do adaptador.

Toda chamada externa deve possuir limite de tempo. Espera indefinida é proibida.

Falha, limite de tempo atingido e resposta inválida são erros esperados e devem possuir estado de operação definido conforme 49.1. Limite de tempo atingido depois do envio da requisição constitui resultado indeterminado.

Repetição somente pode ocorrer quando for segura conforme 49.1, com limite de tentativas e intervalo que não agrave a sobrecarga do serviço.

Alternativa em caso de falha somente é válida quando for semanticamente equivalente ou comunicada como estado degradado. Ela não pode simular sucesso.

As evidências devem reproduzir falha, atraso, limite de tempo atingido e resposta inválida do serviço. A compatibilidade do contrato interno com o serviço real deve ser verificada quando viável.

Limites de tempo, tentativas, intervalos, alternativas e limites de uso concretos pertencem ao `regrasProjeto.md`.

---

# Parte VIII — Regras de front-end

## 54. Organização do front-end

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

## 55. Normalização global de estilos

Todo front-end cuja plataforma aplique estilos padrão divergentes entre os ambientes suportados deve possuir base global de estilos carregada na inicialização para neutralizar diferenças desnecessárias entre esses ambientes.

A base global deve garantir, no mínimo:

- modelo de dimensionamento uniforme e previsível para todos os elementos;
- ausência de espaçamentos padrão não intencionais.

Exemplo em front-end web com CSS:

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

## 56. Responsabilidades estruturais e visuais

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

## 57. Componentes

- Componentes específicos permanecem próximos à página ou funcionalidade.
- Mover para compartilhado somente com equivalência semântica e contrato estável.
- Não manter árvores concorrentes como `src/components` e `src/shared/components` quando representarem a mesma responsabilidade.

## 58. Páginas e telas

Páginas e telas coordenam interface e fluxos de alto nível.

Não devem concentrar:

- transformações complexas;
- geração de arquivos;
- regras de negócio independentes;
- persistência;
- integrações detalhadas.

Para esta regra, transformação complexa ou integração detalhada é aquela que possui responsabilidade, contrato, dependência, teste ou ciclo de mudança próprios segundo os critérios de modularização deste documento. Tamanho físico, quantidade de linhas ou quantidade de chamadas não constituem critério isolado.

## 59. Fonte canônica de estados semânticos

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

## 60. Condições no nível responsável

Toda condição deve ser representada no menor nível com responsabilidade e informação suficientes.

- condições de negócio pertencem ao domínio ou caso de uso;
- condições derivadas de dados pertencem à transformação ou contrato responsável;
- estados funcionais pertencem ao componente ou módulo controlador;
- condições exclusivamente apresentacionais pertencem à camada visual;
- características do ambiente pertencem aos mecanismos da plataforma.

Condições apresentacionais não devem introduzir estado de aplicação, eventos, listeners ou processamento de runtime quando o mecanismo visual for suficiente.

A camada visual não deve reconstruir decisões de negócio a partir de sinais indiretos de apresentação.

## 61. Contratos de variantes

Esta é a definição canônica de contratos de variantes. `regrasUxUi.md` especializa somente suas consequências perceptíveis.

Parâmetros de componentes devem representar conceitos coerentes, como:

- tamanho;
- densidade;
- ênfase ou prioridade;
- intenção;
- orientação;
- estado;
- comportamento;
- contexto de uso.

Cada variante deve possuir finalidade clara e nome semântico. A quantidade de variantes deve permanecer previsível.

Parâmetros públicos não devem transportar detalhes visuais arbitrários, como margens, paddings, cores e posicionamentos.

Detalhes concretos de apresentação permanecem na camada visual ou no sistema de estilos.

Uma exceção exige que o valor seja parte real e estável do contrato público.

## 62. Estado local e compartilhado

- Estado local permanece próximo ao consumidor.
- Promover para store, contexto ou equivalente somente com múltiplos consumidores, sobrevivência necessária ou atualização coordenada.
- Dados derivados devem ser calculados a partir da fonte canônica quando possível.
- A localização técnica do estado não pode reduzir o ciclo de vida exigido pelo comportamento que ele representa.
- Quando a sobrevivência além do consumidor atual fizer parte do comportamento, o estado deve permanecer no menor escopo capaz de preservá-la corretamente.

## 63. Engines e templates

Transformações complexas, cálculos, serialização e geração de arquivos permanecem fora de componentes visuais quando possuírem responsabilidade própria.

Preview e exportação não devem depender de fontes de verdade divergentes.

## 64. Assets

Assets devem ser organizados por finalidade ou domínio.

Não criar subdiretório por asset isolado sem fronteira real.

---

# Parte IX — Regras de back-end

## 65. Organização do back-end

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

## 66. Domínio antes da categoria técnica

Evitar diretórios globais como `controllers`, `services`, `repositories` e `models` quando dispersarem uma funcionalidade por toda a árvore.

Preferir proximidade dos elementos do mesmo domínio.

## 67. Camadas proporcionais

Não criar controller, service, use case, repository, gateway e adapter para todo fluxo automaticamente.

Cada camada deve possuir responsabilidade real.

Camadas que apenas encaminham argumentos devem ser removidas ou incorporadas.

---

# Parte X — Testes e validação

## 68. Grafo comportamental e casos de uso

A estratégia de testes deve mapear dois modelos complementares:

- o grafo de casos de uso, que representa objetivos, casos de uso, conexões e fluxos funcionais relevantes;
- o grafo comportamental, que representa estados semanticamente distintos, transições, precondições, efeitos, invariantes, falhas, recuperação e encerramento.

O grafo comportamental deve abranger todo o comportamento do projeto em uso, sem exceção de escopo.

Os dois modelos devem ser registrados em `modelo-comportamental.md`, derivado do template mantido no repositório `base`. A estrutura do template constitui o conteúdo mínimo obrigatório, e deve existir rastreabilidade explícita entre os casos de uso e os estados, transições ou caminhos comportamentais que os realizam.

Abreviações utilizadas no modelo devem constar de seu glossário.

O mecanismo que demonstra a correspondência entre o modelo e a implementação pertence ao `regrasProjeto.md`.

Em conjunto, os modelos devem representar, conforme aplicável:

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

### 68.1 Modelo comportamental

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

### 68.2 Estados semanticamente distintos

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

### 68.3 Estados de encerramento

Estados que representem encerramento de fluxo devem declarar explicitamente quais transições de saída, se houver, permanecem permitidas.

Não devem existir transições implícitas a partir de estado de encerramento.

Quando o encerramento for definitivo no fluxo correspondente, nenhuma transição de saída deve ser permitida.

### 68.4 Completude do grafo comportamental

O grafo comportamental somente pode ser declarado completo quando todos os estados semanticamente possíveis e alcançáveis no projeto e todas as transições válidas entre eles estiverem catalogados.

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

Transições proibidas não integram o conjunto de transições válidas. Quando uma tentativa de transição proibida puder ocorrer por entrada externa, chamada direta, concorrência, sequência de uso ou outro caminho tecnicamente possível, a proibição deve permanecer explicitamente representada por precondição, invariante, contrato ou restrição do modelo e possuir evidência de rejeição ou prevenção correspondente.

Um estado semanticamente inválido ou inalcançável por construção não precisa integrar o conjunto de estados alcançáveis quando sua impossibilidade decorrer de invariante, tipo, contrato, precondição ou outra restrição verificável. A justificativa de inalcançabilidade deve ser localizável quando necessária para demonstrar a completude do modelo.

Estado ou transição cuja existência permaneça desconhecida, indefinida ou apenas presumida impede declarar o grafo completo.

### 68.5 Conformidade entre modelo e implementação

A implementação não pode produzir estado semanticamente alcançável ausente do grafo comportamental nem permitir transição alcançável não catalogada.

Uma transição semântica não precisa corresponder a exatamente uma função, método, handler ou chamada técnica. Ela pode ser implementada por múltiplos elementos técnicos, e um mesmo elemento técnico pode participar de múltiplas transições, desde que a relação permaneça explícita e rastreável.

Todo caminho técnico capaz de realizar uma transição semanticamente relevante deve estar associado à transição catalogada correspondente. Essa associação pode ser direta ou composta, mas não pode depender de inferência que impeça localizar como o comportamento modelado é realizado.

Quando a análise, execução ou teste revelar estado ou transição alcançável ausente do modelo:

1. o grafo deve ser atualizado para representar o comportamento válido, quando esse comportamento for intencional; ou
2. a implementação deve ser corrigida, quando o comportamento não for válido.

Enquanto a divergência existir, o comportamento afetado não pode ser considerado conforme.

### 68.6 Completude e cobertura

Completude do grafo e cobertura do grafo são critérios independentes e cumulativos.

- completude demonstra que o modelo contém todos os estados e transições semanticamente possíveis e alcançáveis no projeto;
- cobertura demonstra que os elementos aplicáveis do modelo possuem tratamento e evidência de validação adequados.

Todo estado catalogado no grafo deve possuir tratamento compatível com seu papel no modelo e pelo menos uma evidência de validação que demonstre os comportamentos, restrições ou invariantes que o distinguem semanticamente. Essa evidência pode ser compartilhada com evidências de transições de entrada, permanência ou saída quando a relação permanecer explícita.

Toda transição catalogada deve possuir tratamento explícito na implementação ou na fronteira responsável e pelo menos uma evidência de validação correspondente.

Cobertura comportamental completa não pode ser declarada enquanto existir estado catalogado ou transição catalogada sem tratamento definido, sem evidência correspondente ou sem rastreabilidade suficiente para localizar essa evidência.

Cobertura comportamental completa não pode ser declarada para grafo cuja completude não tenha sido estabelecida.

Cobertura comportamental completa não pode ser declarada sem sensibilidade das evidências demonstrada conforme 68.11.

O grafo deve estar formalizado e sua completude deve ser estabelecida antes de declarar cobertura comportamental completa.

### 68.7 Transições isoladas e sequências comportamentais

Cada transição catalogada deve ser validada isoladamente a partir de precondições conhecidas.

Transições também devem ser validadas em sequência quando a execução anterior puder alterar o resultado, as precondições, os efeitos, os invariantes, o estado de origem, o estado de destino ou qualquer propriedade compartilhada da execução seguinte.

Quando duas transições A e B compartilharem estado de origem ou destino, atuarem sobre propriedades comuns ou possuírem possibilidade real de dependência, interferência, reentrada ou efeito residual, devem ser consideradas, quando semanticamente possíveis:

- A → B;
- B → A;
- A → A;
- B → B.

A matriz não exige combinações sem significado no domínio nem enumeração individual de transições cuja independência tenha sido demonstrada de forma verificável.

Sequências adicionais devem ser incluídas quando forem necessárias para representar ciclos, retornos, recuperação, repetição ou outros caminhos relevantes do grafo.

Validar apenas o estado final não substitui validar os efeitos e invariantes relevantes ao longo da sequência.

### 68.8 Rastreabilidade entre modelo e validação

Cada transição catalogada deve apontar para pelo menos uma evidência de validação que demonstre seu comportamento esperado.

Quando a cobertura depender de sequência de transições, a evidência deve identificar explicitamente a sequência ou o caminho do grafo que valida.

Testes ou outras evidências permanentes de comportamento devem identificar os estados, transições ou sequências que protegem de forma suficiente para permitir rastreamento bidirecional entre modelo e validação.

Uma mesma evidência pode validar múltiplos elementos do grafo e um mesmo elemento pode exigir múltiplas evidências, desde que a relação permaneça explícita.

Não pode existir transição catalogada sem evidência localizável nem evidência declarada como cobertura comportamental sem vínculo identificável com o comportamento protegido.

### 68.9 Operações assíncronas, concorrência e respostas obsoletas

Quando operações assíncronas, concorrentes ou sobrepostas puderem afetar o mesmo comportamento, o modelo deve definir a validade dos resultados e as relações de ordem que forem semanticamente relevantes.

Um resultado é obsoleto quando foi produzido para contexto, precondições, versão ou intenção já superados por estado ou operação posterior relevante.

Resultado obsoleto não pode sobrescrever silenciosamente estado válido mais recente. Ele deve ser descartado, reconciliado ou tratado por regra explícita compatível com o comportamento definido.

A validação deve cobrir, quando aplicável:

- sucesso;
- falha antes da produção de efeitos;
- repetição após falha recuperável;
- atraso relevante;
- conclusões fora da ordem de início;
- repetição rápida;
- invocações concorrentes ou sobrepostas;
- cancelamento ou abandono;
- mutação principal concluída seguida de falha em sincronização, comunicação ou efeito secundário;
- resultado cuja conclusão permaneça indeterminada.

Em cada cenário aplicável, devem ser verificados o estado resultante, os efeitos produzidos ou preservados, a validade de resultados tardios e a segurança de eventual repetição.

Não é necessário criar cenários assíncronos artificiais quando a operação não admitir assincronicidade, concorrência, repetição ou ordenação relevante.

### 68.10 Execução única da intenção de domínio

Um mesmo evento lógico, sinal externo ou causa catalogada que represente uma única intenção de domínio deve produzir no máximo uma execução dessa mesma intenção.

A intenção não pode ser executada novamente pelo mesmo evento por duplicação acidental de handlers, listeners, callbacks, propagação, composição de caminhos equivalentes ou reentrada técnica.

Essa regra não limita a quantidade de mutações, chamadas ou efeitos internos necessários para concluir uma única intenção de domínio; ela impede apenas a duplicação não deliberada da própria intenção e de seus efeitos de domínio.

Repetição técnica de transporte, infraestrutura ou integração somente pode ocorrer quando preservar a semântica da intenção e não duplicar efeitos de domínio indevidamente.

Quando o domínio permitir repetição deliberada da mesma intenção, cada nova execução deve corresponder a novo evento semanticamente válido ou utilizar contrato de repetição seguro, como idempotência quando aplicável.

A validação deve demonstrar que um único evento não provoca duplicação da intenção nem de efeitos que deveriam ocorrer uma única vez.

### 68.11 Sensibilidade das evidências e testes de mutação

Uma evidência somente protege um elemento do grafo comportamental quando falha na ausência ou na violação do tratamento correspondente.

Evidência que permanece aprovada após remoção ou violação do tratamento de um estado, transição, precondição, invariante ou efeito não constitui cobertura desse elemento.

A sensibilidade das evidências deve ser demonstrada por teste de mutação sobre todo código associado ao grafo comportamental conforme 68.5.

Quando não existir ferramenta de teste de mutação viável para a tecnologia utilizada, a indisponibilidade deve ser registrada em `regrasProjeto.md`, e a sensibilidade deve ser demonstrada pela falha observada de cada evidência antes da implementação do tratamento correspondente.

Para esta seção:

- mutante é uma versão do código com alteração deliberada capaz de violar comportamento;
- mutante morto é aquele que provoca falha de pelo menos uma evidência;
- mutante sobrevivente é aquele que não provoca falha de nenhuma evidência;
- mutante equivalente é aquele cujo comportamento observável é idêntico ao do código original.

Os operadores de mutação devem incluir, além de alterações sintáticas, as mutações semânticas aplicáveis:

- remoção ou inversão de precondição;
- permissão de transição proibida;
- omissão de efeito;
- duplicação de efeito ou de intenção;
- alteração do estado de destino;
- omissão de invalidação, reinicialização ou descarte declarados;
- alteração de propriedade que a transição deve preservar;
- aceitação de resultado obsoleto;
- inversão de ordem exigida;
- omissão de liberação de recurso.

Todo mutante do escopo deve ser morto.

Mutante sobrevivente constitui divergência entre modelo, implementação e evidência, e deve ser resolvido conforme sua causa:

- evidência insuficiente: a evidência deve ser fortalecida;
- código redundante, sem efeito ou inalcançável: o código deve ser removido;
- código com responsabilidade não funcional, como reutilização de resultados, cache ou redução de custo: deve existir evidência da propriedade garantida por esse código, como quantidade de execuções, de chamadas ou consumo de recursos.

Somente mutante equivalente por equivalência exclusivamente sintática, em que a alteração produza forma alternativa de semântica idêntica, sem código redundante nem responsabilidade não funcional envolvidos, pode permanecer sobrevivente. Cada caso deve possuir justificativa verificável registrada em `modelo-comportamental.md`.

Enquanto existir mutante sobrevivente sem essa justificativa, os elementos afetados não podem ser considerados cobertos.

Resultados de mutação somente são válidos sobre evidências determinísticas. Evidência instável deve ser corrigida antes da avaliação de mutação.

## 69. Níveis de teste

A cobertura deve combinar, conforme necessidade real:

- testes unitários;
- testes de integração;
- testes de ponta a ponta.

Cada comportamento deve ser validado no nível mais adequado.

Uma categoria não deve ser exigida quando não agregar proteção, mas sua omissão deve registrar:

- qual proteção não agregaria;
- quais comportamentos permanecem cobertos;
- por quais níveis de teste.

## 70. Comportamento e permanência

- Testes verificam comportamento observável.
- Regras de negócio relevantes e estáveis devem possuir testes.
- Refatorações devem preservar contratos e comportamento.
- Testes quebrados não podem ser ignorados ou removidos para permitir integração.
- Cenários de erro e limite devem ser testados quando fizerem parte do comportamento.
- Transições catalogadas devem ser verificadas isoladamente e em sequências aplicáveis capazes de revelar dependência ou interferência de estado.
- Operações assíncronas e concorrentes devem ser verificadas nos cenários aplicáveis de ordem, atraso, repetição, falha e recuperação.
- Testes permanentes permanecem versionados.
- Testes temporários só podem ser removidos quando não protegerem comportamento permanente.

## 71. Automação e evidências

- Integração contínua deve executar validações aplicáveis quando utilizada.
- Validações essenciais devem possuir forma documentada de execução local ou equivalente.
- Ausência de execução ou resultado desconhecido não equivale a aprovação.
- Declarações de conformidade de commits seguem a seção de declaração de conformidade.
- Evidências utilizadas para cobertura comportamental devem manter rastreabilidade com os estados, transições ou sequências correspondentes.

### 71.1 Eficiência da execução das evidências

A capacidade de uma evidência de cumprir sua responsabilidade precede sua eficiência de execução. Evidência não otimizada que protege corretamente o comportamento é preferível a evidência otimizada que não o protege.

Nenhuma otimização pode ser adotada quando reduzir, ainda que parcialmente, cobertura comportamental, sensibilidade, determinismo, isolamento, rastreabilidade ou completude da seleção de evidências. Otimização que comprometa qualquer dessas propriedades não é aplicável, e sua não adoção está justificada por esta regra.

Respeitada essa precedência, a execução das evidências deve ser de máxima eficiência.

A execução é de máxima eficiência quando todas as otimizações desta seção aplicáveis à tecnologia estiverem adotadas, a complexidade de execução for a menor conhecida e o tempo medido estiver dentro dos limites definidos em `regrasProjeto.md`. Otimização aplicável não adotada exige justificativa verificável registrada em `regrasProjeto.md`.

São obrigatórias, quando aplicáveis:

- independência de cada evidência em relação à ordem de execução e às demais evidências, admitindo estado compartilhado somente quando imutável ou isolado por execução;
- execução concorrente ou paralela das evidências independentes;
- reutilização de preparação custosa somente quando não permitir vazamento de estado entre evidências;
- sincronização por evento, condição observável ou relógio controlado, sendo proibidas esperas fixas de tempo;
- no commit de conclusão, seleção das evidências pelo impacto da alteração, derivada da rastreabilidade entre código, grafo e evidências, com completude demonstrada; na dúvida, a evidência deve ser incluída;
- na mutação, mutar somente o código do escopo afetado, executar para cada mutante somente as evidências que cobrem o código mutado, encerrar a avaliação do mutante na primeira falha, executar mutantes em paralelo e reutilizar resultados de código e evidências não alterados;
- entre níveis de teste que ofereçam proteção equivalente, o de menor custo de execução.

A otimização da execução de evidências constitui alteração em evidências e deve demonstrar a preservação da cobertura, do resultado de mutação e do determinismo existentes antes da otimização.

Uma evidência é redundante quando outra evidência do mesmo nível protege os mesmos elementos do grafo com sensibilidade igual ou superior, demonstrada pela ausência de mutantes mortos exclusivamente por ela. Evidências redundantes não possuem responsabilidade vigente.

O tempo de execução dos portões deve ser medido conforme 13.4. Regressão além da tolerância definida em `regrasProjeto.md` impede a conclusão da alteração.

---

# Parte XI — Versionamento e integração

## 72. Branches

- Projetos devem identificar a branch estável e a branch de integração, e as branches de trabalho quando existirem.
- A branch estável contém somente estados promovidos para uso em produção.
- Alterações não podem ser registradas diretamente na branch estável; elas chegam à branch estável somente por promoção.
- Nomes pertencem ao `regrasProjeto.md`.
- Atualizações forçadas devem ser evitadas e somente podem ocorrer com autorização explícita e sem perda de histórico relevante.

## 73. Commit de conclusão

Commit de conclusão é o commit que declara concluída uma alteração, como funcionalidade implementada, correção, refatoração ou sincronização com o repositório `base`.

Commits intermediários são permitidos somente fora da branch estável, não declaram conclusão e devem declarar as não conformidades conhecidas que contenham.

Um commit de conclusão somente pode ser realizado quando a alteração satisfizer todas as regras aplicáveis de `regrasDev.md`, `regrasUxUi.md` e `regrasProjeto.md`, conforme o commit do `base` adotado.

No escopo afetado pela alteração, devem estar demonstrados:

- a identificação das regras aplicáveis;
- a ausência de não conformidades conhecidas;
- a correspondência entre o diff e o escopo da alteração;
- o delta do grafo comportamental, compreendendo estados e transições criados, removidos, alterados ou afetados, inclusive sequências e cenários assíncronos que passem a ser relevantes;
- o grafo atualizado e conforme à implementação;
- o tratamento de todo estado e transição do delta;
- a cobertura comportamental conforme 68.6 a 68.8;
- a sensibilidade das evidências conforme 68.11;
- as medições exigidas por 13.4, quando a alteração afetar processo crítico ou meta de desempenho;
- a preservação de contratos e comportamentos protegidos;
- a atualização da documentação afetada;
- a ausência de resíduos, de implementações concorrentes e de elementos sem responsabilidade vigente;
- a eficiência da execução das evidências conforme 71.1, quando a alteração afetar evidências, fixtures ou automações de validação;
- a auditoria integral de conformidade atualizada conforme 76;
- a aprovação de build, testes e demais validações aplicáveis.

Alteração sem impacto comportamental deve declarar ausência de delta do grafo. A declaração é verificável pela preservação do grafo, das evidências e do resultado de mutação.

Alteração exclusivamente em evidências não pode reduzir cobertura nem tornar sobrevivente mutante anteriormente morto.

A verificação deve ser automatizada quando viável.

## 74. Promoção

Promoção é a integração da branch de integração na branch estável quando o conjunto acumulado estiver apto para uso em produção.

A promoção deve produzir commit próprio na branch estável, que registre sua declaração de conformidade. Integração que não produza commit próprio não constitui promoção válida.

Uma promoção somente pode ocorrer a partir de commit de conclusão e quando estiverem demonstrados, para o projeto inteiro:

- a completude do grafo comportamental;
- a cobertura comportamental completa;
- a sensibilidade das evidências por execução completa de mutação;
- a geração do artefato de produção;
- a aprovação dos testes de todos os níveis aplicáveis;
- o nível de validação de UX e UI exigido, quando aplicável;
- as metas de desempenho verificadas conforme 13.4;
- a atualização da documentação e do `README.md`;
- a eficiência da execução das evidências conforme 71.1;
- a auditoria integral de conformidade atualizada conforme 76;
- a ausência de alterações incompatíveis na branch estável;
- a ausência de não conformidades conhecidas.

## 75. Declaração de conformidade

Todo commit de conclusão e todo commit de promoção deve conter declaração de conformidade em sua mensagem.

A declaração é declarativa e não descreve procedimentos. Sua demonstração decorre da reprodutibilidade das evidências a partir do próprio commit.

Declaração do commit de conclusão:

```text
Conformidade: regras aplicáveis satisfeitas
Grafo: atualizado | sem delta
Mutação: escopo afetado, 0 sobreviventes
Base: <hash do commit do base adotado>
```

Declaração do commit de promoção:

```text
Promoção: validação integral satisfeita
Grafo: completo
Mutação: execução completa, 0 sobreviventes
Desempenho: metas verificadas
Base: <hash do commit do base adotado>
```

Commit intermediário que contenha não conformidade conhecida deve declará-la em sua mensagem, identificando documento, regra e escopo afetados:

```text
Não conformidades: regrasDev 68.11 (mutação em pedidos/cancelamento); regrasUxUi 91 (foco no diálogo)
```

Mutantes equivalentes por equivalência exclusivamente sintática e justificados conforme 68.11 não são contados como sobreviventes.

O commit do `base` declarado identifica a versão das regras contra a qual a conformidade foi avaliada. O último commit que o declare identifica a sincronização vigente do projeto.

## 76. Auditoria integral de conformidade

Todo projeto deve manter `auditoria-conformidade.md`, derivado do template mantido no repositório `base`.

A auditoria deve conter uma linha para cada seção e subseção numerada de `regrasDev.md`, de `regrasUxUi.md` e de `regrasProjeto.md` no commit do `base` adotado, identificada por número e título.

As linhas do template constituem o conteúdo mínimo obrigatório. Nenhuma linha pode ser removida, e divergência entre as linhas e as seções dos documentos adotados impede a conclusão da alteração.

Cada linha deve possuir um dos seguintes status:

- `Conforme`: a regra é satisfeita e sua evidência é localizável;
- `Exceção autorizada`: a regra é satisfeita por exceção registrada em `regrasProjeto.md`;
- `N/A`: a regra não se aplica ao projeto, com justificativa verificável;
- `Descritiva`: a seção não impõe obrigação;
- `Não conforme`: a regra é descumprida, permitido somente em commit intermediário.

O status `Descritiva` é atribuído exclusivamente pelo template e não pode ser atribuído pelo projeto.

Para seções de `regrasProjeto.md`, `Conforme` significa que os campos da seção estão preenchidos, ou declarados `Não se aplica.` com justificativa, e que a implementação corresponde às decisões registradas.

A evidência de cada linha deve permitir localizar a demonstração da regra específica. Evidências podem ser referenciadas por código de um catálogo. Quando o código for amplo, a linha deve complementá-lo com referência específica.

Cada entrada do catálogo deve declarar artefatos, tipo e forma de reprodução. O tipo é automatizada, inspeção ou ambos. A forma de reprodução é o comando exato ou, para inspeção, o critério verificado.

O estado auditado é o do commit que contém a auditoria. O cabeçalho deve declarar o commit do `base` adotado.

A conclusão deve declarar a quantidade de linhas por status, e essa contagem deve corresponder à matriz.

A completude da matriz, a correspondência entre números e títulos e a contagem da conclusão devem ser verificadas automaticamente.

A auditoria deve ser atualizada em todo commit de conclusão, na promoção e na sincronização com o repositório `base`.

No repositório `base`, toda alteração nas seções de `regrasDev.md`, `regrasUxUi.md` ou `regrasProjeto.md` deve atualizar as linhas do template de auditoria na mesma alteração.

## 77. Artefatos temporários

- Arquivos, scripts, workflows, branches, pacotes e fragmentos temporários devem possuir finalidade explícita.
- Não devem tornar-se dependências da arquitetura final.
- Automações com escrita devem possuir escopo mínimo e proteção contra ciclos.
- Resíduos temporários que não sejam necessários à própria validação final devem ser removidos antes dela. Artefatos temporários necessários à validação podem permanecer somente enquanto cumprirem essa finalidade e devem seguir a política de evidências aplicável.

---

# Parte XII — Refatoração e manutenção

## 78. Baseline obrigatória

Antes de normalização, migração ou refatoração estrutural, registrar baseline de:

- comportamento;
- contratos;
- formatos;
- resultados observáveis;
- casos de uso afetados.

## 79. Planejamento antes da migração

A árvore final planejada deve ser validada contra:

- responsabilidades;
- contratos;
- dependências;
- casos de uso;
- restrições do projeto.

Nenhuma migração estrutural deve começar sem plano completo.

Para esta regra, o plano está completo para um ramo quando todas as decisões aplicáveis desse ramo na seção de planejamento estrutural de `regrasProjeto.md` estiverem definidas. Decisões marcadas como `Pendente.` bloqueiam somente os ramos que dependem delas, conforme as regras de preenchimento de `regrasProjeto.md`.

## 80. Ordem da refatoração

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

## 81. Preservação de contratos observáveis

Mudanças estruturais devem preservar, salvo alteração funcional explícita:

- conteúdo observável ou contratualmente protegido registrado na baseline;
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

## 82. Migração e poda

Ao mover elemento:

1. confirmar que todo conteúdo necessário existe na estrutura final;
2. atualizar imports, exports, aliases e referências;
3. validar funcionamento;
4. remover versão anterior;
5. confirmar ausência de duplicações e caminhos obsoletos.

A reorganização só termina quando existir uma única árvore válida para cada responsabilidade.

---

# Parte XIII — Critério de conclusão

## 83. Regra de parada

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
