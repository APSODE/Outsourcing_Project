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


#=================================================내부 함수 선언부================================================#
class INTERNAL_FUNC:
    def RISK_CALCULATION(CALC_DATA_LIST):
        """

        RT_DATA_LIST = [USER_LIVING_TYPE, CURRETN_TEMP, CURRETN_HUMIDITY, RESIDENTIAL_ENVIRONMENT, COOKING_UTENSILS, GAS_AUTOMATIC_LOCKING_VALVE]
        
        """
        
        USER_LIVING_TYPE = ["주택유형", CALC_DATA_LIST[0]]
        CURRETN_TEMP = ["현재온도", CALC_DATA_LIST[1]]
        CURRENT_HUMIDITY = ["현재습도", CALC_DATA_LIST[2]]
        RESIDENTIAL_ENVIRONMENT = ["주거환경", CALC_DATA_LIST[3][0], CALC_DATA_LIST[3][1]]
        COOKING_UTENSILS = ["조리도구", CALC_DATA_LIST[4]]
        GAS_AUTOMATIC_LOCKING_VALVE = ["가스벨브", CALC_DATA_LIST[5]]
        
        HOUSE_TYPE = ["주택", "아파트"]

        BASIC_RISK_POINT = 50
        
        # USER_LIVING_TYPE = {"주택유형", CALC_DATA_LIST[0]}
        # CURRETN_TEMP = {"현재온도", CALC_DATA_LIST[1]}
        # CURRENT_HUMIDITY = {"현재습도", CALC_DATA_LIST[2]}
        # RESIDENTIAL_ENVIRONMENT = {"주거환경", CALC_DATA_LIST[3][0], CALC_DATA_LIST[3][1]}
        # COOKING_UTENSILS = {"조리도구", CALC_DATA_LIST[4]}
        # GAS_AUTOMATIC_LOCKING_VALVE = {"가스벨브", CALC_DATA_LIST[5]}

        USE_CALC_DATA_LIST = {USER_LIVING_TYPE[0]: USER_LIVING_TYPE, CURRETN_TEMP[0]: CURRETN_TEMP, CURRENT_HUMIDITY[0]: CURRENT_HUMIDITY, RESIDENTIAL_ENVIRONMENT[0]: RESIDENTIAL_ENVIRONMENT, COOKING_UTENSILS[0]: COOKING_UTENSILS, GAS_AUTOMATIC_LOCKING_VALVE[0]: GAS_AUTOMATIC_LOCKING_VALVE}
        
        KEY_LIST = [KEY for KEY in USE_CALC_DATA_LIST]
        
        # print(f"KEY_LIST = {KEY_LIST}")
        for F_KEY_NAME in KEY_LIST:
            if F_KEY_NAME == USER_LIVING_TYPE[0]: #주택 유형
                if USER_LIVING_TYPE[1] == HOUSE_TYPE[0]:
                    USER_LIVING_HOUSE_TYPE = HOUSE_TYPE[0]
                else:
                    USER_LIVING_HOUSE_TYPE = HOUSE_TYPE[1]
            elif F_KEY_NAME == CURRETN_TEMP[0]: #현재 온도
                pass
            elif F_KEY_NAME == CURRENT_HUMIDITY[0]:
                pass
            elif F_KEY_NAME == RESIDENTIAL_ENVIRONMENT[0]:
                pass

                
            


        
        MSGBOX.showinfo("함수 호출 성공")
        #연산 진행방식

        
        
#=================================================내부 함수 선언부================================================#






#=================================================전역변수 선언부=================================================#
CONFIG_DIR = ".\\Class\\WEATHER_CHECK\\WEATHER_CHECK_CONFIG\\WEATHER_CHECK_CONFIG.json"
SELECTED_EVENT_BINDING = "<<ComboboxSelected>>"


