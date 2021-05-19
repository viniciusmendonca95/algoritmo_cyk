def linha(tam=51):
    return "=" * tam


def cabecalho(txt):
    print()
    print(linha())
    print(txt)
    print(linha())


def menu(lista):
    cabecalho("MENU PRINCIPAL")
    for i, item in enumerate(lista):
        print(f"{i + 1} - {item}")
    print(linha())
    opc = input("Sua opção: ")
    while (not opc.isnumeric() or int(opc) not in range(1, len(lista)+1)):
        opc = input(f"Opção inválida, digite um valor entre 1 e {len(lista)}: ")
    return int(opc)
