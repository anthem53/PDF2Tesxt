startSymbolList = ['•','–','']
endSymbolList = ['.','!','?']


def isStart(s):
    if s[0] in startSymbolList:
        return True
    else :
        return False
    
def isEnd(s):
    if s[-1] in endSymbolList:
        return True
    else:
        return False

def execute(s):
    list = s.split("\n")
    can_Entered = False
    isFirst = True
    result = []

    for s_iter in list:
        
        if isStart(s_iter) == True:
            if isFirst == True :
                result.append(s_iter)
            else :
                result.append("\n" + s_iter)
                can_Entered = False
        elif can_Entered == True :
            result.append("\n" + s_iter)
            can_Entered = False
        else:
            result.append(s_iter)

        if isEnd(s_iter) == True:
            
            can_Entered = True 
        else :
            pass
        isFirst = False 
    resultSentence = ' '.join(result)
    return resultSentence

def TESTNEWLINEPRINT():
    print("THIS IS TEST FUNCTION")