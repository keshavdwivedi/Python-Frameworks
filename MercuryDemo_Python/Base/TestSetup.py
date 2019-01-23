'''
Created on 08-May-2018

@author: Keshavd
'''
import unittest
from selenium import webdriver
from datetime import datetime


class Test(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="C:\\Users\\HP\\PycharmProjects\\MercuryDemo\\drivers\\chromedriver.exe")
        self.driver.maximize_window()
        self.driver.set_page_load_timeout(20)
        print("Chrome Test environment has been created")
        print("The Test has started at", " " + str(datetime.now()))

    def tearDown(self):
        if(self.driver != None):
            print("Chrome Test environment has been destroyed")
            print("The test has been ended at", " " + str(datetime.now()))
            self.driver.close()
            self.driver.quit()
         
