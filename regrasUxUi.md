# Regras de UX e UI

## 1. Objetivo e aplicação

Este documento define os padrões permanentes de experiência do usuário, interface, interação, acessibilidade, responsividade, conteúdo e validação aplicáveis a projetos que possuam interface com usuários.

Todo projeto derivado deste repositório deve utilizar estas regras como base para organizar informações, estruturar fluxos, apresentar estados, permitir interações e comunicar resultados.

As decisões concretas de cada projeto, como público-alvo, plataformas suportadas, design system, identidade visual, paleta, tipografia, escala de espaçamento, breakpoints, bibliotecas, componentes, padrões de navegação e nível de acessibilidade exigido, devem ser registradas em `regrasProjeto.md`.

Este documento define resultados e critérios universais. Não determina soluções visuais específicas quando a decisão depender do contexto do produto.

As regras deste documento complementam `regrasDev.md`:

- `regrasDev.md` define como o sistema deve ser estruturado e implementado;
- `regrasUxUi.md` define como a interface deve comunicar, responder e permitir interação;
- `regrasProjeto.md` define as decisões concretas aplicáveis ao projeto.

Em caso de conflito, aplicar a seguinte precedência:

1. exigências legais, técnicas ou obrigatórias da plataforma;
2. requisitos explícitos de acessibilidade definidos para o projeto;
3. `regrasProjeto.md`;
4. este documento;
5. convenções já consolidadas no produto.

Exceções devem ser explícitas, justificadas, documentadas e restritas ao menor escopo possível.

---

## 2. Princípios fundamentais

### 2.1 Clareza

- A interface deve permitir que o usuário identifique onde está, o que está acontecendo, o que pode fazer e qual será o resultado provável de cada ação.
- A ação principal de cada contexto deve ser identificável sem exploração desnecessária.
- Informações essenciais não devem depender de interpretação subjetiva, conhecimento interno do sistema ou tentativa e erro.
- Elementos visuais, textos e comportamentos devem comunicar a mesma intenção.

### 2.2 Simplicidade

- A interface deve utilizar a menor quantidade de elementos, etapas e decisões necessária para permitir que o usuário conclua seu objetivo com segurança.
- Elementos que não contribuam para compreensão, orientação, execução ou confiança devem ser removidos ou reduzidos.
- Simplificação não deve ocultar informações necessárias, eliminar controle relevante ou aumentar risco.
- Opções avançadas devem ser apresentadas somente quando forem necessárias ao contexto.

### 2.3 Consistência

- Elementos com o mesmo significado devem possuir comportamento, nomenclatura e apresentação equivalentes.
- Elementos com significados diferentes não devem ser apresentados de forma indistinguível.
- Padrões consolidados da plataforma devem ser preservados quando melhorarem reconhecimento e previsibilidade.
- Exceções visuais ou comportamentais devem possuir motivo funcional claro.

### 2.4 Previsibilidade

- O usuário deve conseguir antecipar o resultado de uma ação a partir de seu rótulo, contexto e estado.
- Ações não devem produzir efeitos adicionais relevantes sem indicação explícita.
- Mudanças de contexto, navegação, persistência, publicação, exclusão ou envio devem ser comunicadas de forma proporcional ao impacto.
- O mesmo fluxo deve responder de forma estável às mesmas condições.

### 2.5 Eficiência

- A interface deve reduzir cliques, digitação, memorização, repetição e deslocamentos desnecessários.
- Dados já conhecidos pelo sistema não devem ser solicitados novamente sem justificativa.
- Ações frequentes devem permanecer acessíveis e não ser ocultadas por estruturas excessivamente profundas.
- Atalhos podem ser oferecidos para usuários recorrentes, desde que não prejudiquem o fluxo principal.

### 2.6 Reconhecimento antes de memorização

- Informações, opções e ações necessárias devem permanecer visíveis ou facilmente recuperáveis no contexto em que são utilizadas.
- O usuário não deve precisar memorizar dados, códigos, etapas anteriores ou convenções internas para concluir uma tarefa.
- Rótulos, exemplos, histórico e valores atuais devem ser apresentados quando reduzirem carga cognitiva.

### 2.7 Tolerância a erros

- A interface deve prevenir erros previsíveis antes de depender de mensagens de correção.
- Quando um erro ocorrer, o sistema deve preservar o contexto e orientar a recuperação.
- A consequência de uma ação deve ser proporcionalmente protegida por restrições, confirmação ou possibilidade de desfazer.
- Erros do sistema não devem ser apresentados como culpa do usuário.

### 2.8 Controle do usuário

- O usuário deve manter controle sobre ações relevantes e compreender processos automáticos que afetem seus dados ou resultados.
- Fluxos devem permitir cancelar, voltar, revisar ou desfazer quando técnica e semanticamente viável.
- A interface não deve prender o usuário em processos sem saída clara.
- Preferências e decisões explícitas não devem ser alteradas silenciosamente.

### 2.9 Proporcionalidade

- A complexidade visual, informacional e interativa deve ser proporcional à complexidade e ao risco da tarefa.
- Tarefas simples não devem exigir fluxos extensos.
- Tarefas críticas não devem ser simplificadas a ponto de ocultar consequências ou remover validações necessárias.
- Nenhum padrão de interface deve ser aplicado apenas por hábito, simetria ou aparência.

### 2.10 Inclusão

- A interface deve considerar diferentes capacidades, dispositivos, métodos de entrada, níveis de experiência e condições de uso.
- Funcionalidades essenciais não devem depender exclusivamente de visão, audição, precisão motora, percepção de cor ou uso de mouse.
- A experiência principal deve permanecer compreensível e operável sem exigir adaptações improvisadas do usuário.

---

## 3. Arquitetura da informação

### 3.1 Organização semântica

- Conteúdos e funcionalidades devem ser organizados de acordo com os objetivos e o vocabulário do usuário.
- Categorias técnicas internas não devem determinar a organização visível quando não corresponderem ao modelo mental do usuário.
- Informações relacionadas devem permanecer próximas.
- Informações com motivos de uso distintos devem ser separadas quando sua combinação prejudicar compreensão ou operação.

### 3.2 Hierarquia da informação

A informação deve ser estruturada em níveis proporcionais à complexidade real do conteúdo.

