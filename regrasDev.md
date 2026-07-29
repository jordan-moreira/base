# Regras de Desenvolvimento

## 1. Objetivo e aplicação

Este documento define os padrões permanentes de engenharia, organização, estruturação, modularização e qualidade aplicáveis a todos os projetos.

Todo projeto derivado deste repositório deve utilizar estas regras como base para organizar o código dentro dos arquivos e distribuir arquivos e diretórios na árvore do projeto.

A árvore concreta deve ser registrada em `regrasProjeto.md`, mas deve respeitar integralmente os critérios estruturais definidos neste documento.

As regras gerais aplicam-se a todo o código. As regras específicas de front-end e back-end complementam as regras gerais somente nos contextos correspondentes.

As decisões específicas de cada projeto, como stack, arquitetura adotada, estrutura concreta de diretórios, bibliotecas, integrações e restrições, devem ser registradas em `regrasProjeto.md`.

Em caso de conflito, aplicar a seguinte precedência:

1. `regrasProjeto.md`;
2. este documento;
3. convenções já consolidadas no projeto.

Exceções devem ser explícitas, justificadas e restritas ao menor escopo possível.

---

## 2. Princípios gerais

### 2.1 Clareza

- O código deve priorizar legibilidade, previsibilidade e manutenção.
- A solução mais simples que preserve corretude, segurança e capacidade de evolução deve ser preferida.
- Código explícito é preferível a comportamento implícito difícil de identificar.

### 2.2 Responsabilidade

- Cada módulo, arquivo, função ou componente deve possuir uma responsabilidade principal claramente identificável.
- Uma responsabilidade representa um motivo para mudança.
- Quando um elemento tende a mudar por motivos distintos, ele deve ser avaliado para separação.

### 2.3 Coesão

- Elementos que colaboram para resolver o mesmo problema devem permanecer próximos.
- Código não relacionado deve permanecer separado, mesmo quando possa tecnicamente compartilhar o mesmo arquivo.

### 2.4 Acoplamento

- Dependências entre módulos devem ser explícitas e reduzidas ao necessário.
- Alterações internas de um módulo não devem exigir mudanças indiscriminadas em outros módulos.
- Módulos não devem depender de detalhes internos de outros módulos.

### 2.5 Arquitetura proporcional

- A arquitetura deve crescer conforme a complexidade real do projeto.
- Projetos pequenos não devem reproduzir estruturas próprias de sistemas grandes sem necessidade.
- Projetos maiores não devem permanecer em estruturas simples quando isso comprometer manutenção, testes ou evolução.
- Nenhuma camada, abstração ou diretório deve existir apenas para satisfazer um padrão teórico.

### 2.6 Proximidade

- Código específico deve permanecer próximo do domínio, funcionalidade, página ou módulo que o utiliza.
- Código só deve ser movido para áreas compartilhadas quando houver reutilização real, estável e semanticamente coerente.

### 2.7 Árvore mínima suficiente

A árvore de diretórios deve utilizar o menor número possível de arquivos, diretórios e níveis de profundidade capaz de preservar:

- separação clara de responsabilidades;
- localização intuitiva do código;
- isolamento entre domínios;
- manutenção independente;
- testabilidade;
- direção previsível das dependências.

A redução da quantidade de folhas não deve resultar em arquivos genéricos, responsabilidades misturadas ou diretórios usados como depósitos de código.

A estrutura correta é a menor árvore semanticamente suficiente, e não simplesmente a árvore com menor quantidade absoluta de arquivos.

### 2.8 Balanceamento estrutural

A árvore deve permanecer semanticamente equilibrada entre concentração e fragmentação.

Considera-se concentração excessiva quando:

- um diretório reúne responsabilidades não relacionadas;
- um arquivo contém múltiplos fluxos independentes;
- nomes genéricos escondem conceitos distintos;
- localizar uma responsabilidade exige conhecer previamente sua implementação.

Considera-se fragmentação excessiva quando:

- existem muitos diretórios com uma única folha sem justificativa;
- um fluxo simples está distribuído por vários níveis;
- funções inseparáveis foram transformadas em arquivos independentes;
- existem camadas que apenas repassam chamadas;
- a navegação entre arquivos é maior que o ganho de clareza;
- a árvore reproduz divisões teóricas sem necessidade concreta.

