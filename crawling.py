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

earnings = driver.find_element_by_xpath('//*[@id="earningsHistory6497"]').text

# print('---------------------최근 1년간 매출 추이---------------------')
# print(text)
# print('--------------------------------------------------------------')
textLst = earnings.split('\n')


processingLst = textLst[1:len(textLst)]

revenueLst=[]
for param in processingLst:
    tempLst = param.split(' ')
    revenueLst.append(tempLst[8])
    

cnt = 0

# 정규표현식 규칙(숫자만 추출)
p = re.compile("\d*\.?\d+")

cnt = 0
total = 0

print("test1: {0}".format(revenueLst))
valLst=[]
for param in revenueLst:
    
    if not param:
        revenueLst[cnt] = 0
    # revenueLst[cnt]=(p.finditer(param))
    valLst.extend(p.findall(param))
    # print(str)
    # revenueLst[cnt]=(str)(revenueLst[cnt]).replace("B","")
    cnt = cnt + 1

print(valLst)
valLst = map(float,valLst)
result = sum(valLst)
print(result)