Exemplo conceitual:

```text
produto
└── contexto
    └── página ou fluxo
        └── seção
            └── grupo
                └── informação, campo ou ação
```

Nem todos os níveis precisam existir. Cada nível deve possuir função real de agrupamento, orientação ou progressão.

### 3.3 Menor estrutura informacional suficiente

A interface deve utilizar a menor quantidade de níveis, grupos, páginas e etapas capaz de preservar:

- compreensão;
- localização;
- distinção entre responsabilidades;
- progressão lógica;
- segurança;
- recuperação de contexto.

A redução de níveis não deve resultar em telas sobrecarregadas, informações misturadas ou ações concorrentes.

### 3.4 Agrupamento

- Elementos pertencentes à mesma tarefa ou decisão devem permanecer visual e semanticamente relacionados.
- O agrupamento deve ser comunicado por proximidade, título, contêiner, alinhamento ou outra relação perceptível.
- Elementos não relacionados não devem compartilhar grupo apenas por conveniência de layout.
- Grupos excessivamente amplos devem ser avaliados para subdivisão quando prejudicarem localização ou compreensão.

### 3.5 Nomenclatura

- Títulos, rótulos, categorias e ações devem utilizar termos compreendidos pelo público do produto.
- Nomes internos de tabelas, entidades, APIs, classes ou processos não devem aparecer sem necessidade.
- O mesmo conceito deve utilizar a mesma denominação em toda a interface.
- Abreviações devem ser evitadas quando não forem amplamente compreendidas pelo público.

### 3.6 Localização previsível

- Funcionalidades semelhantes devem aparecer em locais equivalentes.
- Ações devem permanecer próximas do conteúdo que afetam.
- Filtros, ordenações e buscas devem permanecer associados ao conjunto de dados controlado.
- Informações globais e locais devem ser diferenciadas.

### 3.7 Divulgação progressiva

- Conteúdo secundário, técnico ou avançado deve ser apresentado somente quando necessário.
- Informações ocultadas devem continuar localizáveis e possuir indicação clara de existência.
- Divulgação progressiva não deve esconder requisitos, custos, riscos ou consequências relevantes.
- A expansão de conteúdo deve preservar o contexto e a posição do usuário.

### 3.8 Densidade informacional

- A densidade deve ser adequada à tarefa, ao dispositivo e à frequência de uso.
- Interfaces operacionais podem apresentar maior densidade quando isso melhorar comparação e eficiência.
- Interfaces introdutórias, críticas ou ocasionais devem priorizar orientação e compreensão.
- A redução de espaços não deve comprometer legibilidade, agrupamento ou área de interação.

### 3.9 Ordem do conteúdo

- A ordem visual deve acompanhar a ordem lógica de leitura, decisão e execução.
- Informações necessárias para uma ação devem aparecer antes ou junto da ação.
- Conteúdo prioritário deve preceder conteúdo complementar.
- A ordem visual não deve divergir da ordem semântica acessível sem justificativa técnica inevitável.

---

## 4. Navegação e orientação

### 4.1 Localização atual

- A interface deve indicar claramente a página, seção, etapa, aba ou contexto atual.
- O estado ativo da navegação deve ser perceptível visualmente e por tecnologias assistivas.
- Títulos devem descrever o conteúdo ou objetivo atual.
- Quando a profundidade justificar, deve existir mecanismo de orientação entre níveis.

### 4.2 Estrutura de navegação

- A navegação deve representar a arquitetura da informação do produto.
- Itens devem ser agrupados por objetivo, domínio ou contexto compreendido pelo usuário.
- A navegação principal não deve funcionar como depósito de todas as funcionalidades existentes.
- Funcionalidades ocasionais podem permanecer em contextos secundários quando continuarem localizáveis.

### 4.3 Profundidade

- A quantidade de níveis deve ser a menor possível sem misturar contextos diferentes.
- Níveis intermediários sem função de orientação ou agrupamento devem ser removidos.
- Cadeias de páginas que apenas encaminham para uma única opção devem ser evitadas.
- O usuário não deve precisar retornar repetidamente à raiz para acessar funções relacionadas.

### 4.4 Continuidade

- Mudanças de página, etapa ou contexto devem preservar informações necessárias para a continuidade da tarefa.
- Filtros, posição de rolagem, seleção e dados não enviados devem ser preservados quando isso corresponder à expectativa do usuário.
- A perda de contexto deve ser explícita quando for inevitável.
- O retorno deve levar ao contexto anterior de forma previsível.

### 4.5 Retorno e cancelamento

- O usuário deve conseguir voltar ou cancelar sem perda inesperada de dados.
- Quando existirem alterações não salvas, a interface deve preservá-las ou comunicar claramente a consequência da saída.
- Cancelar deve interromper a operação atual sem produzir efeitos ocultos.
- Voltar não deve executar ações equivalentes a excluir ou descartar sem confirmação proporcional.

### 4.6 Links e botões

- Links devem ser utilizados para navegação.
- Botões devem ser utilizados para executar ações.
- Elementos com aparência de link ou botão devem possuir comportamento correspondente.
- A ação deve ser identificável pelo rótulo sem depender apenas de ícone.

### 4.7 Navegação por teclado

- Todos os fluxos essenciais devem ser acessíveis por teclado quando a plataforma oferecer esse método de entrada.
- A ordem de foco deve acompanhar a ordem lógica da interface.
- Não devem existir regiões ou controles inacessíveis por teclado.
- Atalhos não devem impedir comandos consolidados da plataforma.

### 4.8 Navegação em fluxos

- Fluxos com múltiplas etapas devem indicar etapa atual, progresso e possibilidade de retorno quando aplicável.
- Cada etapa deve conter apenas decisões semanticamente relacionadas.
- A divisão em etapas deve reduzir carga cognitiva ou risco, não apenas distribuir visualmente campos.
- O usuário deve poder revisar informações antes de ações irreversíveis ou de alto impacto.

---

## 5. Hierarquia visual

### 5.1 Prioridade visual

- A prioridade visual deve corresponder à prioridade funcional e informacional.
- A ação principal deve possuir destaque suficiente para ser localizada sem competir com múltiplas ações equivalentes.
- Ações secundárias, auxiliares e destrutivas devem possuir diferenciação proporcional.
- Destaque visual não deve ser usado apenas para preencher espaço ou produzir impacto estético.

