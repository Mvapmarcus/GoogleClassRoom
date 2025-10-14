#jogo fiz buzz
print("Bem-vindo ao jogo FizzBuzz!")
print("O computador te pedirá numeros entre 1 e 16" \
"se seu numero for divisivel por 3, responda Fizz" \
"se for divisivel por 5, responda Buzz" \
"se for divisivel por 3 e 5, responda FizzBuzz" \
"se não for nenhum dos casos, responda o numero digitado")
print("Digite qualquer numero fora desse intervalo para sair do jogo.")

fizz = [ 3,6,9,12 ]
buzz = [ 5,10 ]
fizzbuzz = [ 15 ]
numero = 0

while numero > 0 and numero < 17:
    resposta = input("Digite um número entre 1 e 16: ")

    if resposta not in (1,2,fizz,4,buzz,fizz,7,8,fizz,buzz,11,fizz,13,14,fizzbuzz,16):
        print("Número inválido. Tente novamente.")
        break
        
    if  numero % 3 == 0 and numero % 5 == 0:
        numero in fizzbuzz
    elif numero % 3 == 0:
        numero in fizz
    elif numero % 5 == 0:
        numero in buzz
        continue
    else:
        numero = str(numero)
        

# condicional e escrever fizz ou buzz ou fizzbuzz