from selenium import webdriver
from Class.USER_JSON_RW.rw_json import READ_WRITE
import time, datetime, sys, os, json

CONFIG_DIR = ".\\Class\\WEATHER_CHECK\\WEATHER_CHECK_CONFIG\\WEATHER_CHECK_CONFIG.json"

class INTERNAL_FUNC:
    def Del(Second):
        time.sleep(Second)
        return Second
    def Driver_Get_X_Path(XPath, WEBDRIVER):
        time.sleep(1)
        dgxp = WEBDRIVER.find_element_by_xpath(XPath)
        return dgxp
    def Driver_Get_Class(ClassName, WEBDRIVER):
        try:
            dgc = WEBDRIVER.find_element_by_class_name(ClassName)
            return dgc
        except:
            del_sec = 1.5
            time.sleep(del_sec + 5.5) #로딩이 느려 예외가 발생했을 경우 5초 delay를 주어 대기후 다시 코드 시작
            dgc = WEBDRIVER.find_element_by_class_name(ClassName)
            return dgc
    def Driver_Get_Tag(TAG_NAME, WEBDRIVER):
        dgt = WEBDRIVER.find_element_by_tag_name(TAG_NAME)

        return dgt
    def TAG_VALUE_LIST(TAG_NAME, WEBDRIVER):
        dgtl = WEBDRIVER.find_elements_by_tag_name(TAG_NAME)
        return dgtl
    
    def FIND_AREA_XPATH(AREA_NAME):
        
        READ_CONFIG_DATA = READ_WRITE.READ_JSON(CONFIG_DIR)
        BASIC_XPATH = READ_CONFIG_DATA["XPATH_LIST"]["BASIC_XPATH"]

        if AREA_NAME in "서울경기":
            AREA_STRING = "SEGG"
        elif AREA_NAME in "강원영서":
            AREA_STRING = "GWYW"
        elif AREA_NAME in "강원영동":
            AREA_STRING = "GWYE"
        elif AREA_NAME in "충청북도":
            AREA_STRING = "CCND"
        elif AREA_NAME in "충청남도":
            AREA_STRING = "CCSD"
        elif AREA_NAME in "전라북도":
            AREA_STRING = "GRND"
        elif AREA_NAME in "전라남도":
            AREA_STRING = "GRSD"
        elif AREA_NAME in "경상북도":
            AREA_STRING = "GSND"
        elif AREA_NAME in "경상남도":
            AREA_STRING = "GSSD"
        elif AREA_NAME in "제주도":
            AREA_STRING = "JJDO"
        elif AREA_NAME in "울릉독도":
            AREA_STRING = "ULDD"

        CURRENT_AREA_XPATH = BASIC_XPATH + READ_CONFIG_DATA["XPATH_LIST"]["XPATH_SPECIFIC_AREA_STRING"][AREA_STRING]["BASIC_STRING"]

        return CURRENT_AREA_XPATH

    def FIND_SPECIFIC_AREA_XPATH(AREA_INFO_LIST, WEBDRIVER):
        AREA_NAME = AREA_INFO_LIST[0]
        SPECIFIC_AREA_NAME = AREA_INFO_LIST[1]

        if AREA_NAME in "서울경기":
            AREA_NAME_NUM = 1
        elif AREA_NAME in "강원영서":
            AREA_NAME_NUM = 2
        elif AREA_NAME in "강원영동":
            AREA_NAME_NUM = 3
        elif AREA_NAME in "충청북도":
            AREA_NAME_NUM = 4
        elif AREA_NAME in "충청남도":
            AREA_NAME_NUM = 5
        elif AREA_NAME in "전라북도":
            AREA_NAME_NUM = 6
        elif AREA_NAME in "전라남도":
            AREA_NAME_NUM = 7
        elif AREA_NAME in "경상북도":
            AREA_NAME_NUM = 8
        elif AREA_NAME in "경상남도":
            AREA_NAME_NUM = 9
        elif AREA_NAME in "제주도":
            AREA_NAME_NUM = 10
        elif AREA_NAME in "울릉독도":
            AREA_NAME_NUM = 11

        SPECIFIC_AREA_NAME_ROW_LIST = ["1", "2", "3", "4"]
        SPECIFIC_AREA_NAME_COLUMN_LIST = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
        for ROW_NUM in SPECIFIC_AREA_NAME_ROW_LIST:
            for COLUMN_NUM in SPECIFIC_AREA_NAME_COLUMN_LIST:
                try:
                    SPECIFIC_AREA_NUM_XPATH = f"/html/body/table[2]/tbody/tr[3]/td[2]/table/tbody/tr[1]/td/div[@id='Tab{AREA_NAME_NUM}']/div[@id='myDiv']/table/tbody/tr[{ROW_NUM}]/td[{COLUMN_NUM}]/a"
                    CHECK_SPECIFIC_AREA_NAME = INTERNAL_FUNC.Driver_Get_X_Path(XPath = SPECIFIC_AREA_NUM_XPATH, WEBDRIVER = WEBDRIVER).text
                    
                    if SPECIFIC_AREA_NAME == CHECK_SPECIFIC_AREA_NAME:
                        return SPECIFIC_AREA_NUM_XPATH
                except:
                    pass

    def GET_AVERAGE_HUMIDITY(WEBDRIVER):
        HUMIDITY_LIST = []
        TOTAL_HUMIDITY = 0
        for COUNTER in range(2, 10):
            HUMIDITY_XPATH = f"/html/body/table[2]/tbody/tr[3]/td[2]/table/tbody/tr[3]/td/table/tbody/tr[3]/td/table[@id='t1']/tbody/tr[7]/td[{COUNTER}]"
            HUMIDITY_LIST.append(int(INTERNAL_FUNC.Driver_Get_X_Path(XPath = HUMIDITY_XPATH, WEBDRIVER = WEBDRIVER).text))
        LIST_LEN = len(HUMIDITY_LIST)
        for COUNTER in range(LIST_LEN):
            TOTAL_HUMIDITY += HUMIDITY_LIST[COUNTER]
        
        AVERAGE_HUMIDITY = round(TOTAL_HUMIDITY / LIST_LEN)

        return AVERAGE_HUMIDITY
  

