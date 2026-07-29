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

Criar somente quando existir um conjunto coeso de responsabilidades que não pertença naturalmente a outro módulo.

Não criar diretórios vazios, preventivos ou destinados a uma única entrada sem justificativa arquitetural.

### 3.2 Criar um novo arquivo

Criar quando o conteúdo possuir responsabilidade própria, puder ser testado ou reutilizado isoladamente, ou quando sua permanência no arquivo atual comprometer a leitura.

Não dividir arquivos apenas por quantidade de linhas ou para reproduzir automaticamente uma convenção.

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

Prefira:

```text
formatarData.ts
validarCpf.ts
calcularTotalPedido.ts
```

em vez de:

```text
utils.ts
```

quando esses comportamentos representarem responsabilidades independentes.

Prefira:

```text
usuarios/
├── buscarUsuario.ts
├── criarUsuario.ts
└── usuarioRepository.ts
```

em vez de:

```text
services/
└── usuarioService.ts
```

quando essas operações possuírem responsabilidades, dependências ou ciclos de mudança distintos.

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

Exemplo:

```js
async function criarPedido(dadosPedido) {
    const pedidoValidado = validarPedido(dadosPedido);
    const pedidoCalculado = calcularPedido(pedidoValidado);
    const pedidoSalvo = await salvarPedido(pedidoCalculado);

    return apresentarPedido(pedidoSalvo);
}
```

A função coordenadora descreve o fluxo. Cada etapa mantém sua própria responsabilidade.

Não concentrar no mesmo bloco:

- leitura de entrada;
- validação;
- regra de negócio;
- acesso ao banco;
- integração externa;
- formatação da resposta;
- manipulação visual.

Comentários devem identificar blocos lógicos apenas quando a responsabilidade ou a razão da implementação não estiver clara pelo próprio código.

Não utilizar comentários para compensar:

- funções excessivamente extensas;
- nomes genéricos;
- fluxo desorganizado;
- mistura de responsabilidades;
- abstrações pouco claras.

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

A comunicação entre módulos deve ocorrer por:

- interface pública;
- contrato;
- evento;
- serviço de aplicação;
- função explicitamente exportada;
- mecanismo equivalente definido no projeto.

Elementos compartilhados não devem depender de módulos específicos.

A direção aceitável é:

```text
módulo específico
    ↓
código compartilhado
```

A direção abaixo deve ser evitada:

```text
código compartilhado
    ↓
módulo específico
```

Quando uma funcionalidade deixar de ser específica e se tornar realmente compartilhada, ela deve ser movida de forma completa, com atualização dos consumidores e remoção da implementação anterior.

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

## 9. Testes e validação

- Alterações devem ser acompanhadas por validação proporcional ao risco.
- Regras de negócio devem possuir testes quando forem relevantes e estáveis.
- Testes devem verificar comportamento observável, não detalhes internos desnecessários.
- Refatorações devem preservar contratos e comportamento existentes.
- Testes quebrados não devem ser ignorados ou removidos apenas para permitir integração.
- Cenários de erro e limites devem ser testados quando fizerem parte do comportamento esperado.

---

## 10. Refatoração e manutenção

- Refatorações não devem alterar comportamento sem autorização explícita.
- Antes de remover código, confirmar que não existem referências ativas.
- Durante migrações, colocar todo o conteúdo necessário na estrutura final antes da poda.
- Após a migração, remover arquivos, diretórios, imports e caminhos obsoletos.
- Não manter versões antigas e novas da mesma responsabilidade em paralelo.
- Alterações estruturais devem ser validadas por build, testes e execução dos fluxos afetados.
- Dívida técnica deliberada deve ser documentada quando não puder ser resolvida no mesmo momento.

---

## 11. Verificação de estrutura e modularização

Antes de considerar uma implementação ou refatoração concluída, verificar:

### 11.1 Árvore de diretórios

- [ ] Cada diretório possui responsabilidade identificável.
- [ ] Não existem árvores concorrentes para a mesma responsabilidade.
- [ ] Não existem arquivos duplicados em caminhos diferentes.
- [ ] Não existem diretórios antigos após migrações concluídas.
- [ ] Código específico permanece próximo do módulo consumidor.
- [ ] Código compartilhado possui reutilização real.
- [ ] A árvore concreta está documentada em `regrasProjeto.md`.
- [ ] Os nomes permitem localizar o conteúdo sem abrir os arquivos.

### 11.2 Arquivos

- [ ] Cada arquivo possui responsabilidade principal.
- [ ] O nome do arquivo representa seu conteúdo.
- [ ] O arquivo está no diretório semanticamente correto.
- [ ] Não há mistura desnecessária de domínio, persistência, integração e apresentação.
- [ ] Auxiliares locais permanecem próximos de seus consumidores.
- [ ] Arquivos genéricos foram evitados ou devidamente delimitados.
- [ ] Exports representam uma interface pública intencional.

### 11.3 Código interno

- [ ] Cada função possui uma responsabilidade principal.
- [ ] Funções coordenadoras delegam etapas independentes.
- [ ] Validação, transformação, persistência e apresentação estão separadas quando necessário.
- [ ] Não existem blocos extensos executando tarefas não relacionadas.
- [ ] A ordem interna do arquivo é previsível.
- [ ] Os nomes descrevem intenção.
- [ ] Comentários explicam decisões, não linhas de código.

### 11.4 Migrações e refatorações

- [ ] Todo conteúdo necessário foi colocado na árvore final antes da remoção.
- [ ] Imports e referências foram atualizados.
- [ ] A implementação anterior foi removida.
- [ ] Não restaram caminhos obsoletos.
- [ ] O comportamento foi validado após a reorganização.
- [ ] A refatoração não alterou contratos ou regras de negócio sem autorização.
