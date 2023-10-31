# type to terminal:scrapy crawl NTNU
import scrapy
import bs4
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import pyautogui
from time import sleep
import os

class NtnuSpider(scrapy.Spider):
    name = "NTNU"
    allowed_domains = ["university-tw.ldkrsi.men"]
    start_urls = ["https://university-tw.ldkrsi.men/register/"]

    def parse(self, response):
        SAVE_dir = 'logs'
        
        if not os.path.exists(SAVE_dir):    # if folder not exists, then create a folder
                os.makedirs(SAVE_dir)
        
        driver = webdriver.Chrome()     # selenium4.0以上不用輸入path to chromedriver
        driver.implicitly_wait(10)      # if the page doesn't loading completely whitin 10s, a time exception is thrown
        driver.get(r"https://university-tw.ldkrsi.men/register/")       # go to link
        
        wrapper = driver.find_element(By.CLASS_NAME, 'wrapper') # find class 'wrapper'
        a = wrapper.find_elements(By.TAG_NAME, 'a') # find tag 'a' under class 'wrapper'
        
        for i in range(0, 2):   # range=0~128
            a = wrapper.find_elements(By.TAG_NAME, 'a')     # find tag 'a' under class 'wrapper'

            school_name = a[i].text     # text of tag 'a'
            save_dir='{}/{}/'.format(SAVE_dir, school_name)   # using format function to fuse path
            if not os.path.exists(save_dir):
                os.makedirs(save_dir)
            s = a[i].get_attribute('href')  # value of tag 'a' which is a link
           
            pyautogui.hotkey('ctrl', 't', interval=0.1)     # automatic press keyboard keys to create a additional page
            driver.switch_to.window(driver.window_handles[1])       # switch control to new page
            driver.get(s)       

            soup = bs4.BeautifulSoup(driver.page_source, 'lxml')
            data = soup.select('table')[0]  # select table on page
            df = pd.read_html(data.prettify())[0]  #read html and transfer it to pandas frame
            file_name = '{}大學部一年級註冊率'.format(school_name)
            file = os.path.join(save_dir, file_name + '.csv')   # fuse path
            df.to_csv(file)     # save table in csv file

            data = soup.select('table')[1]
            df = pd.read_html(data.prettify())[0]
            file_name = '{}各科系一年級新生註冊率'.format(school_name)
            file = os.path.join(save_dir, file_name + '.csv')
            df.to_csv(file)
            
            pyautogui.hotkey('ctrl', 'w', interval=0.1)     # close page
            driver.switch_to.window(driver.window_handles[0])       # switch control to original page
    
        driver.quit()

        pass
