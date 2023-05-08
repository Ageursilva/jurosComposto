from math import pow

def composto (capital, juros,tempo):
    return capital*pow((1+juros),tempo)

capital = float(input("Qual o capital de Investimento? "))
juros = float(input("Qual a taxa de juros anual em  porcentagem (%) ? "))
juros = juros / 100
tempo = int(input("Quantos meses sera o investimento? "))
tempo = tempo / 12 

valor_final_composto =  composto(capital,juros,tempo)
print(f'O montante final será de : R${valor_final_composto:.02f}')
print(f'O juros do rendimento foram de : R${valor_final_composto - capital:.02f}')
