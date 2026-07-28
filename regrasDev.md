# Regras de Desenvolvimento

## 1. Objetivo e aplicação

Este documento define os padrões permanentes de engenharia, organização e qualidade aplicáveis aos projetos.

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

---

## 5. Modularização e responsabilidades

### 5.1 Modularização entre arquivos

- Cada arquivo deve possuir uma responsabilidade principal.
- Código deve ser extraído quando possuir dependências, testes, reutilização ou ciclo de mudança próprios.
- Funções auxiliares específicas devem permanecer próximas de onde são usadas.
- Utilitários genéricos só devem ser criados quando o comportamento for realmente genérico.

### 5.2 Modularização dentro dos arquivos

- Funções extensas devem ser divididas por etapas lógicas e responsabilidades.
- Blocos de transformação, validação, persistência e apresentação não devem ser misturados sem necessidade.
- A ordem interna deve ser previsível: imports, tipos, constantes, auxiliares, implementação e exports, conforme aplicável.
- Evitar funções que coordenem múltiplas tarefas independentes.

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
- Falhas de segurança não devem ser tratadas apenas como problemas de interface.

### 8.3 Logs e observabilidade

- Logs devem possuir contexto útil, como operação, módulo e identificadores não sensíveis.
- Não registrar senhas, tokens, segredos ou dados pessoais desnecessários.
- Níveis de log devem refletir a gravidade e a possibilidade de ação.
- Logs temporários de depuração devem ser removidos antes da conclusão.
- Erros não devem ser registrados repetidamente em várias camadas sem ganho de contexto.
- Métricas e rastreamento devem ser adicionados quando houver necessidade operacional real.

---

## 9. Testes e qualidade

### 9.1 Testes

- Regras de negócio e fluxos críticos devem ser testados.
- Bugs corrigidos devem receber teste de regressão quando viável.
- Testes devem validar comportamento observável, não detalhes internos sem relevância contratual.
- Testes devem ser determinísticos e independentes.
- Dependências externas devem ser isoladas quando necessário para confiabilidade.
- A quantidade e o tipo de teste devem ser proporcionais ao risco.
- Não manter testes que deixaram de representar o comportamento esperado.

### 9.2 Qualidade

Antes de concluir uma alteração:

- remover código morto;
- remover arquivos órfãos;
- remover imports e dependências não utilizados;
- remover logs e comentários temporários;
- verificar duplicações e estruturas concorrentes;
- executar tipagem, lint, testes e build disponíveis;
- confirmar que o comportamento previsto foi preservado;
- revisar nomes, fronteiras e responsabilidades.

### 9.3 Performance

- Otimizações devem ser motivadas por necessidade real, medição ou risco conhecido.
- Clareza e corretude não devem ser sacrificadas por micro-otimizações sem evidência.
- Gargalos devem ser tratados na origem.
- Cache, memoização, paralelismo e pré-processamento devem possuir estratégia de invalidação, consistência e falha.

---

## 10. Refatoração

Refatoração deve melhorar a estrutura sem alterar comportamento observável, contratos ou regras de negócio, salvo quando a mudança funcional estiver explicitamente incluída no escopo.

### 10.1 Separação de escopos

Distinguir claramente:

- refatoração estrutural;
- alteração funcional;
- mudança arquitetural;
- migração tecnológica;
- correção de bug.

Não combinar escopos independentes sem necessidade.

### 10.2 Regras obrigatórias

- Entender o fluxo existente antes de mover ou remover código.
- Garantir que todo conteúdo necessário esteja na estrutura final antes de remover a estrutura anterior.
- Atualizar imports, referências, testes e configurações afetadas.
- Preservar contratos públicos sem necessidade explícita de alteração.
- Não renomear APIs públicas apenas por preferência estética.
- Não alterar layout, comportamento, estado ou regras de negócio em uma refatoração exclusivamente estrutural.
- Remover definitivamente arquivos, pastas e exports antigos após validar a migração.
- Não manter cópias de segurança dentro da árvore do projeto.
- Confirmar que não existem imports ou referências restantes para estruturas removidas.
- Validar tipagem, lint, testes e build após a mudança.
- Comparar o comportamento antes e depois quando houver risco relevante.

---

# Regras específicas de front-end

## 11. Estrutura do front-end

