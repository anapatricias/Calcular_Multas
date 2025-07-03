#Escolha do local da circulação

try:
    print('\n Onde circulava o veiculo?')
    print('Escolha uma opção:')
    print('1-Localidade')
    print('2-Fora da Localidade')
    print('3-Autoestrada')
    print()
    
    loc = int(input('Introduza o local (1/2/3):'))
    
    if loc not in {1,2,3}:
        raise ValueError('Introduza um valor válido!')
    
    print(f"O veículo circulava no local {loc}.")     
    
    #Velocidade

    vel = int(input('Introduza a velocidade do veículo (km/h):'))

    print(f"O veículo circulava no local {loc} a {vel} km/h.")




except ValueError:
    print('Introduza um valor válido!')
    