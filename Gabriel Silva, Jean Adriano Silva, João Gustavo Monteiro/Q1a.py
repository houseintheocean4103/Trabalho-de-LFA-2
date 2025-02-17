#Q1a

def afd(transicao, inicial, final, cadeia): #método do autômato
    estado = inicial
    for i in cadeia:
        if i in transicao[estado]:          #muda de estado de acordo com o estado anterior e a transição
            estado = transicao[estado][i]
        else:
            return False   #caso o símbolo não seja adequado, retorna 'False'
    return estado == final

def main():

    estados = {                     #função de transição
    "q0": {"0": "q0", "1": "q1"},
    "q1": {"0": "q2"},
    "q2": {"0": "q0"}
    }

    cad = input("Digite a cadeia: ") #recebe a cadeia
    resultado = afd(estados, "q0", "q0", cad)

    if resultado == True:         #caso o método retorne 'True', a cadeia é aceita
        print("Cadeia aceita")
    else:
        print("Cadeia recusada")  #caso o método retorne 'False', a cadeia é rejeitada

main()       
