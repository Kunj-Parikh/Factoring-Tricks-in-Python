def sumOfFactors(number):
    temp = number
    currentPrime = 2
    primeList = []
    while number > 1:
        if number/currentPrime % 1 == 0:
            number /= currentPrime
            primeList.append(currentPrime)
        else:
            currentPrime += 1

    uniqueFactors = list(set(primeList))
    uniqueFactors.sort()
    powers = []
    for i in range(len(uniqueFactors)):
        power = primeList.count(uniqueFactors[i])
        powers.append(power)
    multiplier = []
    total = 0
    for i in range(len(uniqueFactors)):
        # print(i)
        for j in range(powers[i]+1):
            # print(j)
            total += uniqueFactors[i]**j
        multiplier.append(total)
        total = 0
    answer = 1
    for m in multiplier:
        answer *= m
    
    print(f'The sum of the factors of the number {temp} is {answer}.')

sumOfFactors(40)
