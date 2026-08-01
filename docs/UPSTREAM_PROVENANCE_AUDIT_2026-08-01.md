# Auditoria de proveniência do upstream — 2026-08-01

## Escopo

Esta auditoria registra a relação pública entre:

- fork/sujeito: `rafaelmeloreisnovo/myCat-iahelpsus`;
- upstream identificado: `yumiaura/myCat`;
- branch comparada: `main`;
- observação: `2026-08-01T18:29:00-03:00`.

O objetivo é preservar cadeia de custódia técnica, distinguir fatos de inferências e impedir acusações sem evidência suficiente.

## Resultado verificável antes desta aplicação

| campo | valor |
|---|---|
| relação | `behind` |
| commits exclusivos do fork | `0` |
| commits do upstream ainda ausentes | `179` |
| merge-base | `e9fba63be25bfd61cf0518016fd63e5a4b4ad964` |
| head do upstream | `5d9a79c6ab3dcced021d57dd04a1e08445ebf871` |
| head do fork antes dos arquivos de auditoria | `e9fba63be25bfd61cf0518016fd63e5a4b4ad964` |

Após a incorporação destes arquivos, o fork passa a possuir commits locais de governança. Isso **não altera o ponto de derivação**; apenas torna a relação `diverged` ou `ahead/behind` conforme o upstream evoluir.

## Evidências

1. O README histórico do fork referencia imagens, perfil e clonagem de `yumiaura/myCat`.
2. O `pyproject.toml` histórico declara o pacote `mycat`, versão `0.1.3`, com autoria `yumiaura`.
3. A comparação GitHub identifica o merge-base acima e a diferença de 179 commits.
4. O upstream possui CI automatizada com lint e testes.
5. O upstream possui workflow automatizado para empacotar `.deb` e anexá-lo a releases.
6. O PR upstream `#89` registra contribuição externa e conversa contextual entre contas distintas.

O snapshot machine-readable está em [`provenance/upstream_snapshot_2026-08-01.json`](../provenance/upstream_snapshot_2026-08-01.json).

## Classificação

| afirmação | estado |
|---|---|
| o fork deriva de `yumiaura/myCat` | `PROVADO` |
| há automação de CI, testes, pacote e release | `PROVADO` |
| há padrão compatível com humano + automação + assistência por IA | `EVIDENCIADO` |
| a conta é integralmente autônoma e sem operador humano | `TOKEN_VAZIO` |
| follow/unfollow foi causado automaticamente pelo fork/push | `TOKEN_VAZIO` |

`claim_allowed=false` permanece fail-closed para todas as classificações deste registro. O documento serve para auditoria e investigação, não para imputação pessoal.

## Controle de supply chain

Este fork **não sincroniza automaticamente** os 179 commits do upstream. Antes de qualquer atualização devem ocorrer, no mínimo:

1. revisão do diff por grupos funcionais;
2. verificação de licença e atribuição;
3. varredura de dependências, segredos e permissões;
4. execução isolada de testes e análise estática;
5. autorização humana explícita para merge.

Essa contenção evita que a própria auditoria introduza código não revisado.

## Privacidade e legalidade

A coleta está limitada a metadados e conteúdo públicos necessários para a proveniência. Não há enriquecimento de dados pessoais, contorno de controles de acesso, identificação biométrica ou tentativa de atribuir identidade civil a uma conta.

## TOKEN_VAZIO

- `TOKEN_VAZIO_ACCOUNT_AUTONOMY`: padrões públicos não demonstram ausência de operador humano.
- `TOKEN_VAZIO_FOLLOW_TIMELINE`: não há histórico temporal completo de follow/unfollow nas evidências preservadas.
- `TOKEN_VAZIO_DELETED_BRANCH_OR_FORCE_PUSH`: o estado atual não exclui branches apagadas, commits locais ou histórico reescrito.

## F_ok / F_gap / F_next

**F_ok:** upstream, merge-base, ahead/behind, automação e colaboração externa foram materializados.

**F_gap:** autonomia integral e causalidade de follow/unfollow não foram provadas.

**F_next:** executar auditoria recorrente do merge-base, preservar deltas e somente atualizar código upstream após gate de supply chain.