- Páginas ou telas devem coordenar fluxos, não concentrar toda a implementação.
- Funcionalidades devem agrupar componentes, estado, regras e integrações relacionadas quando isso melhorar coesão.
- Componentes específicos devem permanecer próximos de sua página ou funcionalidade.
- Componentes compartilhados exigem reutilização real e significado consistente.
- Serviços, assets e estilos devem ser organizados por responsabilidade.
- A estrutura não deve depender desnecessariamente de um framework específico.
- Estado deve permanecer no menor escopo capaz de atender aos consumidores.

A arquitetura, a biblioteca de estado, o roteamento e a estratégia de estilos devem ser definidos em `regrasProjeto.md`.

---

## 12. Componentes, páginas e estado

### 12.1 Componentes

- Cada componente deve possuir responsabilidade visual ou comportamental clara.
- Componentes visuais não devem concentrar regras de negócio extensas.
- Props devem formar contratos pequenos, semânticos e previsíveis.
- Evitar componentes excessivamente configuráveis que ocultem múltiplas responsabilidades.
- Extrair um componente quando houver reutilização real, isolamento de comportamento ou ganho claro de leitura.
- Não criar automaticamente pasta, estilos, tipos, constantes e auxiliares para cada componente.
- Preferir composição a grandes conjuntos de flags condicionais.

### 12.2 Páginas e telas

- Páginas devem coordenar carregamento, estado e composição da interface.
- Fluxos complexos devem ser delegados a módulos, hooks ou serviços apropriados.
- Estados de carregamento, erro, vazio e sucesso devem ser tratados explicitamente.
- Navegação e parâmetros devem ser validados antes do uso.

### 12.3 Estado

O estado deve ser classificado pelo menor escopo necessário:

1. estado local do componente;
2. estado compartilhado dentro de uma funcionalidade;
3. estado compartilhado entre páginas ou fluxos;
4. estado global da aplicação;
5. estado remoto proveniente do servidor.

- Preferir estado local quando não houver compartilhamento real.
- Estado global deve representar dados efetivamente compartilhados ou persistentes entre áreas.
- Estado remoto deve possuir estratégia clara de carregamento, atualização, cache e invalidação.
- Dados derivados devem preferencialmente ser calculados, não duplicados.
- Não duplicar o mesmo estado em múltiplas fontes sem estratégia explícita de sincronização.
- Efeitos colaterais devem ser isolados e possuir dependências claras.
- A lógica de estado não deve depender desnecessariamente da camada visual.

### 12.4 Hooks e lógica reutilizável

- Extrair hooks ou equivalentes quando houver lógica de estado ou efeitos reutilizável ou complexa.
- Hooks não devem apenas renomear uma chamada simples sem adicionar significado.
- Dependências e efeitos devem ser previsíveis e testáveis.

### 12.5 Regras de negócio no front-end

- Regras de negócio presentes no front-end devem possuir nomes semânticos e permanecer separadas da renderização.
- Regras complexas devem ser isoladas em módulos testáveis.
- Validações críticas não devem existir exclusivamente no front-end.
- A interface pode antecipar restrições para melhorar a experiência, mas o servidor continua responsável por garantir integridade e autorização.

### 12.6 Navegação e rotas

- Rotas, nomes e parâmetros devem seguir convenção consistente.
- Strings de rotas recorrentes não devem ser espalhadas pela aplicação.
- Uma página não deve depender de detalhes internos de outra página.
- Parâmetros recebidos pela navegação devem ser tratados como entrada externa.
- A aplicação não deve presumir execução obrigatória na raiz do domínio.

---

## 13. Interface, estilos e acessibilidade

### 13.1 Interface

- A interface deve preservar consistência visual e comportamental.
- Estados interativos devem possuir resposta clara.
- Ações destrutivas ou irreversíveis devem exigir tratamento proporcional ao risco.
- Mensagens devem orientar o usuário sem expor detalhes técnicos internos.
- Refatorações estruturais não devem alterar layout ou comportamento visual fora do escopo.

### 13.2 Estilos

- Utilizar uma estratégia principal de estilos definida pelo projeto.
- Reutilizar tokens para cores, espaçamento, tipografia, bordas e dimensões recorrentes.
- Evitar valores mágicos repetidos.
- Estilos específicos devem permanecer próximos do componente quando fizer sentido.
- Estilos globais devem ser restritos a responsabilidades realmente globais.
- Não duplicar sistemas visuais concorrentes.

