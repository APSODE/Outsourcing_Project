import subprocess
import sys
import time
class MODUAL_DOWNLOAD:
    def DOWNLOAD():
        def install(package):
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])

        PACKAGE_LIST = ["selenium", "datetime"]
        SUCCESS_LIST = []
        ERROR_LIST = []
        FIRST_TIME = time.perf_counter()
        for NAME in PACKAGE_LIST:
            try:
                install(NAME)
                SUCCESS_LIST.append(NAME)
            except:
                ERROR_LIST.append(NAME)

        SECOND_TIME = time.perf_counter()

        ERROR_LIST_COUNTER = len(ERROR_LIST)

        if ERROR_LIST_COUNTER == 0:
            print("설치가 정상적으로 실행되었습니다\n")    
            SUCCESS_LIST_COUNTER = len(SUCCESS_LIST)
            for COUNT in range(SUCCESS_LIST_COUNTER):
                NAME = SUCCESS_LIST[COUNT]
                print(f"{COUNT + 1}번 모듈 : {NAME}")
        else:
            print("설치가 정상적으로 실행되지 않았습니다\n")    
            print("====설치 성공 모듈 목록====\n")    
            SUCCESS_LIST_COUNTER = len(SUCCESS_LIST)
            for COUNT in range(SUCCESS_LIST_COUNTER):
                NAME = SUCCESS_LIST[COUNT]
                print(f"{COUNT + 1}번 모듈 : {NAME}")
            print("====설치 성공 모듈 목록====\n")    

            print("====설치 실패 모듈 목록====\n")
            for COUNT in range(ERROR_LIST_COUNTER):
                NAME = ERROR_LIST[COUNT]
                print(f"{COUNT + 1}번 모듈 : {NAME}")    
            print("====설치 실패 모듈 목록====\n")

        RUNNING_TIME = round((SECOND_TIME - FIRST_TIME), 0)
        print(f"소요시간 : {RUNNING_TIME}초")