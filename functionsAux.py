def verificaGanhador(board, branco): 
    for i in range(3):
        if(board[i][0] == board[i][1] and board[i][1] == board[i][2] and board[i][0] != branco):
            return board[i][0]
    
    for i in range(3):
        if(board[0][i] == board[1][i] and board[1][i] == board[2][i] and board[0][i] != branco):
            return board[0][i]
    
    if(board[0][0] != branco and board[0][0] == board[1][1] and board[1][1] == board[2][2]):
        return board[0][0]

    if(board[0][2] != branco and board[0][2] == board[1][1] and board[1][1] == board[2][0]):
        return board[0][2]

    for i in range(3):
        for j in range(3):
            if(board[i][j] == branco):
                return False

    return "EMPATE"

def verificaInput(mensagem):
    print(mensagem)
    try:
        n = int(input())
        if(n>=0 and n<=2):
            return n
        else: 
            if("linha" in mensagem):
                print("A linha precisa estar entre 0 e 2")
                return verificaInput(mensagem)
            if("coluna" in mensagem):
                print("A coluna precisa estar entre 0 e 2")
                return verificaInput(mensagem)
    except: 
        print("Entrada tem que ser um número!")
        return verificaInput(mensagem)
