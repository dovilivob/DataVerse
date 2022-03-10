import json

# title = input('title: ')
# size = input('Intlist size: ')

title, size = 'hgcs', 5184

inputFile, outputFile = './Arrays.txt', './Arrays.Json'

deleted = "IntList size="+str(size)+' ['

with open(inputFile, 'r', encoding='utf-8') as file:
    string = file.read()[0:-2]


def getIntList(string, comma):
    strArr = string.split(comma)
    IntArr = []
    for i in range(len(strArr)):
        IntArr.append(int(strArr[i]))
    return IntArr


start = False


def checkIfStart(intArr):
    count = 0
    standard = intArr[0]
    for element in intArr:
        if(element == standard):
            count += 1
    if(count >= size - 100):
        return False
    else:
        return True


string = string.replace(deleted, '')
string = string.replace(' ', '')
arr = string.split(']')
finalArr = []
for i in range(len(arr)):
    intArr = getIntList(arr[i], ',')
    if(start == True):
        finalArr.append(intArr)
    elif (start == False):
        if(checkIfStart(intArr)):
            start = True
        else:
            start = False

        # print(finalArr)


with open(outputFile, 'r', encoding='utf-8') as file:
    jsonFile = json.loads(file.read())

with open(outputFile, 'w', encoding='utf-8') as file:
    finalJson = {title: finalArr}
    jsonFile.update(finalJson)
    file.write(
        json.dumps(jsonFile)
    )
