from visualservices import tela
from functionsAux import verificaGanhador, verificaInput


vazio = " "
jogador = 1 
contJogada = 1

velha = [
    [vazio, vazio, vazio], 
    [vazio, vazio, vazio], 
    [vazio, vazio, vazio]
]

vencedor = verificaGanhador(velha, vazio)

while(not vencedor):
    tela(velha)
    if(jogador):
        player = "O"
    elif (not jogador):
        player = "X"
    jogador = (jogador+1)%2
    linha = verificaInput("Digite a linha: ")
    coluna = verificaInput("Digite a coluna: ")
    velha[linha][coluna] = player
    vencedor = verificaGanhador(velha, vazio)
    print(" ")

tela(velha)
print(" ")
if vencedor != "EMPATE":
    print("O vencedor é: " + vencedor)
else: 
    print("Empate!")