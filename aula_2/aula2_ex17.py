# exercício 17 - Bônus de Funcionário
# Verifica se o funcionário tem direito a bônus com base nos anos de serviço e avaliação

anos = float(input('Quantos anos você trabalha na empresa? '))
avaliacao = float(input('Qual a sua avaliação de desempenho? (0 a 10): '))

if anos >= 5 and avaliacao >= 8:
    print('Você recebeu um bônus de R$ 1500.')
elif anos < 5 and avaliacao >= 9:
   print('Você recebeu um bônus de R$ 1000.')
else:
    print('Você não receberá bônus.')