O equilíbrio deve ser determinado pela responsabilidade, e não pela quantidade uniforme de arquivos em cada diretório.

---

## 3. Critérios de decisão arquitetural

Antes de criar uma nova abstração, pasta, camada, serviço ou módulo, verificar:

- existe uma responsabilidade própria e estável;
- há redução real de acoplamento ou complexidade;
- existe reutilização concreta, e não apenas hipotética;
- o elemento possui ciclo de vida ou dependências próprias;
- a separação melhora leitura, testes ou manutenção;
- não existe alternativa mais simples com a mesma clareza.

### 3.1 Criar um novo diretório

Criar um novo diretório somente quando ele:

- representar uma responsabilidade semanticamente identificável;
- agrupar elementos relacionados;
- separar código de natureza diferente;
- representar domínio, funcionalidade, fronteira técnica ou categoria estável;
- reduzir mistura de responsabilidades no diretório pai;
- melhorar a localização dos arquivos;
- evitar colisões semânticas entre conteúdos diferentes.

Não criar um diretório apenas porque:

- existe um único arquivo de determinado tipo;
- outra arquitetura utiliza esse diretório;
- futuramente outros arquivos poderão ser adicionados;
- o nome técnico do arquivo permite classificá-lo;
- a separação torna a árvore visualmente simétrica.

Diretórios contendo uma única folha são aceitáveis somente quando:

- representam uma fronteira arquitetural real;
- são exigidos pela tecnologia;
- isolam configuração, integração ou recurso com ciclo de vida próprio;
- preservam uma organização necessária entre módulos equivalentes;
- possuem expansão concreta e imediata já prevista.

Caso contrário, o arquivo deve permanecer no diretório semanticamente mais próximo.

### 3.2 Criar um novo arquivo

Criar um novo arquivo quando o conteúdo:

- possuir responsabilidade própria;
- possuir nome semântico próprio;
- mudar por motivo diferente do restante;
- possuir dependências próprias;
- representar contrato, componente, engine, store, serviço ou regra independente;
- puder ser testado isoladamente;
- possuir reutilização real;
- comprometer a coesão ou leitura do arquivo atual.

Não criar um arquivo apenas para:

- reduzir artificialmente o número de linhas;
- armazenar uma constante local;
- separar uma função privada inseparável do fluxo;
- encapsular poucas linhas sem responsabilidade própria;
- criar um wrapper que apenas repassa parâmetros;
- antecipar reutilização inexistente;
- reproduzir um modelo estrutural previamente conhecido.

### 3.3 Criar uma abstração

Criar somente quando ela eliminar repetição relevante, estabilizar um contrato, isolar uma dependência ou representar um conceito real do domínio.

Não abstrair apenas para antecipar necessidades futuras.

### 3.4 Compartilhar código

Compartilhar somente quando os usos possuírem o mesmo significado e comportamento esperado.

Semelhança visual ou estrutural isolada não é suficiente para justificar compartilhamento.

### 3.5 Adicionar uma camada

Adicionar somente quando houver responsabilidade distinta, fronteira técnica ou regra de dependência que justifique sua existência.

Camadas que apenas repassam dados sem transformação, proteção ou coordenação devem ser evitadas.

---

## 4. Organização e arquitetura

- A estrutura deve ser organizada por responsabilidade, domínio ou funcionalidade, conforme a natureza do projeto.
- Cada diretório deve possuir propósito claro e nome semanticamente coerente.
- A árvore deve permitir localizar um código sem conhecer previamente toda a implementação.
- Arquivos relacionados devem permanecer próximos.
- Código compartilhado deve ser separado de código específico.
- Não manter duas árvores concorrentes para a mesma responsabilidade.
- Não preservar diretórios antigos após uma migração concluída.
- Não criar arquivos `index` apenas para reexportar automaticamente todo o conteúdo de uma pasta.
- Reexports devem existir somente quando definirem uma interface pública clara.
- Dependências devem seguir uma direção previsível e evitar ciclos.
- As fronteiras entre módulos devem ser explícitas.

A estrutura concreta de cada projeto deve ser definida em `regrasProjeto.md`.

### 4.1 Padrão obrigatório de organização da árvore

A árvore de diretórios deve representar as responsabilidades reais do sistema.

