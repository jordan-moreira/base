# Regras de Desenvolvimento

## 1. Objetivo e aplicação

Este documento define os padrões permanentes de engenharia, organização, estruturação, modularização e qualidade aplicáveis a todos os projetos.

Todo projeto derivado deste repositório deve utilizar estas regras como base para organizar o código dentro dos arquivos e distribuir blocos lógicos, funções, arquivos, diretórios, módulos e domínios na árvore do projeto.

A estrutura concreta deve ser registrada em `regrasProjeto.md`, respeitando integralmente os critérios definidos neste documento.

As regras gerais aplicam-se a todo o código. As regras específicas de front-end e back-end complementam as regras gerais somente nos contextos correspondentes.

As decisões específicas de cada projeto, como stack, arquitetura adotada, estrutura concreta de diretórios, bibliotecas, integrações e restrições, devem ser registradas em `regrasProjeto.md`.

Em caso de conflito, aplicar a seguinte precedência:

1. exigências técnicas obrigatórias da linguagem, framework ou ferramenta;
2. `regrasProjeto.md`;
3. este documento;
4. convenções já consolidadas no projeto.

Exceções devem ser explícitas, justificadas e restritas ao menor escopo possível.

---

## 2. Princípios gerais

### 2.1 Clareza

- O código deve priorizar legibilidade, previsibilidade e manutenção.
- A solução mais simples que preserve corretude, segurança e capacidade de evolução deve ser preferida.
- Código explícito é preferível a comportamento implícito difícil de identificar.

### 2.2 Responsabilidade

- Cada nó estrutural deve possuir uma responsabilidade principal claramente identificável.
- Uma responsabilidade representa um motivo para mudança.
- Quando um nó tende a mudar por motivos distintos, ele deve ser avaliado para divisão.

### 2.3 Coesão

- Elementos que colaboram para resolver o mesmo problema devem permanecer próximos.
- Código não relacionado deve permanecer separado, mesmo quando possa tecnicamente compartilhar o mesmo nó.

### 2.4 Acoplamento

- Dependências entre nós devem ser explícitas e reduzidas ao necessário.
- Alterações internas de um nó não devem exigir mudanças indiscriminadas em outros nós.
- Um nó não deve depender de detalhes internos de outro nó fora de sua fronteira permitida.

### 2.5 Arquitetura proporcional

- A arquitetura deve crescer conforme a complexidade real do projeto.
- Projetos pequenos não devem reproduzir estruturas próprias de sistemas grandes sem necessidade.
- Projetos maiores não devem permanecer em estruturas simples quando isso comprometer manutenção, testes ou evolução.
- Nenhuma camada, abstração, arquivo ou diretório deve existir apenas para satisfazer um padrão teórico.

### 2.6 Proximidade

- Código específico deve permanecer próximo do domínio, funcionalidade, página, módulo, arquivo ou função que o utiliza.
- Código só deve ser promovido para áreas compartilhadas quando houver reutilização real, estável e semanticamente coerente.

### 2.7 Modelo universal da árvore do projeto

A estrutura completa de um projeto deve ser compreendida como uma única árvore semântica.

- A raiz é o diretório raiz do projeto.
- Os nós intermediários podem ser contextos, domínios, módulos, diretórios, arquivos, funções, métodos, componentes ou blocos lógicos.
- As folhas são os menores blocos lógicos indivisíveis do código.

Um bloco lógico é indivisível quando sua separação não produzir responsabilidades independentes e apenas aumentar a navegação, o acoplamento ou a dificuldade de entendimento.

A definição de folha não está limitada a arquivos ou funções. Ela representa o menor elemento lógico que ainda possui significado coeso dentro da implementação.

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

Nem todos os níveis precisam existir. Cada nível deve ser criado somente quando representar uma responsabilidade real.

### 2.8 Árvore mínima semanticamente suficiente

A estrutura deve utilizar o menor número possível de nós, folhas e níveis de profundidade capaz de preservar:

