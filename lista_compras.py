"""Regras da lista de compras."""


class ListaDeCompras:
    def __init__(self):
        self.itens = []

    def adicionar(self, item):
        item = item.strip()
        if not item:
            raise ValueError("O item não pode ser vazio.")
        if item.lower() in (i.lower() for i in self.itens):
            raise ValueError(f"'{item}' já está na lista.")
        self.itens.append(item)

    def remover(self, item):
        for i in self.itens:
            if i.lower() == item.strip().lower():
                self.itens.remove(i)
                return
        raise ValueError(f"'{item}' não está na lista.")

    def listar(self):
        return list(self.itens)
