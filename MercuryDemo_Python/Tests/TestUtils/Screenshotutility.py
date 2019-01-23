class Capturescreenshot(object):
    
    def __init__(self, driver):
        self.driver = driver
    
    def CaptureSS(self, path):
        directory = "D:\\Workspace\\FirstDemo\\Screenshots\\" 
        self.driver.get_screenshot_as_file(directory + path)
          
