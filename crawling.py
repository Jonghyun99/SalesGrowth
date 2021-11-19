import requests
from bs4 import BeautifulSoup
from selenium import webdriver
url = 'https://kr.investing.com/equities/nvidia-corp-earnings'

#selenium start
driver = webdriver.Chrome("")
driver.get(url)

headers = {'User-Agent': 'Mozilla/5.0'}

response = requests.get(url,headers=headers)

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    revenue_crawl = soup.select('#earningsHistory6497 > tbody > tr > td:nth-of-type(5)')
    for revenue in revenue_crawl:
        print("revenue: {0}".format(revenue.text))

else : 
    print("error: {0}".format(response.status_code))