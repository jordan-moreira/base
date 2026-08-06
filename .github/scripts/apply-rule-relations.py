from pathlib import Path
import re

SECTIONS = {
    "regrasDev.md": r'''---
## Apêndice normativo — Relações entre regras de desenvolvimento

Este apêndice torna explícitas relações anteriormente implícitas ou necessárias. Todos os itens abaixo possuem força normativa equivalente às demais regras deste documento. Os identificadores preservam a origem da relação para auditoria: `I` indica relação anteriormente implícita e `N` indica relação necessária adicionada nesta revisão.

### Dependências

- [DEP-I-07] A nomenclatura de qualquer nó deve ser definida somente depois que sua responsabilidade real tiver sido identificada e estabilizada no escopo analisado.
- [DEP-I-08] Contratos públicos e fronteiras abstratas devem ser definidos antes das implementações concretas que os satisfazem.
- [DEP-I-15] A taxonomia interna de erros deve ser definida antes da conversão desses erros em mensagens externas, respostas de transporte, logs ou métricas.
- [DEP-I-16] Requisitos de segurança e privacidade devem ser definidos antes de decisões sobre logs, persistência, valores padrão, preenchimento automático ou tratamento de dados.
- [DEP-N-01] Toda regra que funcione como pré-condição de outra deve declarar expressamente a relação, o escopo afetado e a evidência necessária para considerar a pré-condição satisfeita.
- [DEP-N-02] A alteração de uma regra antecedente invalida a conformidade das regras dependentes afetadas e exige sua reavaliação antes da continuidade.
- [DEP-N-05] A baseline de comportamento, contratos, formatos e resultados observáveis deve ser registrada antes de qualquer normalização, migração ou refatoração estrutural.
- [DEP-N-06] A árvore final planejada deve ser validada contra responsabilidades, contratos, dependências e casos de uso antes do início da migração estrutural.

### Precedências

- [PRE-I-01] Corretude, segurança e preservação de comportamento prevalecem sobre simplificação, redução estrutural, desempenho ou conveniência de implementação quando não for possível satisfazer simultaneamente esses objetivos.
- [PRE-I-02] Contratos públicos e comportamentos protegidos prevalecem sobre conveniências de refatoração, reorganização ou redução de código.
- [PRE-I-03] Segurança e integridade dos dados prevalecem sobre eficiência, continuidade operacional ou conveniência de interface.
- [PRE-I-05] Estrutura semântica e responsabilidade real prevalecem sobre simetria visual da árvore, uniformidade artificial ou aparência de organização.
- [PRE-I-06] Responsabilidade, coesão e fronteira prevalecem sobre tamanho físico, quantidade de linhas, número de arquivos ou limites numéricos arbitrários.
- [PRE-I-07] Contrato, significado e comportamento compartilhados prevalecem sobre semelhança visual, nominal ou estrutural.
- [PRE-N-01] A precedência deve ser aplicada somente ao trecho e ao escopo em conflito; todas as regras não afetadas continuam cumulativamente obrigatórias.
- [PRE-N-02] Um conflito normativo só existe quando duas regras aplicáveis não podem ser satisfeitas simultaneamente no mesmo escopo.
- [PRE-N-03] Preferência pessoal, custo, prazo, hábito ou conveniência não constituem conflito normativo.
- [PRE-N-04] Nenhuma decisão local pode prevalecer sobre exigência legal, requisito técnico obrigatório, segurança mínima ou integridade de dados.
- [PRE-N-05] Quando regras do mesmo nível entrarem em conflito, deve prevalecer a solução que melhor preserve comportamento, segurança, acessibilidade e contratos, com decisão explícita e documentada.

### Exceções

- [EXC-I-01] Código compartilhado deve retornar ao contexto específico quando seus consumidores deixarem de possuir significado, contrato ou ciclo de mudança equivalentes.
- [EXC-I-02] Uma abstração deve ser removida quando deixar de representar contrato, responsabilidade, fronteira ou reutilização real.
- [EXC-I-03] Uma camada deve ser incorporada ao nó semanticamente correto quando passar a apenas encaminhar dados sem transformação, proteção, coordenação ou adaptação.
- [EXC-N-03] Uma exceção não dispensa regras que não sejam diretamente afetadas pelo motivo que a originou.
- [EXC-N-04] Uma exceção local não cria convenção geral e não pode alterar o comportamento normativo dos documentos canônicos sem revisão formal.
- [EXC-N-06] A omissão de uma categoria de teste deve registrar qual proteção ela não agregaria, quais comportamentos permanecem cobertos e por quais níveis de teste.
- [EXC-N-10] Toda exceção deve ser reavaliada quando mudar a regra afetada, sua dependência, a tecnologia, o risco ou o contexto de aplicação.''',
    "regrasProjeto.md": r'''---
## Apêndice normativo — Relações entre decisões do projeto

Este apêndice torna explícitas relações anteriormente implícitas ou necessárias. Todos os itens abaixo devem ser preenchidos e aplicados junto às decisões correspondentes deste documento. Os identificadores preservam a origem da relação para auditoria: `I` indica relação anteriormente implícita e `N` indica relação necessária adicionada nesta revisão.

### Dependências

- [DEP-I-01] A arquitetura adotada deve ser definida somente depois de objetivo, escopo, requisitos, restrições, premissas e natureza do sistema estarem suficientemente definidos.
- [DEP-I-02] Os módulos e suas fronteiras devem ser definidos somente depois da arquitetura, das responsabilidades e da direção de dependências estarem estabelecidas.
- [DEP-I-03] A árvore concreta de diretórios deve ser definida a partir da arquitetura, dos módulos, dos fluxos técnicos e da direção permitida das dependências.
- [DEP-I-04] Regras de imports e reexports devem ser definidas a partir das fronteiras, interfaces públicas e dependências permitidas entre módulos.
- [DEP-I-05] A escolha da tecnologia de persistência deve depender da existência, propriedade, volume, ciclo de vida, integridade e requisitos de recuperação dos dados.
- [DEP-I-06] A escolha entre estado local, de feature, global ou remoto deve depender da propriedade, dos consumidores, da origem, da duração e da necessidade de sincronização do estado.
- [DEP-I-09] A implementação dos testes deve ocorrer depois que comportamentos observáveis, contratos, casos de uso, conexões, riscos e critérios de sucesso estiverem definidos.
- [DEP-N-03] Uma decisão pendente bloqueia somente os ramos que dependem dela; atividades independentes podem prosseguir desde que não antecipem a decisão.
- [DEP-N-04] O grafo de casos de uso deve estar formalizado antes de qualquer declaração de cobertura integral de testes.
- [DEP-N-07] A documentação afetada deve ser identificada antes da implementação e atualizada antes da conclusão ou promoção da alteração.
- [DEP-N-08] As revisões canônicas de `regrasDev.md`, `regrasProjeto.md` e `regrasUxUi.md` adotadas pelo projeto devem estar identificadas antes de declarar conformidade normativa.

### Precedências

- [PRE-N-06] Quando não for possível determinar a precedência entre regras aplicáveis, a implementação do escopo afetado deve permanecer bloqueada até que a decisão seja registrada explicitamente neste documento.

### Exceções

- [EXC-I-04] Uma compatibilidade existente somente pode ser alterada mediante decisão explícita que autorize a quebra, identifique consumidores afetados e defina estratégia de migração.
- [EXC-N-01] Toda exceção deve registrar a regra afetada, motivo, escopo, responsável, data, impacto, riscos, medidas compensatórias e critério de encerramento.
- [EXC-N-02] Toda exceção temporária deve possuir prazo ou condição objetiva de revisão e remoção.
- [EXC-N-05] O estado `Não se aplica.` exige justificativa verificável baseada na natureza e no escopo do projeto, e não apenas na ausência atual de implementação.
- [EXC-N-08] Exceções relacionadas à segurança exigem análise de risco, autorização explícita e medida compensatória proporcional.
- [EXC-N-09] Exceções que afetem contratos públicos, formatos persistidos ou comportamento observável exigem autorização explícita do responsável pelo projeto e plano de compatibilidade ou migração.
- [EXC-N-11] A conformidade integral só pode ser declarada quando não existirem exceções incompatíveis com o nível de conformidade pretendido.
- [EXC-N-12] Exceções encerradas devem ser removidas da implementação e da documentação normativa ativa, preservando apenas o histórico da decisão no local apropriado.''',
    "regrasUxUi.md": r'''---
## Apêndice normativo — Relações entre regras de UX e UI

Este apêndice torna explícitas relações anteriormente implícitas ou necessárias. Todos os itens abaixo possuem força normativa equivalente às demais regras deste documento. Os identificadores preservam a origem da relação para auditoria: `I` indica relação anteriormente implícita e `N` indica relação necessária adicionada nesta revisão.

### Dependências

- [DEP-I-10] A arquitetura da informação deve ser definida antes da navegação, da hierarquia visual, da divulgação progressiva e da adaptação responsiva.
- [DEP-I-11] A necessidade de um dado deve ser confirmada antes da criação do campo, da escolha do controle, da validação e da mensagem de erro correspondente.
- [DEP-I-12] Os estados relevantes de uma tela, região ou componente devem ser definidos antes de sua implementação ser considerada funcionalmente completa.
- [DEP-I-13] Plataformas, navegadores, dimensões, métodos de entrada e níveis de acessibilidade suportados devem ser definidos antes da validação de responsividade, acessibilidade e compatibilidade.
- [DEP-I-14] O risco, o impacto e a reversibilidade da ação devem ser avaliados antes da escolha entre confirmação, possibilidade de desfazer ou execução direta.
- [DEP-N-09] A acessibilidade deve participar da definição da estrutura, componentes, estados, conteúdo e interação desde o início, não podendo ser tratada apenas como validação posterior.

### Precedências

- [PRE-I-04] Acessibilidade prevalece sobre identidade visual, animações, densidade, personalização estética e convenções locais quando não for possível satisfazê-las simultaneamente.

### Exceções

- [EXC-I-05] A preservação de contexto ou dados pode ser limitada quando segurança, privacidade ou integridade exigirem descarte, desde que a consequência seja informada e proporcional.
- [EXC-I-06] A continuidade de tarefas independentes pode ser temporariamente bloqueada quando a operação em andamento comprometer consistência, segurança ou integridade global.
- [EXC-N-07] Nenhuma exceção de acessibilidade pode reduzir a conformidade abaixo de exigências legais, técnicas obrigatórias ou requisitos mínimos definidos para a plataforma.''',
}

