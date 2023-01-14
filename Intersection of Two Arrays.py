def intersection(num1,num2):
    def findintersection(set1,set2):
        return [ element for element in set1 if element in set2]

    set1= set(num1)
    set2= set(num2)
    
    if(len(set1)<len(set2)):
        return findintersection(set1,set2)
    else:
        return findintersection(set2,set1)
    
print(intersection([4,9,5],[9,4,9,8,4]))