- separação clara de responsabilidades;
- localização intuitiva do código;
- coesão;
- isolamento entre domínios;
- manutenção independente;
- testabilidade;
- direção previsível das dependências.

A redução da quantidade de nós não deve resultar em responsabilidades misturadas, arquivos genéricos, funções extensas ou diretórios usados como depósitos.

A estrutura correta é a menor árvore semanticamente suficiente, e não simplesmente a árvore com menor quantidade absoluta de elementos.

### 2.9 Balanceamento recursivo

As mesmas regras de balanceamento devem ser aplicadas recursivamente da raiz do projeto até cada menor bloco lógico indivisível.

Todo nó deve ser avaliado considerando:

- a responsabilidade que representa;
- as responsabilidades de seus filhos;
- a quantidade de filhos;
- a facilidade de localizar e compreender cada filho;
- a profundidade necessária para alcançar suas folhas;
- o custo de navegação criado pela estrutura.

Um nó deve permanecer indiviso enquanto:

- representar adequadamente uma única responsabilidade;
- seus filhos forem semanticamente relacionados;
- a quantidade de filhos permitir localização e manutenção previsíveis;
- sua profundidade for proporcional à complexidade representada.

Um nó deve ser dividido ou seus filhos devem ser realocados quando:

1. seus filhos representarem responsabilidades diferentes que precisem ser isoladas;
2. a quantidade de filhos prejudicar localização, compreensão, manutenção ou evolução;
3. a responsabilidade do nó se tornar extensa a ponto de exigir sub-responsabilidades explícitas;
4. a divisão reduzir acoplamento ou permitir testes independentes;
5. a realocação reduzir profundidade desnecessária ou sobrecarga do nó atual.

A quantidade de filhos é um indicador, não um limite numérico absoluto. A divisão só deve ocorrer quando essa quantidade causar prejuízo semântico ou operacional.

### 2.10 Balanceamento horizontal e vertical

O balanceamento horizontal controla a quantidade e a relação semântica dos filhos de cada nó.

O balanceamento vertical controla a profundidade entre a raiz e as folhas.

A árvore está adequadamente balanceada quando:

- cada nó possui filhos semanticamente relacionados;
- nós sobrecarregados são subdivididos apenas quando existem grupos reais;
- não existem níveis intermediários sem responsabilidade própria;
- não existem cadeias de nós com filho único sem justificativa;
- a profundidade é proporcional à complexidade;
- a largura não impede localização direta;
- nenhuma divisão existe apenas por simetria visual.

### 2.11 Modularização de dentro para fora

Toda modularização deve começar no menor nível aplicável e avançar progressivamente para níveis superiores.

A ordem obrigatória de avaliação é:

1. blocos lógicos internos;
2. funções, métodos ou componentes;
3. arquivos;
4. diretórios;
5. módulos;
6. domínios ou contextos;
7. estrutura global do projeto.

Em cada nível:

1. organizar os elementos existentes;
2. avaliar responsabilidade, coesão, dependências e extensão;
3. manter no nível atual o que continuar semanticamente coeso;
4. separar ou promover apenas responsabilidades independentes;
5. reavaliar largura e profundidade após a alteração.

A arquitetura global deve emergir das responsabilidades reais do código organizado. Não deve ser imposta antecipadamente por meio de pastas, camadas ou módulos vazios.

---

## 3. Critérios universais de divisão e alocação

### 3.1 Regra de divisão de qualquer nó

Um nó deve ser dividido quando ocorrer pelo menos uma destas condições:

- contém responsabilidades diferentes;
- possui filhos com ciclos de mudança distintos;
- mistura fronteiras técnicas incompatíveis;
- sua responsabilidade única tornou-se extensa e possui sub-responsabilidades nomeáveis;
- a quantidade de filhos dificulta localização, leitura, testes ou manutenção;
- partes internas possuem dependências ou consumidores independentes;
- a divisão reduz acoplamento relevante;
- a divisão torna contratos ou limites mais claros.

O tamanho físico, isoladamente, não justifica divisão.

Quantidade de linhas, funções, arquivos ou diretórios deve ser tratada como sinal para análise, nunca como regra automática.