### 5.2 Tipografia

- A tipografia deve estabelecer níveis claros entre títulos, subtítulos, texto principal, texto auxiliar, rótulos e mensagens de estado.
- A quantidade de estilos tipográficos deve ser limitada ao necessário para comunicar hierarquia.
- Texto essencial deve permanecer legível nos tamanhos e ampliações suportados.
- Diferenças de hierarquia não devem depender apenas de tamanho quando peso, posição ou estrutura puderem reforçar o significado.

### 5.3 Espaçamento

- O espaçamento deve representar relações semânticas.
- Elementos do mesmo grupo devem possuir proximidade maior que elementos de grupos distintos.
- Valores concretos devem seguir uma escala consistente definida no projeto.
- Espaçamento não deve ser utilizado para compensar agrupamentos incorretos ou estrutura informacional confusa.

### 5.4 Alinhamento

- Elementos relacionados devem utilizar alinhamento consistente.
- Colunas, rótulos, valores e ações comparáveis devem favorecer leitura e varredura.
- Alinhamentos arbitrários devem ser evitados.
- Mudanças de alinhamento devem possuir justificativa funcional ou responsiva.

### 5.5 Cor

- A cor deve possuir função de hierarquia, identidade, estado ou orientação.
- A mesma cor funcional deve manter o mesmo significado no mesmo contexto.
- Informações não devem depender exclusivamente de cor.
- Cores decorativas não devem competir com estados, alertas ou ações.

### 5.6 Contraste

- Texto, ícones, bordas necessárias, foco e controles devem possuir contraste suficiente em relação ao fundo e aos estados adjacentes.
- O contraste deve atender ao padrão de acessibilidade definido em `regrasProjeto.md`.
- Estados desabilitados não devem se tornar ilegíveis.
- Imagens de fundo não devem comprometer a leitura do conteúdo sobreposto.

### 5.7 Ícones

- Ícones devem representar conceitos reconhecíveis no contexto do público.
- Ícones ambíguos devem possuir rótulo textual ou descrição acessível.
- O mesmo ícone não deve representar ações diferentes no mesmo produto.
- Ícones decorativos devem ser ignorados por tecnologias assistivas.

### 5.8 Ruído visual

Evitar:

- excesso de bordas;
- sombras sem função;
- cores concorrentes;
- ícones decorativos repetidos;
- múltiplas ações com destaque máximo;
- divisores desnecessários;
- animações sem propósito;
- variações tipográficas sem significado.

### 5.9 Identidade visual

- A identidade visual deve reforçar reconhecimento sem prejudicar compreensão, acessibilidade ou eficiência.
- Elementos de marca não devem ocupar prioridade superior à tarefa principal sem motivo de produto.
- Variações visuais devem permanecer dentro dos contratos do design system adotado.

---

## 6. Componentes e consistência

### 6.1 Responsabilidade do componente

- Cada componente deve representar um elemento, padrão informacional ou comportamento identificável.
- Um componente não deve assumir comportamentos incompatíveis sob a mesma aparência.
- Componentes complexos devem ser compostos por partes coerentes quando isso melhorar clareza, manutenção ou acessibilidade.
- A composição não deve produzir APIs visuais difíceis de prever.

### 6.2 Reutilização semântica

- Componentes devem ser compartilhados quando representarem o mesmo significado, comportamento e expectativa de uso.
- Semelhança visual isolada não justifica compartilhamento.
- Componentes específicos devem permanecer próximos do contexto que lhes dá significado.
- Um componente compartilhado não deve acumular exceções incompatíveis para atender casos não relacionados.

### 6.3 Variantes

- Cada variante deve possuir finalidade clara e nome semanticamente coerente.
- Variantes devem representar diferenças reais de prioridade, estado, comportamento ou contexto.
- Não criar variantes apenas para alterar valores visuais isolados que possam ser resolvidos por composição ou token.
- A quantidade de variantes deve permanecer administrável e previsível.

### 6.4 Estados obrigatórios

Componentes interativos devem prever, quando aplicável:

- padrão;
- hover;
- foco;
- ativo;
- selecionado;
- desabilitado;
- somente leitura;
- carregando;
- erro;
- sucesso.

A ausência de um estado deve ser deliberada e não consequência de implementação incompleta.

### 6.5 Elementos nativos

- Elementos nativos da plataforma devem ser preferidos quando atenderem à necessidade.
- Semântica e comportamento nativos não devem ser recriados sem justificativa.
- Componentes personalizados devem preservar operação por teclado, foco, nome, função, estado e valor acessíveis.
- Aparência personalizada não deve remover sinais necessários de interação.

### 6.6 Área de interação

- Controles devem possuir área de clique ou toque adequada ao dispositivo e ao contexto.
- Elementos adjacentes não devem exigir precisão excessiva.
- A área interativa não deve divergir de forma confusa da área visual do controle.
- O tamanho mínimo concreto deve ser definido pelo padrão de acessibilidade e pelos dispositivos suportados no projeto.

### 6.7 Indicação de interação

- Elementos interativos devem parecer interativos.
- Elementos não interativos não devem parecer controles acionáveis.
- Estados de seleção, expansão, edição e arraste devem ser perceptíveis.
- Dependência exclusiva de hover deve ser evitada.

### 6.8 Design system

Quando existir design system:

- componentes, tokens e padrões aprovados devem ser reutilizados;
- variações locais devem ser justificadas;
- novos padrões devem ser incorporados somente após demonstrarem reutilização real;
- inconsistências entre implementação e documentação devem ser corrigidas;
- componentes obsoletos não devem permanecer em uso após migração concluída.

---

## 7. Interação e feedback

### 7.1 Feedback imediato

- Toda ação deve produzir resposta perceptível em tempo compatível com a expectativa do usuário.
- O feedback pode ocorrer por mudança de estado, atualização de conteúdo, indicador de progresso ou mensagem.
- A ausência de resposta não deve fazer o usuário repetir a ação por incerteza.
- Feedback visual deve possuir equivalente acessível quando necessário.

### 7.2 Correspondência entre ação e resposta

