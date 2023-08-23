def productOfFactors(num):
    temp = num
    if num <= 0:
        print("Number cannot be prime factorized.")
        exit()
    if num == 1:
        print(1)
    currentPrime = 2
    primeList = []
    while num > 1:
        if num/currentPrime % 1 == 0:
            num /= currentPrime
            primeList.append(currentPrime)
        else:
            currentPrime += 1

    uniqueFactors = list(set(primeList))
    uniqueFactors.sort()
    powers = []
    for i in range(len(uniqueFactors)):
        power = primeList.count(uniqueFactors[i])
        powers.append(power+1)
    numOfFactors = 1
    for power in powers:
        numOfFactors *= power
    
    return int(temp**(numOfFactors/2))

print(productOfFactors(36))