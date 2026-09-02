# Regras de UX e UI

## 1. Objetivo

Este documento define as normas universais de experiência do usuário, interface, interação, acessibilidade, responsividade, conteúdo e validação aplicáveis a projetos que possuam interação humana.

Seu objetivo é garantir que a interface utilize a menor estrutura visual e informacional suficiente para permitir compreensão, operação, orientação, acessibilidade e recuperação de contexto.

As decisões concretas de cada projeto, como público, plataformas, design system, identidade visual, paleta, tipografia, espaçamento, breakpoints, bibliotecas, componentes, dispositivos e nível de acessibilidade, pertencem ao `regrasProjeto.md`.

---

## 2. Natureza normativa e mutabilidade

Este documento é:

- normativo;
- universal;
- canônico;
- imutável no contexto de um projeto.

Durante a criação, manutenção ou normalização de um projeto:

- seu conteúdo não pode ser adaptado ao projeto;
- regras não utilizadas não podem ser removidas;
- decisões visuais específicas não podem ser incorporadas localmente;
- sua aplicabilidade e concretização devem ser registradas em `regrasProjeto.md`;
- incompatibilidades devem ser registradas como não conformidades;
- uma incompatibilidade não autoriza modificar, ignorar, reduzir ou suspender a regra universal.

Este documento somente pode ser alterado quando o objeto da alteração for o próprio padrão universal mantido no repositório `base`.

---

## 3. Relação entre os documentos

- `regrasDev.md` define como o sistema deve ser estruturado e implementado.
- `regrasUxUi.md` define como a interface deve comunicar, responder e permitir interação.
- `regrasProjeto.md` concretiza as decisões específicas do produto.
- o código implementa essas decisões.
- o `README.md` descreve o estado efetivamente implementado.

`regrasDev.md` e `regrasUxUi.md` devem ser aplicados cumulativamente.

`regrasProjeto.md` pode escolher tecnologias, valores e estratégias, mas não pode reduzir, contradizer ou dispensar os critérios universais.

### Conceitos transversais

Este documento aplica o mecanismo canônico de classificação, fonte canônica e especialização de conceitos transversais definido em `regrasDev.md`.

No escopo de experiência e interface:

- quando esse mecanismo classificar a responsabilidade fundamental de um conceito como experiência ou interface, este documento contém a definição canônica desse conceito específico;
- quando a responsabilidade fundamental for de engenharia ou arquitetura, este documento contém somente as especializações necessárias à experiência e à interface;
- uma especialização presente neste documento deve preservar integralmente o significado, os critérios mínimos e as restrições da definição canônica;
- uma especialização não pode redefinir o conceito, criar critério concorrente nem constituir segunda fonte canônica;
- uma obrigação transversal aplicável ao escopo deste documento deve ser explicitada aqui sempre que sua ausência puder permitir interpretação local incompleta;
- essa explicitação deve identificar a dependência normativa ou especializar suas consequências observáveis e interativas sem repetir desnecessariamente a definição canônica.

---

## 4. Aplicação independente e cumulativa

Cada regra deve ser analisada, aplicada e validada independentemente das demais.

O atendimento a uma regra não implica atendimento, substituição ou dispensa de outra.

As regras são cumulativas, salvo dependência, precedência, exceção ou não aplicabilidade declarada explicitamente.

Cada regra universal deve ser:

- independente;
- objetiva;
- afirmativa;
- verificável;
- tecnologicamente neutra;
- semanticamente singular.

Quando uma interpretação divergente já tiver ocorrido, a norma correspondente não pode permanecer apenas implícita.

---

## 5. Precedência e conflitos

Em caso de conflito real:

1. exigências legais e restrições técnicas incontornáveis da plataforma;
2. `regrasDev.md` e `regrasUxUi.md`, aplicados cumulativamente;
3. requisitos e decisões específicas de `regrasProjeto.md`;
4. código-fonte e convenções consolidadas no produto.

A precedência aplica-se somente ao escopo incompatível.

Não constituem conflito normativo:

- preferência estética;
- hábito;
- conveniência;
- prazo;
- custo evitável;
- tecnologia escolhida sem obrigatoriedade;
- convenção de dispositivo específico.

Acessibilidade prevalece sobre identidade visual, animações, densidade, personalização estética e convenções locais quando não for possível satisfazê-las simultaneamente.

---

## 6. Não conformidades e exceções

Uma violação inevitável deve ser registrada em `regrasProjeto.md` como não conformidade, contendo:

- regra afetada;
- causa;
- escopo;
- impacto;
- risco;
- medida compensatória;
- tratamento planejado;
- critério ou prazo para correção.

O registro não modifica nem suspende a regra.

Uma exceção somente é válida quando a própria norma universal a autorizar.

Nenhuma exceção pode reduzir conformidade abaixo de exigências legais, técnicas obrigatórias ou requisitos mínimos de acessibilidade da plataforma.

---

# Parte I — Princípios fundamentais

## 7. Clareza

A interface deve permitir que o usuário identifique:

- onde está;
- o que está acontecendo;
- o que pode fazer;
- sobre qual objeto atua;
- qual resultado provável ocorrerá;
- como recuperar-se de falhas.

Informações essenciais não devem depender de tentativa e erro, conhecimento interno ou interpretação subjetiva.

## 8. Simplicidade

A interface deve utilizar a menor quantidade de elementos, etapas e decisões capaz de permitir conclusão segura da tarefa.

Simplificação não pode:

- ocultar informação necessária;
- eliminar controle relevante;
- aumentar risco;
- destruir agrupamentos;
- remover contexto;
- prejudicar acessibilidade.

## 9. Consistência

- Elementos com o mesmo significado devem possuir comportamento, nomenclatura e apresentação equivalentes.
- Elementos com significados diferentes não devem ser apresentados de forma indistinguível.
- Padrões nativos da plataforma devem ser preservados quando melhorarem reconhecimento e previsibilidade.
- Exceções visuais e comportamentais exigem motivo funcional.

## 10. Previsibilidade

- O resultado de uma ação deve ser antecipável por rótulo, contexto e estado.
- Ações não devem produzir efeitos adicionais relevantes sem indicação.
- Mudanças de navegação, persistência, publicação, exclusão ou envio devem ser comunicadas proporcionalmente ao impacto.
- O mesmo fluxo deve responder de forma estável às mesmas condições.

## 11. Eficiência

A interface deve reduzir:

- cliques;
- digitação;
- memorização;
- repetição;
- deslocamento;
- espera;
- retomadas desnecessárias.

Dados já conhecidos não devem ser solicitados novamente sem justificativa.

## 12. Reconhecimento antes de memorização

Informações, opções e ações necessárias devem permanecer visíveis ou facilmente recuperáveis no contexto de uso.

O usuário não deve precisar memorizar dados, códigos, etapas anteriores ou convenções internas para concluir uma tarefa.

## 13. Tolerância a erros

