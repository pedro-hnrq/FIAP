#arquivo = open("Primeiro_Arquivo.txt", "w")

#arquivo.write("Vai ser um sucesso!")

# arquivo.close()

# w -> Escrever; r -> Leitura; a -> Ler e Escrever; x -> Exclusivo; t -> retorna como string;

with open("Primeiro_Arquivo.txt", "r") as arquivo:
    for linha in arquivo.readlines():
        print(linha)