### 13.3 Responsividade

- Tamanhos e dispositivos suportados devem ser definidos no projeto.
- A interface deve adaptar conteúdo e interação, não apenas reduzir dimensões.
- Evitar dependência exclusiva de largura fixa.
- Testar fluxos críticos nos tamanhos relevantes.

### 13.4 Acessibilidade

- Preferir elementos semânticos nativos.
- Interações devem funcionar por teclado quando aplicável.
- Controles devem possuir nome acessível.
- Estados de foco devem permanecer visíveis.
- Cor não deve ser o único meio de transmitir informação.
- Imagens informativas devem possuir descrição adequada.
- Mudanças importantes de estado devem ser comunicadas de forma acessível.

---

## 14. Comunicação com serviços

- Centralizar clientes, URL base, autenticação e políticas comuns.
- Não espalhar endpoints ou detalhes de transporte pelos componentes.
- A camada visual deve consumir contratos claros.
- Requisições devem tratar carregamento, sucesso, erro, cancelamento e repetição quando aplicável.
- Evitar submissões duplicadas.
- Não assumir que a aplicação será executada na raiz do domínio.
- Dados recebidos devem ser tratados como externos e potencialmente inválidos.
- Validação de interface não substitui validação do servidor.
- Transformações entre contratos externos e modelos internos devem ocorrer em fronteiras identificáveis.
- Cache no cliente deve possuir critérios claros de validade e invalidação.

### 14.1 Formulários

- Estado, validação, envio e resposta devem possuir responsabilidades claras.
- Diferenciar campo ausente, formato inválido, regra de negócio violada, falha de comunicação e erro inesperado.
- Erros devem ser associados ao campo ou ao fluxo correspondente.
- Dados devem ser normalizados antes do envio quando necessário.
- O estado de envio deve impedir ações duplicadas.
- Valores iniciais e reinicialização devem ser previsíveis.

---

## 15. Testes e performance do front-end

### 15.1 Testes

- Priorizar fluxos críticos, validações, regras e integrações.
- Testar comportamento percebido pelo usuário.
- Evitar testes excessivamente acoplados à árvore interna de componentes.
- Componentes puramente visuais simples não exigem testes isolados quando já forem cobertos por fluxos relevantes.
- Navegação, formulários, estados de erro e permissões devem ser testados conforme o risco.

### 15.2 Performance

- Evitar renderizações, cálculos e requisições desnecessárias.
- Não adicionar memoização sem necessidade demonstrada.
- Listas extensas devem considerar paginação, virtualização ou carregamento progressivo.
- Recursos pesados devem ser carregados somente quando necessários.
- Imagens e assets devem usar formatos e dimensões adequados.
- Otimizações não devem comprometer consistência de estado ou clareza da implementação.

---

# Regras específicas de back-end

## 16. Estrutura do back-end

- A inicialização deve apenas carregar configuração, montar dependências e iniciar o sistema.
- Regras de negócio não devem permanecer no ponto de entrada.
- Módulos devem ser organizados por domínio ou responsabilidade.
- Fronteiras entre transporte, aplicação, domínio e infraestrutura devem ser claras quando essas camadas existirem.
- Não criar camadas sem responsabilidade real.
- Configuração e dependências devem ser centralizadas e validadas.
- Implementações de infraestrutura não devem contaminar desnecessariamente o domínio.

A arquitetura concreta, o runtime, o framework, o banco e as integrações devem ser definidos em `regrasProjeto.md`.

---

## 17. Transporte, domínio e casos de uso

### 17.1 Transporte

- Rotas, handlers e controllers devem tratar protocolo, autenticação, entrada e tradução de resposta.
- Controllers devem ser pequenos e não conter regras de negócio extensas.
- Detalhes de HTTP, fila ou CLI não devem vazar para o domínio sem necessidade.
- Respostas devem seguir contratos consistentes.
- Status e códigos de erro devem representar corretamente o resultado.

### 17.2 Casos de uso e serviços

