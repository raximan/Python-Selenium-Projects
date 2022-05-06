#"eksı sozluk" is the most famous publıc forum that is used in Turkey

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

web = webdriver.Firefox()

web.get("https://eksisozluk.com/ortadogu-insaninin-en-karakteristik-ozelligi--4782709") #navigating to the wanted topic
time.sleep(5)
entries = web.find_elements(By.CSS_SELECTOR, ".content") # taking all the entries
num = 1
ekşi_path = "C:\\Users\\izzet\\Desktop\\python codes\\selenium\\ekşi.txt"
for entry in entries:
    with open(ekşi_path,"a") as file:
        file.write(f"{num}*********\n{entry.text}\n") # appending all of the entries in one page
        num += 1
        print(entry.text)

numm = 2
url ="https://eksisozluk.com/ortadogu-insaninin-en-karakteristik-ozelligi--4782709?p="
while numm <50: # looping through the pages to append all entries
    web.get(url+str(numm)) # adding the number of the page to the end of the url will be sufficient to go to the next pages
    web.implicitly_wait(4)
    entries = web.find_elements(By.CSS_SELECTOR, ".content")
    num = 1
    ekşi_path = "C:\\Users\\izzet\\Desktop\\python codes\\selenium\\ekşi.txt"
    for entry in entries:
        with open(ekşi_path,"a") as file:
            file.write(f"{num}*********\n{entry.text}\n")
            num += 1
        print(entry.text)
    with open(ekşi_path,"a") as file:
        file.write(f"\n\n\n\n\n{numm+1}**\n\n")
    numm+=1