- O feedback deve aparecer próximo da ação ou do conteúdo afetado.
- Erros locais devem permanecer associados ao elemento que precisa de correção.
- Resultados globais devem ser comunicados em região adequada ao escopo da mudança.
- A posição do feedback deve permanecer previsível.

### 7.3 Operações demoradas

- Operações perceptivelmente demoradas devem indicar que estão em andamento.
- Quando o progresso for mensurável, deve ser apresentado de forma determinada.
- Quando não for mensurável, deve existir indicação de atividade e contexto.
- Estimativas só devem ser apresentadas quando forem suficientemente confiáveis.

### 7.4 Ações duplicadas

- A interface deve impedir submissões repetidas ou operações conflitantes enquanto uma ação estiver em processamento.
- O bloqueio deve ser limitado ao escopo necessário.
- O usuário deve compreender por que um controle está temporariamente indisponível.
- A conclusão ou falha deve restaurar o estado apropriado.

### 7.5 Confirmações

Solicitar confirmação quando:

- a ação for destrutiva;
- houver impacto relevante em dados ou pessoas;
- a reversão for difícil ou impossível;
- o resultado não for evidente;
- existir risco razoável de acionamento acidental.

Não solicitar confirmação para ações triviais, frequentes e facilmente reversíveis.

### 7.6 Animações e transições

- Animações devem explicar mudança, indicar continuidade, orientar atenção ou comunicar progresso.
- Não devem atrasar operações, bloquear interação ou competir com conteúdo principal.
- A duração deve ser proporcional à mudança.
- Preferências de redução de movimento devem ser respeitadas.

### 7.7 Feedback persistente

- Resultados importantes devem permanecer visíveis até que possam ser compreendidos ou dispensados.
- Mensagens temporárias devem possuir duração proporcional ao conteúdo e ao impacto.
- Informações necessárias para recuperação não devem desaparecer automaticamente.
- O histórico da operação deve permanecer acessível quando fizer parte da tarefa.

### 7.8 Processos automáticos

- Processos automáticos que alterem dados, decisões ou resultados devem ser comunicados quando afetarem a compreensão ou o controle do usuário.
- A interface deve diferenciar recomendação, automação e decisão confirmada.
- O usuário deve conseguir revisar ou corrigir resultados automáticos quando o risco justificar.

---

## 8. Estados da interface

### 8.1 Cobertura de estados

Toda tela, região ou componente dependente de dados deve considerar, quando aplicável:

- estado inicial;
- carregamento;
- conteúdo disponível;
- conteúdo vazio;
- erro;
- conteúdo parcial;
- sucesso;
- desabilitado;
- somente leitura;
- offline ou degradado.

Estados não devem ser tratados como casos posteriores à implementação principal.

### 8.2 Estado inicial

- O estado inicial deve indicar o objetivo da tela e as ações disponíveis.
- Configurações ou dados necessários devem ser solicitados de forma orientada.
- A interface não deve parecer quebrada antes da primeira interação.

### 8.3 Estado de carregamento

- O indicador deve ser compatível com a estrutura e duração esperada.
- Conteúdo previsível pode utilizar representação estrutural temporária.
- Operações breves e indeterminadas podem utilizar indicador simples.
- Operações mensuráveis devem apresentar progresso quando isso ajudar o usuário.
- O carregamento não deve causar mudanças desnecessárias de layout.

### 8.4 Estado vazio

O estado vazio deve explicar, quando aplicável:

- o que está ausente;
- por que a ausência pode ocorrer;
- se existe problema ou condição normal;
- qual ação pode ser realizada.

Mensagens genéricas como `Nenhum dado` devem ser evitadas quando houver orientação mais útil.

### 8.5 Estado de erro

O estado de erro deve informar:

- o que não foi concluído;
- o impacto da falha;
- como tentar novamente;
- como corrigir dados, quando aplicável;
- como buscar suporte, quando necessário.

Detalhes internos, códigos e rastreamentos não devem substituir uma explicação compreensível.

### 8.6 Estado parcial

- Conteúdo válido deve permanecer disponível quando uma falha parcial não comprometer segurança ou consistência.
- A região afetada deve indicar a falha sem bloquear áreas independentes.
- O usuário deve compreender quais informações estão completas e quais estão indisponíveis.

### 8.7 Estado desabilitado

- Controles desabilitados devem possuir motivo compreensível quando esse motivo não for evidente.
- A interface deve informar o requisito necessário para habilitação quando aplicável.
- Controles não devem ser desabilitados apenas para ocultar erro de validação que poderia ser explicado.

### 8.8 Estado de sucesso

- A conclusão deve ser confirmada quando a mudança não for imediatamente visível.
- A mensagem deve informar o que foi concluído.
- Próximas ações devem ser apresentadas quando forem relevantes.
- Confirmações genéricas como `Sucesso` devem ser evitadas quando um resultado específico puder ser informado.

### 8.9 Estado offline ou degradado

- Limitações de conexão devem ser comunicadas.
- Conteúdo disponível localmente deve permanecer acessível quando seguro.
- Ações pendentes devem indicar seu estado e possibilidade de retomada.
- O sistema não deve simular conclusão de operações que ainda não foram confirmadas.

---

## 9. Formulários e entrada de dados

### 9.1 Necessidade dos campos

- Solicitar apenas dados necessários para a tarefa atual ou para uma consequência explicitamente informada.
- Informações já conhecidas pelo sistema devem ser preenchidas ou reutilizadas quando seguro.
- Campos futuros, especulativos ou sem uso definido não devem ser adicionados.
- Dados sensíveis devem possuir justificativa e proteção proporcionais.

### 9.2 Rótulos

- Todo campo deve possuir rótulo persistente e associado semanticamente ao controle.
- Placeholder não deve substituir rótulo.
- Rótulos devem descrever o dado esperado, não a implementação interna.
- Instruções complementares devem permanecer próximas do campo correspondente.

### 9.3 Formato esperado

- Formatos específicos devem ser comunicados por exemplo, máscara, unidade ou instrução.
- A interface deve aceitar variações razoáveis quando puder normalizá-las com segurança.
- Restrições devem ser apresentadas antes do envio quando forem conhecidas.
- Máscaras não devem impedir edição, colagem ou uso de tecnologias assistivas.

### 9.4 Tipo de controle

