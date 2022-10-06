from funcoes_JSON import*
import os 

if os.path.exists("inventario.json"):
    with open("inventario.json", "r") as arq_json:inventario = json.load(arq_json)
else:inventario={}

inventario = ler_arquivo("inventario.json")
opcao=chamarMenu()
while opcao>0 and opcao<3:
    if opcao==1:
        print(registrar(inventario, "inventario.json"))
    elif opcao==2:
        exibir("inventario.json")
    opcao = chamarMenu()