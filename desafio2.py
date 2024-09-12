#2) Escreva um programa que verifique, em uma string, a existência da letra ‘a’, seja maiúscula ou minúscula, além de informar a quantidade de vezes em que ela ocorre.

while True:
 palavra = (input("Digite uma palavra:"))

 if palavra.isdigit():
  print("Palavra inválida! Encerramento do programa...")
  break

 letra = "A"

 contagem = palavra.upper().count(letra.upper())
 print(f"A letra {letra} aparece um total de {contagem} vezes")

