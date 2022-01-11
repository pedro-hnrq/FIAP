def perguntar():
    return input("O que deseja realizar?\n" +
                 "<I> - Inserir um usuário\n" +
                 "<P> - Pesquisar um usuário\n" +
                 "<E> - Excluirr um usuário\n" +
                 "<L> - Listar um usuário: ").upper()


def inserir(dicionario):
    dicionario[input("Digite o login: ").upper()] = [input("Digite o nome: ").upper(),
                                                     input(
                                                         "Digite a última data de acesso: "),
                                                     input("Qual a última estação acessada: ").upper()]
    salvar(dicionario)


def salvar(dicionario):
    with open("bd.txt", "a") as arquivo:
        for chave, valor in dicionario.items():
            arquivo.write(chave + ":" + str(valor))