### 3.2 Regra de permanência no mesmo nó

Elementos devem permanecer no mesmo nó quando:

- participam do mesmo fluxo;
- possuem o mesmo motivo de mudança;
- utilizam as mesmas dependências;
- não possuem valor ou consumidores independentes;
- sua separação aumentaria apenas a navegação;
- o nó atual continua claro, coeso e previsível.

### 3.3 Regra de alocação

Cada elemento deve ser alocado no menor nó semanticamente correto capaz de representá-lo.

Ao dividir um nó:

- criar nós irmãos quando as responsabilidades estiverem no mesmo nível de abstração;
- criar subnós quando representarem partes internas de uma responsabilidade maior;
- realocar para outro ramo quando a responsabilidade pertencer a outro domínio ou contexto;
- criar área compartilhada somente quando houver consumidores reais em ramos distintos;
- preservar uma única localização canônica para cada responsabilidade.

A divisão não deve criar nós primos artificialmente apenas para distribuir visualmente a árvore.

### 3.4 Regra de parada

A modularização deve parar quando todos os nós avaliados:

- representarem responsabilidades claras;
- possuírem filhos semanticamente relacionados;
- apresentarem quantidade administrável de filhos;
- mantiverem profundidade proporcional;
- não exigirem conhecimento excessivo para localização;
- não puderem ser divididos sem criar fragmentação artificial.

### 3.5 Criar uma abstração

Criar uma abstração somente quando ela:

- eliminar repetição relevante;
- estabilizar um contrato;
- isolar uma dependência;
- representar conceito real do domínio;
- proteger uma fronteira;
- simplificar consumidores.

Não abstrair apenas para antecipar necessidades futuras.

### 3.6 Compartilhar código

Compartilhar somente quando os usos possuírem o mesmo significado e comportamento esperado.

Semelhança visual ou estrutural isolada não é suficiente para justificar compartilhamento.

### 3.7 Adicionar uma camada

Adicionar uma camada somente quando houver responsabilidade distinta, fronteira técnica ou regra de dependência que justifique sua existência.

Camadas que apenas repassam dados sem transformação, proteção, coordenação ou adaptação devem ser evitadas.

---

## 4. Organização e arquitetura

### 4.1 Organização obrigatória

- A estrutura deve ser organizada por responsabilidade, domínio ou funcionalidade, conforme a natureza do projeto.
- Cada nó deve possuir propósito claro e nome semanticamente coerente.
- A árvore deve permitir localizar um código sem conhecer previamente toda a implementação.
- Elementos relacionados devem permanecer próximos.
- Código compartilhado deve ser separado de código específico.
- Não manter duas árvores concorrentes para a mesma responsabilidade.
- Não preservar estruturas antigas após uma migração concluída.
- Dependências devem seguir direção previsível e evitar ciclos.
- Fronteiras entre módulos devem ser explícitas.

A estrutura concreta de cada projeto deve ser definida em `regrasProjeto.md`.

### 4.2 Modelo abstrato da estrutura

```text
projeto/
├── documentação e regras
├── configurações
├── scripts e automações
├── código-fonte/
│   ├── inicialização e composição
│   ├── domínios ou funcionalidades
│   │   └── módulo/
│   │       ├── interface ou apresentação
│   │       ├── aplicação ou coordenação
│   │       ├── domínio ou regras
│   │       ├── infraestrutura ou integrações
│   │       └── contratos e testes específicos
│   ├── compartilhado
│   └── infraestrutura global
├── recursos estáticos
└── testes externos, quando aplicável
```

Esse modelo é conceitual. Nenhum diretório ou camada é obrigatório sem responsabilidade real.

### 4.3 Profundidade controlada

A profundidade deve ser a menor possível sem comprometer a separação semântica.

Um novo nível só deve ser criado quando:

- representar responsabilidade própria;
- agrupar múltiplos elementos relacionados;
- separar conteúdo de natureza distinta;
- reduzir sobrecarga real no nível atual;
- tornar localização mais previsível.

Não criar níveis que:

- apenas repitam o nome do nível anterior;
- contenham um único filho sem justificativa;
- representem somente categoria técnica desnecessária;
- aumentem navegação sem melhorar entendimento.

### 4.4 Largura controlada

Não existe quantidade máxima fixa de filhos por nó.

Um nó deve ser avaliado para subdivisão quando:

- contém muitos elementos difíceis de localizar;
- utiliza prefixos repetidos para simular agrupamentos;
- mistura grupos semanticamente distintos;
- novos elementos não possuem posição previsível;
- sua manutenção exige busca frequente por conteúdo.

Não subdividir apenas para reduzir visualmente a quantidade de filhos.

### 4.5 Promoção progressiva

Todo conteúdo deve começar na estrutura mais simples semanticamente correta.

A promoção deve seguir, quando necessária:

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

### 4.6 Proximidade antes do compartilhamento

Todo código deve permanecer próximo do consumidor principal durante sua criação inicial.

Mover para área compartilhada somente quando:

- existirem consumidores reais em mais de um módulo;
- o significado for igual em todos os usos;
- o comportamento for estável;
- o código não depender de detalhes internos de um módulo específico.

### 4.7 Diretórios genéricos

Diretórios como `components`, `utils`, `services`, `helpers`, `common`, `shared`, `types` e `hooks` devem possuir escopo claro.

Não devem ser usados como depósitos de elementos classificados apenas pelo tipo técnico.

### 4.8 Reorganizações

Quando um elemento for movido:

1. confirmar que todo conteúdo necessário existe na estrutura final;
2. atualizar imports, referências e contratos;
3. validar o funcionamento;
4. remover a versão anterior;
5. confirmar que não restaram duplicações ou caminhos obsoletos.

A reorganização só estará concluída quando existir uma única árvore válida para cada responsabilidade.

---

## 5. Modularização do código

### 5.1 Blocos lógicos indivisíveis

O menor bloco lógico indivisível deve:

- executar uma parte coesa do fluxo;
- possuir propósito identificável;
- não misturar responsabilidades independentes;
- permanecer próximo do contexto que lhe dá significado;
- não ser separado quando a extração apenas aumentar navegação.

Um bloco deixa de ser indivisível quando contém partes com responsabilidades, dependências, ciclos de mudança ou possibilidades de teste independentes.

### 5.2 Funções, métodos e componentes

Cada função, método ou componente deve:

- executar uma responsabilidade principal;
- possuir nome que descreva sua intenção;
- receber apenas os dados necessários;
- tornar efeitos externos explícitos;
- retornar resultado previsível;
- evitar misturar validação, transformação, persistência e apresentação;
- delegar etapas independentes;
- evitar aninhamento excessivo;
- tratar erros na fronteira adequada.

Uma função coordenadora pode representar um fluxo composto, desde que delegue etapas independentes para filhos semanticamente claros.

### 5.3 Arquivos

Cada arquivo deve possuir responsabilidade principal identificável pelo nome e pela posição na árvore.

Criar novo arquivo quando o conteúdo:

- representar conceito próprio;
- possuir motivo de mudança diferente;
- depender de recursos distintos;
- puder ser testado isoladamente;
- possuir reutilização real;
- implementar fronteira ou contrato;
- comprometer a coesão do arquivo atual.

Não criar arquivo apenas para:

- reduzir quantidade de linhas;
- armazenar constante local sem contexto próprio;
- separar função privada inseparável do fluxo;
- criar wrapper sem responsabilidade;
- antecipar reutilização inexistente;
- reproduzir convenção de outro projeto.

### 5.4 Diretórios

Criar diretório somente quando houver conjunto de arquivos ou subdiretórios que:

- represente responsabilidade semanticamente identificável;
- possua relação coesa;
- forme domínio, funcionalidade ou fronteira;
- torne o diretório pai sobrecarregado;
- precise ser localizado como grupo.

Diretório com único filho exige justificativa arquitetural ou técnica explícita.

### 5.5 Módulos e domínios

Criar módulo quando um conjunto possuir:

- responsabilidade funcional ou de negócio própria;
- contratos próprios;
- dependências próprias;
- ciclo de vida relativamente independente;
- fronteira clara com o restante do sistema.

Módulos devem expor interface pública e não permitir acesso indiscriminado a detalhes internos.

### 5.6 Modularização interna de arquivos

Quando aplicável, utilizar ordem previsível:

1. imports;
2. tipos e contratos locais;
3. constantes locais;
4. validações;
5. funções auxiliares privadas;
6. implementação principal;
7. composição ou coordenação;
8. exports.

Essa ordem pode ser adaptada à tecnologia, mas deve permanecer consistente no projeto.

### 5.7 Duplicação

- Duplicação ocasional e pequena pode ser preferível a abstração incorreta.
- Extrair quando a repetição representar o mesmo conceito e possuir manutenção conjunta.
- Não unificar comportamentos que apenas parecem semelhantes.

---

## 6. Nomenclatura, tipagem e contratos

### 6.1 Nomenclatura semântica

Códigos, blocos, funções, variáveis, arquivos, diretórios, módulos e domínios devem possuir nomes semânticos, sugestivos e coerentes com a responsabilidade representada.

O nome deve permitir inferir a finalidade sem abrir o elemento ou conhecer previamente sua implementação.

- Usar `camelCase` para variáveis, funções, métodos e propriedades.
- Usar `PascalCase` para componentes, classes, tipos, interfaces e enums.
- Usar `UPPER_SNAKE_CASE` apenas para constantes globais convencionais.
- Funções devem indicar ação.
- Booleanos devem indicar condição, preferencialmente com `is`, `has`, `can` ou `should`.
- Coleções devem usar nomes no plural.
- Evitar abreviações não consolidadas e nomes ambíguos.
- Evitar repetir no nome do filho o contexto já expresso pelo nó pai.
- Evitar nomes genéricos quando houver alternativa mais específica.

### 6.2 Convenções de nomenclatura

Uma convenção pode prevalecer sobre o nome semanticamente ideal quando:

- for obrigatória para a linguagem, framework ou ferramenta;
- permitir descoberta automática;
- reduzir configuração ou código adicional;
- for consolidada no ecossistema;
- melhorar previsibilidade para quem utiliza a tecnologia.

A convenção não deve ser aplicada apenas por hábito quando um nome semântico produzir estrutura mais clara.

### 6.3 Tipagem

- Contratos públicos devem possuir tipos explícitos.
- Preferir `unknown` a `any` quando o dado ainda precisar ser validado.
- Evitar casts usados apenas para silenciar erros.
- Dados externos devem ser validados em tempo de execução quando necessário.
- Tipos devem impedir estados inválidos sempre que viável.
- Tipos locais devem permanecer próximos da implementação.
- Tipos compartilhados devem representar contratos realmente compartilhados.

### 6.4 Contratos

Contrato é qualquer interface estável entre módulos, processos ou sistemas.

- Contratos devem ser explícitos e previsíveis.
- Mudanças incompatíveis devem ser tratadas deliberadamente.
- Implementações internas não devem vazar para consumidores.
- Campos opcionais, valores nulos e estados de erro devem ser intencionais.

### 6.5 Comentários e documentação

- Comentários devem explicar intenção, restrição, decisão ou motivo não evidente.
- Não comentar linha a linha comportamentos já claros.
- Comentários devem permanecer sincronizados com a implementação.
- Código desativado não deve permanecer comentado.
- Documentação afetada por alteração deve ser atualizada junto com o código.

---

## 7. Dependências, imports e configuração

### 7.1 Dependências

Antes de adicionar uma dependência, verificar se:

- resolve problema real;
- não existe solução adequada no projeto ou plataforma;
- reduz mais complexidade do que adiciona;
- possui manutenção, documentação e licença compatíveis;
- seu impacto em segurança, tamanho e desempenho é aceitável.

Dependências não utilizadas devem ser removidas.

### 7.2 Imports

