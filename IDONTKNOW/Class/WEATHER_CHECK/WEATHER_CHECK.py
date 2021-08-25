from selenium import webdriver
import time, datetime, sys, os, json


class INTERNAL_FUNC:
    def Del(Second):
        time.sleep(Second)
        return Second
    def Driver_Get_X_Path(XPath, DRIVER):
        time.sleep(1)
        driver = DRIVER
        dgxp = driver.find_element_by_xpath(XPath)
        return dgxp
    def Driver_Get_Class(ClassName, driver):
        try:
            dgc = driver.find_element_by_class_name(ClassName)
            return dgc
        except:
            del_sec = 1.5
            time.sleep(del_sec + 5.5) #로딩이 느려 예외가 발생했을 경우 5초 delay를 주어 대기후 다시 코드 시작
            dgc = driver.find_element_by_class_name(ClassName)
            return dgc
    def Driver_Get_Tag(TAG_NAME, WEBDRIVER):
        dgt = WEBDRIVER.find_element_by_tag_name(TAG_NAME)

        return dgt
    def TAG_VALUE_LIST(TAG_NAME, WEBDRIVER):
        dgtl = WEBDRIVER.find_elements_by_tag_name(TAG_NAME)
        return dgtl

class WEATHER:
    def TODAY_WEATHER():
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
        CURRENT_VALUE = []
        
        CH_DRIVER_DIR = ".\\chromedriver_win32\\chromedriver.exe"
        OPTION = webdriver.ChromeOptions()
        OPTION.add_argument("headless")
        DRIVER = webdriver.Chrome(CH_DRIVER_DIR, options = OPTION)
        #DRIVER = webdriver.Chrome(CH_DRIVER_DIR)
        DRIVER.get("https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EC%8A%B5%EB%8F%84&oquery=%EC%98%A4%EB%8A%98%EC%9D%98%EB%82%A0%EC%94%A8&tqi=heG%2FSwprvmZssDpZu%2Fdssssstgh-058891")

        CURRENT_HUMIDITY_XPATH = "/html/body[@class='wrap-new api_animation']/div[@id='wrap']/div[@id='container']/div[@id='content']/div[@id='main_pack']/section[@class='sc_new cs_weather _weather']/div[@class='api_subject_bx']/div[@class='api_cs_wrap']/div[@class='weather_box']/div[@class='weather_area _mainArea']/div[@class='today_area _mainTabContent']/div[@class='table_info bytime _todayWeatherByTime']/div[@class='info_list humidity _tabContent _center']/ul[@class='list_area']/li[@class='on now']/dl/dd[@class='weather_item _dotWrapper']/span[1]"
        CURRENT_HUMIDITY = int(INTERNAL_FUNC.Driver_Get_X_Path(XPath = CURRENT_HUMIDITY_XPATH, DRIVER = DRIVER).text)
        CURRENT_TEMP_XPATH = "/html/body[@class='wrap-new api_animation']/div[@id='wrap']/div[@id='container']/div[@id='content']/div[@id='main_pack']/section[@class='sc_new cs_weather _weather']/div[@class='api_subject_bx']/div[@class='api_cs_wrap']/div[@class='weather_box']/div[@class='weather_area _mainArea']/div[@class='today_area _mainTabContent']/div[@class='main_info']/div[@class='info_data']/p[@class='info_temperature']/span[@class='todaytemp']"
        CURRENT_TEMP = int(INTERNAL_FUNC.Driver_Get_X_Path(XPath = CURRENT_TEMP_XPATH, DRIVER = DRIVER).text) 


        #CURRENT_HUMIDITY_CONDITION = 1 ==> 건조한 기후
        #CURRENT_HUMIDITY_CONDITION = 2 ==> 평범한 기후
        #CURRENT_HUMIDITY_CONDITION = 3 ==> 습한 기후
        if CURRENT_HUMIDITY <= 70: #70%이하
            CURRENT_HUMIDITY_CONDITION = 1
        elif CURRENT_HUMIDITY > 70 and int(CURRENT_HUMIDITY) <= 78: #70% 초과 / 78%이하
            CURRENT_HUMIDITY_CONDITION = 2
        elif CURRENT_HUMIDITY > 78: #78%초과
            CURRENT_HUMIDITY_CONDITION = 3
            
        CURRENT_HUMIDITY_VALUE = str(CURRENT_HUMIDITY) + "%"
        CURRENT_TEMP_VALUE = str(CURRENT_TEMP) + "도"

        CURRENT_VALUE.append([CURRENT_HUMIDITY_CONDITION, CURRENT_HUMIDITY_VALUE, CURRENT_HUMIDITY])
        CURRENT_VALUE.append([CURRENT_TEMP_VALUE, CURRENT_TEMP])
        print(CURRENT_VALUE)
        return CURRENT_VALUE


        