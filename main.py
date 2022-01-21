from pickle import TRUE
import tkinter
from tkinter import scrolledtext
from tkinter.constants import COMMAND, S
from tkinter import messagebox
from typing import Text
import newLine
from translate import init_translate, writeSource,readTarget,quit_translate_window

startSymbolList = ['•','–','']
endSymbolList = ['.','!','?']

# 8226, 8211, 61548
# newline ascii code  10 == \n

UI_DEBUG = False
font_size = 23
currentTranslateWindow = None

def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        if UI_DEBUG == False:
            quit_translate_window()
        root.destroy()

def on_closeing_window(window):
    window.destroy()
    currentTranslateWindow = None
def on_closing_translateWindow():
    global currentTranslateWindow
    if(currentTranslateWindow != None):
        currentTranslateWindow.destroy()
        currentTranslateWindow = None

def getUIWithName(UI_LIST,UI_name):
    for (elem,name) in UI_LIST:
        if name == UI_name:
            return elem

    print("Wrong UI_name input. Check your code. Wrong UI_NAME : [",UI_name,"]")
    return None

def printCharinString(s):
    print("start printCharinString function")
    for c in s:
        print("c",c,ord(c))
    print("end printCharinString function")

def translate (UI_LIST):
    global currentTranslateWindow
    if currentTranslateWindow != None :
         on_closeing_window(currentTranslateWindow)
         
    targetText = getUIWithName(UI_LIST,"targetText")
    
    content = targetText.get(1.0, tkinter.END+"-1c")
    writeSource(content)
    translateResult = readTarget()
 
 
    currentTranslateWindow = tkinter.Tk()
    currentTranslateWindow.title("Translate result")
    currentTranslateWindow.geometry("1300x550")

    # create new window
    tempMenubar = tkinter.Menu(currentTranslateWindow)
    filemenu = tkinter.Menu(tempMenubar,tearoff=0)
    filemenu.add_cascade(label="Exit",command= lambda: currentTranslateWindow.destroy())
    currentTranslateWindow.config(menu=tempMenubar)
    targetText= scrolledtext.ScrolledText(currentTranslateWindow)
    targetText.config(font=("맑은 고딕", 27))
    targetText.pack(expand=1,side="bottom",fill="both")
    targetText.delete(1.0,"end")
    targetText.insert(1.0,translateResult)
    targetText.config(state='disabled')
    currentTranslateWindow.protocol("WM_DELETE_WINDOW", on_closing_translateWindow)
    currentTranslateWindow.mainloop()

def removeNewline(UI_LIST):
    targetText = getUIWithName(UI_LIST,"targetText")
    
    content = targetText.get(1.0, tkinter.END+"-1c")
    #print(content)
    print("content len", len(content))
    #printCharinString(content)
    
    result = newLine.execute(content)
    targetText.delete(1.0,"end")
    targetText.insert(1.0,result)
    pass

def setFontSize(UI_LIST,fontsize):
    print("setFontSize function start")
    print("UI_LIST : ",UI_LIST,", fontsize : ", fontsize )
    targetText = getUIWithName(UI_LIST,"targetText")
    targetText.config(font=("맑은 고딕", fontsize))
    


    

def addMenu(root,UI_LIST):
    menubar = tkinter.Menu(root)
    filemenu = tkinter.Menu(menubar,tearoff=0)
    menubar.add_cascade(label="File", menu=filemenu)
    filemenu.add_command(label="Open")
    filemenu.add_command(label="Save")
    filemenu.add_command(label="Exit",command=on_closing)

    menubar.add_cascade(label="remove newLine", command = lambda: removeNewline(UI_LIST))
    menubar.add_cascade(label="translate", command = lambda: translate(UI_LIST))

    fontmenu = tkinter.Menu(menubar,tearoff=0)
    menubar.add_cascade(label="font size", menu=fontmenu)
    fontmenu.add_command(label="11",command= lambda: setFontSize(UI_LIST,11))
    fontmenu.add_command(label="12",command= lambda: setFontSize(UI_LIST,12))
    fontmenu.add_command(label="14",command= lambda: setFontSize(UI_LIST,14))
    fontmenu.add_command(label="17",command= lambda: setFontSize(UI_LIST,17))
    fontmenu.add_command(label="20",command= lambda: setFontSize(UI_LIST,20))
    fontmenu.add_command(label="23",command= lambda: setFontSize(UI_LIST,23))
    fontmenu.add_command(label="27",command= lambda: setFontSize(UI_LIST,27))
    fontmenu.add_command(label="35",command= lambda: setFontSize(UI_LIST,35))
    fontmenu.add_command(label="48",command= lambda: setFontSize(UI_LIST,48))
    
    root.config(menu=menubar)
    return [(filemenu,"fileMenu")]

def addTargetText(root):
    targetTextFrame = tkinter.Frame(root)
    targetTextFrame.pack(expand=1,side="left",fill="both")

    TargetTextTitle = tkinter.Label(targetTextFrame , text= "Your Text")
    TargetTextTitle.pack(side="top")

    targetText= scrolledtext.ScrolledText(targetTextFrame)
    targetText.config(font=("맑은 고딕", font_size))
    targetText.pack(expand=1,side="bottom",fill="both")
    return [(targetText,"targetText")]

def addTranslatedText(root):
    targetTextFrame2 = tkinter.Frame(root)
    targetTextFrame2.pack(expand=1,side="right",fill="both")

    traslatedTextTitle = tkinter.Label(targetTextFrame2 , text= "Translated Text")
    traslatedTextTitle.pack(side="top")

    traslatedText= scrolledtext.ScrolledText(targetTextFrame2)
    traslatedText.config(font=("맑은 고딕", 11))    
    traslatedText.pack(expand=1,side="bottom",fill="both")
    return [(traslatedText,"traslatedText")]
    
def addButtons(root):
    buttonFrame = tkinter.Frame(root)
    buttonFrame.pack(side="left")

    newlineButton = tkinter.Button(buttonFrame, width=15, repeatdelay=1000, repeatinterval=100)
    newlineButton.config(text= "Remove\nWrong newline")
    newlineButton.pack(side="top")

    translateButton= tkinter.Button(buttonFrame, width=15, repeatdelay=1000, repeatinterval=100)
    translateButton.config(text= "Translate")
    translateButton.pack(side="top")


    return [(newlineButton,"newlineButton"),(translateButton,"translateButton")]

def init_UI(root):
    UI_result = addTargetText(root)
    UI_result = UI_result + addMenu(root,UI_result)
    return UI_result

def init_UI_Action(root,UI_LIST):

    removeNewlineButton = getUIWithName(UI_LIST,"newlineButton")
    translateButton = getUIWithName(UI_LIST, "translateButton")



if __name__ == "__main__":
    
    root = tkinter.Tk()
    root.title("PDF 2 TEXT")
    root.geometry("1300x550")

    UI_LIST = init_UI(root)
    #init_UI_Action(root,UI_LIST)
    root.protocol("WM_DELETE_WINDOW", on_closing)
    
    if UI_DEBUG == False:
        init_translate()

    root.mainloop()

    print("TEST")
