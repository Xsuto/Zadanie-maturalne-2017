from random import randint

def filterArray(arr):
    print(arr)
    firstEvenNumber = True
    biggestNumber = 0
    smallestNumber = 0
    oddNumbers = 0
    evenNumbers = 0
    for i in range(0,len(arr)):
        if(arr[i] % 2 == 0):
            if(firstEvenNumber == True):
                firstEvenNumber = arr[i]
                evenNumbers += 1
            else:
                evenNumbers += 1
        else:
            oddNumbers += 1
        if(arr[i] > biggestNumber):
            biggestNumber = arr[i]
            
        if(arr[i] < smallestNumber):
            smallestNumber = arr[i]

    print("Pierwsza parzysta",firstEvenNumber)
    print("Ilosc liczb nieparzystych",oddNumbers)
    print("Ilosc liczb parzystych",evenNumbers)
    print("Najmniejasza liczba",smallestNumber) 
    print("Najwieksza liczba",biggestNumber)
    print("Roznica pomiędzy najwieksza i najmniejsza liczba",biggestNumber - smallestNumber)       

def generateRandomNumbers(lenght):
    numbers = []
    for i in range(0,lenght):
        numbers.append(randint(0,10000))
    return numbers 

filterArray(generateRandomNumbers(100))

#Parzysta z pliku


def generateRandomNumbersToFile(lenght):
    numbers = ''
    for i in range(0,lenght):
        if i == lenght - 1:
            numbers += str(randint(0,10000)) 
        else:
            numbers += str(randint(0,10000)) + ","

    with open('numbers.txt', 'w') as file:
        file.write(numbers)

def firstEvenFromFile():
    with open("numbers.txt", "r") as file:
        numbersAsString = file.read()
        numbers = numbersAsString.split(',')                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
        for i in range(len(numbers)):
            numbers[i] = int(numbers[i])
        filterArray(numbers)    

#generateRandomNumbersToFile(100)
#firstEvenFromFile()
