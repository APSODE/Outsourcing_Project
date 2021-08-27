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

QUESTION_PROCESS_LIST = []

CONFIG_DIR = ".\\Class\\WEATHER_CHECK\\WEATHER_CHECK_CONFIG\\WEATHER_CHECK_CONFIG.json"

class INTERNAL_FUNC:
    def BTN2_CMD(EVENT):
        # if QUESTION_2_VALUE != QUESTION_2_PRIMARY_DISPLAY_TEXT:
        
        QUESTION_2_VALUE = QUESTION_2_COMBO_BOX.get()
        SPECIFIC_AREA_NAME_LIST = [SPECIFIC_AREA_NAME for SPECIFIC_AREA_NAME in READ_CONFIG_DATA["AREA_LIST"][QUESTION_2_VALUE]]
        SPECIFIC_AREA_NAME_LIST.append("이 항목을 선택하여 취소")
        QUESTION_2_1_COMBO_BOX = TTK.Combobox(MAIN_UI, width = 50, values = SPECIFIC_AREA_NAME_LIST, state = "readonly")
        QUESTION_2_1_COMBO_BOX.set(QUESTION_2_1_PRIMARY_DISPLAY_TEXT)
        QUESTION_2_1_COMBO_BOX.grid(row = 2, column = 0)   

        def CANCEL_CHECK(EVENT):
            QUESTION_2_1_COMBO_BOX.bind()
            QUESTION_2_1_VALUE = QUESTION_2_1_COMBO_BOX.get()
            if QUESTION_2_1_VALUE == "이 항목을 선택하여 취소":
                # print("작동확인")
                QUESTION_2_1_COMBO_BOX.destroy() 
                QUESTION_2_COMBO_BOX.set(QUESTION_2_PRIMARY_DISPLAY_TEXT)
            else:
                START_PROGRAM_BUTTON = Button(MAIN_UI, text = "시작", command = WEATHER_RETURN)
                START_PROGRAM_BUTTON.place(relx = 0.875, rely = 0.0, anchor = NE, width = 80, height = 60)
                # WEATHER_RETURN
        def WEATHER_RETURN():
            SELECT_TYPE = QUESTION_1_COMBO_BOX.get()
            AREA_NAME = QUESTION_2_COMBO_BOX.get()
            SPECIFIC_AREA_NAME = QUESTION_2_1_COMBO_BOX.get()
            INPUT_AREA_INFO_LIST = [AREA_NAME, SPECIFIC_AREA_NAME]

            if SELECT_TYPE != PRIMARY_DISPLAY_TEXT and AREA_NAME != QUESTION_2_PRIMARY_DISPLAY_TEXT and SPECIFIC_AREA_NAME != QUESTION_2_1_PRIMARY_DISPLAY_TEXT:
                MSGBOX.showinfo("확인버튼을 눌러주세요.", f"{SELECT_TYPE}으로 진행합니다")
                RETURN_DATA_LIST = WEATHER.TODAY_WEATHER(AREA_INFO_LIST = INPUT_AREA_INFO_LIST)

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

                PRINT_WEATHER_VALUE = f"온도 : {CURRENT_TEMP_VALUE}\n습도 : {CURRENT_HUMIDITY_VALUE} (일 평균)\n{CURRENT_HUMIDITY_TYPE}"

                WEATHER_VALUE_TEXT = Label(MAIN_UI, text = PRINT_WEATHER_VALUE)
                WEATHER_VALUE_TEXT.place(relx = 0.0, rely = 0.0, anchor = NW)
                QUESTION_1_COMBO_BOX.destroy()
                QUESTION_2_COMBO_BOX.destroy()
                QUESTION_2_1_COMBO_BOX.destroy()
                # START_PROGRAM_BUTTON.destroy()
                # QUESTION_PROCESS_LIST.append(1)
                # WEATHER_VALUE_TEXT.pack()
            else:
                PRINT_ERROR_MESSAGE = ""
                ERROR_COUNT = 0
                if SELECT_TYPE == PRIMARY_DISPLAY_TEXT:
                    ERROR_COUNT += 1
                    PRINT_ERROR_MESSAGE += f"{ERROR_COUNT}. 주택 / 아파트 이 두 유형중 하나는 꼭 선택해야합니다.\n"
                if AREA_NAME == QUESTION_2_PRIMARY_DISPLAY_TEXT:
                    ERROR_COUNT += 1
                    PRINT_ERROR_MESSAGE += f"{ERROR_COUNT}. 도 / 특별시 항목은 필수로 채워져야 합니다.\n"
                if SPECIFIC_AREA_NAME == QUESTION_2_1_PRIMARY_DISPLAY_TEXT:
                    ERROR_COUNT += 1
                    PRINT_ERROR_MESSAGE += f"{ERROR_COUNT}. 세부도시 항목은 필수로 채워져야 합니다.\n"
                MSGBOX.showinfo("ERROR", f"{PRINT_ERROR_MESSAGE}")

        QUESTION_2_1_COMBO_BOX.bind("<<ComboboxSelected>>", CANCEL_CHECK)

        
        
        

        # def WEATHER_RETURN():
        #     SELECT_TYPE = QUESTION_1_COMBO_BOX.get()
        #     AREA_NAME = QUESTION_2_COMBO_BOX.get()
        #     SPECIFIC_AREA_NAME = QUESTION_2_1_COMBO_BOX.get()

        #     if SELECT_TYPE != PRIMARY_DISPLAY_TEXT and AREA_NAME != QUESTION_2_PRIMARY_DISPLAY_TEXT and SPECIFIC_AREA_NAME != QUESTION_2_1_PRIMARY_DISPLAY_TEXT:
        #         MSGBOX.showinfo("확인버튼을 눌러주세요.", f"{SELECT_TYPE}으로 진행합니다")
        #         RETURN_DATA_LIST = WEATHER.TODAY_WEATHER()

        #         HUMIDITY_DATA = RETURN_DATA_LIST[0]
        #         CURRENT_HUMIDITY_CONDITION = HUMIDITY_DATA[0]
        #         CURRENT_HUMIDITY_VALUE = HUMIDITY_DATA[1]
        #         CURRETN_HUMIDITY = HUMIDITY_DATA[2]

        #         TEMP_DATA = RETURN_DATA_LIST[1]
        #         CURRENT_TEMP_VALUE = TEMP_DATA[0]
        #         CURRETN_TEMP = TEMP_DATA[1]

        #         if CURRENT_HUMIDITY_CONDITION == 1:
        #             CURRENT_HUMIDITY_TYPE = "건조한 기후"
        #         elif CURRENT_HUMIDITY_CONDITION == 2:
        #             CURRENT_HUMIDITY_TYPE = "평범한 기후"
        #         elif CURRENT_HUMIDITY_CONDITION == 3:
        #             CURRENT_HUMIDITY_TYPE = "습한 기후"

        #         PRINT_WEATHER_VALUE = f"온도 : {CURRENT_TEMP_VALUE}\n습도 : {CURRENT_HUMIDITY_VALUE}\n{CURRENT_HUMIDITY_TYPE}"

        #         WEATHER_VALUE_TEXT = Label(MAIN_UI, text = PRINT_WEATHER_VALUE)
        #         WEATHER_VALUE_TEXT.place(relx = 0.0, rely = 0.0, anchor = NW)
        #         QUESTION_1_COMBO_BOX.destroy()
        #         # START_PROGRAM_BUTTON.destroy()
        #         # QUESTION_PROCESS_LIST.append(1)
        #         # WEATHER_VALUE_TEXT.pack()
        #     else:
        #         PRINT_ERROR_MESSAGE = ""
        #         ERROR_COUNT = 0
        #         if SELECT_TYPE == PRIMARY_DISPLAY_TEXT:
        #             ERROR_COUNT += 1
        #             PRINT_ERROR_MESSAGE += f"{ERROR_COUNT}. 주택 / 아파트 이 두 유형중 하나는 꼭 선택해야합니다.\n"
        #         if AREA_NAME == QUESTION_2_PRIMARY_DISPLAY_TEXT:
        #             ERROR_COUNT += 1
        #             PRINT_ERROR_MESSAGE += f"{ERROR_COUNT}. 도 / 특별시 항목은 필수로 채워져야 합니다.\n"
        #         if SPECIFIC_AREA_NAME == QUESTION_2_1_PRIMARY_DISPLAY_TEXT:
        #             ERROR_COUNT += 1
        #             PRINT_ERROR_MESSAGE += f"{ERROR_COUNT}. 세부도시 항목은 필수로 채워져야 합니다.\n"
        #         MSGBOX.showinfo("ERROR", f"{PRINT_ERROR_MESSAGE}")

        
        

