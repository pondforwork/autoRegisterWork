import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pyautogui as pg

def clickonimage(path):
    print("Wait Page Load")
    time.sleep(1.5)
    try:
        img_location = pg.locateOnScreen(path, confidence=0.8)
        if img_location:
            print("Image found at:", img_location)
            pg.moveTo(img_location)
            pg.click()
        else:
            print("Image not found.")
    except Exception as e:
            print("An error occurred:", str(e))

def doubleclickonimage(path):
    print("Wait Page Load")
    time.sleep(1.5)
    try:
        img_location = pg.locateOnScreen(path, confidence=0.8)
        if img_location:
            print("Image found at:", img_location)
            pg.moveTo(img_location)
            pg.click()
            pg.doubleClick()
        else:
            print("Image not found.")
    except Exception as e:
            print("An error occurred:", str(e))


def clickChangePath(path):
    print("Wait Page Load")
    time.sleep(1.5)
    try:
        img_location = pg.locateOnScreen(path, confidence=0.8)
        if img_location:
            print("Image found at:", img_location)
            pg.moveTo(img_location)
            pg.move(50, 0)
            pg.click()
        else:
            print("Image not found.")
    except Exception as e:
            print("An error occurred:", str(e))

def typeWord(word):
     pg.typewrite(word)




def openAndLogin(username,password,employer):

   if(employer == "employer"): 
        radioemployer = driver.find_element(By.XPATH, "/html/body/div[1]/center/table/tbody/tr/td[3]/div/form/div[1]/table/tbody/tr[1]/td[2]/div/label[1]")
        radioemployer.click()
   else:
        radioemployer = driver.find_element(By.XPATH, "/html/body/div[1]/center/table/tbody/tr/td[3]/div/form/div[1]/table/tbody/tr[1]/td[2]/div/label[2]/input")
   
   employerUsername = driver.find_element(By.XPATH, "/html/body/div[1]/center/table/tbody/tr/td[3]/div/form/div[1]/table/tbody/tr[2]/td[2]/input")
   employerPassword = driver.find_element(By.XPATH, "/html/body/div[1]/center/table/tbody/tr/td[3]/div/form/div[1]/table/tbody/tr[3]/td[2]/input")


   loginbtn = driver.find_element(By.XPATH, "/html/body/div[1]/center/table/tbody/tr/td[3]/div/form/div[2]/a")
   employerUsername.send_keys(username)
   employerPassword.send_keys(password)
   loginbtn.click()

# start program 
myoptions = webdriver.ChromeOptions()
myoptions.add_experimental_option("detach",True)
myoptions.add_argument("--start-maximized")
driver = webdriver.Chrome(options = myoptions)
# Open a website
driver.get("https://e-workpermit.doe.go.th/")

# radioemployer = driver.find_element(By.XPATH, "/html/body/div[1]/center/table/tbody/tr/td[3]/div/form/div[1]/table/tbody/tr[1]/td[2]/div/label[1]")
# radioemployer.click()
# employerUsername = driver.find_element(By.XPATH, "/html/body/div[1]/center/table/tbody/tr/td[3]/div/form/div[1]/table/tbody/tr[2]/td[2]/input")
# employerPassword = driver.find_element(By.XPATH, "/html/body/div[1]/center/table/tbody/tr/td[3]/div/form/div[1]/table/tbody/tr[3]/td[2]/input")
# loginbtn = driver.find_element(By.XPATH, "/html/body/div[1]/center/table/tbody/tr/td[3]/div/form/div[2]/a")
# employerUsername.send_keys("1101401499748")
# employerPassword.send_keys("499748")
# loginbtn.click()

def redirectTo(redirectTo):
     if(redirectTo == "visa"):
          driver.get("https://e-workpermit.doe.go.th/CLMV-WEB/main.php?menu=reqhealthext")
     elif(redirectTo == "bt50"):
          print("bt50")

def inserteEmpId(employeeid):
     employeeId = driver.find_element(By.XPATH, "/html/body/form/div[2]/div[2]/div/div/div/div[2]/div/div/div/div[7]/div[2]/input")
     employeeId.send_keys(employeeid)
     searchBtn = driver.find_element(By.XPATH, "/html/body/form/div[2]/div[2]/div/div/div/div[2]/div/div/div/div[8]/div[2]/button")
     searchBtn.click()
     
    

openAndLogin("1101401499748","499748","employer")
redirectTo("visa")
inserteEmpId("12324234589")
