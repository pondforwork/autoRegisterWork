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

def inserteEmpIdANDSelect(employeeid):
     employeeId = driver.find_element(By.XPATH, "/html/body/form/div[2]/div[2]/div/div/div/div[2]/div/div/div/div[7]/div[2]/input")
     employeeId.send_keys(employeeid)
     searchBtn = driver.find_element(By.XPATH, "/html/body/form/div[2]/div[2]/div/div/div/div[2]/div/div/div/div[8]/div[2]/button")
     searchBtn.click()
     selectRadio = driver.find_element(By.XPATH, "/html/body/form/div[2]/div[2]/div/div/div/div[2]/div/div/div/div[10]/div/div/table/tbody/tr/td[1]/input")
     selectRadio.click()
     selectBTN = driver.find_element(By.XPATH, "/html/body/form/div[2]/div[2]/div/div/div/div[2]/div/div/div/div[12]/div[3]/button")
     selectBTN.click()

def insertAddressData():
     addressWithEmployerRadio = driver.find_element(By.XPATH, "/html/body/form/div[2]/div[2]/div/div/div/div[2]/div/div/div/div[17]/div[2]/div/label[1]")
     addressWithEmployerRadio.click()
     print("with Employer")

def insertPassportData(documentType,docId,docOutFrom,startDate,endDate):
     document = driver.find_element(By.XPATH, "/html/body/form/div[2]/div[2]/div/div/div/div[2]/div/div/div/div[25]/div[2]/div/label[3]")
     document.click()
     documentId = driver.find_element(By.XPATH, "/html/body/form/div[2]/div[2]/div/div/div/div[2]/div/div/div/div[26]/div[2]/input")
     documentId.send_keys(docId)
     documentOutFrom = driver.find_element(By.XPATH, "/html/body/form/div[2]/div[2]/div/div/div/div[2]/div/div/div/div[27]/div[2]/input")
     documentOutFrom.send_keys(docOutFrom)
     documentStartDate = driver.find_element(By.XPATH, "/html/body/form/div[2]/div[2]/div/div/div/div[2]/div/div/div/div[28]/div[2]/input")
     documentStartDate.send_keys(startDate)
     documentEndDate = driver.find_element(By.XPATH, "/html/body/form/div[2]/div[2]/div/div/div/div[2]/div/div/div/div[28]/div[5]/input")
     documentEndDate.send_keys(endDate)
     
     
def insertVisaData(visanum,visaOut,visaExpDate,visaoutfromwhere):
      visaNumber = driver.find_element(By.XPATH, "/html/body/form/div[2]/div[2]/div/div/div/div[2]/div/div/div/div[30]/div[5]/input")
      visaNumber.send_keys(visanum)
      visaOutDate = driver.find_element(By.XPATH, "/html/body/form/div[2]/div[2]/div/div/div/div[2]/div/div/div/div[31]/div[2]/input")
      visaOutDate.send_keys(visaOut)
      visaExpireDate = driver.find_element(By.XPATH, "/html/body/form/div[2]/div[2]/div/div/div/div[2]/div/div/div/div[31]/div[5]/input")
      visaExpireDate.send_keys(visaExpDate)
      visaOutFrom = driver.find_element(By.XPATH, "/html/body/form/div[2]/div[2]/div/div/div/div[2]/div/div/div/div[32]/div[2]/input")
      visaOutFrom.send_keys(visaoutfromwhere)
      stayUntil = driver.find_element(By.XPATH, "/html/body/form/div[2]/div[2]/div/div/div/div[2]/div/div/div/div[32]/div[5]/input")
      stayUntil.send_keys(visaExpDate)
     
      


openAndLogin("3140900242144","242144","employer")
redirectTo("visa")
inserteEmpIdANDSelect("0023031078501")
insertAddressData()
insertPassportData(1,"T0776432","MIN PHNOM PENH","16/01/2023","16/01/2028")
insertVisaData("2995/67","12/1/2024","13/02/2025","CHACHOENGSAO IMMIGRATION OFFICE")

