'''
Created on 08-May-2018

@author: Keshavd
'''

from Tests.Pageobject.LocatorRepo import Locators
from selenium.webdriver.common.by import By


class Home(object):
    
    def __init__(self, driver):
        self.driver = driver
        # defining values of homepage objects
        self.logo = driver.find_element(By.XPATH, Locators.logo)
        self.register = driver.find_element(By.XPATH, Locators.register)
        self.support = driver.find_element(By.XPATH, Locators.support)
        self.contact = driver.find_element(By.XPATH, Locators.contact)
        self.signon = driver.find_element(By.XPATH, Locators.signon)
    
    def getlogo(self):
        return self.logo
    
    def getregister(self):
        return self.register
    
    def getsupport(self):
        return self.support
    
    def getcontact(self):
        return self.contact
    
    def getsignon(self):
        return self.signon    

