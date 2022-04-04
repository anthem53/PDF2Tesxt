startSymbolList = ['•','–','']
endSymbolList = ['.','!','?']
properNounList = ["StyleGAN2"]
replaceDict = {}

testSentence  = '''
Though these techniques can potentially represent complicated and highresolution geometry, they have so far been limited to simple shapes with low\n
geometric complexity, resulting in oversmoothed renderings. We show that an alternate strategy of optimizing networks to encode 5D radiance fields (3D volumes with 2D view-dependent appearance) can represent higher-resolution geometry\n
and appearance to render photorealistic novel views of complex scenes.
'''
def initReplaceDict():
    replaceDict['StyleGAN2'] = '"StyleGAN2"'
    replaceDict['StyleGAN'] = '"StyleGAN"'
    replaceDict[''' ""StyleGAN"2" '''] = '"StyleGAN2"'
    replaceDict['AdaIN'] = '"[AdaIN]"'
    replaceDict[''] = ''

def replaceword(s):
    for key  in replaceDict:
        s = s.replace(key,replaceDict[key])
    return s

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
    initReplaceDict()
    list = s.split("\n")
    can_Entered = False
    isFirst = True
    isSameWord = False
    result = []

    for s_iter in list:
        if s_iter != '':
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
        else : # s_iter == ''
            result.append("\n")
            pass

        
    resultSentence = ' '.join(result)
    resultSentence = replaceword(resultSentence)

    return resultSentence

def TESTNEWLINEPRINT():
    print(execute(testSentence))

if __name__ == "__main__":
    TESTNEWLINEPRINT()