numbers = []

numbersString = input("Type a list of numbers (separated by a comma): ")
numbersStringList = numbersString.split()

for n in numbersStringList:
  numbers.append(int(n))

# Exemple given
# numbers = [1, 2, 3, 4, 5]

newArray = []

for i in range(len(numbers)):
  multResult = 1
  for n in numbers:
    if n != numbers[i]:
      multResult *= n
  newArray.append(multResult)

print(newArray)