FRONTEND_STYLE_ANCHOR = "Nenhuma dessas divisões deve ser criada automaticamente.\n\n### 9.2 Componentes"
FRONTEND_STYLE_REPLACEMENT = r'''Nenhuma dessas divisões deve ser criada automaticamente.

### 9.1.1 Normalização global de estilos

Todo projeto front-end deve possuir uma base global de estilos carregada na inicialização da aplicação para neutralizar diferenças desnecessárias entre os estilos padrão dos navegadores suportados.

O reset mínimo obrigatório é:

```css
*,
*::before,
*::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}
```

A base global também deve, quando aplicável ao projeto:

- fazer controles de formulário herdarem tipografia e cor do contexto;
- impedir que imagens, vídeos, SVGs e canvases ultrapassem o contêiner;
- definir comportamento previsível para elementos de mídia e conteúdo substituído;
- normalizar altura mínima, renderização de texto e outros padrões que variem entre navegadores suportados;
- remover estilos padrão adicionais somente quando houver necessidade real e substituição intencional no design system ou no componente correspondente.

O reset global não deve:

- remover foco visível sem substituição acessível equivalente;
- eliminar semântica ou comportamento nativo necessário;
- remover globalmente marcadores de listas, decoração de links, bordas de controles ou outros sinais de interação sem que o projeto defina uma alternativa clara;
- introduzir regras específicas de componentes ou funcionalidades na base global.

### 9.2 Componentes'''

