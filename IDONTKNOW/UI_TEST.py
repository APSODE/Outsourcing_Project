import time
from tkinter import *
import tkinter.messagebox as MSGBOX
import tkinter.ttk as TTK




SELECTED_EVENT_BINDING = "<<ComboboxSelected>>"
TEST_LIST = []

def CREATE():
    BTN.destroy()
    for COUNTER in range(10):
        
        TEST_COMBO_BOX = TTK.Combobox(MAIN_UI, values = ["TEST1", "TEST2", "TEST3"], height = 3, state = "readonly")
        time.sleep(0.5)
        TEST_COMBO_BOX.grid(row = COUNTER, column = 0)

MAIN_UI = Tk()
MAIN_UI.title("AI 화재 예방")
MAIN_UI.geometry("680x480")

BTN = Button(MAIN_UI, text = "start", command = CREATE)
BTN.pack()






# TEST_BTN = Button(TEST_FRAME, text = "테스트").pack()

MAIN_UI.mainloop()