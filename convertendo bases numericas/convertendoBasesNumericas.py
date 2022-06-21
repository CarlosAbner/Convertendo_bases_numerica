num = int(input('Digite qualquer valor inteiro:'))
print(''' Escolha um das bases para conversao:
[1] converter para BINÁRIO
[2] converter para OCTAL
[3] converter para HEXADECIMAL
[4] CONVERTER TODAS''')

opcao = int(input('Escolha uma das opcoes acima:'))

if opcao == 1:
	print('{} convertido para BINÁRIO é {}'.format(num, bin(num)[2:]))
elif opcao == 2:
	print('{} convertido para OCTAL é {}'.format(num, oct(num)[2:]))
elif opcao == 3:
	print('{} convertido para HEXADECIMAL é {}'.format(num, hex(num) [2:]))
elif opcao == 4:
	print('''{} convertido em BINÁRIO {},
Convertido em OCTAL {},
Convertido em HEXADECIAL {}'''.format(num, bin(num)[2:], oct(num)[2:], hex(num)[2:]))
else:
	print('''DESCULPE :(  Opcao invalida!
			 Tente novamente!!''')