- Casos de uso devem coordenar operações de aplicação.
- Cada caso de uso deve representar uma intenção clara do sistema.
- Serviços não devem se tornar agrupamentos genéricos de funções sem coesão.
- Coordenação, validação de negócio e transações devem possuir fronteiras explícitas.
- Dependências devem ser recebidas de forma identificável e testável.

### 17.3 Domínio

- Regras de negócio devem ser explicitamente nomeadas e centralizadas.
- O domínio não deve depender desnecessariamente de transporte, framework ou banco.
- Invariantes devem ser protegidas na camada adequada.
- Entidades e valores devem representar conceitos reais do negócio, não apenas tabelas.
- Regras não devem ser duplicadas entre controllers, serviços e persistência.

---

## 18. Persistência, contratos e validação

### 18.1 Persistência

- Consultas e detalhes do banco devem permanecer em módulos de persistência identificáveis.
- Controllers não devem acessar o banco diretamente sem justificativa explícita.
- Repositories ou equivalentes devem ser criados quando isolarem consultas, contratos ou dependências relevantes.
- Não criar repositories que apenas repassem chamadas sem agregar fronteira ou significado.
- Consultas devem buscar apenas os dados necessários.
- Integridade deve ser protegida pelo banco quando possível.
- Alterações de schema devem possuir migração versionada.
- Migrações devem ser reproduzíveis e compatíveis com a estratégia de implantação.
- Migrações destrutivas devem definir estratégia de backup, reversão ou recuperação.
- Dados iniciais, dados de teste e dados de produção devem possuir responsabilidades e mecanismos separados.
- Migrações não devem executar cargas arbitrárias de dados sem justificativa e controle explícitos.

### 18.2 Contratos e DTOs

- Entradas e saídas externas devem possuir contratos explícitos.
- DTOs devem representar a fronteira e não necessariamente o modelo interno.
- Não retornar entidades de persistência diretamente quando isso expuser detalhes internos.
- Versionar contratos incompatíveis quando necessário.
- Campos opcionais, nulos e valores padrão devem ser definidos intencionalmente.

### 18.3 Validação

- Toda entrada externa deve ser validada.
- Validação estrutural deve ocorrer antes da regra de negócio.
- Validação estrutural não substitui invariantes do domínio.
- Normalização deve ocorrer de maneira previsível.
- Dados inválidos devem produzir respostas consistentes e sem exposição interna.
- Regras críticas não devem depender apenas de validação no cliente.

---

## 19. Segurança, integrações e consistência

### 19.1 Autenticação e autorização

- Autenticação identifica o agente; autorização define o que ele pode realizar.
- Autorização deve ser validada no servidor para cada operação protegida.
- Aplicar menor privilégio.
- Sessões, tokens e credenciais devem possuir expiração e armazenamento adequados.
- Não confiar em identificadores ou permissões enviados pelo cliente.
- Operações sensíveis devem possuir rastreabilidade proporcional ao risco.

### 19.2 Segurança operacional

- CORS deve permitir somente origens, métodos e cabeçalhos necessários.
- Limites de tamanho, frequência e duração devem ser definidos conforme o risco.
- Rate limiting deve ser aplicado em operações suscetíveis a abuso.
- Credenciais e senhas devem utilizar armazenamento apropriado e nunca ser registradas em texto puro.
- Entradas devem ser protegidas contra injeção, traversal, execução indevida e formatos maliciosos conforme a tecnologia utilizada.
- Configurações permissivas de desenvolvimento não devem ser transportadas automaticamente para produção.

### 19.3 Integrações externas

- Integrações devem ser encapsuladas atrás de contratos internos claros.
- Definir timeout, tratamento de falha, fallback e política de repetição.
- Respostas externas devem ser validadas antes de afetar o estado interno.
- Erros externos devem ser convertidos para erros internos previsíveis.
- Repetições devem evitar duplicação de efeitos.
- Operações não idempotentes não devem ser repetidas automaticamente sem proteção explícita.
- Falhas externas não devem corromper o estado interno.
- Dependência externa indisponível deve produzir comportamento previsível.

### 19.4 Transações e consistência

- Operações compostas devem preservar invariantes.
- Usar transações quando múltiplas alterações precisarem ocorrer de forma atômica.
- Transações devem ser mantidas pelo menor tempo necessário.
- Não realizar chamadas externas dentro de transações sem justificativa forte.
- Processos distribuídos devem definir estratégia para falha parcial, reversão, compensação ou retomada.
- O resultado de falhas intermediárias deve ser conhecido e testável.