A organização deve seguir a seguinte ordem de decisão:

1. separar contextos técnicos de alto nível quando possuírem execução, dependências ou responsabilidades distintas;
2. organizar o código principal por domínio, módulo ou funcionalidade;
3. manter dentro de cada módulo os elementos específicos daquele contexto;
4. mover para áreas compartilhadas apenas elementos realmente reutilizados por múltiplos módulos;
5. manter infraestrutura, configuração e pontos de entrada separados das regras de domínio.

A árvore deve permitir responder, sem abrir os arquivos:

- qual é a responsabilidade de cada diretório;
- a qual domínio ou funcionalidade um arquivo pertence;
- quais elementos são específicos;
- quais elementos são compartilhados;
- onde estão os pontos de entrada;
- onde estão as integrações externas;
- onde estão as regras de negócio.

Não devem existir:

- dois diretórios com a mesma responsabilidade;
- estruturas antigas mantidas após uma migração;
- arquivos duplicados em árvores diferentes;
- diretórios genéricos usados como depósito de código;
- módulos específicos armazenados em áreas compartilhadas;
- arquivos compartilhados que dependam de módulos consumidores;
- diretórios criados apenas para reproduzir uma árvore previamente conhecida;
- níveis intermediários que não expressem uma responsabilidade real.

Quando um arquivo for movido durante uma reorganização:

1. confirmar que o arquivo necessário existe na árvore final;
2. atualizar todos os imports e referências;
3. validar o funcionamento;
4. remover a versão anterior;
5. confirmar que não restaram duplicações ou caminhos obsoletos.

A reorganização só estará concluída quando existir uma única árvore válida para cada responsabilidade.

### 4.2 Modelo abstrato da árvore

A estrutura concreta depende da tecnologia e deve ser definida em `regrasProjeto.md`, mas deve derivar conceitualmente do seguinte modelo:

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

Esse modelo é conceitual.

Os nomes, diretórios e camadas concretos só devem existir quando houver responsabilidade real no projeto.

Não é obrigatório criar todas as divisões representadas. É obrigatório preservar a separação semântica correspondente quando essas responsabilidades existirem.

### 4.3 Profundidade mínima necessária

A profundidade da árvore deve ser a menor possível sem comprometer a separação semântica.

Um novo nível de diretório só deve ser criado quando:

- agrupar múltiplos elementos relacionados;
- representar uma responsabilidade própria;
- separar conteúdo de natureza distinta;
- reduzir mistura relevante no nível atual;
- tornar a localização mais previsível.

Não criar níveis intermediários que:

- apenas repitam o nome do nível anterior;
- contenham uma única folha sem justificativa;
- representem somente uma categoria técnica desnecessária;
- aumentem a navegação sem melhorar entendimento.

### 4.4 Promoção progressiva da estrutura

Todo código deve começar na estrutura mais simples semanticamente correta.

Um conteúdo deve ser promovido para novo arquivo, diretório ou módulo somente quando:

- adquirir responsabilidade própria;
- passar a possuir múltiplos elementos relacionados;
- ganhar dependências ou ciclo de mudança próprios;
- precisar ser testado isoladamente;
- possuir mais de um consumidor real;
- comprometer a coesão da estrutura atual.

Não criar antecipadamente uma estrutura destinada a uma complexidade que ainda não existe.

A estrutura deve crescer conforme a responsabilidade cresce.

### 4.5 Proximidade antes do compartilhamento

Todo código deve permanecer próximo do consumidor principal durante sua criação inicial.

Mover para uma área compartilhada somente quando:

- existirem consumidores reais em mais de um módulo;
- o significado for igual em todos os usos;
- o comportamento for estável;
- o código não depender de detalhes internos de um módulo específico.

Não mover código para diretórios como `shared`, `common`, `utils`, `components`, `services` ou equivalentes apenas por possibilidade futura de reutilização.

### 4.6 Diretórios genéricos

Diretórios genéricos devem possuir escopo e finalidade claros.

Exemplos:

```text
components
utils
services
helpers
common
shared
types
hooks
```

Esses diretórios não devem ser usados como depósitos de elementos classificados apenas pelo tipo técnico.

Quando o conteúdo possuir domínio ou funcionalidade própria, ele deve permanecer próximo desse domínio.

