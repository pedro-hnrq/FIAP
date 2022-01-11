import socket

resp = "S"

while(resp=="S"):
    url = input("Digite uma URL: ")
    ip = socket.gethostbyname(url)
    print("O IP refente a URL é: ", ip)
    resp = input("Digite <s> para continue: ").upper()