---
Tags: Métodos de Lista, Listas
Nível: Iniciante
---

## Objetivo

Praticar o método `append`, usado para adicionar um item ao final de uma lista. Inserir novos itens é uma das operações mais frequentes ao trabalhar com coleções de dados.

## Especificação

### Adicionar item ao fim da lista

Abra o arquivo `main.py`. Dentro dele, localize a função `resposta`.

A função recebe uma lista (`lista`) e um valor (`item`). Adicione o `item` ao **final** da lista e retorne a lista resultante.

Regras:

- Utilize o método `append`.
- O novo item deve ficar na última posição.

Exemplos:

- `resposta(['banana', 'laranja'], 'manga')` deve retornar `['banana', 'laranja', 'manga']`
- `resposta([], 1)` deve retornar `[1]`

**Atenção:** utilize `return`, não `print`.