Utilizar o controle mais adequado à natureza da entrada:

- checkbox para opções independentes;
- radio para escolha exclusiva entre poucas opções visíveis;
- select ou busca para conjuntos maiores;
- campo numérico para números;
- seletor de data para datas quando melhorar a entrada;
- campo de texto quando a resposta não puder ser representada adequadamente por opções.

### 9.5 Ordem de preenchimento

- A ordem dos campos deve acompanhar o fluxo mental e operacional da tarefa.
- Campos relacionados devem permanecer agrupados.
- Dependências entre campos devem ser apresentadas de forma progressiva.
- A ordem visual e a ordem de foco devem permanecer coerentes.

### 9.6 Obrigatoriedade

- Campos obrigatórios e opcionais devem ser identificados de forma consistente.
- O padrão adotado deve ser documentado no projeto.
- Campos condicionais só devem aparecer como obrigatórios quando a condição estiver ativa.
- A obrigatoriedade não deve depender apenas de cor.

### 9.7 Validação

- A validação deve ocorrer no momento mais útil para prevenção ou correção.
- Erros não devem ser apresentados antes de o usuário ter oportunidade razoável de preencher o campo.
- Validações locais e de servidor devem produzir mensagens coerentes.
- A validação não deve remover ou modificar silenciosamente dados válidos.

### 9.8 Mensagens de erro

Mensagens devem:

- identificar o campo ou problema;
- explicar a restrição;
- indicar como corrigir;
- utilizar linguagem não acusatória;
- permanecer disponíveis até a correção ou dispensa adequada.

Mensagens genéricas como `Valor inválido` devem ser evitadas quando a regra puder ser especificada.

### 9.9 Preservação de dados

- Dados preenchidos não devem ser apagados após falha de validação, conexão ou processamento.
- Mudanças de etapa devem preservar informações quando fizerem parte do mesmo fluxo.
- Descarte deliberado deve ser comunicado e confirmado quando houver perda relevante.
- Dados sensíveis podem exigir tratamento diferente por segurança, desde que o comportamento seja informado.

### 9.10 Ações do formulário

- A ação principal deve indicar o resultado, como `Salvar treino` ou `Enviar convite`.
- Ações secundárias não devem competir visualmente com a principal.
- Envio deve ser impedido quando produzir duplicação ou inconsistência.
- A tecla Enter deve possuir comportamento previsível e seguro.

### 9.11 Formulários extensos

- Formulários extensos devem ser agrupados ou divididos somente quando isso reduzir carga cognitiva ou risco.
- A divisão não deve ocultar dependências entre campos.
- Progresso e possibilidade de retorno devem ser apresentados quando existirem múltiplas etapas.
- Resumos devem ser fornecidos antes de confirmações de alto impacto.

---

## 10. Prevenção e recuperação de erros

### 10.1 Prevenção

- Restrições conhecidas devem ser aplicadas antes do envio quando possível.
- Valores impossíveis ou incompatíveis devem ser impedidos ou claramente sinalizados.
- Opções indisponíveis não devem parecer executáveis.
- A prevenção não deve impedir entradas válidas por excesso de restrição.

### 10.2 Valores padrão

- Valores padrão devem ser seguros, previsíveis e adequados à maioria dos casos.
- Padrões não devem autorizar, publicar, excluir ou compartilhar dados sem decisão explícita quando houver impacto relevante.
- Valores herdados ou calculados devem ser identificáveis quando puderem causar interpretação incorreta.

### 10.3 Ações destrutivas

Ações destrutivas devem possuir:

- rótulo explícito;
- diferenciação visual proporcional;
- indicação do objeto afetado;
- confirmação quando necessária;
- possibilidade de desfazer quando viável.

Rótulos genéricos como `Confirmar` devem ser substituídos pelo resultado concreto, como `Excluir treino`.

### 10.4 Desfazer

- Desfazer deve ser preferido a confirmações repetitivas em ações reversíveis.
- A possibilidade de desfazer deve permanecer disponível por tempo suficiente para uso razoável.
- O escopo da reversão deve ser claro.
- O sistema deve informar quando a ação não puder mais ser desfeita.

### 10.5 Recuperação

- Após um erro, a interface deve preservar contexto, dados válidos e caminho de continuidade.
- A correção não deve exigir reiniciar todo o fluxo quando apenas uma etapa falhar.
- Tentativas novamente executadas devem evitar duplicação de efeitos.
- O sistema deve distinguir falha temporária, erro de entrada e indisponibilidade permanente quando isso alterar a ação recomendada.

### 10.6 Erros locais e globais

- Erros locais devem aparecer próximos do elemento afetado.
- Erros globais devem ser utilizados somente quando afetarem a operação inteira ou não puderem ser associados a um elemento específico.
- Uma mensagem global não deve substituir mensagens locais necessárias.
- Múltiplos erros devem ser apresentados de forma que permitam correção previsível.

### 10.7 Mensagens técnicas

- Detalhes técnicos devem ser registrados para diagnóstico, mas não apresentados como explicação principal ao usuário.
- Mensagens externas não devem expor segredos, infraestrutura, rastreamentos ou dados sensíveis.
- Identificadores de suporte podem ser apresentados quando ajudarem o diagnóstico sem comprometer segurança.

---

## 11. Acessibilidade

### 11.1 Princípio geral

- Acessibilidade deve ser considerada desde a estrutura inicial da interface e não apenas após sua conclusão.
- Funcionalidades essenciais devem permanecer perceptíveis, operáveis, compreensíveis e robustas nos contextos definidos pelo projeto.
- O padrão e o nível de conformidade adotados devem ser registrados em `regrasProjeto.md`.

### 11.2 Estrutura semântica

- Elementos devem utilizar semântica correspondente à sua função.
- Títulos devem formar hierarquia coerente.
- Botões devem representar ações, links devem representar navegação e tabelas devem representar dados tabulares.
- Semântica nativa deve ser preferida a atributos adicionais que tentem recriá-la.

### 11.3 Teclado

- Toda funcionalidade essencial deve ser operável por teclado quando aplicável à plataforma.
- Não devem existir armadilhas de foco.
- A ordem de navegação deve acompanhar a sequência lógica.
- Controles personalizados devem possuir interação equivalente ao padrão que representam.