MAIN_UI = Tk()
MAIN_UI.title("AI 화재 예방")
MAIN_UI.geometry("680x480")

PRIMARY_DISPLAY_TEXT = "현재 거주중인 주택 유형을 선택해주세요."
QUESTION_2_PRIMARY_DISPLAY_TEXT = "도 / 특별시"
QUESTION_2_1_PRIMARY_DISPLAY_TEXT = "세부도시명"

EXIT_PROGRAM_BUTTON = Button(MAIN_UI, text = "종료", command = MAIN_UI.destroy)
EXIT_PROGRAM_BUTTON.place(relx = 1.0, rely = 0.0, anchor = NE, width = 80, height = 60)

# START_PROGRAM_BUTTON = Button(MAIN_UI, text = "시작", command = INTERNAL_FUNC.BTN2_CMD)
# START_PROGRAM_BUTTON.place(relx = 0.875, rely = 0.0, anchor = NE, width = 80, height = 60)


# QUESTION_2_1_BUTTON.grid(row = 2, column = 1)
#============================================PROGRESS_BAR============================================#

# QUESTION_PROGRESSBAR = TTK.Progressbar(MAIN_UI, maximum = 100, length = 500)
# QUESTION_PROGRESSBAR.pack()


#============================================PROGRESS_BAR============================================#

