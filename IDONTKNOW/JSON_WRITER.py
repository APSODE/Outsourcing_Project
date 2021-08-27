from Class.WEATHER_CHECK.WEATHER_CHECK import WEATHER, INTERNAL_FUNC
from Class.USER_JSON_RW.rw_json import READ_WRITE
from selenium import webdriver
import time, json



CONFIG_DIR = ".\\Class\\WEATHER_CHECK\\WEATHER_CHECK_CONFIG\\WEATHER_CHECK_CONFIG.json"
CH_DRIVER_DIR = ".\\chromedriver_win32\\chromedriver.exe"
OPTION = webdriver.ChromeOptions()
OPTION.add_argument("headless")
# DRIVER = webdriver.Chrome(CH_DRIVER_DIR, options = OPTION)
DRIVER = webdriver.Chrome(CH_DRIVER_DIR)


#======================================================NAVER_WEATHER_INFO======================================================#
# DRIVER.get("https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EC%8A%B5%EB%8F%84&oquery=%EC%98%A4%EB%8A%98%EC%9D%98%EB%82%A0%EC%94%A8&tqi=heG%2FSwprvmZssDpZu%2Fdssssstgh-058891")

# CURRENT_HUMIDITY_XPATH = "/html/body[@class='wrap-new api_animation']/div[@id='wrap']/div[@id='container']/div[@id='content']/div[@id='main_pack']/section[@class='sc_new cs_weather _weather']/div[@class='api_subject_bx']/div[@class='api_cs_wrap']/div[@class='weather_box']/div[@class='weather_area _mainArea']/div[@class='today_area _mainTabContent']/div[@class='table_info bytime _todayWeatherByTime']/div[@class='info_list humidity _tabContent _center']/ul[@class='list_area']/li[@class='on now']/dl/dd[@class='weather_item _dotWrapper']/span[1]"
# CURRENT_HUMIDITY = int(INTERNAL_FUNC.Driver_Get_X_Path(XPath = CURRENT_HUMIDITY_XPATH, DRIVER = DRIVER).text)
# CURRENT_TEMP_XPATH = "/html/body[@class='wrap-new api_animation']/div[@id='wrap']/div[@id='container']/div[@id='content']/div[@id='main_pack']/section[@class='sc_new cs_weather _weather']/div[@class='api_subject_bx']/div[@class='api_cs_wrap']/div[@class='weather_box']/div[@class='weather_area _mainArea']/div[@class='today_area _mainTabContent']/div[@class='main_info']/div[@class='info_data']/p[@class='info_temperature']/span[@class='todaytemp']"
# CURRENT_TEMP = int(INTERNAL_FUNC.Driver_Get_X_Path(XPath = CURRENT_TEMP_XPATH, DRIVER = DRIVER).text) 
#======================================================NAVER_WEATHER_INFO======================================================#

DRIVER.get("https://www.weatheri.co.kr/forecast/forecast01.php?mNum=1&sNum=1")

AREA_NAME_LIST = ["서울경기", "강원영서", "강원영동", "충청북도", "충청남도", "전라북도", "전라남도", "경상북도", "경상남도", "제주도", "울릉독도"]
READ_CONFIG_DATA = READ_WRITE.READ_JSON(CONFIG_DIR)
BASIC_XPATH = READ_CONFIG_DATA["XPATH_LIST"]["BASIC_XPATH"]

for AREA_NAME in AREA_NAME_LIST:
    if AREA_NAME in "서울경기":
        AREA_NAME_NUM = 1
        AREA_STRING = "SEGG"
    elif AREA_NAME in "강원영서":
        AREA_NAME_NUM = 2
        AREA_STRING = "GWYW"
    elif AREA_NAME in "강원영동":
        AREA_NAME_NUM = 3
        AREA_STRING = "GWYE"
    elif AREA_NAME in "충청북도":
        AREA_NAME_NUM = 4
        AREA_STRING = "CCND"
    elif AREA_NAME in "충청남도":
        AREA_NAME_NUM = 5
        AREA_STRING = "CCSD"
    elif AREA_NAME in "전라북도":
        AREA_NAME_NUM = 6
        AREA_STRING = "GRND"
    elif AREA_NAME in "전라남도":
        AREA_NAME_NUM = 7
        AREA_STRING = "GRSD"
    elif AREA_NAME in "경상북도":
        AREA_NAME_NUM = 8
        AREA_STRING = "GSND"
    elif AREA_NAME in "경상남도":
        AREA_NAME_NUM = 9
        AREA_STRING = "GSSD"
    elif AREA_NAME in "제주도":
        AREA_NAME_NUM = 10
        AREA_STRING = "JJDO"
    elif AREA_NAME in "울릉독도":
        AREA_NAME_NUM = 11
        AREA_STRING = "ULDD"
    SPECIFIC_AREA_NAME_LIST = []
    CURRENT_AREA_XPATH = BASIC_XPATH + READ_CONFIG_DATA["XPATH_LIST"]["XPATH_SPECIFIC_AREA_STRING"][AREA_STRING]["BASIC_STRING"]
    INTERNAL_FUNC.Driver_Get_X_Path(XPath = CURRENT_AREA_XPATH,  WEBDRIVER = DRIVER).click()
    print(f"AREA_NAME = {AREA_NAME}")
    SPECIFIC_AREA_NAME_ROW_LIST = ["1", "2", "3", "4"]
    SPECIFIC_AREA_NAME_COLUMN_LIST = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
    for ROW_NUM in SPECIFIC_AREA_NAME_ROW_LIST:
        for COLUMN_NUM in SPECIFIC_AREA_NAME_COLUMN_LIST:
            try:
                SPECIFIC_AREA_NUM_XPATH = f"/html/body/table[2]/tbody/tr[3]/td[2]/table/tbody/tr[1]/td/div[@id='Tab{AREA_NAME_NUM}']/div[@id='myDiv']/table/tbody/tr[{ROW_NUM}]/td[{COLUMN_NUM}]"
                CHECK_SPECIFIC_AREA_NAME = INTERNAL_FUNC.Driver_Get_X_Path(XPath = SPECIFIC_AREA_NUM_XPATH, WEBDRIVER = DRIVER).text
                print(f"    CHECK_SPECIFIC_AREA_NAME = {CHECK_SPECIFIC_AREA_NAME}")
                SPECIFIC_AREA_NAME_LIST.append(CHECK_SPECIFIC_AREA_NAME)
            except:
                pass
    with open(CONFIG_DIR, "w", encoding = "utf-8") as WRITE_CONFIG_PROFILE:
        READ_CONFIG_DATA["AREA_LIST"][f"{AREA_NAME}"] = SPECIFIC_AREA_NAME_LIST
        json.dump(READ_CONFIG_DATA, WRITE_CONFIG_PROFILE, indent = 4)

# print(type(round(0.5)))