class WEATHER:
    def TODAY_WEATHER(AREA_INFO_LIST):
        """
        RETURN
        --------
            type(CURRENT_VALUE) ==> list
            CURRENT_VALUE = [[CURRENT_HUMIDITY_CONDITION, CURRENT_HUMIDITY_VALUE, CURRENT_HUMIDITY], [CURRENT_TEMP_VALUE, CURRENT_TEMP]]

            CURRENT_VALUE[0] : HUMIDITY_DATA
            --------
                CURRENT_HUMIDITY_CONDITION = 1 ==> 건조한 기후\n
                CURRENT_HUMIDITY_CONDITION = 2 ==> 평범한 기후\n
                CURRENT_HUMIDITY_CONDITION = 3 ==> 습한 기후\n
                
                type(CURRENT_HUMIDITY_VALUE) ==> str\n
                Ex) CURRENT_HUMIDITY_VALUE ==> 90%\n

                typr(CURRENT_HUMIDITY) ==> int\n

            CURRENT_VALUE[1] : TEMP_DATA
            --------
                type(CURRENT_TEMP_VALUE) ==> str\n
                Ex) CURRENT_TEMP_VALUE ==> 25도\n

                type(CURRENT_TEMP) ==> int
        """
        INPUT_AREA_INFO_LIST = AREA_INFO_LIST
        INPUT_AREA_NAME = INPUT_AREA_INFO_LIST[0]
        # INPUT_SPECIFIC_AREA_NAME = INPUT_AREA_INFO_LIST[1]

        CURRENT_VALUE = []
        
        CH_DRIVER_DIR = ".\\chromedriver_win32\\chromedriver.exe"
        OPTION = webdriver.ChromeOptions()
        OPTION.add_argument("headless")
        DRIVER = webdriver.Chrome(CH_DRIVER_DIR, options = OPTION)
        # DRIVER = webdriver.Chrome(CH_DRIVER_DIR)
        
        
        #======================================================NAVER_WEATHER_INFO======================================================#
        # DRIVER.get("https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EC%8A%B5%EB%8F%84&oquery=%EC%98%A4%EB%8A%98%EC%9D%98%EB%82%A0%EC%94%A8&tqi=heG%2FSwprvmZssDpZu%2Fdssssstgh-058891")

        # CURRENT_HUMIDITY_XPATH = "/html/body[@class='wrap-new api_animation']/div[@id='wrap']/div[@id='container']/div[@id='content']/div[@id='main_pack']/section[@class='sc_new cs_weather _weather']/div[@class='api_subject_bx']/div[@class='api_cs_wrap']/div[@class='weather_box']/div[@class='weather_area _mainArea']/div[@class='today_area _mainTabContent']/div[@class='table_info bytime _todayWeatherByTime']/div[@class='info_list humidity _tabContent _center']/ul[@class='list_area']/li[@class='on now']/dl/dd[@class='weather_item _dotWrapper']/span[1]"
        # CURRENT_HUMIDITY = int(INTERNAL_FUNC.Driver_Get_X_Path(XPath = CURRENT_HUMIDITY_XPATH, DRIVER = DRIVER).text)
        # CURRENT_TEMP_XPATH = "/html/body[@class='wrap-new api_animation']/div[@id='wrap']/div[@id='container']/div[@id='content']/div[@id='main_pack']/section[@class='sc_new cs_weather _weather']/div[@class='api_subject_bx']/div[@class='api_cs_wrap']/div[@class='weather_box']/div[@class='weather_area _mainArea']/div[@class='today_area _mainTabContent']/div[@class='main_info']/div[@class='info_data']/p[@class='info_temperature']/span[@class='todaytemp']"
        # CURRENT_TEMP = int(INTERNAL_FUNC.Driver_Get_X_Path(XPath = CURRENT_TEMP_XPATH, DRIVER = DRIVER).text) 
        #======================================================NAVER_WEATHER_INFO======================================================#

        DRIVER.get("https://www.weatheri.co.kr/forecast/forecast01.php?mNum=1&sNum=1")
        INPUT_AREA_XPATH = INTERNAL_FUNC.FIND_AREA_XPATH(AREA_NAME = INPUT_AREA_NAME)
        INTERNAL_FUNC.Driver_Get_X_Path(XPath = INPUT_AREA_XPATH,  WEBDRIVER = DRIVER).click()
        INPUT_SPECIFIC_AREA_XPATH = INTERNAL_FUNC.FIND_SPECIFIC_AREA_XPATH(AREA_INFO_LIST = INPUT_AREA_INFO_LIST, WEBDRIVER = DRIVER)
        # PRINT_SPECIFIC_AREA_NAME = INTERNAL_FUNC.Driver_Get_X_Path(XPath = INPUT_SPECIFIC_AREA_XPATH, WEBDRIVER = DRIVER).text
        # print(PRINT_SPECIFIC_AREA_NAME)
        time.sleep(0.5)
        INTERNAL_FUNC.Driver_Get_X_Path(XPath = INPUT_SPECIFIC_AREA_XPATH, WEBDRIVER = DRIVER).click()
        CURRENT_TEMP = (str(INTERNAL_FUNC.Driver_Get_X_Path(XPath = READ_WRITE.READ_JSON(CONFIG_DIR)["XPATH_LIST"]["TD_TEMP_XPATH"], WEBDRIVER = DRIVER).text).split("℃")[0]).split(" ")[0]
        print(f"CURRENT_TEMP = {CURRENT_TEMP}")
        CURRENT_AVERAGE_HUMIDITY = int(INTERNAL_FUNC.GET_AVERAGE_HUMIDITY(WEBDRIVER = DRIVER))
        print(f"AVERAGE_HUMIDITY = {CURRENT_AVERAGE_HUMIDITY}")

        #CURRENT_HUMIDITY_CONDITION = 1 ==> 건조한 기후
        #CURRENT_HUMIDITY_CONDITION = 2 ==> 평범한 기후
        #CURRENT_HUMIDITY_CONDITION = 3 ==> 습한 기후


        if CURRENT_AVERAGE_HUMIDITY <= 70: #70%이하
            CURRENT_AVERAGE_HUMIDITY_CONDITION = 1
        elif CURRENT_AVERAGE_HUMIDITY > 70 and int(CURRENT_AVERAGE_HUMIDITY) <= 78: #70% 초과 / 78%이하
            CURRENT_AVERAGE_HUMIDITY_CONDITION = 2
        elif CURRENT_AVERAGE_HUMIDITY > 78: #78%초과
            CURRENT_AVERAGE_HUMIDITY_CONDITION = 3
            
        CURRENT_AVERAGE_HUMIDITY_VALUE = str(CURRENT_AVERAGE_HUMIDITY) + "%"
        CURRENT_TEMP_VALUE = str(CURRENT_TEMP) + "도"

        CURRENT_VALUE.append([CURRENT_AVERAGE_HUMIDITY_CONDITION, CURRENT_AVERAGE_HUMIDITY_VALUE, CURRENT_AVERAGE_HUMIDITY])
        CURRENT_VALUE.append([CURRENT_TEMP_VALUE, CURRENT_TEMP])
        print(CURRENT_VALUE)
        DRIVER.quit()
        return CURRENT_VALUE


        