if 1 not in QUESTION_PROCESS_LIST:
    READ_CONFIG_DATA = READ_WRITE.READ_JSON(CONFIG_DIR)
    
    AREA_NAME_LIST = [KEY for KEY in READ_CONFIG_DATA["AREA_LIST"]]
    # SPECIFIC_AREA_NAME_LIST = []
    #=============================================(COMBO_BOX의 값이 기본값인지 확인하고 기본값이 아닌 값이 지정되었다면 다음 COMBO_BOX의 값을 추가)=============================================#
    
        
    
        
        # QUESTION_2_1_COMBO_BOX.update()
    #=============================================(COMBO_BOX의 값이 기본값인지 확인하고 기본값이 아닌 값이 지정되었다면 다음 COMBO_BOX의 값을 추가)=============================================#
    # QUESTION_ANSWER_LIST = {"QUESTION_1" : False, "QUESTION_2" : False, "QUESTION_2_1" : False}

    SELECT_TYPE_LIST = ["주택", "아파트"]
    SELECT_VALUE = [str(VALUE) for VALUE in SELECT_TYPE_LIST]
    #=============================================(1 : 거주유형 / 2 : 도,특별시 / 3 : 세부도시명) COMBO_BOX=============================================#
    QUESTION_1_COMBO_BOX = TTK.Combobox(MAIN_UI, height = 2, width = 50, values = SELECT_TYPE_LIST, state = "readonly")
    QUESTION_1_COMBO_BOX.set(PRIMARY_DISPLAY_TEXT)
    QUESTION_1_COMBO_BOX.grid(row = 0, column = 0)
    #QUESTION_1_COMBO_BOX.bind("<<ComboboxSelected>>", INTERNAL_FUNC.BTN1_CMD)

    QUESTION_2_COMBO_BOX = TTK.Combobox(MAIN_UI, width = 50, values = AREA_NAME_LIST, state = "readonly")
    QUESTION_2_COMBO_BOX.set(QUESTION_2_PRIMARY_DISPLAY_TEXT)
    QUESTION_2_COMBO_BOX.grid(row = 1, column = 0)
    QUESTION_2_COMBO_BOX.bind("<<ComboboxSelected>>", INTERNAL_FUNC.BTN2_CMD)

    # QUESTION_2_VALUE = QUESTION_2_COMBO_BOX.get()
    # SPECIFIC_AREA_NAME_LIST = [SPECIFIC_AREA_NAME for SPECIFIC_AREA_NAME in READ_CONFIG_DATA["AREA_LIST"][QUESTION_2_VALUE]]
    # SPECIFIC_AREA_NAME_LIST.append("이 항목을 선택하여 취소")
    # QUESTION_2_1_COMBO_BOX = TTK.Combobox(MAIN_UI, width = 50, values = SPECIFIC_AREA_NAME_LIST, state = "readonly")
    # QUESTION_2_1_COMBO_BOX.set(QUESTION_2_1_PRIMARY_DISPLAY_TEXT)

    #=============================================(1 : 거주유형 / 2 : 도,특별시 / 3 : 세부도시명) COMBO_BOX=============================================#
    
    
    
    #=============================================(각 번호의 답변을 적용시켜 UI를 새로고침)=============================================#
    # QUESTION_1_BUTTON = Button(MAIN_UI, text = "설정", command = QUESTION_1_COMBO_BOX.update)
    # QUESTION_1_BUTTON = Button(MAIN_UI, text = "설정")
    # QUESTION_1_BUTTON.grid(row = 0, column = 1)

    # # QUESTION_2_BUTTON = Button(MAIN_UI, text = "설정", command = QUESTION_2_COMBO_BOX.update)
    # QUESTION_2_BUTTON = Button(MAIN_UI, text = "설정")
    # QUESTION_2_BUTTON.grid(row = 1, column = 1)

    
    #=============================================(각 번호의 답변을 적용시켜 UI를 새로고침)=============================================#
    # for AREA_NAME in AREA_NAME_LIST:
    #     len(READ_CONFIG_DATA["AREA_LIST"][AREA_NAME])

    # QUESTION_1_COMBO_BOX = Listbox(MAIN_UI, height = 2)
    
    # for QUESTION_1_ANSWER_TYPE in SELECT_TYPE_LIST:
    #     QUESTION_1_COMBO_BOX.insert(END, QUESTION_1_ANSWER_TYPE)
    
    # QUESTION_1_COMBO_BOX.place(relx = 0.0, rely = 0.1, anchor = NW)

    
    
    
    #QUESTION_1_COMBO_BOX.set(PRIMARY_DISPLAY_TEXT)
    # QUESTION_1_BUTTON.place(relx = 0.0, rely = 0.15, anchor = NW)
    

    
# print(f"QUESTION_PROCESS_LIST = {QUESTION_PROCESS_LIST}")
# MAIN_UI.after(10, MAIN_UI.update)
MAIN_UI.mainloop()








