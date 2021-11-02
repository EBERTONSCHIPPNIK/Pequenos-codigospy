def principal():
    peso = float(input('Peso (Kg): '))
    altura = float(input('Altura (m): '))

    imc = peso / (altura**2)
    situacao = situacao_por_imc(imc)

    print(f'SEU IMC é = {imc}')
    print(f'Situação é {situacao}')
    

def situacao_por_imc(imc):
    if imc < 17:        
       situacao = 'Muito abaixo do peso'    
    elif imc < 18.49:
       situacao = 'Abaixo do peso'    
    elif imc < 24.99:
       situacao = 'Peso normal' 
    elif imc < 29.99:
        situacao = 'Acima do Peso'
    elif imc < 34.99:
        situacao = 'Obesidade I'
    elif imc < 39.99:  
         situacao = 'Obsedidade II'
    else:
         situacao = 'Obesidade III'

    return situacao

principal()