Manter em diretórios compartilhados apenas elementos:

- verdadeiramente reutilizados;
- independentes de módulos específicos;
- semanticamente coerentes entre todos os consumidores;
- com contrato estável.

### 4.7 Critério de redução de folhas

A quantidade de folhas da árvore deve ser minimizada sem sacrificar coesão.

Antes de criar uma nova folha, verificar:

- se o conteúdo possui responsabilidade própria;
- se permanecer no arquivo atual prejudica leitura ou manutenção;
- se a nova folha reduz ou aumenta a navegação;
- se a separação cria apenas um wrapper ou arquivo intermediário;
- se a responsabilidade pode permanecer próxima do consumidor;
- se existe justificativa além do tamanho do arquivo.

Agrupar conteúdos pequenos quando:

- pertencem ao mesmo fluxo;
- compartilham dependências;
- mudam pelos mesmos motivos;
- não possuem uso independente;
- a separação não melhora testes ou manutenção.

Separar conteúdos quando:

- possuem ciclos de mudança diferentes;
- representam conceitos independentes;
- misturam apresentação, domínio, persistência ou integração;
- possuem consumidores distintos;
- exigem testes isolados.

---

## 5. Modularização e responsabilidades

### 5.1 Modularização entre arquivos

Cada arquivo deve possuir uma responsabilidade principal, identificável por seu nome e por sua posição na árvore.

Um arquivo deve ser separado quando o conteúdo:

- representa um conceito próprio;
- possui motivo de mudança diferente do restante;
- depende de recursos diferentes;
- pode ser testado isoladamente;
- possui reutilização real;
- implementa uma fronteira ou contrato;
- trata uma etapa independente do fluxo;
- compromete a leitura quando permanece junto ao restante.

A separação deve ocorrer por responsabilidade, e não apenas por tamanho.

A modularização deve minimizar simultaneamente:

- a quantidade de responsabilidades por arquivo;
- a quantidade de arquivos sem responsabilidade própria;
- a profundidade da navegação;
- a duplicação;
- o acoplamento entre módulos.

Não existe quantidade ideal fixa de linhas ou arquivos.

O resultado esperado é o menor conjunto de arquivos capaz de representar corretamente as responsabilidades existentes.

Não devem ser criados arquivos diferentes apenas para:

- reduzir artificialmente o número de linhas;
- armazenar uma única constante sem contexto próprio;
- encapsular uma função usada uma única vez e inseparável do fluxo;
- reproduzir uma convenção de outro projeto;
- antecipar reutilização ainda inexistente;
- criar camadas que apenas repassam chamadas.

Cada arquivo deve:

- possuir nome semanticamente específico;
- estar no diretório correspondente à sua responsabilidade;
- expor apenas o necessário;
- evitar conhecer detalhes internos de outros módulos;
- manter auxiliares locais próximos da implementação;
- importar dependências por interfaces estáveis quando aplicável.

Arquivos genéricos como `utils`, `helpers`, `common`, `service`, `manager`, `misc` ou `shared` não devem existir sem delimitação semântica adicional.

### 5.2 Modularização dentro dos arquivos

O conteúdo de um arquivo deve ser organizado em blocos lógicos previsíveis.

Quando aplicável, utilizar a seguinte ordem:

1. imports;
2. tipos e contratos locais;
3. constantes locais;
4. validações;
5. funções auxiliares privadas;
6. implementação principal;
7. composição ou coordenação;
8. exports.

Essa ordem pode ser adaptada à linguagem ou framework, mas deve permanecer consistente dentro do projeto.

Cada função deve:

- executar uma responsabilidade principal;
- possuir nome que descreva a ação realizada;
- receber apenas os dados necessários;
- evitar alterar estado externo sem tornar isso explícito;
- retornar resultado previsível;
- evitar misturar validação, transformação, persistência e apresentação;
- delegar etapas independentes para funções próprias;
- evitar níveis excessivos de aninhamento;
- tratar erros na fronteira adequada.

Uma função coordenadora pode executar um fluxo composto, desde que delegue as etapas específicas.

Não concentrar no mesmo bloco:

- leitura de entrada;
- validação;
- regra de negócio;
- acesso ao banco;
- integração externa;
- formatação da resposta;
- manipulação visual.

