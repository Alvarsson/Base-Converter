import math

#TODO: SMALL TO SMALL
#TODO: LARGE TO LARGE
def converter(tal, startBase, endBase): #Konverterar tal
    if startBase == 10 and endBase < 10: #För decimal till alla mindre
        decToSmall(tal,startBase,endBase)

    elif endBase == 10 and startBase < 10:
        smallToDec(tal,startBase,endBase)

    elif endBase > 10 and startBase == 10:
        decToLarge(tal,startBase,endBase)

    elif endBase == 10 and startBase > 10:
        largeToDec(tal,startBase,endBase)

    elif endBase > 10 and startBase < 10:
        smlToLrg(tal,startBase,endBase)
    elif endBase < 10 and startBase > 10:
        lrgTosml(tal,startBase,endBase)

def decToSmall(tal,startBase,endBase):
    array = []
    string = ""
    while tal > 0:
        rest = tal % endBase
        tal = tal // endBase
        array.append(rest) # Första varvet [0], andra varvet [0,0] För talet 12  >>> [0,0,1,1]
        array.reverse()
    for i in array:
        string = string + str(i)
    print("End value is: "+ string) 
    
def smallToDec(tal,startBase,endBase):
    array = []
    value = 0
    count = 0
    while tal > 0: #Ett sätt att göra array på
        i = tal % 10
        array.append(i)
        tal = tal // 10
    for i in array:
        value = value + i*(startBase**count)
        count = count + 1
    print("decimal value is: "+str(value))
    return value

def decToLarge(tal,startBase,endBase):
    array = []
    tString = ""
    while tal > 0:
        rest = tal % endBase
        tal = tal // endBase
        array.append(rest)
    array.reverse()
    for i in array:
        if (i + 55) >= 65:
            tString = tString + chr(55+i)
        else:
            tString = tString + str(i)
    print("End value is: "+ tString)

def largeToDec(tal,startBase,endBase):
    array = [] #WHAT?
    value = 0
    count = 0
    for i in tal: #annta sätt att göra array på
        array.append(i)
    array.reverse()
    for i in array:
        if ord(i) >= 65: #Kanske bra med övre gräns också
            value = value + (ord(i)-55)*startBase**count
            count += 1
        else:
            value = value + int(i)*(startBase**count)
            count += 1
    print("Decimal value is: "+ str(value))
    return value

def lrgTosml(tal,startBase,endBase):
    nytt_tal = largeToDec(tal,startBase,10)
    decToSmall(nytt_tal,10,endBase)
def smlToLrg(tal,startBase,endBase):
    nytt_tal = smallToDec(tal,startBase,10)
    decToLarge(nytt_tal,10,endBase)


converter(11001000,2,4)

