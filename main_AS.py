
    #Função para calcular multa

def calcular_multa (velocidade,local):
    multa = 0
    
    if velocidade < 50:
        print("Sem multa. Velocidade abaixo de 50 km/h.")
        return
    
    if local == 1 :
        if velocidade >= 120:
            multa = 320
        elif velocidade >= 90:
            multa = 120
        elif velocidade > 50:
            multa = 60
    
    elif local == 2:
        if velocidade >=120:
            multa = 120
        elif velocidade >90:
            multa = 60
            
    elif local == 3:
        if velocidade > 175:
            multa = 360
        elif velocidade > 150:
            multa = 120
        elif velocidade > 120:
            multa = 60
            
    if multa > 0:
        print (f"Multa de {multa} € ")
    else:
        print("Sem multa.")
        
        

    try:
        print ('\n Onde circulava o veículo?')
        print ('Escolha uma opção:')
        print ('1-Localidade')
        print ('2 - Fora da localidade')
        print ('3- Autoestrada')
        print ()
                   
        loc = int (input ('Introduza o local (1/2/3):'))
            
        if loc not in {1,2,3}:
                raise ValueError ('Introduza um valor válido')
            
        vel = int (input ('Introduza a velocidade do veículo (km/h):'))
   
    
        calcular_multa (vel,loc)
            
        if input('\n Deseja continuar? (s/n): '). lower () =='n':
                
        
    except ValueError:
       print ('Introduza um valor válido!')
          
            
