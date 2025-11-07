#le o numero dos casos de teste 
N = int(input())

for i in range(N):
    
    # Le o numero inteiro positivo
    X = int(input("Digite um numero inteiro positivo: "))
    
    # Verifica se X eh primo
    if X <= 1:
        print(f"{X} nao eh primo")
    else:
        divisor = 2
        
        # Testa os divisores ate a raiz quadrada de X
        while divisor * divisor <= X:
            
            # Se X for divisivel por algum divisor, nao eh primo
            if X % divisor == 0:
                print(f"{X} nao eh primo")
                break
            
            # Incrementa o divisor
            divisor += 1
            
        # Se nenhum divisor foi encontrado, X eh primo
        if divisor * divisor > X:
            print(f"{X} eh primo")