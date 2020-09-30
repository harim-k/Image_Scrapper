
from urllib.request import urlopen
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import os

search = "wifi password"
URL = "https://www.google.co.in/search?q=" + search + "&tbm=isch"

driver = webdriver.Chrome()
driver.get(URL)


time.sleep(3)

for i in range(2000):
	driver.execute_script('window.scrollBy(0,10000)')

time.sleep(3)


html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

results = soup.select(".isv-r")



if not os.path.exists(search):
    os.mkdir(search)

n = 1
for result in results:
	
	if result.select_one('.bRMDJf') == None or result.select_one('.bRMDJf').img == None or result.select_one('.bRMDJf').img.get('src') == None:
		continue

	imgUrl = result.select_one('.bRMDJf').img['src']

	with urlopen(imgUrl) as fr:
		with open(f'./{search}/{search}{str(n)}.jpg', 'wb') as fw:
			img = fr.read()
			fw.write(img)
	n += 1

print("succesfully downloaded")
driver.close()