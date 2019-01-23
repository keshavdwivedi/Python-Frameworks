'''
Created on 08-May-2018

@author: Keshavd
'''


class Locators(object):
    # Home page locators
    logo = "//img[@alt='Mercury Tours']"
    signon = "//a[contains(text(),'SIGN-ON')]"
    register = "//a[contains(text(),'REGISTER')]"
    support = "//a[contains(text(),'SUPPORT')]"
    contact = "//a[contains(text(),'CONTACT')]"
    
    # Signup page Locators
 
    signuplink = "//a[contains(text(),'REGISTER')]"
    firstname = "input[name='firstName']"
    lastname = "lastName"
    phoneno = "phone"
    email = "userName"
    address = "address1"
    cityname = "city"
    statename = "state"
    pincode = "postalCode"
    countrydrp = "country"
    Username = "email"
    password = "password"    
    cpassword = "confirmPassword"
    Submitbutton = "register"