- Erros previsíveis devem ser prevenidos antes de depender de mensagens de correção.
- Falhas devem preservar contexto e orientar recuperação.
- Consequências devem ser protegidas conforme risco e reversibilidade.
- Erros do sistema não devem ser apresentados como culpa do usuário.

## 14. Controle do usuário

- O usuário deve compreender processos automáticos que afetem dados ou resultados.
- Fluxos devem permitir cancelar, voltar, revisar ou desfazer quando viável.
- A interface não deve prender o usuário em processo sem saída clara.
- Preferências explícitas não devem ser alteradas silenciosamente.

## 15. Proporcionalidade

A complexidade visual, informacional e interativa deve ser proporcional:

- à tarefa;
- à frequência de uso;
- ao risco;
- ao impacto;
- à experiência do público;
- ao dispositivo;
- ao contexto operacional.

## 16. Inclusão

A interface deve considerar diferentes:

- capacidades;
- dispositivos;
- métodos de entrada;
- níveis de experiência;
- condições ambientais;
- tecnologias assistivas.

Funcionalidades essenciais não podem depender exclusivamente de visão, audição, precisão motora, percepção de cor, mouse ou hover.

---

# Parte II — Arquitetura da informação

## 17. Organização semântica

Conteúdos e funcionalidades devem ser organizados conforme objetivos e vocabulário do usuário.

Categorias técnicas internas não devem determinar a organização visível quando não corresponderem ao modelo mental do público.

## 18. Hierarquia informacional

A informação deve utilizar somente os níveis necessários.

Exemplo conceitual:

```text
produto
└── contexto
    └── página ou fluxo
        └── seção
            └── grupo
                └── informação, campo ou ação
```

Cada nível deve possuir função real de agrupamento, orientação ou progressão.

## 19. Menor estrutura informacional suficiente

A interface deve utilizar a menor quantidade de páginas, níveis, grupos e etapas capaz de preservar:

- compreensão;
- localização;
- distinção de responsabilidades;
- progressão lógica;
- segurança;
- recuperação de contexto.

A redução não pode produzir telas sobrecarregadas, informação misturada ou ações concorrentes.

## 20. Agrupamento perceptível

A relação entre elementos deve permanecer perceptível, especialmente entre:

- rótulo e controle;
- título e conteúdo;
- ação e objeto afetado;
- erro e campo;
- legenda e dado;
- estado e componente;
- grupo e seus elementos.

O agrupamento pode ser comunicado por:

- proximidade;
- alinhamento;
- título;
- separador;
- fundo;
- contêiner;
- outro recurso proporcional.

## 21. Nomenclatura

- Títulos, rótulos, categorias e ações devem utilizar termos compreendidos pelo público.
- Nomes internos de tabelas, entidades, APIs e classes não devem aparecer sem necessidade.
- O mesmo conceito deve utilizar a mesma denominação.
- Abreviações devem ser evitadas quando não forem conhecidas pelo público.

## 22. Localização previsível

- Funcionalidades semelhantes devem aparecer em locais equivalentes.
- Ações devem permanecer próximas do conteúdo afetado.
- Filtros, ordenações e buscas devem permanecer associados ao conjunto controlado.
- Informações globais e locais devem ser diferenciadas.

## 23. Divulgação progressiva

Conteúdo secundário, técnico ou avançado pode permanecer oculto até ser necessário quando:

- sua existência continuar perceptível;
- sua recuperação for direta;
- sua ocultação não aumentar risco;
- o contexto for preservado.

Divulgação progressiva não pode esconder requisitos, custos, riscos, consequências ou informação essencial.

## 24. Ordem do conteúdo

A ordem visual deve acompanhar a ordem lógica de:

- leitura;
- foco;
- decisão;
- navegação;
- execução.

Informações necessárias devem aparecer antes ou junto da ação correspondente.

A ordem visual não deve divergir da ordem semântica acessível sem justificativa técnica inevitável.

---

# Parte III — Densidade e compactação

## 25. Densidade informacional

Densidade é a relação entre informação útil e espaço utilizado, não apenas redução de dimensões.

Uma interface não é melhor apenas por possuir menor altura ou largura quando isso aumentar:

- esforço de leitura;
- ambiguidade;
- quantidade de ações;
- precisão motora exigida;
- quebras;
- rolagem horizontal;
- perda de contexto.

## 26. Densidade conforme a natureza do conteúdo

Podem aceitar maior densidade:

- tabelas;
- métricas;
- comparações;
- painéis operacionais;
- listas repetitivas;
- dados estruturados.

Devem priorizar maior orientação e espaçamento:

- formulários críticos;
- conteúdo narrativo;
- onboarding;
- avisos;
- decisões de risco;
- tarefas ocasionais.

A aplicação não precisa utilizar uma única densidade em todos os contextos.

## 27. Ordem de compactação

Ao aumentar densidade, avaliar na seguinte ordem:

1. remover informação redundante;
2. eliminar contêineres sem função;
3. reduzir margens externas excedentes;
4. reduzir espaços entre elementos relacionados;
5. reduzir paddings excedentes;
6. simplificar bordas, fundos e sombras;
7. otimizar distribuição, alinhamento e grades;
8. abreviar conteúdo redundante;
9. ajustar tipografia auxiliar;
10. reduzir dimensões interativas somente quando acessibilidade, dispositivo e contexto permitirem.

A sequência deve parar assim que a densidade necessária for alcançada.

## 28. Informação redundante

Conteúdo pode ser abreviado, combinado ou removido visualmente quando o significado permanecer inequívoco.

Quando a forma compacta não for suficiente para tecnologias assistivas, o nome ou a descrição acessível completa deve ser preservado.

## 29. Informação essencial

Dados necessários para compreender ou executar a tarefa devem permanecer disponíveis no momento adequado.

A classificação entre essencial e secundário deve ser definida em `regrasProjeto.md` quando depender do produto.

---

# Parte IV — Hierarquia visual

## 30. Menor estrutura visual suficiente

A interface deve utilizar o menor número de:

- contêineres;
- níveis;
- separadores;
- fundos;
- bordas;
- sombras;
- estilos;

capaz de preservar:

- compreensão;
- agrupamento;
- hierarquia;
- operação;
- acessibilidade;
- recuperação de contexto.

Redução estrutural não pode misturar responsabilidades, tornar agrupamentos ambíguos ou eliminar sinais necessários.

## 31. Função dos contêineres visuais

Bordas, fundos, sombras, raios e paddings devem existir somente quando contribuírem para:

- agrupamento;
- separação;
- hierarquia;
- estado;
- interatividade;
- orientação;
- legibilidade.

Contêineres aninhados devem ser simplificados quando repetirem a mesma função visual.

A remoção de um contêiner deve preservar a relação perceptível dos elementos agrupados.

## 32. Prioridade visual

- A prioridade visual deve corresponder à prioridade funcional e informacional.
- A ação principal deve ser localizável sem competir com várias ações equivalentes.
- Ações secundárias, auxiliares e destrutivas devem possuir diferenciação proporcional.
- Destaque não deve existir apenas para produzir impacto estético.

