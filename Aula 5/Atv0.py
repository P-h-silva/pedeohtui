def contar_numeros():
  """
  Pede ao usuário dois números e realiza a contagem entre eles, 
  crescente ou decrescente, dependendo da ordem.
  """
  try:
    primeiro_numero = int(input("Digite o primeiro número: "))
    ultimo_numero = int(input("Digite o último número: "))

    if ultimo_numero > primeiro_numero:
      print(f"Contagem crescente de {primeiro_numero} até {ultimo_numero}:")
      for i in range(primeiro_numero, ultimo_numero + 1):
        print(i)
    elif ultimo_numero < primeiro_numero:
      print(f"Contagem decrescente de {primeiro_numero} até {ultimo_numero}:")
      for i in range(primeiro_numero, ultimo_numero - 1, -1):
        print(i)
    else:
      print("Os números são iguais, nenhuma contagem necessária.")

  except ValueError:
    print("Por favor, insira apenas números inteiros.")

contar_numeros()