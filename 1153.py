#solicita ao usuario um numero inteiro
n = int(input("Digite um numero maior que 0 e menor que 13: "))

# Verifica se o numero esta dentro do intervalo
if n <= 0 or n >= 13:
    print("Valor fora do intervalo (0 < N < 13)")

# Calcula o fatorial usando um loop while
if 0 < n < 13:
    
    # Inicializa o fatorial e uma copia de n
    factorial = 1
    copy_of_n = n
    while True:
        
        # Multiplica o fatorial pelo valor atual de copy_of_n
        factorial *= copy_of_n
        
        # Decrementa copy_of_n
        copy_of_n -= 1
        
        # Sai do loop quando copy_of_n chegar a 0
        if copy_of_n == 0:
            break
    
    print("Fatorial =", factorial)