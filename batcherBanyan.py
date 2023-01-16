import random

def generateRandomNumbers(n):
    inputList = random.sample(range(0, 15), n)
    return inputList

def sortInputList(nonSortedList):
    return nonSortedList.sort()

def convertDecimalToBinary(value):
    temp = value
    i = 0
    bnum = []
    while value!=0:
        rem = value%2
        bnum.insert(i, rem)
        i = i+1
        value = int(value/2)

    i = i-1
    bin=[]
    while i>=0:
        bin.append(str(bnum[i]))
        i = i-1

      # initialize an empty string
    str1 = "" 
    
    # traverse in the string  
    for ele in bin: 
        str1 += ele 

    str1 = str1.zfill(4);
    
    # return string  
    return str1 

def mapNodes():
        initialNodesMapping = {0:'A1',
                    1:'A2',
                    2:'A3',
                    3:'A4',
                    4:'A5',
                    5:'A6',
                    6:'A7',
                    7:'A8',
                    8:'A1',
                    9:'A2',
                    10:'A3',
                    11:'A4',
                    12:'A5',
                    13:'A6',
                    14:'A7',
                    15:'A8'
                    }

        a_b = {
            'A1' : ['B1', 'B5'],
            'A2' : ['B2', 'B6'],
            'A3' : ['B3', 'B7'],
            'A4' : ['B4', 'B8'],
            'A5' : ['B1', 'B5'],
            'A6' : ['B2', 'B6'],
            'A7' : ['B3', 'B7'],
            'A8' : ['B4', 'B8'],
        }

        b_c = {
            'B1' : ['C1', 'C3'],
            'B2' : ['C2', 'C4'],
            'B3' : ['C1', 'C3'],
            'B4' : ['C2', 'C4'],
            'B5' : ['C5', 'C7'],
            'B6' : ['C6', 'C8'],
            'B7' : ['C5', 'C7'],
            'B8' : ['C6', 'C8'],
        }

        c_d = {
            'C1' : ['D1', 'D2'],
            'C2' : ['D1', 'D2'],
            'C3' : ['D3', 'D4'],
            'C4' : ['D3', 'D4'],
            'C5' : ['D5', 'D6'],
            'C6' : ['D5', 'D6'],
            'C7' : ['D6', 'D7'],
            'C8' : ['D6', 'D7'],            
        }

        d_output = {
            'D1' : ['output - 0', 'Output - 1'],
            'D2' : ['output - 2', 'Output - 3'],
            'D3' : ['output - 4', 'Output - 5'],
            'D4' : ['output - 6', 'Output - 7'],
            'D5' : ['output - 8', 'Output - 9'],
            'D6' : ['output - 10', 'Output - 11'],
            'D7' : ['output - 12', 'Output - 13'],
            'D8' : ['output - 14', 'Output - 15'],             
        }

        return initialNodesMapping, a_b, b_c, c_d, d_output;


if __name__ == "__main__":
    n = int(input("Enter the number of inputs(range 0 to 15) that you want to provide to this program "))
    inputList = generateRandomNumbers(n);
    print("Random Number Generated which are generated : " , inputList)
    sortInputList(inputList)
    print("Sorted List : " , inputList)

    mappingNodes, a_b, b_c, c_d, d_output = mapNodes();
    
    for i in inputList:
        print("path for", i, mappingNodes[i])
        binaryValue = convertDecimalToBinary(i)

        x= 0
        p1 = a_b.get(mappingNodes[i])
        pathA = p1[int(binaryValue[x])]

        x+=1
        p2 = b_c.get(pathA)
        pathB = p2[int(binaryValue[x])]

        x+=1
        p3 = c_d.get(pathB)
        pathC = p3[int(binaryValue[x])]

        x+=1
        p4 = d_output.get(pathC)
        pathD = p4[int(binaryValue[x])]
        output = mappingNodes[i]+" -> "+pathA+" -> "+pathB+" -> "+pathC+" -> "+pathD;
        print( output )