## 33. Tipografia

- A tipografia deve estabelecer níveis claros.
- A quantidade de estilos deve ser limitada ao necessário.
- Texto essencial deve permanecer legível nos tamanhos e ampliações suportados.
- Hierarquia não deve depender somente de tamanho.

## 34. Espaçamento

- Espaçamento deve representar relações semânticas.
- Elementos do mesmo grupo devem possuir proximidade maior que grupos distintos.
- Valores concretos devem seguir escala definida no projeto.
- Espaçamento não deve compensar estrutura informacional incorreta.

## 35. Alinhamento

- Elementos relacionados devem utilizar alinhamento consistente.
- Colunas, rótulos, valores e ações comparáveis devem favorecer varredura.
- Mudanças de alinhamento exigem justificativa funcional ou responsiva.

## 36. Cor e contraste

- Cor deve possuir função de hierarquia, identidade, estado ou orientação.
- Informação não pode depender exclusivamente de cor.
- Texto, ícones, foco e controles devem possuir contraste suficiente.
- Estados desabilitados devem permanecer legíveis.
- Valores concretos pertencem ao padrão de acessibilidade definido no projeto.

## 37. Ícones

- Ícones devem representar conceitos reconhecíveis.
- Ícones ambíguos devem possuir rótulo ou descrição acessível.
- O mesmo ícone não deve representar ações diferentes no mesmo produto.
- Ícones decorativos devem ser ignorados por tecnologias assistivas.

## 38. Ruído visual

Evitar:

- excesso de bordas;
- sombras sem função;
- cores concorrentes;
- ícones decorativos repetidos;
- múltiplas ações com destaque máximo;
- divisores desnecessários;
- animações sem propósito;
- variações tipográficas sem significado.

## 39. Identidade visual

A identidade visual deve reforçar reconhecimento sem prejudicar compreensão, acessibilidade ou eficiência.

Elementos de marca não devem superar a prioridade da tarefa principal sem motivo de produto.

---

# Parte V — Componentes e estados

## 40. Responsabilidade do componente

- Cada componente deve representar elemento, padrão informacional ou comportamento identificável.
- Um componente não deve assumir comportamentos incompatíveis sob a mesma aparência.
- Componentes complexos devem ser compostos quando isso melhorar clareza, manutenção ou acessibilidade.
- A composição não deve produzir APIs imprevisíveis.

## 41. Reutilização semântica

Compartilhar componente somente quando ele representar:

- mesmo significado;
- mesmo comportamento;
- mesmo contrato;
- mesma expectativa de uso;
- evolução previsivelmente conjunta.

Semelhança visual isolada não justifica compartilhamento.

## 42. Variantes

- Cada variante deve possuir finalidade clara e nome semântico.
- Variantes devem representar prioridade, estado, comportamento, intenção ou contexto.
- Não criar variante apenas para transportar valor visual isolado.
- A quantidade de variantes deve permanecer previsível.

## 43. Estados obrigatórios

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

A ausência de estado deve ser deliberada.

Textos como `Selecionado` ou `Ativo` não são obrigatórios quando o estado já for perceptível sem depender apenas de cor e estiver exposto programaticamente.

### 43.1 Estados e transições de interface

Os estados e transições da interface especializam o modelo comportamental definido em `regrasDev.md` e não constituem modelo concorrente.

Devem integrar esse modelo, quando alterarem comportamento semanticamente relevante, estados relacionados a:

- foco;
- seleção;
- expansão;
- edição;
- carregamento;
- sucesso;
- erro;
- vazio ou ausência;
- indisponibilidade;
- confirmação;
- fluxos temporários, como diálogos, menus e sobreposições;
- estado exposto às tecnologias assistivas.

Ações do usuário, métodos de entrada, resultados de operações, mudanças de contexto e demais causas observáveis devem ser tratadas como causas de transição quando produzirem mudança semântica.

### 43.2 Consistência semântica do estado

A fonte canônica e a sincronização dos estados de interface obedecem às regras de estados semânticos definidas em `regrasDev.md`.

Em um estado estável, devem representar o mesmo significado semântico:

- apresentação visual;
- comportamento interativo;
- conteúdo apresentado;
- estado acessível;
- disponibilidade das ações.

Uma representação não pode indicar seleção, disponibilidade, conclusão, erro, expansão ou outro estado enquanto outra representação do mesmo conceito indicar estado semanticamente incompatível.

Quando a plataforma exigir representações derivadas ou transitórias distintas, sua sincronização deve permanecer determinística e não pode expor significado contraditório como estado válido.

## 44. Elementos nativos

- Elementos nativos devem ser preferidos quando atenderem à necessidade.
- Semântica e comportamento nativos não devem ser recriados sem justificativa.
- Componentes personalizados devem preservar teclado, foco, nome, função, estado e valor acessíveis.
- Aparência personalizada não deve remover sinais necessários.

## 45. Área de interação

- Controles devem possuir área adequada ao dispositivo e contexto.
- Elementos adjacentes não devem exigir precisão excessiva.
- Área interativa não deve divergir de forma confusa da área visual.
- Dimensões mínimas concretas pertencem ao `regrasProjeto.md`.

Para esta regra, área adequada e precisão excessiva devem ser avaliadas contra as dimensões concretas de interação e o padrão de acessibilidade adotados em `regrasProjeto.md`, considerando o dispositivo e o método de entrada suportados.

## 46. Indicação de interação

- Elementos interativos devem parecer interativos.
- Elementos não interativos não devem parecer controles.
- Seleção, expansão, edição e arraste devem ser perceptíveis.
- Funcionalidade essencial não deve depender exclusivamente de hover.

## 47. Design system

Quando existir:

- componentes, tokens e padrões aprovados devem ser reutilizados;
- variações locais devem ser justificadas;
- novos padrões devem demonstrar reutilização real;
- inconsistências entre implementação e documentação devem ser corrigidas;
- componentes obsoletos devem ser removidos após migração.

---

# Parte VI — Navegação e orientação

## 48. Localização atual

A interface deve indicar claramente página, seção, etapa, aba ou contexto atual.

Estado ativo deve ser perceptível visualmente e por tecnologias assistivas.

## 49. Estrutura de navegação

- A navegação deve representar a arquitetura da informação.
- Itens devem ser agrupados por objetivo, domínio ou contexto do usuário.
- A navegação principal não deve ser depósito de todas as funcionalidades.
- Funções ocasionais podem permanecer em contextos secundários quando localizáveis.

## 50. Profundidade

- A quantidade de níveis deve ser a menor possível sem misturar contextos.
- Níveis intermediários sem função devem ser removidos.
- Páginas que apenas encaminham para uma única opção devem ser evitadas.
- O usuário não deve retornar repetidamente à raiz para acessar funções relacionadas.

## 51. Continuidade

Toda transição de interface deve preservar as propriedades de estado cuja alteração não faça parte dos efeitos definidos no modelo comportamental.

