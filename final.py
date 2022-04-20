import smtplib
import random
from selenium import webdriver
from time import sleep
import webdriver_manager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import stdiomask
from selenium.webdriver.common.keys import Keys
import time
 
sample_otp=[1,2,3,4]
random_otp=random.randint(1111,9999)

def new_user():
    #This function creates a new user profile and takes in all the credentials to the system
    email=input("enter your email id:")
    master_pass=stdiomask.getpass(prompt="Create a masterpassword")
    fb_email=input("Enter email associated with your facebook account:")
    fb_password=stdiomask.getpass(prompt="Enter the password associated with your facebook account:")
    insta_email=input("Enter email associated with instagram account:")
    insta_password=stdiomask.getpass(prompt="Enter password associated with instagram:")
    
    with open("facebook.txt","a") as f:
        f.write(fb_email +"\n"+ fb_password)
    with open("instagram.txt","a") as g:
        g.write(insta_email +"\n"+ insta_password)
    with open("masterpass_email.txt","a") as h:
        h.write(master_pass+"\n"+email)

    print("You have successfully entered your details, please select existing user for accesing the websites through automation")
    
def otp_email():
    #This function sends OTP to the user through email
     with open("masterpass_email.txt","r") as f:
         f.readline()
         mailto=f.readline()

     gmailaddress = "miniprojectnhce@gmail.com"
     gmailpassword = "dhyanadithya1234"
     msg = "The otp is "+ str(random_otp)
     mailServer = smtplib.SMTP('smtp.gmail.com' , 587)
     mailServer.ehlo()
     mailServer.starttls()
     mailServer.login(gmailaddress , gmailpassword)
     mailServer.sendmail(gmailaddress, mailto, msg)      
     mailServer.quit()


def facebook_login():
    #This function automates the process of logging into facebook
    with open("facebook.txt","r") as q:
        a=q.readline()
        b=q.readline() 
                   
    usr=a
    pwd=b
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://www.facebook.com/')
    print ("Opened facebook")
    sleep(1)
    username_box = driver.find_element_by_id('email')
    username_box.send_keys(usr)
    print ("Email Id entered")
    sleep(1)
    password_box = driver.find_element_by_id('pass')
    password_box.send_keys(pwd)
    print ("Password entered")
    login_box = driver.find_element_by_id('loginbutton')
    login_box.click()
    print ("Done")
    input('Press anything to quit')
    driver.quit()
    print("Finished")

def instagram_login():
    #This function automates the instagram login process

    with open("instagram.txt","r") as d:
        a=d.readline()
        b=d.readline()
    
    usr=a
    pwd=b
    browser  =  webdriver.Chrome(ChromeDriverManager().install())
    sleep(2)
    browser.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
    sleep(3)
    username = browser.find_element_by_name('username')
    username.send_keys(usr)
    password = browser.find_element_by_name('password')
    password.send_keys(pwd)
    submit = browser.find_element_by_tag_name('form')
    submit.submit()
    input("press anything to quit")
     
 
    browser.quit()


def otp_checking():
    #This function checks whether the OTP entered is right, and procedes to the automation process
    otp=int(input("please enter the otp sent to your registered email id: "))
    if otp == random_otp:
        t=input("Enter 1 to login into Facebook, 2 to login into Instagram: ")
        if t== "1":
            facebook_login()
            print("login done successfully please check your browser")
        elif t== "2":
            instagram_login()
            print("login done successfully please check your browser")
        else:
            print("Please enter a valid response")
    #after the otp is checked then the next func will ask option for logging into insta or fb and do the same
    else:
        print("The entered otp is wrong, please try again")


def existing_user():
    #This function verifies whether the user is an existing user or not
    with open("masterpass_email.txt","r") as f:
        mp=f.readline().rstrip()
         
    
    login_mp=stdiomask.getpass(prompt="Enter your masterpassword:")
    
    if mp ==login_mp:
        print("Entered masterpassword is correct, please check your email for the otp")
        otp_email()
        otp_checking()
    elif login_mp!=mp:
        print("you have entered wrong masterpassword, please retry from the begining")
    else:
        print("wrong")

#The program starts from here, and the respective functions are called based on the flow of the code
firstquestion=str(input("Are you a new user or an existing user?(enter new/old): "))
if firstquestion == "new":
    new_user()
else:
    existing_user()



