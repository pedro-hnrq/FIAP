nome = input("Digite um funcionário: ")
empresa = input("Digite a instituição: ")
qtde_funcionarios = int(input("Digite a Quantidade de funcionários: "))
mediaMesalidade = float(input("Digite a média da mensalidade: "))
print(nome + " trabalha na empresa " + empresa)
print("Possui: ", qtde_funcionarios, " funcionarios.")
print("A média da mensalidade é de: " + str(mediaMesalidade))
print("================Verifique os tipos de dados abaixo: ===============")
print("O tipo de dado da variável [nome] é: ", type(nome))
print("O tipo de dado da variável [Empresa] é: ", type(empresa))
print("O tipo de dado da variável [Quantidado Funcionários] é: ", type(
    qtde_funcionarios))
print("O tipo de dado da variável [Mensalidade] é: ", type(mediaMesalidade))