### 19.5 Concorrência e idempotência

- Operações sujeitas a repetição devem considerar idempotência.
- Concorrência deve proteger recursos compartilhados e invariantes.
- Não presumir que uma verificação seguida de escrita seja atômica.
- Atualizações concorrentes devem possuir estratégia de bloqueio, versão, restrição ou detecção de conflito quando necessário.
- Filas e tarefas assíncronas devem tratar repetição, ordem, reprocessamento e falha.
- Identificadores idempotentes devem possuir escopo e validade definidos.

### 19.6 Logs

- Registrar contexto suficiente para reconstruir o fluxo.
- Não registrar segredos ou corpos sensíveis indiscriminadamente.
- Correlation IDs ou equivalentes devem ser usados quando necessários para rastrear operações distribuídas.
- Falhas devem ser registradas na camada que possui contexto útil, evitando duplicação sem valor.

---

## 20. Testes e performance do back-end

### 20.1 Testes

- Testes unitários devem proteger regras isoladas.
- Testes de integração devem validar banco, filas, contratos e integrações relevantes.
- Testes end-to-end devem cobrir fluxos críticos quando o risco justificar.
- Persistência deve ser testada contra comportamento real quando mocks não forem suficientes.
- Autorização, validação, transações, concorrência e falhas externas devem receber cobertura proporcional ao risco.
- Testes devem controlar relógio, aleatoriedade e dependências externas quando necessário.

### 20.2 Performance

- Evitar consultas repetidas, N+1, processamento redundante e carregamento excessivo.
- Paginar conjuntos potencialmente grandes.
- Índices devem refletir consultas reais e ser avaliados pelo custo de escrita.
- Cache deve possuir estratégia de invalidação, consistência e fallback.
- Processamento pesado deve ser deslocado para tarefas assíncronas somente quando isso melhorar o fluxo e a confiabilidade.
- Limites de memória, tempo e concorrência devem ser considerados.
- Otimizar com base em métricas, perfis ou risco conhecido.

---

## 21. Checklist final

### 21.1 Geral

- [ ] A alteração respeita `regrasProjeto.md` e este documento.
- [ ] A solução possui responsabilidade e fronteiras claras.
- [ ] A arquitetura é proporcional à complexidade.
- [ ] Não foram criadas abstrações, arquivos ou pastas sem necessidade.
- [ ] Nomes são semânticos e seguem as convenções.
- [ ] Contratos e tipos estão explícitos.
- [ ] Não existem imports, dependências ou código mortos.
- [ ] Erros e entradas externas foram tratados.
- [ ] Dados sensíveis não são expostos ou registrados.
- [ ] Testes relevantes foram criados ou atualizados.
- [ ] Tipagem, lint, testes e build disponíveis foram executados.
- [ ] A documentação afetada foi atualizada.

### 21.2 Front-end

- [ ] Componentes e páginas possuem responsabilidades claras.
- [ ] Estado permanece no menor escopo possível.
- [ ] Não há duplicação desnecessária de estado derivado.
- [ ] Loading, erro, vazio e sucesso foram tratados.
- [ ] Rotas e parâmetros são centralizados e validados.
- [ ] A interface preserva responsividade e acessibilidade.
- [ ] Requisições e formulários evitam ações duplicadas.
- [ ] Layout e comportamento não foram alterados fora do escopo.

### 21.3 Back-end

- [ ] Controllers tratam apenas responsabilidades de transporte.
- [ ] Regras de negócio estão centralizadas.
- [ ] Entradas e respostas possuem contratos e validação.
- [ ] Autenticação e autorização foram aplicadas corretamente.
- [ ] Configurações obrigatórias são validadas na inicialização.
- [ ] Persistência protege integridade e evita consultas desnecessárias.
- [ ] Migrações possuem estratégia segura de implantação e recuperação.
- [ ] Transações, concorrência e idempotência preservam consistência.
- [ ] Integrações possuem timeout, validação e tratamento de falha.
- [ ] Logs permitem diagnóstico sem expor dados sensíveis.

---

Este documento deve permanecer estável. Alterações devem representar evolução real do padrão de desenvolvimento, e não particularidades isoladas de um único projeto.