### 11.4 Foco

- O foco deve ser visível em todos os elementos interativos.
- Mudanças de contexto devem mover o foco deliberadamente quando necessário para compreensão.
- Ao fechar elementos temporários, o foco deve retornar ao contexto anterior quando apropriado.
- O estilo de foco não deve ser removido sem substituição perceptível.

### 11.5 Tecnologias assistivas

- Controles devem expor nome, função, estado e valor compreensíveis.
- Mudanças importantes de estado devem ser comunicadas quando não forem identificáveis pela estrutura normal.
- Conteúdo oculto visualmente não deve permanecer acessível quando estiver inativo.
- Atributos de acessibilidade devem complementar a semântica, não substituir elementos adequados.

### 11.6 Contraste e cor

- Informações não devem depender exclusivamente de cor.
- Texto e controles devem atender aos critérios de contraste adotados pelo projeto.
- Estados de foco, erro, sucesso, seleção e desabilitação devem continuar distinguíveis.
- Gráficos e visualizações devem possuir distinções adicionais quando as cores representarem categorias ou valores.

### 11.7 Texto alternativo

- Imagens informativas devem possuir alternativa que comunique sua função ou conteúdo relevante.
- Imagens decorativas devem ser ignoradas por tecnologias assistivas.
- Alternativas não devem repetir texto adjacente sem necessidade.
- Gráficos complexos devem possuir resumo ou representação alternativa dos dados essenciais.

### 11.8 Movimento e tempo

- Preferências de redução de movimento devem ser respeitadas.
- Conteúdo não deve piscar ou mover-se de forma que comprometa segurança ou leitura.
- Limites de tempo devem ser evitados quando não forem necessários.
- Quando houver limite, o usuário deve ser informado e possuir extensão ou recuperação quando viável.

### 11.9 Ampliação e redimensionamento

- A interface deve permanecer utilizável com ampliação de texto e zoom dentro dos requisitos adotados.
- Conteúdo não deve ser cortado, sobreposto ou depender de rolagem em duas direções sem necessidade.
- A ordem e o significado devem ser preservados após reorganização responsiva.

### 11.10 Mídia

- Conteúdo audiovisual deve possuir alternativas adequadas ao tipo de informação.
- Controles de mídia devem ser acessíveis por teclado e tecnologias assistivas.
- Reprodução automática com som deve ser evitada.
- Legendas, transcrições ou descrições devem ser fornecidas quando exigidas pelo conteúdo e pelo nível de conformidade adotado.

---

## 12. Responsividade e dispositivos

### 12.1 Conteúdo antes do dispositivo

- A adaptação deve ser definida pela necessidade do conteúdo e da interação, não apenas por modelos específicos de aparelho.
- Breakpoints devem existir quando o layout deixar de preservar compreensão, operação ou legibilidade.
- Valores concretos devem ser registrados em `regrasProjeto.md` ou no design system.

### 12.2 Fluxo responsivo

- Elementos devem reorganizar-se sem perder ordem semântica ou relações essenciais.
- A interface deve evitar cortes, sobreposições e rolagens desnecessárias.
- Mudanças de disposição não devem alterar o significado das ações.
- Conteúdo principal deve permanecer acessível antes de conteúdo complementar.

### 12.3 Prioridade de conteúdo

- Em espaços reduzidos, conteúdo secundário pode ser recolhido ou movido para acesso sob demanda.
- Ações essenciais não devem desaparecer sem alternativa equivalente.
- Ocultação responsiva não deve remover informações necessárias à decisão atual.
- A prioridade deve ser definida pelo objetivo do usuário, não pela conveniência do layout.

### 12.4 Toque e ponteiro

- Áreas de toque devem ser adequadas e possuir espaçamento suficiente.
- A interface não deve depender exclusivamente de hover.
- Ações de arraste devem possuir alternativa quando forem essenciais.
- Gestos não evidentes devem ser evitados ou acompanhados por indicação e alternativa.

### 12.5 Teclados e entradas móveis

- Campos devem utilizar tipos de entrada adequados para facilitar teclados virtuais e preenchimento.
- A abertura do teclado não deve ocultar o campo, a mensagem de erro ou a ação principal sem possibilidade de acesso.
- Autocompletar deve ser utilizado quando melhorar eficiência e privacidade for preservada.

### 12.6 Tabelas e dados densos

Tabelas e visualizações densas devem adotar estratégia proporcional ao conteúdo, como:

- rolagem horizontal controlada;
- colunas prioritárias;
- detalhamento sob demanda;
- visualização alternativa;
- agrupamento por cartões quando não comprometer comparação.

A estratégia não deve destruir relações tabulares importantes.

### 12.7 Orientação e redimensionamento

- A interface deve permanecer funcional nas orientações e dimensões suportadas.
- Mudanças de tamanho da janela não devem exigir recarregamento ou perda de contexto.
- Restrições de orientação devem existir somente quando forem indispensáveis à tarefa.

### 12.8 Diferentes métodos de entrada

- A interface deve considerar mouse, teclado, toque, caneta e tecnologias assistivas quando aplicáveis.
- Um método não deve bloquear o uso dos demais sem necessidade técnica.
- Estados de foco, hover, toque e seleção devem permanecer coerentes.

---

## 13. Conteúdo e linguagem

### 13.1 Linguagem direta

- Textos devem ser claros, específicos e orientados à tarefa.
- Construções excessivamente formais, ambíguas ou indiretas devem ser evitadas.
- Informações essenciais devem aparecer antes de explicações complementares.
- Frases devem ser tão curtas quanto possível sem perder precisão.

### 13.2 Vocabulário do usuário

- A interface deve utilizar termos conhecidos pelo público e pelo domínio.
- Termos internos de implementação devem ser traduzidos para o conceito compreendido pelo usuário.
- Vocabulário especializado pode ser utilizado quando fizer parte do conhecimento esperado do público.
- Termos potencialmente desconhecidos devem possuir explicação quando forem necessários.

### 13.3 Consistência terminológica

- O mesmo conceito deve possuir o mesmo nome em toda a interface e documentação de uso.
- Sinônimos não devem ser alternados quando puderem sugerir entidades ou ações diferentes.
- Mudanças terminológicas devem ser aplicadas integralmente aos fluxos afetados.
- Glossários podem ser utilizados quando o domínio possuir termos específicos relevantes.

