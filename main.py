while True:
    print(f'\n \nEscolha uma opção: \n1. Converter Temperatura \n2. Sair')
    escolha = input(f"\nDigite o número da opção desejada: ")
    if escolha == '1':
        opcao = input("Deseja converter de Celsius para Fahrenheit (Digite C) ou de Fahrenheit para Celsius (Digite F)? : ").lower()  
        if opcao == 'c':
            while True:
                try:
                    temperaturaCelsius = float(input('Digite a temperatura em Celsius: '))
                    temperaturaFahrenheit = (temperaturaCelsius * 9/5) + 32
                    print(f'A temperatura em Fahrenheit é: {temperaturaFahrenheit:.2f}°F')
                    break
                except:
                    print('Por favor, digite um número válido para a conversão! EX:(32).')
                    
        elif opcao == 'f':
            while True:
                try:
                    temperaturaFahrenheit = float(input('Digite a temperatura em Fahrenheit: '))
                    temperaturaCelsius = (temperaturaFahrenheit - 32) * 5/9
                    print(f'A temperatura em Celsius é: {temperaturaCelsius:.2f}°')
                    break
                except:
                    print('Por favor, digite um número válido para as notas.')
        else:
            print('Opção inválida. Por favor, escolha C ou F.')
    elif escolha == '2':
        print('Fechando o programa...')
        break
    else:
        print('Opção inválida. Por favor, escolha 1 ou 2.')