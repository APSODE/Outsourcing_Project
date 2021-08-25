try:
    from Class.USER_JSON_RW.rw_json import READ_WRITE
    from Class.WEATHER_CHECK.WEATHER_CHECK import WEATHER
    from tkinter import *
    import tkinter.messagebox as MSGBOX
    import tkinter.ttk as TTK
    from selenium import webdriver
    import time, datetime, sys, os

except:
    from Class.PYTHON_MODUAL_DOWN.PYTHON_MODUAL_DOWN import MODUAL_DOWNLOAD

    MODUAL_DOWNLOAD.DOWNLOAD
    from Class.USER_JSON_RW.rw_json import READ_WRITE
    from Class.WEATHER_CHECK.WEATHER_CHECK import WEATHER
    from tkinter import *
    import tkinter.messagebox as MSGBOX
    import tkinter.ttk as TTK
    from selenium import webdriver
    import time, datetime, sys, os



# 1.주택,아파트 
# 2.어느 지역에 사시나요(기상청 습도 자동 나옴)
# 3.흡연자가 있나요?
# 4.인덕션 사용 가구 인가요?
# 5.가스 자동 잠금벨브가 있나요?

class INTERNAL_FUNC:
    def WEATHER_RETURN():
        SELECT_TYPE = QUESTION_1_COMBO_BOX.get()
        MSGBOX.showinfo("확인버튼을 눌러주세요.", f"{SELECT_TYPE}으로 진행합니다")
        RETURN_DATA_LIST = WEATHER.TODAY_WEATHER()

        HUMIDITY_DATA = RETURN_DATA_LIST[0]
        CURRENT_HUMIDITY_CONDITION = HUMIDITY_DATA[0]
        CURRENT_HUMIDITY_VALUE = HUMIDITY_DATA[1]
        CURRETN_HUMIDITY = HUMIDITY_DATA[2]

        TEMP_DATA = RETURN_DATA_LIST[1]
        CURRENT_TEMP_VALUE = TEMP_DATA[0]
        CURRETN_TEMP = TEMP_DATA[1]

        if CURRENT_HUMIDITY_CONDITION == 1:
            CURRENT_HUMIDITY_TYPE = "건조한 기후"
        elif CURRENT_HUMIDITY_CONDITION == 2:
            CURRENT_HUMIDITY_TYPE = "평범한 기후"
        elif CURRENT_HUMIDITY_CONDITION == 3:
            CURRENT_HUMIDITY_TYPE = "습한 기후"

        PRINT_WEATHER_VALUE = f"온도 : {CURRENT_TEMP_VALUE}\n습도 : {CURRENT_HUMIDITY_VALUE}\n{CURRENT_HUMIDITY_TYPE}"

        WEATHER_VALUE_TEXT = Label(MAIN_UI, text = PRINT_WEATHER_VALUE)
        WEATHER_VALUE_TEXT.place(relx = 0.0, rely = 0.0, anchor = NW)
        WEATHER_VALUE_TEXT.pack()
        # print(f"RETURN_DATA_LIST = {RETURN_DATA_LIST}")

MAIN_UI = Tk()
MAIN_UI.title("AI 화재 예방")
MAIN_UI.geometry("680x480")
    
    



SELECT_TYPE_LIST = ["주택", "아파트"]
SELECT_VALUE = [str(VALUE) for VALUE in SELECT_TYPE_LIST]
QUESTION_1_COMBO_BOX = TTK.Combobox(MAIN_UI, height = 2, width = 50, values = SELECT_VALUE, state = "readonly")
QUESTION_1_COMBO_BOX.pack()
QUESTION_1_COMBO_BOX.set("현재 거주중인 주택 유형을 선택해주세요.")

QUESTION_1_BUTTON = Button(MAIN_UI, text = "설정", command = INTERNAL_FUNC.WEATHER_RETURN)
QUESTION_1_BUTTON.pack()

MAIN_UI.mainloop()








