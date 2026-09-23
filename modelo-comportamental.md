# Modelo comportamental

## Objetivo do documento

Este documento registra o grafo de casos de uso e o grafo comportamental do projeto, conforme `regrasDev.md` e `regrasUxUi.md`. Ele define os estados, as transições válidas e proibidas, as restrições e as evidências que demonstram o comportamento válido. Sua estrutura constitui o conteúdo mínimo obrigatório: nenhuma seção pode ser removida.

## Natureza do documento

É normativo, específico e plástico: define o comportamento válido deste projeto e deve ser atualizado na mesma alteração que modificar estados, transições, restrições ou evidências. Divergência entre este documento e a implementação segue o procedimento de conformidade entre modelo e implementação de `regrasDev.md`.

## Regras de preenchimento

- Cada estado é identificado pelo nome qualificado pela região, como `REGIAO.ESTADO`.
- Transições, proibições, restrições, estados inalcançáveis, sequências e mutantes equivalentes recebem identificadores conforme o glossário.
- Identificadores são estáveis: não são reutilizados nem renumerados após citados em evidências.
- Toda transição válida e toda transição proibida aponta para pelo menos uma evidência localizável.
- Evidências são citadas por arquivo e nome, como `arquivo.test.ext::nome_do_teste`.
- Abreviações próprias do projeto devem constar do glossário e de `regrasProjeto.md`.
- Usar `N/A: motivo` quando um cenário não se aplicar.
- Substituir a seção `Região: <NOME_DA_REGIAO>` por uma seção para cada região, preservando todas as suas subseções.

## Referências

Commit do `base` adotado:

Mecanismo de correspondência com a implementação: conforme `regrasProjeto.md`.

## Glossário

### Identificadores

| Prefixo | Significado | Formato |
|---|---|---|
| `UC` | caso de uso | `UC-n` |
| `TRV` | transição válida | `REGIAO.TRV-n` |
| `TRP` | transição proibida: tentativa que deve ser rejeitada ou prevenida | `REGIAO.TRP-n` |
| `RST` | restrição entre regiões | `RST-n` |
| `EIN` | estado composto inalcançável | `EIN-n` |
| `SEQ` | sequência de transições validada em conjunto | `SEQ-n` |
| `MEQ` | mutante equivalente justificado | `MEQ-n` |

### Notação

| Símbolo | Significado |
|---|---|
| `A \| B` | A ou B |
| `A → B` | de A para B, ou A seguido de B |
| `∈ {A, B}` | pertence ao conjunto {A, B} |
| `≠` | diferente de |
| `N/A: motivo` | não se aplica, pelo motivo indicado |
| `REGIAO.TRV-*` | todas as transições válidas da região |

### Abreviações do projeto

| Abreviação | Significado |
|---|---|

## Regiões

Cada região representa uma dimensão independente do comportamento. O estado do sistema é a composição dos estados de todas as regiões.

| Região | Responsabilidade | Fonte canônica | Estado inicial |
|---|---|---|---|

## Casos de uso

| ID | Objetivo | Caminho no grafo | Encerramentos válidos |
|---|---|---|---|

## Região: <NOME_DA_REGIAO>

Repetir esta seção para cada região.

### Estados

Quando a região não possuir interface, a coluna de apresentação registra `N/A: sem interface`.

| Estado | Significado | Apresentação e estado acessível | Ações disponíveis |
|---|---|---|---|

### Transições válidas

| ID | Origem | Evento | Guarda | Efeitos | Preserva | Destino | Falha | Evidências |
|---|---|---|---|---|---|---|---|---|

### Transições proibidas

| ID | Tentativa proibida | Restrição | Evidência |
|---|---|---|---|

### Falha por etapa

Para transições compostas por etapas, registrar a falha possível em cada etapa e a transição que a trata, ou a justificativa de sua impossibilidade.

| Transição | Etapa | Falha possível | Tratamento |
|---|---|---|---|

### Encerramento

Estados de encerramento e transições de saída permitidas a partir deles.

| Estado | Tipo de encerramento | Saídas permitidas |
|---|---|---|

### Caminhos técnicos

Mapeamento de cada transição válida para os elementos técnicos que a realizam.

| Transição | Caminho técnico |
|---|---|

## Restrições entre regiões

| ID | Condição | Efeito | Evidência |
|---|---|---|---|

## Estados compostos inalcançáveis

| ID | Estado composto | Justificativa |
|---|---|---|

## Sequências

Sequências que validam dependência, interferência, reentrada, repetição ou efeito residual entre transições, incluindo as combinações A → B, B → A, A → A e B → B aplicáveis.

| ID | Sequência | Risco coberto | Evidência |
|---|---|---|---|

## Matriz assíncrona

Uma linha por operação assíncrona, concorrente ou sujeita a sobreposição. Cada célula aponta para a transição ou sequência que trata o cenário, ou registra `N/A: motivo`.

| Operação | Sucesso | Falha antes do efeito | Repetição após falha | Atraso | Fora de ordem | Repetição rápida | Concorrência | Cancelamento | Efeito principal com falha secundária | Indeterminado |
|---|---|---|---|---|---|---|---|---|---|---|

## Invariantes

Propriedades que permanecem verdadeiras em todos os estados alcançáveis, cada uma com evidência.

| Invariante | Evidência |
|---|---|

## Mutantes equivalentes

Somente mutantes de equivalência exclusivamente sintática, conforme `regrasDev.md`.

| ID | Local | Mutação | Justificativa |
|---|---|---|---|

## Evidência de completude

Todos os estados e transições alcançáveis estão catalogados:

Transições não catalogadas são rejeitadas ou impossíveis:

Cobertura comportamental completa:

Sensibilidade das evidências:
