import sys

def twoSums(list,sum):
    sum = int(sum)
    pair = []
    hashTable = {}
    for index, value in enumerate(list):
        value = int(value)
        complement = sum - value
        if complement not in hashTable:
            hashTable[value] = index
        else:
            pair = [hashTable[complement],index]

    if(len(pair) == 0):
        return "output tidak ditemukan"
    elif(len(pair) == 2):
        return pair
    else:
        return "Invalid"


if __name__ == "__main__":
    if(len(sys.argv) == 3):
        input = (sys.argv[1][1:len(sys.argv[1])-1]).split(",")
        sum = sys.argv[2]
        output = twoSums(input,sum)
        print(output)
    elif(len(sys.argv) == 1):
        listInput = [[2,7,11,15],[3,2,4],[3,3]]
        sum = [13,6,6]
        for x in range(3):
            output = twoSums(listInput[x],sum[x])
            print(output)
    else:
        print("Argument tidak valid")