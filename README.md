# Gitflow Demo - Lista de Compras

Projeto de demonstração para praticar **Git e Gitflow**.
É uma lista de compras simples, que roda no terminal, feita em Python.

## Como rodar

```bash
python main.py
```

## Como rodar os testes

```bash
python -m unittest
```

## Fluxo de branches (Gitflow)

- `main` → produção (código estável)
- `develop` → desenvolvimento (onde as features são integradas)
- `feature/*` → uma branch para cada funcionalidade nova, criada a partir da `develop` e integrada via Pull Request

## Padrão de commits

Este projeto segue o [Conventional Commits](https://www.conventionalcommits.org/pt-br/):
`feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`.
