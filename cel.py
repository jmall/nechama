from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from tkinter import messagebox
import time

PATH = '/Applications/chromedriver'

driver = webdriver.Chrome(PATH)

def zap():
    driver.get('https://www.zap.co.il/')
    search = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//*[contains(@href, 'cat.aspx?cat=catall')]")))
    search[0].send_keys(Keys.RETURN)
    search1 = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//*[contains(@href, 'models.aspx?sog=c-mouse')]")))
    search1[0].send_keys(Keys.RETURN)
    search2 = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//*[contains(@href, 'models.aspx?sog=c-mouse&orderby=price')]")))
    search2[0].send_keys(Keys.RETURN)
    search3 = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'pricesTxt')))
    first_price = 0
    error = False
    for x in search3:
        # print(x.text)
        splitted = x.text.split(": ")
        if(len(splitted) == 1):
            splitted = x.text.split(" - ")
        splitted = splitted[1].split(" ")
        if (int(splitted[0]) < first_price):
            messagebox.showinfo(message="Error in sorting")
            error = True
            exit(-100)
        else:
            first_price = int(splitted[0])
        print(splitted[0])

    if (error == False):
        messagebox.showinfo(message="Sorting success")
    driver.close()


zap()
