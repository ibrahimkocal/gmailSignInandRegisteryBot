from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time

class Mail(): 
    def browser(self):
        self.browser = webdriver.Chrome()

    def signIn(self, email, password):
        self.email = email
        self.password = password
        self.browser.get("https://gmail.com")
        
        time.sleep(3)

        emailInput = self.browser.find_element(By.XPATH,"//*[@id='identifierId']").send_keys(self.email)
        
        time.sleep(2)
        self.browser.find_element(By.XPATH,"//*[@id='identifierNext']/div/button").send_keys(Keys.ENTER)

        time.sleep(2)
        passwordInput = self.browser.find_element(By.XPATH,"//*[@id='password']/div[1]/div/div[1]/input").send_keys(self.password)

        time.sleep(2)
        self.browser.find_element(By.XPATH,"//*[@id='passwordNext']/div/button").send_keys(Keys.ENTER)

    def Register(self, firstname, lastname, mail, password, passwordAgain):
        self.firstname = firstname
        self.lastname = lastname
        self.mail = mail
        self.password = password
        self.passwordAgain = passwordAgain
        self.browser.get("https://accounts.google.com/signup")
        time.sleep(2)

        firstnameInput = self.browser.find_element(By.XPATH,"//*[@id='firstName']").send_keys(self.firstname)
        lastnameInput = self.browser.find_element(By.XPATH,"//*[@id='lastName']").send_keys(self.lastname)  
        time.sleep(1)
        mailInput = self.browser.find_element(By.XPATH,"//*[@id='username']]").send_keys.get_attribulate()      
        time.sleep(2)
        passwordInput = self.browser.find_element(By.XPATH,"//*[@id='passwd']/div[1]/div/div[1]/input").send_keys(self.password)
        time.sleep(1)
        passwordaAgainInput = self.browser.find_element(By.XPATH,"//*[@id='confirm-passwd']/div[1]/div/div[1]/input").send_keys(self.passwordAgain)
        time.sleep(1)
        self.browser.find_element(By.XPATH,"//*[@id='accountDetailsNext']/div/button").send_keys(Keys.ENTER)

        time.sleep(2)

while True:
    print(" MENU ".center(50, "*"))
    print("© Created by ibrahimkocal ©".center(50))
    yourchoice = input("1- Sign In\n2- Registery\n3- Exit\nYour Choice: ")
    if yourchoice == "1":
        email = input("Your E-Mail: ")
        password = input("Your Password: ")
        mail = Mail()
        mail.browser() 
        mail.signIn(email, password)   
    elif yourchoice == "2":
        firstname = input("Your Name: ")
        lastname = input("Your Surname: ")
        mail = input("Your E-Mail: ").strip("@gmail.com").lower()
        password = input("Your Password: ")
        mail = Mail()
        mail.browser()
        mail.Register(firstname, lastname, mail, password, password)
    elif yourchoice == "3":
        quit()
    else:    
        print("ERROR! TRY AGAIN\n")    
