def numOfFactors(number):
    # number = int(input("What number would you like to find the number of factors of? "))
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
    powers = []
    for i in range(len(uniqueFactors)):
        power = primeList.count(uniqueFactors[i])
        powers.append(power+1)
    answer = 1
    for power in powers:
        answer *= power
    
    return answer

print(numOfFactors(400))