Isso inclui, quando aplicável:

- busca;
- filtros;
- paginação;
- rolagem;
- seleção;
- dados não enviados;
- foco;
- expansão;
- contexto da tarefa.

Reinicialização, invalidação ou descarte dessas propriedades deve constituir efeito explícito da transição correspondente.

Perda inevitável de contexto deve ser explícita.

## 52. Retorno e cancelamento

- Voltar ou cancelar não deve causar perda inesperada.
- Alterações não salvas devem ser preservadas ou ter consequência comunicada.
- Cancelar deve produzir somente os efeitos compatíveis com a semântica declarada para a operação conforme a seção 59.1 e não pode ocultar efeitos já produzidos.

## 53. Links e botões

- Links representam navegação.
- Botões executam ações.
- Aparência e comportamento devem corresponder.
- A intenção não deve depender apenas de ícone.

## 54. Fluxos com etapas

Fluxos de múltiplas etapas devem indicar:

- etapa atual;
- progresso;
- possibilidade de retorno;
- consequência da continuidade.

Cada etapa deve conter decisões semanticamente relacionadas.

---

# Parte VII — Interação e feedback

## 55. Feedback imediato

Toda ação deve produzir resposta perceptível em tempo compatível com a expectativa.

A ausência de resposta não deve induzir repetição por incerteza.

Quando a classificação temporal depender do produto, expressões como tempo compatível, operação instantânea ou operação demorada devem ser interpretadas segundo as metas de resposta percebida e os requisitos de desempenho concretizados em `regrasProjeto.md`.

## 56. Correspondência entre ação e resposta

- Feedback deve aparecer próximo da ação ou conteúdo afetado.
- Erros locais permanecem associados ao elemento corrigível.
- Resultados globais devem ser comunicados em região correspondente ao escopo.

## 57. Operações demoradas

- Operações perceptíveis devem indicar atividade.
- Progresso mensurável deve ser apresentado quando útil.
- Estimativas só devem ser exibidas quando confiáveis.

## 58. Ações duplicadas

- Submissões repetidas ou operações conflitantes devem ser impedidas quando necessário.
- O bloqueio deve ser limitado ao escopo afetado.
- Conclusão ou falha deve restaurar estado apropriado.

### 58.1 Acionamentos equivalentes e intenção única

Quando clique, toque, `Enter`, tecla de ativação, atalho, comando de tecnologia assistiva ou outro método suportado representarem a mesma ação semântica, todos devem convergir para a mesma intenção comportamental e, quando houver efeito de domínio, para a mesma intenção de domínio.

Uma única interação física ou ativação lógica não pode executar a mesma intenção comportamental mais de uma vez por sobreposição de handlers, comportamento nativo combinado com handler manual, propagação, submissão implícita, atalhos concorrentes ou mecanismos equivalentes. Quando existir intenção de domínio associada, ela também não pode ser duplicada pelo mesmo evento.

A execução única da intenção não proíbe múltiplos efeitos internos coordenados necessários à mesma ação.

Nova interação deliberada do usuário constitui novo evento e não deve ser descartada indevidamente; quando repetição rápida puder produzir conflito ou duplicação de efeito, o bloqueio deve seguir a regra de ações duplicadas e permanecer limitado ao escopo necessário.

## 59. Confirmações e desfazer

Solicitar confirmação quando houver:

- destruição;
- impacto relevante;
- reversão difícil;
- resultado não evidente;
- risco de acionamento acidental.

Preferir desfazer a confirmações repetitivas em ações reversíveis.

### 59.1 Cancelamento, desfazer e reversibilidade

A interface somente pode oferecer `Cancelar`, `Desfazer`, restaurar ou ação equivalente quando a operação subjacente possuir semântica técnica compatível com o efeito comunicado, conforme definido em `regrasDev.md`.

`Cancelar` deve distinguir, quando necessário, entre impedir uma operação ainda não efetivada, interromper processamento futuro e desfazer efeitos já produzidos.

`Desfazer` somente pode comunicar restauração quando a operação for reversível ou quando existir compensação cuja consequência seja semanticamente equivalente ao resultado prometido.

Quando existirem efeitos irrevogáveis, reversão parcial ou compensação que não restaure exatamente o estado anterior, essa limitação deve ser comunicada antes de o usuário depender da ação.

Uma ação de recuperação não pode prometer restauração, cancelamento ou reversão mais forte do que a garantia técnica disponível.

## 60. Animações

Animações devem explicar mudança, continuidade, atenção ou progresso.

Não devem atrasar operações, bloquear interação ou competir com conteúdo.

Preferências de redução de movimento devem ser respeitadas.

## 61. Processos automáticos

A interface deve diferenciar:

- recomendação;
- automação;
- decisão confirmada.

Resultados automáticos devem poder ser revisados ou corrigidos quando o risco justificar.

---

# Parte VIII — Estados da interface

## 62. Cobertura de estados

Toda tela, região ou componente dependente de dados deve considerar, quando aplicável:

- inicial;
- carregamento;
- conteúdo disponível;
- vazio;
- erro;
- parcial;
- sucesso;
- desabilitado;
- somente leitura;
- offline ou degradado.

Estados não devem ser tratados somente depois da implementação principal.

## 63. Estado inicial

Deve indicar objetivo e ações disponíveis sem parecer quebrado antes da primeira interação.

## 64. Carregamento

- O indicador deve ser compatível com estrutura e duração.
- Conteúdo previsível pode usar representação estrutural temporária.
- Carregamento não deve causar mudanças desnecessárias de layout.

## 65. Estado vazio

Deve explicar, quando aplicável:

- o que está ausente;
- por que a ausência ocorre;
- se é condição normal ou problema;
- qual ação pode ser realizada.

## 66. Estado de erro

Deve informar:

- o que não foi concluído;
- impacto;
- forma de tentar novamente;
- forma de corrigir;
- suporte, quando necessário.

Detalhes técnicos não substituem explicação compreensível.

A representação de erro deve corresponder ao estado real conhecido da operação. Falha posterior a efeito principal concluído não pode ser apresentada como se toda a operação necessariamente não tivesse ocorrido.

Erros semanticamente diferentes que permitam formas diferentes de continuidade ou recuperação devem permanecer distinguíveis o suficiente para orientar a ação correta.

Quando o resultado da operação for indeterminado, a interface não pode afirmar sucesso nem ausência de efeito sem confirmação.

## 67. Estado parcial

Conteúdo válido deve permanecer disponível quando uma falha parcial não comprometer segurança ou consistência.

A região afetada deve indicar a falha sem bloquear áreas independentes.

## 68. Estado desabilitado

- O motivo deve ser compreensível quando não for evidente.
- O requisito para habilitação deve ser informado quando aplicável.
- Desabilitação não deve ocultar erro que poderia ser explicado.

### 68.1 Permissões e disponibilidade de ações

Quando a interface conhecer o estado de permissão aplicável, a disponibilidade apresentada das ações deve ser compatível com esse estado para não induzir expectativa de execução inválida.