EXPECTED_IDS = {
    *(f"DEP-I-{index:02d}" for index in range(1, 17)),
    *(f"DEP-N-{index:02d}" for index in range(1, 10)),
    *(f"PRE-I-{index:02d}" for index in range(1, 8)),
    *(f"PRE-N-{index:02d}" for index in range(1, 7)),
    *(f"EXC-I-{index:02d}" for index in range(1, 7)),
    *(f"EXC-N-{index:02d}" for index in range(1, 13)),
}

MARKER = "## Apêndice normativo — Relações"

dev_path = Path("regrasDev.md")
dev_content = dev_path.read_text(encoding="utf-8")
if FRONTEND_STYLE_ANCHOR not in dev_content:
    raise RuntimeError("Âncora da seção de front-end não encontrada em regrasDev.md")
dev_path.write_text(dev_content.replace(FRONTEND_STYLE_ANCHOR, FRONTEND_STYLE_REPLACEMENT, 1), encoding="utf-8")

for file_name, section in SECTIONS.items():
    path = Path(file_name)
    original = path.read_text(encoding="utf-8")
    if MARKER in original:
        raise RuntimeError(f"{file_name} já contém um apêndice normativo; revisão manual necessária")
    path.write_text(f"{original.rstrip()}\n\n{section}\n", encoding="utf-8")

found_ids = []
for file_name in SECTIONS:
    content = Path(file_name).read_text(encoding="utf-8")
    found_ids.extend(re.findall(r"^- \[((?:DEP|PRE|EXC)-(?:I|N)-\d{2})\]", content, flags=re.MULTILINE))

if len(found_ids) != 56:
    raise RuntimeError(f"Quantidade incorreta de relações: {len(found_ids)}; esperado: 56")

if len(found_ids) != len(set(found_ids)):
    raise RuntimeError("Existem identificadores de relações duplicados")

if set(found_ids) != EXPECTED_IDS:
    missing = sorted(EXPECTED_IDS - set(found_ids))
    extra = sorted(set(found_ids) - EXPECTED_IDS)
    raise RuntimeError(f"Inventário divergente; ausentes={missing}; extras={extra}")

updated_dev = dev_path.read_text(encoding="utf-8")
required_style_tokens = [
    "### 9.1.1 Normalização global de estilos",
    "box-sizing: border-box;",
    "margin: 0;",
    "padding: 0;",
]
for token in required_style_tokens:
    if token not in updated_dev:
        raise RuntimeError(f"Regra de estilos incompleta; ausente: {token}")

print("56 relações normativas e baseline global de estilos explicitadas e validadas")
