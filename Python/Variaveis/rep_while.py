#numero = int (input("Digite um numero entre 1 a 10: "))
#
# while numero < 10:
#    print("\t" + str (numero))
#    numero = numero + 1
#print("Laço encerrado...")

nome = input("Digite Nome: ")
idade = int(input("Digite a idade: "))
doencaInfectocontagiosa = input("Suspeita de doença Infecto-Contagiosa?(SIM ou NÂO) ").upper()

while doencaInfectocontagiosa != "SIM" and doencaInfectocontagiosa != "Não":
    print("Digite Sim ou Não")
    doencaInfectocontagiosa = input("Suspeita de doença Infecto-Contagiosa?(SIM ou NÂO) ").upper()

if doencaInfectocontagiosa == "SIM":
        print("Encaminhe o paciente para a sala AMARELA")
else:
        print("Encaminhe o paciente para a sala BRANCA"
              )
if idade >= 65:
    #prioridade = "Sim"
    print("O paciente " + nome + " Possui atendimento prioritário!")
else:
    genero = input("Digite o gênero dopaciente: ").upper()
    if genero == "FEMININO" and idade > 10:
        gravidez = input("A paciente está grávida? ").upper()
        if gravidez == "SIM":
            print("Paciente COM prioridade")
        else:
            print("Paciente SEM prioridade")
    else:
        print("Paciente SEM prioridade")
