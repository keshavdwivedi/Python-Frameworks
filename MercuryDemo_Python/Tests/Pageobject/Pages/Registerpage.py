'''
Created on 14-May-2018

@author: KeshavD
'''

from selenium.webdriver.common.by import By
from Tests.Pageobject.LocatorRepo import Locators
from selenium.webdriver.support.select import Select


class Register(object):

    def __init__(self, driver):
        self.driver = driver
        self.signuplink = driver.find_element(By.XPATH, Locators.signuplink)
        self.firstname = driver.find_element(By.CSS_SELECTOR, Locators.firstname)
#         self.lastname = driver.find_element(By.NAME, Locators.lastname)
#         self.phone = driver.find_element(By.NAME, Locators.phoneno)
#         self.email = driver.find_element(By.NAME, Locators.email)
#         self.address = driver.find_element(By.NAME, Locators.address)
#         self.city = driver.find_element(By.NAME, Locators.cityname)
#         self.state = driver.find_element(By.NAME, Locators.statename)
#         self.pincode = driver.find_element(By.NAME, Locators.pincode)
#         self.country = driver.find_element(By.NAME, Locators.countrydrp)
#         self.username = driver.find_element(By.NAME, Locators.Username)
#         self.password = driver.find_element(By.NAME, Locators.password)
#         self.cpassword = driver.find_element(By.NAME, Locators.cpassword)
#         self.registerbutton = driver.find_element(By.NAME, Locators.Submitbutton)
        
    def getsignuplink(self):
        return self.signuplink
        
    def fillfirstname(self, fname): 
        self.firstname.clear()
        self.firstname.send_keys(fname)
        
    def fillLastname(self, lname):
        self.lastname.clear()
        self.lastname.send_keys(lname)
    
    def fillPhone(self, pno):
        self.phone.clear()
        self.phone.send_keys(pno) 
        
    def fillEmail(self, lname):
        self.lastname.clear()
        self.lastname.send_keys(lname) 
        
    def fillAddress(self, address):
        self.address.clear()
        self.address.send_keys(address)
        
    def fillCity(self, city):
        self.city.clear()
        self.city.send_keys(city) 
    
    def fillstate(self, state):
        self.state.clear()
        self.state.send_keys(state) 
        
    def fillpincode(self, pincode):
        self.pincode.clear()
        self.pincode.send_keys(pincode) 
        
    def fillcountry(self, countrytxt):
        s = Select(self.country)
        s.select_by_visible_text(countrytxt)
        
    def fillsignondetails(self, Username, Password):
        self.username.send_keys(Username)
        self.password.send_keys(Password)
        self.cpassword.send_keys(Password)
        self.registerbutton.click()            
        