Uma ação conhecida como não autorizada não deve ser apresentada como normalmente executável. Conforme o contexto, ela pode ser omitida, desabilitada ou substituída por orientação adequada, desde que a decisão preserve compreensão e acessibilidade.

Ocultar ou desabilitar uma ação não constitui autorização nem fronteira de segurança. A validação autoritativa permanece obrigatória conforme `regrasDev.md`.

Quando a permissão estiver desconhecida, pendente ou puder ter mudado, a interface não deve afirmar disponibilidade definitiva com base apenas em estado local obsoleto.

Mudança de permissão deve atualizar estado visual, comportamento, disponibilidade e estado acessível de forma semanticamente consistente.

## 69. Estado de sucesso

A conclusão deve ser confirmada quando não for imediatamente visível.

A mensagem deve identificar o resultado e próximas ações relevantes.

## 70. Estado offline ou degradado

- Limitações de conexão devem ser comunicadas.
- Conteúdo local seguro deve permanecer acessível.
- Ações pendentes devem indicar estado.
- O sistema não deve simular conclusão não confirmada.

---

# Parte IX — Formulários e entrada

## 71. Necessidade dos campos

Solicitar somente dados necessários à tarefa atual ou consequência explicitamente informada.

Dados já conhecidos devem ser reutilizados quando seguro.

## 72. Rótulos

- Todo campo deve possuir rótulo persistente e semanticamente associado.
- Placeholder não substitui rótulo.
- Rótulos descrevem o dado, não a implementação.
- Instruções permanecem próximas ao campo.

## 73. Formato esperado

- Formatos específicos devem ser comunicados por exemplo, máscara, unidade ou instrução.
- Variações razoáveis devem ser aceitas quando puderem ser normalizadas com segurança.
- Restrições devem ser apresentadas antes do envio quando conhecidas.
- Máscaras devem preservar cursor, seleção, exclusão, colagem, teclado virtual e tecnologias assistivas.

## 74. Tipo de controle

Utilizar o controle adequado à natureza da entrada:

- checkbox para opções independentes;
- radio para escolha exclusiva entre poucas opções;
- select ou busca para conjuntos maiores;
- campo numérico para números;
- seletor de data quando melhorar entrada;
- texto livre quando opções não forem adequadas.

## 75. Ordem de preenchimento

- A ordem deve acompanhar o fluxo mental e operacional.
- Campos relacionados permanecem agrupados.
- Dependências aparecem progressivamente.
- Ordem visual e de foco permanecem coerentes.

## 76. Obrigatoriedade

- Campos obrigatórios e opcionais devem ser identificados consistentemente.
- O padrão concreto pertence ao projeto.
- Obrigatoriedade condicional só existe quando a condição estiver ativa.
- Não depender apenas de cor.

## 77. Validação

- Deve ocorrer no momento mais útil para prevenção ou correção.
- Erros não devem aparecer antes de oportunidade razoável de preenchimento.
- Cliente e servidor devem produzir mensagens coerentes.
- Dados válidos não devem ser removidos silenciosamente.
- Validação antecipada da interface deve preservar o mesmo significado semântico da validação autoritativa definida para a regra correspondente em `regrasDev.md`.
- A interface pode validar mais cedo para melhorar feedback, mas não pode relaxar, contradizer ou substituir a validação autoritativa.
- Diferenças de máscara, formato, normalização ou mensagem são permitidas somente quando não alterarem semanticamente quais estados são válidos ou inválidos para a mesma regra.

## 78. Mensagens de erro

Devem:

- identificar problema;
- explicar restrição;
- indicar correção;
- utilizar linguagem não acusatória;
- permanecer até correção ou dispensa adequada.

## 79. Preservação de dados

Dados preenchidos não devem ser apagados após falha de validação, conexão ou processamento, salvo exigência de segurança explicitamente comunicada.

## 80. Ações do formulário

- A ação principal deve indicar resultado concreto.
- Ações secundárias não devem competir com a principal.
- Envio duplicado deve ser impedido quando causar inconsistência.
- Enter deve possuir comportamento previsível e seguro.

## 81. Formulários extensos

Dividir ou agrupar somente quando isso reduzir carga cognitiva ou risco.

A divisão não deve ocultar dependências entre campos.

---

# Parte X — Prevenção e recuperação de erros

## 82. Prevenção

- Restrições conhecidas devem ser aplicadas antes do envio quando possível.
- Valores impossíveis devem ser impedidos ou sinalizados.
- Opções indisponíveis não devem parecer executáveis.
- Prevenção não pode bloquear entradas válidas por excesso de restrição.

## 83. Valores padrão

- Devem ser seguros, previsíveis e adequados à maioria dos casos.
- Não devem autorizar, publicar, excluir ou compartilhar dados sem decisão explícita quando houver impacto.
- Valores herdados ou calculados devem ser identificáveis quando puderem causar interpretação incorreta.

## 84. Ações destrutivas

Devem possuir:

- rótulo explícito;
- diferenciação proporcional;
- indicação do objeto afetado;
- confirmação quando necessária;
- possibilidade de desfazer quando viável.

## 85. Recuperação

Após erro, preservar:

- contexto;
- dados válidos;
- caminho de continuidade;
- proteção contra duplicação de efeitos.

As ações de recuperação oferecidas devem ser compatíveis com o estado real conhecido da operação e com as garantias técnicas definidas em `regrasDev.md`.

Tentar novamente somente deve ser apresentado como ação segura quando a repetição não puder duplicar efeito indevido ou quando o sistema possuir mecanismo capaz de reconciliar a repetição corretamente.

Quando uma mutação principal tiver sido concluída e apenas sincronização, comunicação ou efeito secundário falhar, a recuperação deve tratar essa condição sem induzir repetição da mutação principal como se nada tivesse ocorrido.

Quando o resultado permanecer indeterminado, a interface deve orientar verificação ou recuperação compatível sem apresentar resultado definitivo não confirmado.

Cancelar, desfazer, restaurar ou recuperar somente podem ser oferecidos quando a operação subjacente possuir semântica compatível com a consequência comunicada; limitações de reversibilidade devem permanecer explícitas.

## 86. Erros locais e globais

- Erros locais aparecem próximos ao elemento afetado.
- Erros globais são usados somente quando afetarem toda a operação ou não puderem ser associados.
- Mensagem global não substitui mensagens locais necessárias.

## 87. Mensagens técnicas

Detalhes técnicos devem permanecer no diagnóstico interno e não constituir explicação principal ao usuário.

Não expor segredos, infraestrutura, rastreamentos ou dados sensíveis.

---

# Parte XI — Acessibilidade

## 88. Princípio geral

Acessibilidade deve participar da definição da estrutura, componentes, estados, conteúdo e interação desde o início.

Não pode ser tratada somente como validação posterior.

## 89. Estrutura semântica

- Elementos devem utilizar semântica correspondente à função.
- Títulos devem formar hierarquia coerente.
- Botões representam ações, links representam navegação e tabelas representam dados tabulares.
- Semântica nativa deve ser preferida.

