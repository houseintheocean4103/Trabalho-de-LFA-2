#Q3

def afd(transicao, inicial, final, cadeia): #método de leitura do autômato

  acumul = 0 #variável para acumular os valores, representando o total

  estado = inicial #recebe o estado inicial

  for symbol in cadeia: #aborda cada valor da sequência

    if symbol in transicao[estado]:
        estado = transicao[estado][symbol] #muda de estados de acordo com o estado anterior e a transição
    else:
      return "Cadeia rejeitada."
                     #faz o 'casting' dos valores para 'float'
    acumul += float(symbol) #acumula os valores

    if acumul/100 >= 1:      #se o resultado for no mínimo '1' emite a latinha, e subtrai 100, ou seja, fica apenas o que sobrou de valores excedentes
      print(int(acumul),", vale 1 latinha.")
      acumul = acumul - 100
    else:
      print(int(acumul),", vale 0 latinhas.")   #se o resultado for menor que 1, ou seja, se não houver uma quantia suficiente, imprime 0

  if acumul == 0:
    return f'Não há quantias sobrando (Cadeia aceita).'
  if acumul < 100:
    return f'Sobram {acumul} centavos. Faltam {100 - acumul} centavos para uma latinha.'

def main(): #método principal

    trans_afd = {                                #transições
    'q0': {'25': 'q1', '50': 'q2', '100': 'q4'},
    'q1': {'25': 'q2', '50': 'q3', '100': 'q5'},
    'q2': {'25': 'q3', '50': 'q4', '100': 'q6'},
    'q3': {'25': 'q4', '50': 'q5', '100': 'q7'},
    'q4': {'25': 'q1', '50': 'q2', '100': 'q4'},
    'q5': {'25': 'q2', '50': 'q3', '100': 'q5'},
    'q6': {'25': 'q3', '50': 'q4', '100': 'q6'},
    'q7': {'25': 'q4', '50': 'q5', '100': 'q7'},
    }

    entrada = str(input("Digite uma sequência de valores separados por espaço: "))
    seq = entrada.split(" ") #'seq' recebe a sequência(lista) de valores

    result = afd(trans_afd, 'q0', {'q4', 'q5', 'q6', 'q7'}, seq)  #aplicação do método

    print(result)

main()
