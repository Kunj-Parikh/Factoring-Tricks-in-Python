number = int(input("What number would you like to prime factorize? "))
if number <= 0:
    print("Number cannot be prime factorized.")
    exit()
if number == 1:
    print(1)
currentPrime = 2
primeList = []
while number > 1:
    temp = number/currentPrime
    if temp % 1 == 0:
        number /= currentPrime
        primeList.append(currentPrime)
    else:
        currentPrime += 1

uniqueFactors = list(set(primeList))
uniqueFactors.sort()

for i in range(len(uniqueFactors)):
    power = primeList.count(uniqueFactors[i])
    if power != 1 and i != len(uniqueFactors)-1:
        print(f'{uniqueFactors[i]}^{power} * ', end="")
    elif i != len(uniqueFactors)-1:
        print(f'{uniqueFactors[i]} * ', end="")
    else:
        print(f'{uniqueFactors[i]}', end="")
