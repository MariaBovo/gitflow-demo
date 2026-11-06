#Testes da lista de compras. Rode com: python -m unittest

import unittest

from lista_compras import ListaDeCompras

class TestListaDeCompras(unittest.TestCase):
    def setUp(self):
        self.lista = ListaDeCompras()

    def test_adiciona_item(self):
        self.lista.adicionar("Arroz")
        self.assertEqual(self.lista.listar(), ["Arroz"])

    def test_nao_aceita_item_vazio(self):
        with self.assertRaises(ValueError):
            self.lista.adicionar("   ")

    def test_nao_aceita_item_repetido(self):
        self.lista.adicionar("Café")
        with self.assertRaises(ValueError):
            self.lista.adicionar("café")

    def test_remove_item(self):
        self.lista.adicionar("Leite")
        self.lista.remover("Leite")
        self.assertEqual(self.lista.listar(), [])

    def test_erro_ao_remover_item_inexistente(self):
        with self.assertRaises(ValueError):
            self.lista.remover("Pão")

if __name__ == "__main__":
    unittest.main()