## 90. Teclado

- Toda funcionalidade essencial deve ser operável por teclado quando aplicável.
- Não devem existir armadilhas de foco.
- A ordem deve acompanhar a sequência lógica.
- Controles personalizados devem possuir interação equivalente ao padrão representado.

## 91. Foco

- Foco deve ser visível.
- Mudanças de contexto devem mover foco deliberadamente quando necessário.
- Ao fechar elementos temporários, foco deve retornar ao contexto apropriado.
- Estilo de foco não pode ser removido sem substituição perceptível.

## 92. Tecnologias assistivas

Controles devem expor:

- nome;
- função;
- estado;
- valor.

Mudanças importantes devem ser comunicadas quando não forem identificáveis pela estrutura normal.

## 93. Contraste e cor

- Informação não depende exclusivamente de cor.
- Texto e controles devem atender aos critérios adotados pelo projeto.
- Foco, erro, sucesso, seleção e desabilitação devem permanecer distinguíveis.

## 94. Texto alternativo e mídia

- Imagens informativas possuem alternativa adequada.
- Imagens decorativas são ignoradas.
- Gráficos complexos possuem resumo ou representação alternativa.
- Conteúdo audiovisual possui alternativas conforme natureza e nível de conformidade.

## 95. Movimento e tempo

- Preferências de redução de movimento devem ser respeitadas.
- Conteúdo não deve piscar ou mover-se de forma insegura.
- Limites de tempo devem ser evitados quando desnecessários.
- Quando existirem, devem ser informados e permitir extensão ou recuperação quando viável.

## 96. Ampliação e redimensionamento

A interface deve permanecer utilizável com ampliação de texto e zoom nos limites definidos pelo projeto.

Conteúdo não deve ser cortado, sobreposto ou exigir rolagem bidirecional sem necessidade.

---

# Parte XII — Responsividade e dispositivos

## 97. Contexto responsável pela adaptação

A adaptação deve ser controlada pelo menor contexto que possua informação suficiente.

- condições globais pertencem ao ambiente, janela ou viewport;
- condições locais pertencem ao espaço disponível do componente;
- condições de dados pertencem ao estado ou contrato;
- preferências do usuário pertencem ao mecanismo da plataforma.

A tecnologia concreta pertence ao `regrasProjeto.md`.

Não observar o viewport global para controlar comportamento que dependa exclusivamente do espaço local quando a plataforma oferecer mecanismo adequado.

## 98. Conteúdo antes do dispositivo

A adaptação deve ser definida pela necessidade do conteúdo e da interação, não por modelos específicos de aparelho.

## 99. Breakpoints justificados

Um breakpoint deve representar necessidade observável, como:

- mudança de composição;
- perda de legibilidade;
- quebra de controle;
- alteração de navegação;
- insuficiência de espaço;
- necessidade de reorganização.

Não criar breakpoint apenas por convenção, dispositivo específico ou ajuste isolado.

Valores e justificativas pertencem ao `regrasProjeto.md`.

## 100. Adaptação contínua e discreta

Propriedades que variem continuamente sem mudança estrutural devem preferir comportamento fluido e previsível.

Isso se aplica, quando adequado, a:

- espaçamento;
- largura;
- altura;
- tipografia;
- distribuição;
- colunas;
- proporções.

Breakpoints ou estados discretos devem ser usados quando houver mudança real de composição ou comportamento.

## 101. Fluxo responsivo

- Elementos devem reorganizar-se sem perder ordem semântica ou relações essenciais.
- A interface deve evitar cortes, sobreposições e rolagens desnecessárias.
- Mudanças de disposição não podem alterar significado das ações.
- Conteúdo principal deve preceder conteúdo complementar.

## 102. Prioridade de conteúdo

Em espaços reduzidos, conteúdo secundário pode ser recolhido quando:

- ações essenciais permanecerem disponíveis;
- informação necessária não desaparecer;
- a alternativa for equivalente;
- a prioridade seguir o objetivo do usuário.

## 103. Toque e ponteiro

- Áreas de toque devem ser adequadas.
- Não depender exclusivamente de hover.
- Arraste essencial deve possuir alternativa.
- Gestos não evidentes devem possuir indicação e alternativa.

## 104. Teclados móveis

- Campos devem utilizar tipos de entrada adequados.
- O teclado não deve ocultar campo, erro ou ação principal sem possibilidade de acesso.
- Autocompletar pode ser usado quando melhorar eficiência e preservar privacidade.

## 105. Tabelas e dados densos

Podem utilizar:

- rolagem horizontal controlada;
- colunas prioritárias;
- detalhamento sob demanda;
- visualização alternativa;
- agrupamento por cartões quando não comprometer comparação.

A estratégia não pode destruir relações tabulares importantes.

## 106. Orientação e métodos de entrada

- A interface deve permanecer funcional nas orientações suportadas.
- Redimensionamento, mudança de orientação, adaptação responsiva, recomposição ou remontagem não devem exigir recarregamento nem descartar estado ainda semanticamente válido.
- Quando composições diferentes representarem o mesmo comportamento, a troca entre elas deve preservar as propriedades de estado que continuarem aplicáveis.
- Reinicialização deliberada durante adaptação deve constituir efeito explícito de transição prevista no modelo comportamental.
- Mouse, teclado, toque, caneta e tecnologias assistivas devem coexistir quando aplicáveis.

---

# Parte XIII — Conteúdo e linguagem

## 107. Linguagem direta

Textos devem ser claros, específicos e orientados à tarefa.

Informações essenciais devem aparecer antes de explicações complementares.

## 108. Vocabulário do usuário

Termos internos de implementação devem ser traduzidos para conceitos compreendidos pelo público.

Vocabulário especializado pode ser usado quando fizer parte do conhecimento esperado.

## 109. Consistência terminológica

- O mesmo conceito deve possuir o mesmo nome.
- Sinônimos não devem sugerir entidades diferentes.
- Mudanças terminológicas devem ser aplicadas integralmente.

## 110. Rótulos de ação

- Botões e comandos devem indicar ação ou resultado concreto.
- Rótulos genéricos devem ser evitados quando o resultado não for evidente.
- Ações destrutivas devem nomear a consequência.

## 111. Mensagens de estado

Mensagens devem informar:

- o que aconteceu;
- impacto;
- próxima ação, quando necessária.

## 112. Tom

O tom deve ser coerente com público, domínio e gravidade.

Situações críticas priorizam precisão e ação.

A interface não deve culpar, constranger ou manipular.

## 113. Datas, números e unidades

- Devem seguir contexto regional e domínio.
- Unidades devem acompanhar valores quando necessárias.
- Precisão numérica deve ser proporcional à decisão.
- Formatos ambíguos devem ser evitados.

## 114. Internacionalização

Quando aplicável:

- textos não devem ser concatenados de forma que impeça tradução;
- layouts devem suportar variação de comprimento;
- pluralização, gênero, datas e números devem respeitar localização;
- conteúdo do usuário deve permanecer distinto do texto traduzido.