- Remover imports não utilizados.
- Evitar imports circulares.
- Preferir caminhos estáveis.
- Evitar conhecimento excessivo da estrutura interna de outros módulos.
- Evitar reexports em cadeia.

### 7.3 Configuração

- Configurações variáveis devem ser centralizadas.
- Valores de ambiente devem ser validados na inicialização.
- Configurações obrigatórias ausentes devem produzir erro claro.
- Segredos nunca devem ser versionados.
- Valores específicos de ambiente não devem ser codificados na regra de negócio.

---

## 8. Erros, segurança e observabilidade

### 8.1 Erros

- Erros não devem ser ignorados silenciosamente.
- Erros esperados devem ser representados de forma previsível.
- Falhas inesperadas devem preservar contexto para diagnóstico.
- Mensagens externas não devem expor detalhes internos.
- Recuperação automática só deve ocorrer quando for segura.

### 8.2 Segurança

- Toda entrada externa deve ser considerada não confiável.
- Validação, autenticação e autorização devem ocorrer na fronteira adequada.
- Aplicar o princípio do menor privilégio.
- Dados sensíveis devem ser protegidos em armazenamento, transporte e logs.
- Não confiar no cliente para decisões de segurança.

### 8.3 Observabilidade

- Logs devem possuir contexto suficiente para diagnóstico.
- Não registrar segredos ou dados sensíveis sem necessidade explícita.
- Mensagens de log devem ser consistentes e acionáveis.
- Métricas e rastreamento devem existir quando houver necessidade operacional real.

---

## 9. Regras específicas de front-end

### 9.1 Organização semântica

A árvore de front-end deve representar responsabilidades reais da interface e dos fluxos da aplicação.

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

Nenhuma dessas divisões deve ser criada automaticamente.

### 9.2 Componentes

Componentes usados por uma única página ou funcionalidade devem permanecer próximos dela.

Mover para área compartilhada somente com reutilização real e contrato estável.

Não manter simultaneamente `src/components` e `src/shared/components` quando ambas representarem a mesma responsabilidade.

### 9.3 Páginas e telas

Páginas e telas devem coordenar interface e fluxos de alto nível.

Não devem concentrar transformações complexas, geração de arquivos, regras de negócio, persistência ou integrações detalhadas.

### 9.4 Estado

Estado local deve permanecer próximo do consumidor.

Promover para store, contexto ou equivalente somente quando houver múltiplos consumidores, sobrevivência entre componentes ou atualização coordenada.

### 9.5 Engines e templates

Transformações complexas, cálculos, serialização e geração de arquivos devem permanecer fora de componentes visuais quando representarem responsabilidades próprias.

Preview e exportação não devem depender de fontes de verdade divergentes.

### 9.6 Assets

Assets devem ser organizados por finalidade ou domínio.

Não criar subdiretórios para cada asset isolado sem fronteira real.

---

## 10. Regras específicas de back-end

### 10.1 Organização semântica

A árvore de back-end deve ser organizada prioritariamente por domínio ou funcionalidade.

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

Nenhuma subdivisão deve ser criada automaticamente.

### 10.2 Domínio antes da categoria técnica

Evitar diretórios globais como `controllers`, `services`, `repositories` e `models` quando dispersarem uma mesma funcionalidade por toda a árvore.

Preferir manter próximos os elementos pertencentes ao mesmo domínio.

### 10.3 Camadas proporcionais

Não criar controller, service, use case, repository, gateway e adapter para todo fluxo automaticamente.

Cada camada deve possuir responsabilidade real.

Camadas que apenas encaminham argumentos devem ser removidas ou incorporadas ao nó semanticamente correto.

---

## 11. Testes e validação

- Alterações devem ser acompanhadas por validação proporcional ao risco.
- Regras de negócio devem possuir testes quando relevantes e estáveis.
- Testes devem verificar comportamento observável.
- Refatorações devem preservar contratos e comportamento.
- Testes quebrados não devem ser ignorados ou removidos para permitir integração.
- Cenários de erro e limites devem ser testados quando fizerem parte do comportamento esperado.

---