### 13.4 Rótulos de ação

- Botões e comandos devem indicar a ação ou o resultado concreto.
- Rótulos genéricos como `OK`, `Confirmar` ou `Continuar` devem ser evitados quando o resultado não estiver evidente.
- A mesma ação deve manter o mesmo verbo.
- Ações destrutivas devem nomear explicitamente a consequência.

### 13.5 Mensagens de estado

- Mensagens devem informar o que aconteceu, o impacto e a próxima ação quando necessária.
- Mensagens de sucesso devem identificar o resultado concluído.
- Mensagens de erro devem orientar correção ou recuperação.
- Mensagens de carregamento devem identificar a operação quando a espera for relevante.

### 13.6 Tom

- O tom deve ser coerente com o público, o domínio e a gravidade do contexto.
- Situações críticas devem priorizar precisão e ação, sem humor ou linguagem promocional.
- A interface não deve culpar, constranger ou manipular o usuário.
- Textos comerciais não devem ocultar consequências ou reduzir clareza operacional.

### 13.7 Datas, números e unidades

- Datas, horários, números, moedas e unidades devem seguir o contexto regional e o domínio do usuário.
- Unidades devem ser apresentadas junto aos valores quando necessárias à interpretação.
- Precisão numérica deve ser proporcional à decisão realizada.
- Formatos ambíguos devem ser evitados.

### 13.8 Internacionalização

Quando aplicável:

- textos não devem estar concatenados de forma que impeça tradução correta;
- layouts devem suportar variação de comprimento;
- pluralização, gênero, datas, números e unidades devem respeitar a localização;
- conteúdo inserido por usuários deve permanecer distinto do texto traduzido da interface.

---

## 14. Desempenho percebido

### 14.1 Resposta à interação

- A interface deve responder visualmente assim que uma ação for reconhecida.
- Processamento posterior não deve impedir a confirmação de que a interação ocorreu.
- Interações essenciais não devem ser bloqueadas por tarefas secundárias.

### 14.2 Carregamento progressivo

- Conteúdo prioritário deve ser apresentado antes de conteúdo secundário quando possível.
- Partes independentes da interface devem carregar sem bloquear o conjunto inteiro.
- A ordem de carregamento deve preservar compreensão e estabilidade.

### 14.3 Estabilidade visual

- Espaço deve ser reservado para conteúdo assíncrono previsível.
- Elementos não devem mudar de posição inesperadamente durante leitura ou interação.
- Atualizações devem preservar a posição do usuário quando possível.
- Indicadores temporários não devem alterar desnecessariamente as dimensões dos controles.

### 14.4 Atualizações otimistas

Atualizações otimistas podem ser utilizadas quando:

- a probabilidade de sucesso for alta;
- a reversão for segura;
- a falha puder ser comunicada claramente;
- a interface não representar como definitivo um resultado ainda incerto de alto impacto.

### 14.5 Indicadores proporcionais

- Operações instantâneas não devem exibir indicadores que introduzam atraso perceptível.
- Operações demoradas não devem permanecer sem feedback.
- Indicadores devem corresponder ao escopo da região afetada.
- Carregamento global só deve bloquear toda a interface quando a operação realmente impedir qualquer continuidade segura.

### 14.6 Continuidade

- Atualizações parciais devem evitar recarregar toda a interface quando apenas uma região mudou.
- Navegação e filtros devem preservar dados já disponíveis quando adequado.
- O usuário deve poder continuar tarefas independentes durante processamentos secundários.

### 14.7 Métricas

Quando houver necessidade operacional real, acompanhar métricas relacionadas a:

- tempo até conteúdo útil;
- resposta à interação;
- estabilidade visual;
- conclusão de tarefas;
- abandono de fluxo;
- repetição de ações por falta de feedback;
- falhas e tentativas de recuperação.

Métricas devem apoiar decisões e não substituir observação do comportamento real.

---

## 15. Validação e testes de usabilidade

### 15.1 Validação funcional

- Fluxos principais devem ser executados integralmente nos contextos suportados.
- Estados de sucesso, erro, vazio, carregamento e recuperação devem ser verificados.
- A validação deve considerar o comportamento observável, não apenas a renderização da tela.

### 15.2 Inspeção heurística

A interface deve ser avaliada considerando, quando aplicável:

- visibilidade do estado do sistema;
- correspondência com o modelo mental do usuário;
- controle e liberdade;
- consistência;
- prevenção de erros;
- reconhecimento antes de memorização;
- eficiência;
- clareza visual;
- recuperação de falhas;
- disponibilidade de ajuda necessária.

### 15.3 Testes com usuários

- Testes devem utilizar participantes ou perfis representativos quando o risco e o estágio do produto justificarem.
- As tarefas devem reproduzir objetivos reais sem instruir o caminho exato.
- O comportamento observado deve ter prioridade sobre opiniões genéricas.
- O facilitador não deve ensinar a interface durante a execução da tarefa.

### 15.4 Critérios de sucesso

Fluxos relevantes devem possuir critérios mensuráveis, como:

- conclusão da tarefa;
- quantidade e gravidade de erros;
- tempo necessário;
- necessidade de ajuda;
- abandono;
- retrabalho;
- confiança no resultado.

Os valores esperados devem ser definidos em `regrasProjeto.md` ou na documentação do produto quando necessários.

### 15.5 Testes de acessibilidade

A validação deve combinar, quando aplicável:

- ferramentas automáticas;
- inspeção semântica;
- navegação por teclado;
- tecnologias assistivas;
- ampliação e redimensionamento;
- verificação de contraste;
- testes com pessoas com deficiência.

Ferramentas automáticas não são suficientes para declarar conformidade integral.

### 15.6 Dispositivos e contextos

- A interface deve ser validada nas plataformas, navegadores, dimensões e métodos de entrada definidos em `regrasProjeto.md`.
- Simulação não deve substituir integralmente testes em dispositivos reais quando existirem riscos específicos.
- Conexões lentas, falhas parciais e dados extremos devem ser considerados quando fizerem parte do uso esperado.

### 15.7 Regressão visual e comportamental