---

# Parte XIV — Desempenho percebido

## 115. Resposta à interação

A interface deve responder visualmente assim que a ação for reconhecida.

Tarefas secundárias não devem bloquear interações independentes sem necessidade.

As garantias de resposta e não bloqueio especializam as regras de eficiência computacional, caminho crítico, concorrência e paralelismo definidas em `regrasDev.md`.

Trabalho que não seja necessário para reconhecer a interação, produzir o próximo resultado observável necessário ou liberar a próxima ação dependente não deve atrasar essas respostas quando puder avançar fora do caminho crítico com segurança.

## 116. Carregamento progressivo

- Conteúdo prioritário deve aparecer antes do secundário quando possível.
- Regiões independentes devem carregar sem bloquear o conjunto.
- A ordem deve preservar compreensão e estabilidade.

### 116.1 Caminho crítico e independência técnica

Para a interface, o caminho crítico observável corresponde ao trabalho necessário para disponibilizar o próximo conteúdo prioritário, feedback necessário ou operação da qual a continuidade do usuário realmente dependa.

Conteúdo, regiões ou tarefas secundárias tecnicamente independentes não devem ser serializados antes do resultado prioritário apenas por conveniência de implementação.

Quando existir independência técnica real e benefício relevante, regiões e trabalhos independentes devem poder avançar incrementalmente, concorrentemente ou em paralelo conforme as garantias de `regrasDev.md`.

Dependências reais devem preservar sua ordem e seus invariantes. Desempenho percebido não justifica concorrência ou paralelismo que comprometam corretude, segurança, consistência, acessibilidade, contratos ou limites de recursos.

## 117. Estabilidade visual

- Reservar espaço para conteúdo assíncrono previsível.
- Elementos não devem mudar de posição inesperadamente.
- Atualizações devem preservar posição do usuário quando possível.
- Indicadores temporários não devem alterar dimensões dos controles sem necessidade.

## 118. Atualizações otimistas

Podem ser utilizadas quando:

- probabilidade de sucesso for alta;
- reversão for segura;
- falha puder ser comunicada;
- resultado incerto de alto impacto não for apresentado como definitivo.

## 119. Indicadores proporcionais

- Operações instantâneas não devem receber indicadores que introduzam atraso.
- Operações demoradas não devem permanecer sem feedback.
- Indicadores devem corresponder ao escopo afetado.
- Carregamento global só deve bloquear tudo quando necessário para consistência ou segurança.

---

# Parte XV — Validação

## 120. Validação funcional

Fluxos principais devem ser executados integralmente nos contextos suportados.

Verificar estados de sucesso, erro, vazio, carregamento e recuperação.

A validação deve considerar comportamento observável, não apenas renderização.

### 120.1 Reentrada e sequências de fluxos temporários

Fluxos temporários, canceláveis ou reabertos devem ser validados em sequências capazes de revelar perda de contexto ou efeito residual entre entradas sucessivas.

Quando semanticamente aplicável, deve ser validada ao menos a sequência:

```text
abrir → cancelar → reabrir → confirmar
```

Quando o fluxo suportar diferentes formas de encerramento ou confirmação, cada forma suportada que possa produzir transição distinta, compartilhar estado, alterar foco ou apresentar interferência com outra forma deve ser validada. Isso inclui, quando aplicável:

- `Escape`;
- `Enter`;
- clique ou toque fora da região temporária;
- controle visível de fechar, cancelar ou confirmar.

Formas suportadas comprovadamente equivalentes podem compartilhar a mesma evidência quando a equivalência comportamental estiver demonstrada e rastreável.

Reabrir um fluxo deve produzir o estado previsto pelo modelo comportamental, preservar somente o contexto que continuar válido e restaurar foco, seleção ou demais propriedades quando esse comportamento estiver definido.

A validação deve identificar as transições ou sequências do grafo comportamental que o cenário protege.

### 120.2 Operações assíncronas e recuperação observável

Quando uma interação iniciar operação assíncrona ou sujeita a resultados sobrepostos, a validação deve especializar os cenários definidos em `regrasDev.md` e verificar o comportamento observável correspondente.

Devem ser considerados, quando aplicável:

- sucesso;
- falha;
- atraso relevante;
- tentativa novamente;
- repetição rápida da interação;
- respostas concluídas fora da ordem;
- resposta obsoleta depois de estado mais recente;
- mutação principal concluída seguida de falha de sincronização, comunicação ou efeito secundário;
- resultado indeterminado.

Resposta tardia ou obsoleta não pode regredir silenciosamente foco, seleção, conteúdo, disponibilidade de ações ou outro estado válido produzido por interação posterior.

Feedback, mensagens e ações de recuperação devem corresponder ao estado real conhecido da operação, sem induzir repetição insegura nem apresentar como definitivo resultado ainda não confirmado.

## 121. Inspeção heurística

Avaliar, quando aplicável:

- visibilidade do estado;
- correspondência com modelo mental;
- controle e liberdade;
- consistência;
- prevenção de erros;
- reconhecimento antes de memorização;
- eficiência;
- clareza visual;
- recuperação;
- ajuda necessária.

## 122. Testes com usuários

Quando risco e estágio justificarem:

- utilizar participantes representativos;
- reproduzir objetivos reais;
- não ensinar o caminho durante a tarefa;
- priorizar comportamento observado sobre opinião genérica.

## 123. Critérios de sucesso

Fluxos relevantes podem medir:

- conclusão;
- erros;
- tempo;
- necessidade de ajuda;
- abandono;
- retrabalho;
- confiança.

Valores concretos pertencem ao `regrasProjeto.md`.

## 124. Testes de acessibilidade

Combinar, quando aplicável:

- ferramentas automáticas;
- inspeção semântica;
- teclado;
- tecnologias assistivas;
- ampliação;
- contraste;
- testes com pessoas com deficiência.

Ferramentas automáticas não são suficientes para declarar conformidade integral.

## 125. Dispositivos e contextos

Validar nas plataformas, navegadores, dimensões e métodos de entrada definidos no projeto.

Simulação não substitui integralmente dispositivo real quando existirem riscos específicos.

### 125.1 Alternância entre métodos de entrada

Quando mais de um método de entrada puder operar o mesmo fluxo, a validação não pode limitar-se a executar o fluxo completo separadamente com cada método.

Devem ser incluídas sequências que alternem os métodos suportados quando a alternância for semanticamente possível, como:

```text
teclado → ponteiro → teclado
```

ou outras combinações relevantes entre teclado, mouse, toque, caneta e tecnologias assistivas.

A mudança do método de entrada não pode causar perda indevida de:

- foco;
- alvo da interação;
- seleção;
- estado válido;
- contexto;
- disponibilidade ou funcionamento dos atalhos aplicáveis.

As transições produzidas por métodos de entrada equivalentes devem preservar o mesmo significado comportamental, salvo diferença explicitamente definida no modelo.