## 12. Refatoração e manutenção

Toda refatoração estrutural deve ocorrer de dentro para fora:

1. compreender o comportamento atual;
2. organizar os blocos lógicos internos;
3. modularizar funções, métodos e componentes;
4. extrair arquivos quando necessário;
5. organizar arquivos em diretórios quando necessário;
6. consolidar módulos e domínios;
7. ajustar a estrutura global;
8. atualizar imports, referências e contratos;
9. remover estruturas antigas;
10. validar comportamento, build e testes.

Além disso:

- Refatorações não devem alterar comportamento sem autorização explícita.
- Antes de remover código, confirmar que não existem referências ativas.
- Colocar todo o conteúdo necessário na estrutura final antes da poda.
- Não manter versões antigas e novas da mesma responsabilidade em paralelo.
- Dívida técnica deliberada deve ser documentada.

Mover código desorganizado para uma nova árvore apenas transfere o problema. A responsabilidade interna deve ser compreendida antes da realocação externa.

---

## 13. Verificação de estrutura e modularização

### 13.1 Modelo da árvore

- [ ] A raiz considerada é o diretório raiz do projeto.
- [ ] As folhas consideradas são os menores blocos lógicos indivisíveis do código.
- [ ] A regra de balanceamento foi aplicada recursivamente em todos os níveis.
- [ ] Cada nó possui responsabilidade identificável.
- [ ] Cada folha permanece indivisível sem misturar responsabilidades.

### 13.2 Balanceamento

- [ ] Filhos do mesmo nó são semanticamente relacionados.
- [ ] Responsabilidades diferentes foram separadas ou realocadas.
- [ ] Nós com muitos filhos continuam fáceis de localizar e manter.
- [ ] Nós extensos foram subdivididos somente em sub-responsabilidades reais.
- [ ] Não existem limites numéricos arbitrários usados como regra automática.
- [ ] A profundidade é proporcional à complexidade.
- [ ] Não existem níveis intermediários sem responsabilidade própria.
- [ ] Não existem cadeias de filho único sem justificativa.
- [ ] A navegação não é maior que o ganho de clareza.
- [ ] A árvore é a menor estrutura semanticamente suficiente.

### 13.3 Modularização de dentro para fora

- [ ] A modularização começou pelos blocos lógicos internos.
- [ ] Funções, métodos e componentes foram organizados antes da extração de arquivos.
- [ ] Arquivos só foram criados para responsabilidades próprias.
- [ ] Diretórios só foram criados para agrupamentos semânticos reais.
- [ ] Módulos só foram criados após consolidação das responsabilidades internas.
- [ ] A arquitetura global surgiu das responsabilidades reais do código.
- [ ] Nenhuma pasta ou camada foi criada preventivamente.

### 13.4 Nomenclatura

- [ ] Blocos, funções, arquivos e pastas possuem nomes semânticos e sugestivos.
- [ ] O nome permite inferir a responsabilidade do elemento.
- [ ] O contexto do nó pai não é repetido desnecessariamente no nome do filho.
- [ ] Termos genéricos possuem delimitação semântica.
- [ ] Convenções prevaleceram somente quando necessárias ou mais eficientes.

### 13.5 Arquivos e código interno

- [ ] Cada arquivo possui responsabilidade principal.
- [ ] Cada função possui responsabilidade principal.
- [ ] Funções coordenadoras delegam etapas independentes.
- [ ] Validação, transformação, persistência e apresentação estão separadas quando necessário.
- [ ] Não existem blocos extensos executando tarefas não relacionadas.
- [ ] Auxiliares locais permanecem próximos de seus consumidores.
- [ ] Exports representam interface pública intencional.

### 13.6 Migrações e refatorações

- [ ] Todo conteúdo necessário foi colocado na árvore final antes da remoção.
- [ ] Imports e referências foram atualizados.
- [ ] A implementação anterior foi removida.
- [ ] Não restaram caminhos obsoletos ou duplicados.
- [ ] O comportamento foi validado após a reorganização.
- [ ] Contratos e regras de negócio foram preservados.