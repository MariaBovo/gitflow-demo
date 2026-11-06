#Menu interativo da lista de compras.

from lista_compras import ListaDeCompras


def mostrar_menu():
    print("\n=== Lista de Compras ===")
    print("1 - Adicionar item")
    print("2 - Remover item")
    print("3 - Ver lista")
    print("0 - Sair")


def main():
    lista = ListaDeCompras()
    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ").strip()

        try:
            if opcao == "1":
                lista.adicionar(input("Item: "))
                print("Item adicionado!")
            elif opcao == "2":
                lista.remover(input("Item: "))
                print("Item removido!")
            elif opcao == "3":
                itens = lista.listar()
                if not itens:
                    print("A lista está vazia.")
                for numero, item in enumerate(itens, start=1):
                    print(f"{numero}. {item}")
            elif opcao == "0":
                print("Até mais!")
                break
            else:
                print("Opção inválida.")
        except ValueError as erro:
            print(f"Erro: {erro}")

if __name__ == "__main__":
    main()
