#Q2

def afd(transicao, inicial, final, cadeia):    #método para contagem
    pos_computadores = [] #lista de posições

    estado = inicial #recebe o estado inicial
    for pos, symbol in enumerate(cadeia):      #dispõe cada posição e símbolo da cadeia

        if symbol in transicao[estado]:
            estado = transicao[estado][symbol] #muda de estados de acordo com o estado anterior e a transição
        else:
            estado = inicial #se o símbolo não for aceito, o processo de reconhecimento recomeça 
        if estado == final:
            pos_computadores.append(pos-10)    #ao reconhecer, inclui na lista a posição da primeira letra ("c") daquela iteração de computador

    return pos_computadores #retorna a lista de posições

def main(): #método principal
    cadeia = input("Digite sua cadeia: ") #entrada

    trans_afd = {                                 #transições
        'q0': {' ': 'q1', ",": "q1", ".": "q1"},
        'q1': {'c': 'q2'},
        'q2': {'o': 'q3'},
        'q3': {'m': 'q4'},
        'q4': {'p': 'q5'},
        'q5': {'u': 'q6'},
        'q6': {'t': 'q7'},
        'q7': {'a': 'q8'},
        'q8': {'d': 'q9'},
        'q9': {'o': 'q10'},
        'q10': {'r': 'q11'},
        'q11': {' ': 'q12', ',': "q12", '.': "q12"},
        'q12': {}
    }
                                                                                                                           #retira quebras de linha para facilitar manipulação
    print("Segue a localização das ocorrências da palavra 'computador' no texto: ", afd(trans_afd, 'q0', 'q12', cadeia.replace("\n", "")))

main()
