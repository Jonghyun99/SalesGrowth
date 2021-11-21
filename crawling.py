import requests
import time
import re
from bs4 import BeautifulSoup
from selenium import webdriver


url = 'https://kr.investing.com/equities/nvidia-corp-earnings'

#selenium start
chrome_driver_dir = "./chromedriver.exe"

options = webdriver.ChromeOptions()

#크롬창 숨기기
options.add_argument("headless")

driver = webdriver.Chrome(chrome_driver_dir,options=options)
driver.implicitly_wait(1)
driver.get(url)
driver.execute_script('showMoreEarningsHistory(6497)')

time.sleep(3)

text = driver.find_element_by_xpath('//*[@id="earningsHistory6497"]').text
# print('---------------------최근 1년간 매출 추이---------------------')
# print(text)
# print('--------------------------------------------------------------')
textLst = text.split('\n')


processingLst = textLst[1:len(textLst)]

revenueLst=[]
for param in processingLst:
    tempLst = param.split(' ')
    revenueLst.append(tempLst[8])
    

cnt = 0

# 정규표현식 규칙(숫자만 추출)
p = re.compile("\d*\.?\d+")

cnt = 0
for param in revenueLst:
    if param == '--':
        revenueLst[cnt] = 0
    revenueLst[cnt]=(p.findall(param))
    print(revenueLst[cnt])
    cnt = cnt + 1
    