QUESTION_1_PRIMARY_DISPLAY_TEXT = "주거유형 [주택 / 아파트]"
QUESTION_2_PRIMARY_DISPLAY_TEXT = "주거지역 [도 / 특별시]"
QUESTION_3_PRIMARY_DISPLAY_TEXT = "주거지역 [세부지역]"
QUESTION_4_PRIMARY_DISPLAY_TEXT_T1 = "흡연자 존재 유무"
QUESTION_4_PRIMARY_DISPLAY_TEXT_T2 = "아파트 준공 이후 7년 이상 경과 여부"
QUESTION_5_PRIMARY_DISPLAY_TEXT = "인덕션레인지 사용가구 여부"
QUESTION_6_PRIMARY_DISPLAY_TEXT = "가스 자동 잠금 벨브 설치 여부"


SELECT_CANCEL_TEXT = "===[이 항목을 선택해 취소]==="


READ_CONFIG_DATA = READ_WRITE.READ_JSON(CONFIG_DIR)
LIVING_TYPE = ["주택", "아파트", SELECT_CANCEL_TEXT]
AREA_NAME_LIST = [KEY for KEY in READ_CONFIG_DATA["AREA_LIST"]]
AREA_NAME_LIST.append(SELECT_CANCEL_TEXT)
YES_OR_NO_LIST = ["예", "아니오", SELECT_CANCEL_TEXT]
#=================================================전역변수 선언부=================================================#


#=================================================MAIN_UI 선언부=================================================#

MAIN_UI = Tk()
MAIN_UI.title("AI 화재 예방")
MAIN_UI.geometry("570x700")

#=================================================MAIN_UI 선언부=================================================#




#=================================================[Frame / Labelframe]선언부=================================================#
ZONE_F_FRAME = Frame(MAIN_UI)
ZONE_F_FRAME.pack()

ZONE_S_FRAME = Frame(MAIN_UI)
ZONE_S_FRAME.pack()

ZONE_T_FRAME = Frame(MAIN_UI)
ZONE_T_FRAME.pack()


BUTTON_PLACE_FRAME = LabelFrame(ZONE_F_FRAME, text = "시작 및 종료")
BUTTON_PLACE_FRAME.grid(row = 0, column = 1, padx = 10, pady = 10)

WEATHER_INFO_FRAME = LabelFrame(ZONE_F_FRAME, text = "현재 날씨 정보")
WEATHER_INFO_FRAME.grid(row = 0, column = 0, padx = 10, pady = 10)

QUESTION_PLACE_FRAME = LabelFrame(ZONE_S_FRAME, text = "주거유형 및 거주지역 선택")
QUESTION_PLACE_FRAME.grid(row = 0, column = 0)

SPECIFIC_QUESTION_PLACE_FRAME = Frame(QUESTION_PLACE_FRAME)
SPECIFIC_QUESTION_PLACE_FRAME.pack(anchor = CENTER)

QUESTION_PLACE_FRAME_S = LabelFrame(ZONE_S_FRAME, text = "주거 환경 조사")


SPECIFIC_QUESTION_PLACE_FRAME_S = Frame(QUESTION_PLACE_FRAME_S)
SPECIFIC_QUESTION_PLACE_FRAME_S.pack(anchor = CENTER)
#=================================================[Frame / Labelframe]선언부=================================================#