Comentários devem identificar blocos lógicos apenas quando a responsabilidade ou a razão da implementação não estiver clara pelo próprio código.

### 5.3 Quando não dividir

Não dividir quando a separação:

- aumentar a navegação sem melhorar entendimento;
- criar arquivos sem responsabilidade própria;
- espalhar um fluxo simples por várias camadas;
- existir apenas para reduzir o tamanho aparente do arquivo;
- tornar dependências simples mais difíceis de acompanhar.

### 5.4 Duplicação

- Duplicação ocasional e pequena pode ser preferível a uma abstração incorreta.
- A extração deve ocorrer quando a repetição representar o mesmo conceito e possuir tendência real de manutenção conjunta.
- Não unificar comportamentos que apenas parecem semelhantes.

### 5.5 Limites dos módulos

Cada módulo deve possuir uma fronteira clara.

Um módulo deve concentrar:

- regras específicas do seu domínio;
- componentes específicos;
- contratos específicos;
- serviços específicos;
- validações específicas;
- testes específicos;
- integrações usadas exclusivamente por ele.

Um módulo não deve acessar arquivos internos de outro módulo diretamente.

A comunicação entre módulos deve ocorrer por interface pública, contrato, evento, serviço de aplicação, função explicitamente exportada ou mecanismo equivalente definido no projeto.

Elementos compartilhados não devem depender de módulos específicos.

### 5.6 Agrupamento semântico

Conteúdos podem permanecer no mesmo arquivo quando:

- participam do mesmo fluxo;
- possuem o mesmo motivo de mudança;
- utilizam as mesmas dependências;
- não possuem valor isolado;
- não possuem consumidores independentes;
- sua separação aumentaria apenas a navegação.

Conteúdos devem ser separados quando:

- possuem responsabilidades independentes;
- representam conceitos nomeáveis diferentes;
- misturam fronteiras técnicas;
- possuem ciclos de mudança distintos;
- exigem testes isolados;
- são reutilizados separadamente.

O agrupamento deve ocorrer por significado e responsabilidade, nunca apenas por tipo técnico.

---

## 6. Nomenclatura, tipagem e contratos

### 6.1 Nomenclatura

- Usar `camelCase` para variáveis, funções, métodos e propriedades.
- Usar `PascalCase` para componentes, classes, tipos, interfaces e enums.
- Usar `UPPER_SNAKE_CASE` apenas para constantes globais verdadeiramente imutáveis e convencionais.
- Funções devem indicar ação.
- Booleanos devem indicar condição, preferencialmente com prefixos como `is`, `has`, `can` ou `should`.
- Coleções devem usar nomes no plural.
- Nomes devem representar intenção, não detalhes acidentais de implementação.
- Evitar abreviações não consolidadas, nomes genéricos e identificadores ambíguos.
- Evitar nomes como `data`, `item`, `value`, `temp`, `utils` ou `service` quando um nome mais específico for possível.

### 6.2 Tipagem

- Contratos públicos devem possuir tipos explícitos.
- Preferir `unknown` a `any` quando o tipo ainda precisar ser validado.
- Evitar `any`, tipagem excessivamente ampla e casts usados apenas para silenciar erros.
- Dados externos devem ser validados em tempo de execução quando a tipagem estática não oferecer garantia suficiente.
- Tipos devem impedir estados inválidos sempre que isso for viável.
- Estados mutuamente exclusivos devem preferir uniões discriminadas ou representação equivalente.
- Tipos locais devem permanecer próximos da implementação.
- Tipos compartilhados devem representar contratos realmente compartilhados.
- Não duplicar manualmente o mesmo contrato em diferentes partes do sistema quando houver uma fonte única viável.

### 6.3 Contratos

Contrato é qualquer interface estável entre módulos, processos ou sistemas, incluindo funções públicas, eventos, estruturas de dados, APIs e formatos persistidos.

- Contratos devem ser explícitos e previsíveis.
- Mudanças incompatíveis devem ser tratadas deliberadamente.
- Implementações internas não devem vazar para consumidores.
- Campos opcionais, valores nulos e estados de erro devem ser definidos intencionalmente.

### 6.4 Comentários e documentação

