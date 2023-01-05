def finalValueAfterOperations( operations):

    count  = 0
    length = len(operations)
    for i in range(length):
        if(operations[i] == "++X" or operations[i] =="X++"):
            count+=1
        elif(operations[i] == "--X" or operations[i] == "X--"):
            count-=1
    return count
    
print(finalValueAfterOperations(["--X","X++","X++"]))

# output = 1