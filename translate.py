from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
import time
import pyperclip
# https://answer-id.com/ko/52791220 셀레니움 창 위치 관련 링크
driver = None

def openURL(url):
    driver.get(url)

def click(address):
    category = driver.find_element_by_xpath(address)
    category.click()

def setEng2Kor():
    click('''//*[@id="ddSourceLanguage"]/div[1]/button[2]/span''')
    time.sleep(0.1)
    click('''//*[@id="ddSourceLanguage"]/div[2]/ul/li[3]''')
    #//*[@id="ddSourceLanguage"]/div[1]/button[2]/span //
    #//*[@id="ddSourceLanguage"]/div[2]/ul/li[3] #영어

def writeSource(sentence):
    s = driver.find_element_by_xpath('''//*[@id="txtSource"]''')
    s.click()
    pyperclip.copy(sentence) 
    s.send_keys(Keys.CONTROL, 'a') 
    s.send_keys(Keys.CONTROL, 'v') 
    time.sleep(2) 
    pass

def readTarget():
    return driver.find_element_by_xpath('''//*[@id="txtTarget"]''').text

def init_translate():
    # 옵션 생성
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    path = "C://Users//LeeJihyeon//Documents//python//PDF2TEXT//chromedriver.exe"  
    global driver
    
    driver = webdriver.Chrome(path, options=options)
    driver.set_window_position(0,-2000)
    
    openURL("https://papago.naver.com/")
    driver.implicitly_wait(10) 
    setEng2Kor()

def quit_translate_window():
    driver.quit()

if __name__ == "__main__":
    init_translate()

    writeSource("Introduction: Introduce yourself, explain the goals of the interview,reassure about the ethical issues, ask to record, and present the informed consent form.")

    result = readTarget()

    print(result)

    print("Finish")
    time.sleep(1)  
    driver.quit()