- Comentários devem explicar intenção, restrição, decisão ou motivo não evidente.
- Não comentar linha a linha comportamentos que o próprio código já expressa com clareza.
- Comentários devem permanecer sincronizados com a implementação.
- Código desativado não deve permanecer comentado; deve ser removido e recuperado pelo histórico quando necessário.
- Contratos públicos, fluxos complexos e decisões arquiteturais relevantes devem ser documentados quando não forem evidentes pelo código.
- Documentação afetada por uma alteração deve ser atualizada junto com o código.

---

## 7. Dependências, imports e configuração

### 7.1 Dependências

Antes de adicionar uma dependência, verificar se:

- resolve um problema real;
- não existe solução adequada na linguagem, plataforma ou projeto;
- reduz mais complexidade do que adiciona;
- possui manutenção, documentação e licença compatíveis;
- seu impacto em segurança, tamanho e desempenho é aceitável.

- Dependências não utilizadas devem ser removidas.
- Bibliotecas não devem ser usadas para tarefas triviais quando uma implementação simples e segura for suficiente.
- Dependências centrais devem ser encapsuladas quando sua substituição ou isolamento for relevante.

### 7.2 Imports

- Remover imports não utilizados.
- Evitar imports circulares.
- Preferir caminhos estáveis e sem conhecimento excessivo da estrutura interna de outros módulos.
- Imports devem seguir uma ordem consistente definida pelas ferramentas do projeto.
- Evitar reexports em cadeia que dificultem identificar a origem de uma dependência.

### 7.3 Configuração

- Configurações variáveis devem ser centralizadas.
- Valores de ambiente devem ser validados na inicialização.
- Configurações obrigatórias ausentes ou inválidas devem interromper a inicialização com erro claro.
- Valores padrão só devem existir quando forem seguros e semanticamente válidos.
- Ambientes como desenvolvimento, teste, homologação e produção devem possuir diferenças explícitas e controladas.
- Deve existir exemplo documentado das variáveis necessárias, sem segredos reais.
- URLs, chaves, limites e parâmetros operacionais não devem ser espalhados pelo código.
- Segredos nunca devem ser versionados.
- Valores específicos de ambiente não devem ser codificados diretamente na regra de negócio.
- Valores fixos de domínio devem possuir nome e contexto claros.

---

## 8. Erros, segurança e observabilidade

### 8.1 Tratamento de erros

- Erros não devem ser ignorados silenciosamente.
- Erros esperados devem ser representados de forma previsível.
- Falhas inesperadas devem preservar contexto suficiente para diagnóstico.
- Diferenciar erros esperados, inesperados, recuperáveis e fatais quando isso afetar o fluxo.
- Mensagens externas não devem expor detalhes internos, caminhos, credenciais ou stack traces.
- Tratamentos genéricos não devem ocultar a causa original.
- Recuperação automática só deve ocorrer quando for segura e claramente definida.
- Recursos devem ser liberados mesmo em cenários de falha.

### 8.2 Segurança

- Toda entrada externa deve ser considerada não confiável.
- Validação, autenticação e autorização devem ocorrer na fronteira adequada.
- Aplicar o princípio do menor privilégio.
- Dados sensíveis devem ser protegidos em armazenamento, transporte e logs.
- Não confiar no cliente para decisões de segurança.
- Dependências e configurações de segurança devem ser mantidas atualizadas conforme o projeto.

### 8.3 Observabilidade

- Logs devem possuir contexto suficiente para diagnóstico.
- Não registrar segredos, credenciais ou dados sensíveis sem necessidade explícita.
- Mensagens de log devem ser consistentes e acionáveis.
- Métricas e rastreamento devem ser adicionados quando houver necessidade operacional real.

---

## 9. Regras específicas de front-end

### 9.1 Organização semântica

A árvore de front-end deve representar responsabilidades reais da interface e dos fluxos da aplicação.

Quando existirem, distinguir semanticamente:

- inicialização e composição da aplicação;
- páginas, telas ou rotas;
- funcionalidades ou domínios;
- componentes compartilhados;
- componentes específicos de uma funcionalidade;
- estado compartilhado;
- estado local;
- regras de transformação;
- engines de geração ou processamento;
- templates e definições declarativas;
- integrações externas;
- assets;
- tipos e contratos compartilhados;
- utilitários semanticamente delimitados.

Modelo conceitual:

