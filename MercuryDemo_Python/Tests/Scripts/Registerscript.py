'''
Created on 14-May-2018

@author: KeshavD
'''
from Base.TestSetup import Test
from Tests.Pageobject.Pages.Registerpage import Register
from time import sleep


class MyClass(Test):

    def testregister(self):
        driver = self.driver
        driver.get("http://newtours.demoaut.com/")
        r = Register(driver) 
        if r.getsignuplink().is_displayed():
            print("Register link displayed")
            sleep(8)
            r.getsignuplink().click()
            sleep(4)
        r.fillfirstname("Radha")
#         r.fillLastname("Shukla")
#         r.fillPhone(1234567890)
#         r.fillEmail("abc@gmail.com")  
#         r.fillAddress("alinagar")
#         r.fillCity("Mumbai")
#         r.fillstate("Maharashtra")
#         r.fillpincode(123456)
#         r.fillcountry("TURKEY")
#         r.fillsignondetails("Radha Shukla", "123456")
        
