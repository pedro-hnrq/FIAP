nome = input("Digite Nome: ")
idade = int (input("Digite a idade: "))
#prioridade = "Não"
doencaInfectocontagiosa = input("Suspeita de doença Infecto-Contagiosa?").upper()

if idade >= 65:
    #prioridade = "Sim"
    print("O paciente "+ nome + " Possui atendimento prioritário!")
elif doencaInfectocontagiosa == "SIM":
    print("O paciente "+ nome + " deve ser direcionado para sala de espera reservada. ")
else:
    print("O paciente " + nome + " Não possui atendimento prioritário e pode aguardar na sala comum!")