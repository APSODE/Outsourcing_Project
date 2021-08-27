from tkinter import *
import tkinter.messagebox as MSGBOX
import tkinter.ttk as TTK


SELECT_TYPE_LIST = ["TEST1", "TEST2"]
def CALL_BACK_FUNC(TEXT):
    print("SUCCESS")
    print(f"TEXT = {TEXT}")
    QUESTION_1_COMBO_BOX = TTK.Combobox(MAIN_UI, height = 2, width = 50, values = SELECT_TYPE_LIST, state = "readonly")
    QUESTION_1_COMBO_BOX.set("TEST_1")
    QUESTION_1_COMBO_BOX.grid(row = 1, column = 0)
    def TEST():
        print("TEST_FUNC_WORK")

    




MAIN_UI = Tk()
MAIN_UI.title("AI 화재 예방")
MAIN_UI.geometry("680x480")

PRIMARY_DISPLAY_TEXT = "TEST"

QUESTION_1_COMBO_BOX = TTK.Combobox(MAIN_UI, height = 2, width = 50, values = SELECT_TYPE_LIST, state = "readonly")
QUESTION_1_COMBO_BOX.set(PRIMARY_DISPLAY_TEXT)
QUESTION_1_COMBO_BOX.grid(row = 0, column = 0)
QUESTION_1_COMBO_BOX.bind("<<ComboboxSelected>>", CALL_BACK_FUNC(QUESTION_1_COMBO_BOX.get()))
print(SELECT_TYPE_LIST)
MAIN_UI.mainloop()