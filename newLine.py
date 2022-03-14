startSymbolList = ['•','–','']
endSymbolList = ['.','!','?']
properNounList = ["StyleGAN2"]


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
def isProperNoun(s):
    if s in properNounList:
        return True 
    else:
        return False

def execute(s):
    list = s.split("\n")
    can_Entered = False
    isFirst = True
    isSameWord = False
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
            if isSameWord == False:
                result.append(s_iter)
            else:
                result[-1] = result[-1][0:len(result[-1]) - 1] + s_iter
                isSameWord = False
                pass
        if s_iter[-1] == "-":
            isSameWord = True
        else:
            isSameWord = False
            
        if isEnd(s_iter) == True:
            can_Entered = True 
        else :
            pass
        isFirst = False 

        
    resultSentence = ' '.join(result)
    resultSentence = resultSentence.replace('StyleGAN2','"StyleGAN2"')
    resultSentence = resultSentence.replace('StyleGAN','"StyleGAN"')
    resultSentence = resultSentence.replace(''' ""StyleGAN"2" ''','"StyleGAN2"')

    return resultSentence

def TESTNEWLINEPRINT():
    print("THIS IS TEST FUNCTION")