```text
src/
├── inicialização e composição
├── páginas ou telas
├── funcionalidades ou domínios
├── componentes compartilhados
├── estado compartilhado
├── engines e transformações
├── templates e definições
├── integrações
├── assets
├── contratos
└── utilitários delimitados
```

Esse modelo não obriga a existência de todos os diretórios.

Criar apenas os diretórios correspondentes às responsabilidades realmente presentes.

### 9.2 Componentes específicos e compartilhados

Componentes usados por uma única página ou funcionalidade devem permanecer próximos dela.

Mover um componente para uma área compartilhada somente quando:

- existir reutilização real;
- o significado visual e comportamental for o mesmo;
- não houver dependência de estado ou regra específica;
- o contrato estiver estável.

Não manter simultaneamente árvores como `src/components` e `src/shared/components` quando ambas representarem a mesma responsabilidade.

Deve existir uma única localização válida para componentes compartilhados.

### 9.3 Páginas e telas

Páginas e telas devem coordenar a interface e os fluxos de alto nível.

Não devem concentrar transformação complexa de dados, geração de arquivos, regras de negócio, integração externa detalhada, persistência ou validações reutilizáveis.

Essas responsabilidades devem ser delegadas para módulos próprios quando possuírem complexidade ou reutilização real.

### 9.4 Estado no front-end

Estado local deve permanecer no componente ou funcionalidade que o consome.

Estado compartilhado deve ser promovido para store, contexto ou mecanismo equivalente somente quando:

- for usado por múltiplos consumidores;
- precisar sobreviver à troca de componentes;
- representar fluxo compartilhado;
- exigir atualização coordenada.

Não mover estado para uma store global apenas para centralização preventiva.

### 9.5 Engines e transformações

Transformações complexas, geração de arquivos, cálculos, serialização e processamento não devem permanecer em páginas ou componentes visuais.

Criar uma engine ou módulo equivalente quando:

- existir fluxo de transformação próprio;
- houver entrada e saída bem definidas;
- a implementação puder ser testada sem a interface;
- o processamento for reutilizado;
- a regra não pertencer à apresentação.

Engines devem evitar dependência direta de componentes visuais.

### 9.6 Templates e definições declarativas

Templates devem ser separados de páginas e engines quando representarem definições reutilizáveis, metadados, contratos de renderização ou configurações declarativas.

A apresentação visual e a geração final não devem depender de duas fontes de verdade divergentes.

Quando preview e exportação utilizarem tecnologias diferentes, os dados compartilhados devem estar representados em contratos ou metadados explícitos.

### 9.7 Assets

Assets devem ser organizados por finalidade ou domínio de uso.

Não criar subdiretórios para cada asset isolado.

Criar agrupamentos apenas quando existirem múltiplos recursos relacionados ou fronteira de uso claramente distinta.

---

## 10. Regras específicas de back-end

### 10.1 Organização semântica

A árvore de back-end deve ser organizada prioritariamente por domínio ou funcionalidade.

Quando existirem, distinguir:

- inicialização e composição;
- domínios ou funcionalidades;
- casos de uso;
- regras de negócio;
- persistência;
- integrações externas;
- transporte HTTP, filas ou eventos;
- contratos;
- configuração;
- infraestrutura compartilhada.

Modelo conceitual:

```text
src/
├── inicialização e composição
├── domínios ou funcionalidades
│   └── módulo/
│       ├── aplicação
│       ├── domínio
│       ├── persistência
│       ├── transporte
│       └── integrações
├── infraestrutura compartilhada
├── configuração
└── contratos compartilhados
```

Não criar todas essas subdivisões automaticamente.

Um módulo pequeno pode manter seus elementos diretamente no diretório da funcionalidade até que a complexidade justifique novos níveis.

### 10.2 Domínio antes da categoria técnica

Evitar concentrar todas as responsabilidades em diretórios globais como `controllers`, `services`, `repositories` e `models` quando isso dispersar uma mesma funcionalidade por toda a árvore.

Preferir manter próximos os elementos pertencentes ao mesmo domínio.

Subdiretórios internos devem surgir somente quando a quantidade ou complexidade dos elementos justificar a separação.

### 10.3 Camadas proporcionais

Não criar controller, service, use case, repository, gateway e adapter para todo fluxo de forma automática.