## 126. Regressão visual e comportamental

- Alterações em componente compartilhado devem ser verificadas nos consumidores principais.
- Mudanças visuais não devem alterar comportamento, foco ou acessibilidade sem decisão explícita.
- Referências visuais devem ser acompanhadas por validação semântica e funcional.

## 127. Registro de problemas

Problemas devem registrar:

- contexto;
- objetivo;
- ação;
- resultado observado;
- resultado esperado;
- impacto;
- evidência;
- correção proposta;
- prioridade.

## 128. Níveis de validação

O nível alcançado deve ser declarado conforme evidências:

- estrutural;
- automatizado;
- operacional;
- empírico;
- integral.

O nível exigido pertence ao `regrasProjeto.md`.

Não declarar nível sem evidência correspondente.

## 129. Validação de densidade e responsividade

Alterações de densidade, compactação, hierarquia visual ou responsividade devem ser verificadas considerando, quando aplicável:

- menor espaço suportado;
- maior ampliação suportada;
- conteúdo mínimo;
- conteúdo máximo;
- textos extensos;
- traduções;
- erros;
- estados vazios;
- estados selecionados;
- navegação por teclado;
- toque;
- orientações;
- preferências de acessibilidade;
- mudanças dinâmicas de conteúdo.

Limites concretos pertencem ao `regrasProjeto.md`.

## 130. Critério de conclusão

Uma interface somente pode ser considerada concluída quando:

- fluxos principais funcionarem nos contextos suportados;
- estados semanticamente aplicáveis à interface e catalogados no modelo comportamental estiverem implementados;
- problemas críticos de usabilidade e acessibilidade estiverem resolvidos;
- não conformidades restantes estiverem registradas;
- comportamento observado corresponder aos objetivos;
- nível de validação exigido tiver sido alcançado.

---

# Checklist de conformidade

## Princípios

- [ ] O usuário identifica contexto, ações e resultados prováveis.
- [ ] A interface utiliza a menor complexidade suficiente.
- [ ] Padrões equivalentes permanecem consistentes.
- [ ] Complexidade é proporcional à tarefa e ao risco.

## Informação e navegação

- [ ] Conteúdo segue objetivos e vocabulário do usuário.
- [ ] Agrupamentos permanecem perceptíveis.
- [ ] Cada nível possui função real.
- [ ] A ordem visual preserva leitura, foco e execução.
- [ ] Informação essencial permanece disponível.
- [ ] Transições preservam propriedades de contexto cuja alteração não esteja definida entre seus efeitos.

## Densidade e estrutura visual

- [ ] Densidade aumenta informação útil, não apenas reduz dimensões.
- [ ] A ordem de compactação foi respeitada.
- [ ] Contêineres possuem função.
- [ ] Não existem bordas, fundos ou sombras redundantes.
- [ ] Áreas interativas não foram reduzidas indevidamente.

## Componentes e estados

- [ ] Componentes possuem responsabilidade identificável.
- [ ] Compartilhamento possui equivalência semântica.
- [ ] Variantes representam conceitos reais.
- [ ] Estados semanticamente aplicáveis à interface e catalogados no modelo comportamental foram implementados.
- [ ] Estados e transições interativos aplicáveis especializam o modelo comportamental de desenvolvimento.
- [ ] Estado visual, interativo, informacional e acessível permanecem semanticamente equivalentes.
- [ ] Disponibilidade apresentada das ações reflete permissões conhecidas sem substituir autorização técnica.
- [ ] Elementos nativos são utilizados quando adequados.

## Interação

- [ ] Toda ação relevante produz feedback.
- [ ] Operações demoradas indicam atividade.
- [ ] Acionamentos equivalentes convergem para uma única intenção comportamental e, quando aplicável, uma única intenção de domínio sem duplicação pelo mesmo evento.
- [ ] Cancelar e desfazer somente são oferecidos quando a operação subjacente suporta a consequência comunicada.
- [ ] Limitações de reversibilidade são comunicadas quando aplicáveis.
- [ ] Ações destrutivas comunicam consequência.
- [ ] Processos automáticos são distinguíveis de decisões confirmadas.

## Acessibilidade

- [ ] Estrutura utiliza semântica adequada.
- [ ] Fluxos essenciais são operáveis por teclado.
- [ ] Foco é visível e lógico.
- [ ] Controles expõem nome, função, estado e valor.
- [ ] Informação não depende apenas de cor.
- [ ] Ampliação e redução de movimento foram consideradas.

## Responsividade

- [ ] A adaptação ocorre no menor contexto suficiente.
- [ ] Breakpoints representam mudanças justificáveis.
- [ ] Variações contínuas utilizam comportamento fluido quando adequado.
- [ ] Ordem semântica e ações essenciais foram preservadas.
- [ ] Redimensionamento e troca de composição preservam estado semanticamente válido.
- [ ] Métodos de entrada suportados permanecem utilizáveis.

## Desempenho percebido

- [ ] Feedback e próxima ação não são atrasados por trabalho secundário independente sem necessidade.
- [ ] Conteúdo prioritário e regiões independentes não são serializados artificialmente antes de trabalho do qual não dependem.
- [ ] Trabalhos independentes avançam incrementalmente, concorrentemente ou em paralelo quando há benefício relevante e segurança semântica.
- [ ] Dependências reais preservam ordem, consistência e invariantes.
- [ ] Ganho de desempenho percebido não é obtido por concorrência ou paralelismo que comprometam corretude, segurança, acessibilidade ou limites de recursos.

## Conteúdo

- [ ] O mesmo conceito utiliza o mesmo termo.
- [ ] Rótulos descrevem ações concretas.
- [ ] Mensagens informam resultado, impacto e próxima ação.
- [ ] Datas, números e unidades seguem o contexto.

## Validação

- [ ] Fluxos principais foram executados.
- [ ] Validações antecipadas da interface permanecem semanticamente compatíveis com a validação autoritativa.
- [ ] Estados de erro, vazio, carregamento e recuperação foram verificados.
- [ ] Fluxos temporários e canceláveis foram validados em sequências de reentrada aplicáveis.
- [ ] Formas suportadas de encerramento e confirmação que possam produzir transição distinta, compartilhar estado ou apresentar interferência foram validadas.
- [ ] Métodos de entrada compartilhados por um fluxo foram validados também em sequências intercaladas.
- [ ] Alternância de método de entrada preserva foco, alvo, seleção, estado, contexto e atalhos aplicáveis.
- [ ] Operações assíncronas aplicáveis foram verificadas em atraso, repetição, ordem de respostas e recuperação.
- [ ] Respostas obsoletas não regressam estado válido produzido por interação posterior.
- [ ] Falhas posteriores a efeito principal concluído são apresentadas e recuperadas conforme o estado real da operação.
- [ ] Densidade e responsividade foram testadas em condições limite.
- [ ] Navegação por teclado e estrutura acessível foram verificadas.
- [ ] O nível declarado corresponde às evidências.
