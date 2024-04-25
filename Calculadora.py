while pergunta < 0:
print ("Número errado")
pergunta = int(input("Digite o número proposto: "))
if pergunta == 0:
break
pergunta += 0

while pergunta > 0:
print ("Número errado")
pergunta = int(input("Digite o número proposto: "))
if pergunta == 0:
break
pergunta += 0

if pergunta == 0:
print ("|----------TABUADA----------|")

print("1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão ")

i = int(input("Digite o número correspondente a operação: "))

while i < 1:
print ("Opção inválida, ecolha uma opção válida")
print("1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão ")
i = int(input("Digite o número correspondente a operação: "))
if i == 3:
break
i += 0

while i > 4:
print ("Opção inválida, escolha uma opção válida")

print("1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão ")
i = int(input("Digite o número correspondente a operação: "))
if i == 3:
break
i += 0

if i == 1:
print ("Operação selecionada: SOMA")

elif i == 2:
print ("Operação selecionada: SUBTRAÇÃO")

elif i == 3:
print ("Operação selecionada: MULTIPLICAÇÃO")

elif i == 4:
print ("Operação selecionada: DIVISÃO")

num = int(input("Digite um número: "))

print ("|----- RESULTADO --- SOMA DO", num ," -----|")

if i == 1:
for i in range (1, 11):
print("|{} + {} = {}|" .format(num, i, num+i ))

elif i == 2:
for i in range (1, 11):
print("|{} - {} = {}|" .format(num, i, num-i ))

elif i == 3:

for i in range (1, 11):
print("|{} x {} = {}|" .format(num, i, num*i ))

elif i == 4:
for i in range (1, 11):
print("|{} / {} = {}|" .format(num, i, num/i ))