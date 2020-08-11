numbers = [10, 15, 3, 7]
k = 17

# TODO: Implementar a entrada de uma lista de numeros
# numbers = input("Digite uma lista de numeros: ")
# print(numbers)
# k = input("Digite um target: ")

result = False

for i in range(len(numbers)):
  for j in range(i+1, len(numbers)):
    if (numbers[i] + numbers[j]) == k:
      result = True

print(result)
      


