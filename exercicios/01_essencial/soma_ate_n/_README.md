---
Tags: Laços de Repetição (while), Operações Aritméticas
Nível: Iniciante
---

## Objetivo

Praticar o uso de uma variável **acumuladora** dentro de um laço `while`. Acumular um total enquanto uma condição é verdadeira é um padrão muito comum em cálculos e relatórios.

## Especificação

### Soma dos números até n

Abra o arquivo `main.py`. Dentro dele, localize a função `resposta`.

A função recebe um número inteiro `n` e deve retornar a **soma** de todos os números inteiros de `1` até `n` (incluindo o `n`). O cálculo deve ser feito com um laço `while`.

Regras:

- Utilize obrigatoriamente o laço `while`.
- Não utilize a função `sum()`.
- Se `n` for menor que `1`, retorne `0`.

Exemplos:

- `resposta(5)` deve retornar `15` (pois 1 + 2 + 3 + 4 + 5)
- `resposta(1)` deve retornar `1`
- `resposta(0)` deve retornar `0`

**Atenção:** utilize `return`, não `print`.
