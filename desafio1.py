#1) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

while True:
  numero = int(input("Informe um numero:"))
  if numero == -1:
     print("Encerramento do programa")
     break

  a, b = 0, 1
  numero_sequencia = [a, b]

  while b < numero:
    a,b = b, a + b
    numero_sequencia.append(b)

    

  if numero in numero_sequencia:
       print(f"O numero {numero} pertence a sequencia de Fibonacci")

  else:

      print(f"O numero {numero} não pertence a sequencia de Fibonacci")