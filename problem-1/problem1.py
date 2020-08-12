# Exemple given.
# numbers = [10, 15, 3, 7]
# k = 17

numbers = []
numbersString = input("Type a list of numbers (separated by a comma): ")
numbersStringList = numbersString.split()

for n in numbersStringList:
  numbers.append(int(n))

k = int(input("Type target number: "))

result = False

for i in range(len(numbers)):
  for j in range(i+1, len(numbers)):
    if (numbers[i] + numbers[j]) == k:
      result = True

print(result)
      


