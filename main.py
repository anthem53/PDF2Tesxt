import tkinter
from tkinter import scrolledtext
from tkinter.constants import COMMAND, S
from typing import Text



def getUIWithName(UI_LIST,UI_name):
    for (elem,name) in UI_LIST:
        if name == UI_name:
            return elem

    print("Wrong UI_name input. Check your code ")
    return None

def translate (UI_LIST):

    targetText = getUIWithName(UI_LIST,"targetText")
    traslatedText = getUIWithName(UI_LIST,"traslatedText")
    content = targetText.get(1.0, tkinter.END+"-1c")
    traslatedText.delete(1.0,"end")
    traslatedText.insert(1.0,content)

def removeNewline(UI_LIST):
    targetText = getUIWithName(UI_LIST,"targetText")
    traslatedText = getUIWithName(UI_LIST,"traslatedText")
    content = targetText.get(1.0, tkinter.END+"-1c")
    content = content[::-1]
    traslatedText.delete(1.0,"end")
    traslatedText.insert(1.0,content)
    pass
    

def addMenu(root):
    menubar = tkinter.Menu(root)
    #menubar.pack(side="top")
    filemenu = tkinter.Menu(menubar)
    filemenu.add_command(label="Open")
    filemenu.add_command(label="Save")
    filemenu.add_command(label="Exit")
    menubar.add_cascade(label="File", menu=filemenu)
    root.config(menu=menubar)
    return [(filemenu,"fileMenu")]

def addTargetText(root):
    targetTextFrame = tkinter.Frame(root)
    targetTextFrame.pack(side="left",fill="both")

    TargetTextTitle = tkinter.Label(targetTextFrame , text= "Your Text")
    TargetTextTitle.pack(side="top")

    targetText= scrolledtext.ScrolledText(targetTextFrame)
    targetText.config(font=("맑은 고딕", 11))
    targetText.pack(side="top",fill="both")
    return [(targetText,"targetText")]

def addTranslatedText(root):
    targetTextFrame2 = tkinter.Frame(root)
    targetTextFrame2.pack(side="left",fill="both")

    traslatedTextTitle = tkinter.Label(targetTextFrame2 , text= "Translated Text")
    traslatedTextTitle.pack(side="top")

    traslatedText= scrolledtext.ScrolledText(targetTextFrame2)
    traslatedText.config(font=("맑은 고딕", 11))    
    traslatedText.pack(side="top",fill="both")
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

    UI_result = addMenu(root) + addTargetText(root)+ addButtons(root)+  addTranslatedText(root)
    
    return UI_result

def init_UI_Action(root,UI_LIST):

    removeNewlineButton = getUIWithName(UI_LIST,"newlineButton")
    translateButton = getUIWithName(UI_LIST, "translateButton")

    removeNewlineButton.config(command = lambda: removeNewline(UI_LIST))
    translateButton.config(command = lambda: translate(UI_LIST))

    pass

if __name__ == "__main__":
    root = tkinter.Tk()
    root.title("PDF 2 TEXT")
    root.geometry("1300x550")

    UI_LIST = init_UI(root)
    init_UI_Action(root,UI_LIST)
    print(UI_LIST)
    

    root.mainloop()

    print("TEST")
