from dataclasses import replace
import newLine


newLine.initReplaceDict()

for x in newLine.replaceDict:
    print(x,newLine.replaceDict[x])