#=================================================COMBO_BOX 선언부=================================================#
class COMBO_BOX:

    #=================================================QUESTION_1_COMBO_BOX=================================================#
    def CREATE_QUESTION_BOX():
        QUESTION_1_LABEL_FRAME = LabelFrame(SPECIFIC_QUESTION_PLACE_FRAME, text = QUESTION_1_PRIMARY_DISPLAY_TEXT)
        QUESTION_1_LABEL_FRAME.grid(row = 0, column = 0, padx = 5, pady = 5)
        QUESTION_1_COMBO_BOX = TTK.Combobox(QUESTION_1_LABEL_FRAME, values = LIVING_TYPE, state = "readonly", height = 2, width = 60)
        QUESTION_1_COMBO_BOX.grid(row = 0, column = 0, padx = 10, pady = 10)
        QUESTION_1_COMBO_BOX.set(QUESTION_1_PRIMARY_DISPLAY_TEXT)
        #=================================================QUESTION_2_COMBO_BOX=================================================#
        def QUESTION_COMBO_BOX_2(EVENT):
            USER_LIVING_TYPE = QUESTION_1_COMBO_BOX.get()
            print(f"USER_LIVING_TYPE = {USER_LIVING_TYPE}")
            if USER_LIVING_TYPE != None and USER_LIVING_TYPE != QUESTION_1_PRIMARY_DISPLAY_TEXT and USER_LIVING_TYPE != SELECT_CANCEL_TEXT:
                QUESTION_2_LABEL_FRAME = LabelFrame(SPECIFIC_QUESTION_PLACE_FRAME, text = QUESTION_2_PRIMARY_DISPLAY_TEXT)
                QUESTION_2_LABEL_FRAME.grid(row = 1, column = 0, padx = 5, pady = 5)
                QUESTION_2_COMBO_BOX = TTK.Combobox(QUESTION_2_LABEL_FRAME, values = AREA_NAME_LIST, state = "readonly", width = 60)
                QUESTION_2_COMBO_BOX.grid(row = 1, column = 0, padx = 10, pady = 10)
                QUESTION_2_COMBO_BOX.set(QUESTION_2_PRIMARY_DISPLAY_TEXT)

                #=================================================QUESTION_3_COMBO_BOX=================================================#
                def QUESTION_COMBO_BOX_3(EVENT):
                    USER_LIVING_AREA = QUESTION_2_COMBO_BOX.get()
                    print(f"USER_LIVING_AREA = {USER_LIVING_AREA}")
                    if USER_LIVING_AREA != None and USER_LIVING_AREA != QUESTION_2_PRIMARY_DISPLAY_TEXT and USER_LIVING_AREA != SELECT_CANCEL_TEXT:
                        QUESTION_3_LABEL_FRAME = LabelFrame(SPECIFIC_QUESTION_PLACE_FRAME, text = QUESTION_3_PRIMARY_DISPLAY_TEXT)
                        QUESTION_3_LABEL_FRAME.grid(row = 2, column = 0, padx = 5, pady = 5)
                        USER_LIVING_SPECIFIC_AREA_LIST = [SPECIFIC_AREA_NAME for SPECIFIC_AREA_NAME in READ_CONFIG_DATA["AREA_LIST"][USER_LIVING_AREA]]
                        USER_LIVING_SPECIFIC_AREA_LIST.append(SELECT_CANCEL_TEXT)
                        QUESTION_3_COMBO_BOX = TTK.Combobox(QUESTION_3_LABEL_FRAME, values = USER_LIVING_SPECIFIC_AREA_LIST, state = "readonly", width = 60)
                        QUESTION_3_COMBO_BOX.grid(row = 2, column = 0, padx = 10, pady = 10)
                        QUESTION_3_COMBO_BOX.set(QUESTION_3_PRIMARY_DISPLAY_TEXT)
                        
                        def CREATE_START_BUTTON(EVENT):
                            USER_LIVING_SPECIFIC_AREA = QUESTION_3_COMBO_BOX.get()
                            print(f"USER_LIVING_SPECIFIC_AREA = {USER_LIVING_SPECIFIC_AREA}")
                            

                            if USER_LIVING_SPECIFIC_AREA != None and USER_LIVING_SPECIFIC_AREA != QUESTION_3_PRIMARY_DISPLAY_TEXT and USER_LIVING_SPECIFIC_AREA != SELECT_CANCEL_TEXT:  
                                def WEATHER_RETURN():
                                    if USER_LIVING_TYPE != None and USER_LIVING_AREA != None and USER_LIVING_SPECIFIC_AREA != None:
                                        INPUT_USER_LIVING_AREA_INFO = [USER_LIVING_AREA, USER_LIVING_SPECIFIC_AREA]

                                        MSGBOX.showinfo("확인버튼을 눌러주세요.", f"{USER_LIVING_TYPE}으로 진행합니다")
                                        RETURN_DATA_LIST = WEATHER.TODAY_WEATHER(AREA_INFO_LIST = INPUT_USER_LIVING_AREA_INFO)
                                        # QUESTION_PLACE_FRAME.destroy()

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

                                        WEATHER_INFO_1_FRAME = LabelFrame(WEATHER_INFO_FRAME, text = "현재 온도")
                                        WEATHER_INFO_1_FRAME.grid(row = 0, column = 0, padx = 5, pady = 5)
                                        WEATHER_INFO_1 = Text(WEATHER_INFO_1_FRAME, width = 10, height = 3)
                                        WEATHER_INFO_1.pack(anchor = CENTER, padx = 5, pady = 5)
                                        WEATHER_INFO_1.insert(END, f"\n{CURRENT_TEMP_VALUE}\n")
                                        WEATHER_INFO_1.config(state = DISABLED)


                                        WEATHER_INFO_2_FRAME = LabelFrame(WEATHER_INFO_FRAME, text = "평균 습도")
                                        WEATHER_INFO_2_FRAME.grid(row = 0, column = 1, padx = 5, pady = 5)
                                        WEATHER_INFO_2 = Text(WEATHER_INFO_2_FRAME, width = 10, height = 3)
                                        WEATHER_INFO_2.pack(anchor = CENTER, padx = 5, pady = 5)
                                        WEATHER_INFO_2.insert(END, f"\n{CURRENT_HUMIDITY_VALUE}\n")
                                        WEATHER_INFO_2.config(state = DISABLED)


                                        WEATHER_INFO_3_FRAME = LabelFrame(WEATHER_INFO_FRAME, text = "습도 판별")
                                        WEATHER_INFO_3_FRAME.grid(row = 0, column = 2, padx = 5, pady = 5)
                                        WEATHER_INFO_3 = Text(WEATHER_INFO_3_FRAME, width = 10, height = 3)
                                        WEATHER_INFO_3.pack(anchor = CENTER, padx = 5, pady = 5)
                                        WEATHER_INFO_3.insert(END, f"\n{CURRENT_HUMIDITY_TYPE}\n")
                                        WEATHER_INFO_3.config(state = DISABLED)
                                        
                                        #=================================================QUESTION_4_COMBO_BOX=================================================#
                                        QUESTION_PLACE_FRAME_S.grid(row = 1, column = 0)
                                        if USER_LIVING_TYPE == LIVING_TYPE[0]:
                                            QUESTION_TYPE = 1
                                            QUESTION_4_LABEL_FRAME = LabelFrame(SPECIFIC_QUESTION_PLACE_FRAME_S, text = QUESTION_4_PRIMARY_DISPLAY_TEXT_T1)
                                        elif USER_LIVING_TYPE == LIVING_TYPE[1]:
                                            QUESTION_TYPE = 2
                                            QUESTION_4_LABEL_FRAME = LabelFrame(SPECIFIC_QUESTION_PLACE_FRAME_S, text = QUESTION_4_PRIMARY_DISPLAY_TEXT_T2)

                                        QUESTION_4_LABEL_FRAME.grid(row = 0, column = 0, padx = 5, pady = 5)
                                        QUESTION_4_TEXT = ""
                                        QUESTION_4_COMBO_BOX = TTK.Combobox(QUESTION_4_LABEL_FRAME, values = YES_OR_NO_LIST, state = "readonly", height = 3, width = 60) 
                                        QUESTION_4_COMBO_BOX.grid(row = 0, column = 0, padx = 10, pady = 10)

                                        if USER_LIVING_TYPE == LIVING_TYPE[0]:
                                            QUESTION_4_COMBO_BOX.set(QUESTION_4_PRIMARY_DISPLAY_TEXT_T1)
                                            QUESTION_4_TEXT = QUESTION_4_PRIMARY_DISPLAY_TEXT_T1
                                        elif USER_LIVING_TYPE == LIVING_TYPE[1]:
                                            QUESTION_4_COMBO_BOX.set(QUESTION_4_PRIMARY_DISPLAY_TEXT_T2)
                                            QUESTION_4_TEXT = QUESTION_4_PRIMARY_DISPLAY_TEXT_T2
                                        
                                        def QUESTION_COMBO_BOX_5(EVENT):
                                            RESIDENTIAL_ENVIRONMENT = QUESTION_4_COMBO_BOX.get()

                                            if RESIDENTIAL_ENVIRONMENT != None and RESIDENTIAL_ENVIRONMENT != QUESTION_4_TEXT:
                                                #=================================================QUESTION_5_COMBO_BOX=================================================#
                                                QUESTION_5_LABEL_FRAME = LabelFrame(SPECIFIC_QUESTION_PLACE_FRAME_S, text = QUESTION_5_PRIMARY_DISPLAY_TEXT)
                                                QUESTION_5_LABEL_FRAME.grid(row = 1, column = 0, padx = 5, pady = 5)
                                                QUESTION_5_COMBO_BOX = TTK.Combobox(QUESTION_5_LABEL_FRAME, values = YES_OR_NO_LIST, state = "readonly", height = 3, width = 60)
                                                QUESTION_5_COMBO_BOX.grid(row = 1, column = 0, padx = 10, pady = 10)
                                                QUESTION_5_COMBO_BOX.set(QUESTION_5_PRIMARY_DISPLAY_TEXT)

                                                def QUESTION_COMBO_BOX_6(EVENT):
                                                    COOKING_UTENSILS = QUESTION_5_COMBO_BOX.get()
                                                    if COOKING_UTENSILS != None and COOKING_UTENSILS != QUESTION_5_PRIMARY_DISPLAY_TEXT:
                                                        #=================================================QUESTION_6_COMBO_BOX=================================================#
                                                        QUESTION_6_LABEL_FRAME = LabelFrame(SPECIFIC_QUESTION_PLACE_FRAME_S, text = QUESTION_6_PRIMARY_DISPLAY_TEXT)
                                                        QUESTION_6_LABEL_FRAME.grid(row = 2, column = 0, padx = 5, pady = 5)
                                                        QUESTION_6_COMBO_BOX = TTK.Combobox(QUESTION_6_LABEL_FRAME, values = YES_OR_NO_LIST, state = "readonly", height = 3, width = 60)
                                                        QUESTION_6_COMBO_BOX.grid(row = 2, column = 0, padx = 10, pady = 10)
                                                        QUESTION_6_COMBO_BOX.set(QUESTION_6_PRIMARY_DISPLAY_TEXT)
                                                        
                                                        def CALL_INTERNAL_FUNC(RT_DATA_LIST):
                                                            INTERNAL_FUNC.RISK_CALCULATION(CALC_DATA_LIST = RT_DATA_LIST)

                                                        def QUESTION_FINAL_CHECK(EVENT):    
                                                            GAS_AUTOMATIC_LOCKING_VALVE = QUESTION_6_COMBO_BOX.get()
                                                            
                                                            
                                                            if GAS_AUTOMATIC_LOCKING_VALVE != None and GAS_AUTOMATIC_LOCKING_VALVE != QUESTION_6_PRIMARY_DISPLAY_TEXT:
                                                                ANSWER_VERIFICATION = ["예", "아니요"]
                                                                ANSWER_QUESTION_4_VERIFICATION = None
                                                                ANSWER_QUESTION_5_VERIFICATION = None
                                                                ANSWER_QUESTION_6_VERIFICATION = None
                                                                if RESIDENTIAL_ENVIRONMENT in ANSWER_VERIFICATION:
                                                                    ANSWER_QUESTION_4_VERIFICATION = True
                                                                if COOKING_UTENSILS in ANSWER_VERIFICATION:
                                                                    ANSWER_QUESTION_5_VERIFICATION = True
                                                                if GAS_AUTOMATIC_LOCKING_VALVE in ANSWER_VERIFICATION:
                                                                    ANSWER_QUESTION_6_VERIFICATION = True
                                                                if ANSWER_QUESTION_4_VERIFICATION == True and ANSWER_QUESTION_5_VERIFICATION == True and ANSWER_QUESTION_6_VERIFICATION == True:
                                                                    ANSWER_LIST = [USER_LIVING_TYPE, CURRETN_TEMP, CURRETN_HUMIDITY, [RESIDENTIAL_ENVIRONMENT, QUESTION_TYPE], COOKING_UTENSILS, GAS_AUTOMATIC_LOCKING_VALVE]
                                                                    CALL_INTERNAL_FUNC(RT_DATA_LIST = ANSWER_LIST)
                                                            elif GAS_AUTOMATIC_LOCKING_VALVE == SELECT_CANCEL_TEXT:
                                                                QUESTION_6_COMBO_BOX.set(QUESTION_6_PRIMARY_DISPLAY_TEXT) 
                                                                QUESTION_6_COMBO_BOX.update()

                                                        QUESTION_6_COMBO_BOX.bind(SELECTED_EVENT_BINDING, QUESTION_FINAL_CHECK)
                                                        #=================================================QUESTION_6_COMBO_BOX=================================================#
                                                    elif COOKING_UTENSILS == SELECT_CANCEL_TEXT:
                                                        QUESTION_5_COMBO_BOX.set(QUESTION_5_PRIMARY_DISPLAY_TEXT)
                                                        QUESTION_5_COMBO_BOX.update()

                                                QUESTION_5_COMBO_BOX.bind(SELECTED_EVENT_BINDING, QUESTION_COMBO_BOX_6)
                                                #=================================================QUESTION_5_COMBO_BOX=================================================#
                                            elif RESIDENTIAL_ENVIRONMENT == SELECT_CANCEL_TEXT:
                                                QUESTION_4_COMBO_BOX.set(QUESTION_4_TEXT)
                                                QUESTION_4_COMBO_BOX.update()
                                            


                                        QUESTION_4_COMBO_BOX.bind(SELECTED_EVENT_BINDING, QUESTION_COMBO_BOX_5)
                                        #=================================================QUESTION_4_COMBO_BOX=================================================#

                                START_PROGRAM_BUTTON = Button(BUTTON_PLACE_FRAME, text = "시작", command = WEATHER_RETURN)
                                START_PROGRAM_BUTTON.grid(row = 0, column = 0, ipadx = 10, ipady = 8, padx = 10, pady = 10)  

                            elif USER_LIVING_SPECIFIC_AREA == SELECT_CANCEL_TEXT:
                                QUESTION_3_COMBO_BOX.destroy()
                               
                        QUESTION_3_COMBO_BOX.bind(SELECTED_EVENT_BINDING, CREATE_START_BUTTON)
                    elif USER_LIVING_AREA == SELECT_CANCEL_TEXT:
    
                        QUESTION_2_COMBO_BOX.set(QUESTION_2_PRIMARY_DISPLAY_TEXT)
                        QUESTION_2_COMBO_BOX.update()
                #=================================================QUESTION_3_COMBO_BOX=================================================#

                QUESTION_2_COMBO_BOX.bind(SELECTED_EVENT_BINDING, QUESTION_COMBO_BOX_3)

        #=================================================QUESTION_2_COMBO_BOX=================================================#
            elif USER_LIVING_TYPE == SELECT_CANCEL_TEXT:
                QUESTION_1_COMBO_BOX.set(QUESTION_1_PRIMARY_DISPLAY_TEXT)
                QUESTION_1_COMBO_BOX.update()

            
        QUESTION_1_COMBO_BOX.bind(SELECTED_EVENT_BINDING, QUESTION_COMBO_BOX_2)
    #=================================================QUESTION_1_COMBO_BOX=================================================#
        
#=================================================COMBO_BOX 선언부=================================================#


#=================================================COMBO_BOX 표기 구문=================================================#


COMBO_BOX.CREATE_QUESTION_BOX()


#=================================================COMBO_BOX 표기 구문=================================================#


#=================================================BUTTON 선언부=================================================#


EXIT_PROGRAM_BUTTON = Button(BUTTON_PLACE_FRAME, text = "종료", command = MAIN_UI.destroy)
EXIT_PROGRAM_BUTTON.grid(row = 0, column = 1, ipadx = 10, ipady = 8, padx = 10, pady = 10)


#=================================================BUTTON 선언부=================================================#







MAIN_UI.mainloop()