- Alterações em componentes compartilhados devem ser verificadas nos principais consumidores.
- Mudanças visuais não devem alterar comportamento, ordem de foco ou acessibilidade sem decisão explícita.
- Referências visuais podem ser utilizadas para detectar alterações, mas devem ser acompanhadas por validação semântica e funcional.

### 15.8 Registro de problemas

Problemas encontrados devem registrar:

- contexto;
- objetivo do usuário;
- ação executada;
- resultado observado;
- resultado esperado;
- impacto;
- evidência;
- correção proposta;
- prioridade.

### 15.9 Critério de conclusão

Uma interface só pode ser considerada concluída quando:

- os fluxos principais funcionarem nos contextos suportados;
- estados relevantes estiverem implementados;
- problemas críticos de usabilidade e acessibilidade estiverem resolvidos;
- exceções restantes estiverem documentadas e justificadas;
- o comportamento observado corresponder aos objetivos definidos.

---

## 16. Verificação de conformidade

### 16.1 Princípios

- [ ] O usuário identifica onde está, o que pode fazer e o resultado provável das ações.
- [ ] A interface utiliza a menor complexidade suficiente para a tarefa.
- [ ] Padrões equivalentes mantêm nomenclatura, aparência e comportamento consistentes.
- [ ] A complexidade da interação é proporcional ao risco e ao objetivo.
- [ ] Funcionalidades essenciais não dependem de uma única capacidade ou método de entrada.

### 16.2 Arquitetura da informação

- [ ] Conteúdos e funcionalidades estão organizados segundo objetivos e vocabulário do usuário.
- [ ] Elementos relacionados permanecem próximos.
- [ ] Cada nível de hierarquia possui função real.
- [ ] A quantidade de páginas, grupos e etapas é a menor semanticamente suficiente.
- [ ] Opções avançadas permanecem localizáveis sem sobrecarregar o fluxo principal.

### 16.3 Navegação

- [ ] O contexto atual está claramente identificado.
- [ ] A navegação representa a organização real do produto.
- [ ] Não existem níveis intermediários sem função.
- [ ] É possível voltar ou cancelar sem perda inesperada.
- [ ] Fluxos essenciais podem ser percorridos por teclado quando aplicável.

### 16.4 Hierarquia visual

- [ ] A prioridade visual acompanha a prioridade funcional.
- [ ] Existe apenas uma ação principal por contexto quando aplicável.
- [ ] Tipografia, espaçamento e alinhamento comunicam relações semânticas.
- [ ] Cor não é o único meio de transmitir informação.
- [ ] Não existem elementos decorativos competindo com conteúdo ou estados relevantes.

### 16.5 Componentes

- [ ] Componentes equivalentes possuem comportamento consistente.
- [ ] Variantes representam diferenças semânticas reais.
- [ ] Estados interativos necessários foram implementados.
- [ ] Elementos nativos são utilizados quando adequados.
- [ ] Controles possuem área de interação suficiente e indicação clara de uso.

### 16.6 Feedback e estados

- [ ] Toda ação relevante produz feedback perceptível.
- [ ] Operações demoradas indicam atividade ou progresso.
- [ ] Ações duplicadas ou conflitantes são impedidas quando necessário.
- [ ] Estados inicial, vazio, carregando, erro e sucesso foram considerados.
- [ ] Falhas parciais não bloqueiam regiões independentes sem necessidade.

### 16.7 Formulários

- [ ] Apenas dados necessários são solicitados.
- [ ] Todos os campos possuem rótulo persistente.
- [ ] Formatos e restrições são informados antes ou durante o preenchimento.
- [ ] Mensagens de erro explicam como corrigir.
- [ ] Dados válidos são preservados após falhas.
- [ ] A ação principal descreve o resultado concreto.

### 16.8 Erros

- [ ] Erros previsíveis são prevenidos quando possível.
- [ ] Ações destrutivas nomeiam explicitamente a consequência.
- [ ] A possibilidade de desfazer é utilizada quando adequada.
- [ ] Erros locais permanecem associados ao elemento afetado.
- [ ] Mensagens externas não expõem detalhes internos ou dados sensíveis.

### 16.9 Acessibilidade

- [ ] A estrutura utiliza semântica adequada.
- [ ] Funcionalidades essenciais são operáveis por teclado.
- [ ] O foco é visível e possui ordem lógica.
- [ ] Controles expõem nome, função, estado e valor compreensíveis.
- [ ] Contraste, cor, ampliação e redução de movimento foram considerados.
- [ ] Imagens e mídias possuem alternativas adequadas quando necessárias.

### 16.10 Responsividade

- [ ] A interface funciona nas dimensões e dispositivos definidos pelo projeto.
- [ ] A reorganização preserva ordem semântica e ações essenciais.
- [ ] A interface não depende exclusivamente de hover ou gestos não evidentes.
- [ ] Campos e controles permanecem utilizáveis com teclado virtual.
- [ ] Conteúdo denso utiliza estratégia adequada sem destruir relações importantes.

### 16.11 Conteúdo

- [ ] O mesmo conceito utiliza o mesmo termo em toda a interface.
- [ ] Rótulos descrevem ações concretas.
- [ ] Mensagens informam resultado, impacto e próxima ação quando necessária.
- [ ] Datas, números, unidades e moedas seguem o contexto do usuário.
- [ ] O tom é proporcional ao público e à gravidade da situação.

### 16.12 Desempenho percebido

- [ ] A interface responde imediatamente ao reconhecimento da interação.
- [ ] Conteúdo prioritário é apresentado antes de conteúdo secundário quando possível.
- [ ] O layout permanece estável durante carregamentos e atualizações.
- [ ] Indicadores de progresso são proporcionais à duração e ao escopo da operação.
- [ ] Tarefas secundárias não bloqueiam interações independentes sem necessidade.

### 16.13 Validação

- [ ] Os fluxos principais foram executados integralmente.
- [ ] Cenários de erro, vazio, carregamento e recuperação foram testados.
- [ ] Navegação por teclado e estrutura acessível foram verificadas.
- [ ] Contextos de dispositivo e entrada definidos no projeto foram validados.
- [ ] Problemas encontrados foram corrigidos ou documentados com justificativa.
- [ ] A interface atende aos critérios de sucesso definidos para o produto.
