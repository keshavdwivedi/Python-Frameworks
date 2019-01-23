'''
Created on 09-May-2018

@author: KeshavD
'''
from Base.TestSetup import Test
from Tests.Pageobject.Pages.Homepage import Home
from time import sleep
from Tests.TestUtils.Screenshotutility import Capturescreenshot


class Homescript(Test):
    
    ss_path = "D:\\Workspace\\FirstDemo\\Screenshots"
    
    def testhomepage(self):
        driver = self.driver
        driver.get("http://newtours.demoaut.com/")
        sleep(3)
        
        home = Home(driver)
        if home.getlogo().is_displayed():
            print("The homepage logo has been validated")
        
        expected_title = "Welcome: Mercury Tours"    
        
        try:
            if expected_title == driver.title:
                print("Title validated successfully")
                self.assertEqual(driver.title, expected_title)
        except Exception as e:
            print("Unable to validate title" + e)       
        
        ss = Capturescreenshot(driver)
        ss.CaptureSS("home.png")


'''   
if __name__ == "__main__":
    unittest.main() 
 ''' 