Cada camada deve possuir responsabilidade real.

Camadas que apenas encaminham argumentos sem validar, transformar, proteger fronteiras, coordenar, aplicar regras ou adaptar contratos devem ser removidas ou incorporadas à camada semanticamente correta.

---

## 11. Testes e validação

- Alterações devem ser acompanhadas por validação proporcional ao risco.
- Regras de negócio devem possuir testes quando forem relevantes e estáveis.
- Testes devem verificar comportamento observável, não detalhes internos desnecessários.
- Refatorações devem preservar contratos e comportamento existentes.
- Testes quebrados não devem ser ignorados ou removidos apenas para permitir integração.
- Cenários de erro e limites devem ser testados quando fizerem parte do comportamento esperado.

---

## 12. Refatoração e manutenção

- Refatorações não devem alterar comportamento sem autorização explícita.
- Antes de remover código, confirmar que não existem referências ativas.
- Durante migrações, colocar todo o conteúdo necessário na estrutura final antes da poda.
- Após a migração, remover arquivos, diretórios, imports e caminhos obsoletos.
- Não manter versões antigas e novas da mesma responsabilidade em paralelo.
- Alterações estruturais devem ser validadas por build, testes e execução dos fluxos afetados.
- Dívida técnica deliberada deve ser documentada quando não puder ser resolvida no mesmo momento.

---

## 13. Verificação de estrutura e modularização

Antes de considerar uma implementação ou refatoração concluída, verificar:

### 13.1 Árvore de diretórios

- [ ] Cada diretório possui responsabilidade identificável.
- [ ] Não existem árvores concorrentes para a mesma responsabilidade.
- [ ] Não existem arquivos duplicados em caminhos diferentes.
- [ ] Não existem diretórios antigos após migrações concluídas.
- [ ] Código específico permanece próximo do módulo consumidor.
- [ ] Código compartilhado possui reutilização real.
- [ ] A árvore concreta está documentada em `regrasProjeto.md`.
- [ ] Os nomes permitem localizar o conteúdo sem abrir os arquivos.

### 13.2 Balanceamento da árvore

- [ ] A árvore utiliza o menor número possível de folhas sem misturar responsabilidades.
- [ ] Não existem diretórios com uma única folha sem justificativa.
- [ ] Não existem níveis intermediários sem responsabilidade própria.
- [ ] Diretórios genéricos não são usados como depósitos.
- [ ] Código específico permanece próximo dos consumidores.
- [ ] Código compartilhado possui reutilização real.
- [ ] A profundidade é proporcional à complexidade.
- [ ] A estrutura não antecipa necessidades inexistentes.
- [ ] A navegação não é maior que o ganho de clareza.
- [ ] A árvore cresce por promoção progressiva.
- [ ] Não existem classificações concorrentes para o mesmo conteúdo.
- [ ] Cada folha representa responsabilidade própria ou agrupamento coeso.

### 13.3 Arquivos

- [ ] Cada arquivo possui responsabilidade principal.
- [ ] O nome do arquivo representa seu conteúdo.
- [ ] O arquivo está no diretório semanticamente correto.
- [ ] Não há mistura desnecessária de domínio, persistência, integração e apresentação.
- [ ] Auxiliares locais permanecem próximos de seus consumidores.
- [ ] Arquivos genéricos foram evitados ou devidamente delimitados.
- [ ] Exports representam uma interface pública intencional.

### 13.4 Código interno

- [ ] Cada função possui uma responsabilidade principal.
- [ ] Funções coordenadoras delegam etapas independentes.
- [ ] Validação, transformação, persistência e apresentação estão separadas quando necessário.
- [ ] Não existem blocos extensos executando tarefas não relacionadas.
- [ ] A ordem interna do arquivo é previsível.
- [ ] Os nomes descrevem intenção.
- [ ] Comentários explicam decisões, não linhas de código.

### 13.5 Migrações e refatorações

- [ ] Todo conteúdo necessário foi colocado na árvore final antes da remoção.
- [ ] Imports e referências foram atualizados.
- [ ] A implementação anterior foi removida.
- [ ] Não restaram caminhos obsoletos.
- [ ] O comportamento foi validado após a reorganização.
- [ ] A refatoração não alterou contratos ou regras de negócio sem autorização.
