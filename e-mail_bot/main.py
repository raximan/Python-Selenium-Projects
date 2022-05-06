
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time
from random_gen import gen_psw
from random_gen import mail_gen
from random_gen import birthday_gen
from random_gen import birthyear_gen
from random_gen import name_gen
from random_gen import surname_gen
from random_gen import full_name_gen
from random_gen import  full_mail_gen
PATH = "C:\Program Files\chromedriver.exe"

dic={}
driver = webdriver.Chrome(PATH)

phone_num="731297022"



for i in range(2):
    driver.get("https://accounts.google.com/signup/v2/webcreateaccount?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&flowName=GlifWebSignIn&flowEntry=SignUp")
    driver.implicitly_wait(5)
    number_bool = False
    while number_bool is not True :

        driver.refresh()

        driver.implicitly_wait(20)

        ad = driver.find_element(By.ID,"firstName")
        first_name=name_gen()
        ad.send_keys(first_name)

        Soyad = driver.find_element(By.ID,"lastName")
        last_name=surname_gen()
        Soyad.send_keys(last_name)

        ıd = driver.find_element(By.ID,"username")
        username=mail_gen(first_name,last_name)
        ıd.send_keys(username)

        psw =driver.find_element(By.NAME,"Passwd")
        password=gen_psw(9)
        psw.send_keys((password))

        con_psw=driver.find_element(By.NAME,"ConfirmPasswd")
        con_psw.send_keys(password)


        ılerı = driver.find_element(By.CLASS_NAME,"VfPpkd-vQzf8d")
        ılerı.click()
        driver.implicitly_wait(2)
        try:
            number = driver.find_element(By.ID, "phoneNumberId")
            number_bool=True
        except:
            number_bool = False
    number=driver.find_element(By.ID, "phoneNumberId")
    number.send_keys(phone_num)
    """try:
        element =WebDriverWait(driver,35).until(EC.presence_of_element_located((By.ID, "day")))
    finally:
        driver.quit()
        print("fail to load last page")"""
    time.sleep(20)
    tel= driver.find_element(By.ID,"phoneNumberId")
    tel.clear()
    gun = driver.find_element(By.ID,"day")
    day = birthday_gen()
    gun.send_keys(day)

    months = Select(driver.find_element(By.ID,"month"))
    months.select_by_visible_text("Temmuz")

    yıl=driver.find_element(By.ID,"year")
    year=birthyear_gen()
    yıl.send_keys(year)

    genders =Select(driver.find_element(By.ID,"gender"))
    genders.select_by_value("1")

    time.sleep(3)

    final_ılerı=driver.find_element(By.CLASS_NAME,"VfPpkd-vQzf8d")
    final_ılerı.click()

    time.sleep(3)

    list = [username, password]
    dict_val = f"{first_name} {last_name}"
    add_dict = {dict_val: list}
    dic.update(add_dict)


print(dic)
