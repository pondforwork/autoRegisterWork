import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pyautogui as pg
import keyboard

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


def SelectBT46():
    print("Wait Page Load")
    time.sleep(1.5)
    try:
        img_location = pg.locateOnScreen(fr'image\46.png', confidence=0.8)
        if img_location:
            print("Image found at:", img_location)
            pg.moveTo(img_location)
            pg.click()
            pg.doubleClick()
        else:
            print("Image not found.")
    except Exception as e:
            print("An error occurred:", str(e))

def SelectPassport():
    print("Wait Page Load")
    time.sleep(1.5)
    try:
        img_location = pg.locateOnScreen(fr'image\pass.png', confidence=0.8)
        if img_location:
            print("Image found at:", img_location)
            pg.moveTo(img_location)
            pg.click()
            pg.doubleClick()
        else:
            print("Image not found.")
    except Exception as e:
            print("An error occurred:", str(e))


def SelectHouseDocument():
    print("Wait Page Load")
    time.sleep(1.5)
    try:
        img_location = pg.locateOnScreen(fr'image\housedocument.png', confidence=0.8)
        if img_location:
            print("Image found at:", img_location)
            pg.moveTo(img_location)
            pg.click()
            pg.doubleClick()
        else:
            print("Image not found.")
    except Exception as e:
            print("An error occurred:", str(e))

def selectfolder(personNo):
    personNoString = str(personNo)
    print("Wait Page Load")
    time.sleep(1.5)
    try:
        img_location = pg.locateOnScreen(fr'image\person{personNoString}.png', confidence=0.97)
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
     
def moveMouseandpressEnd():
     pg.moveTo(109,270)
     pg.click()
     pg.press('end')


def clickuploadPassport(): 
     try:
          img_location = pg.locateOnScreen(r'image\insertpassportBtn.png', confidence=0.8) 
          if img_location:
               print("Image found at:", img_location)
               pg.moveTo(img_location)
               pg.move(600,0)
               pg.leftClick()
          else:
               print("Image not found.")
     except Exception as e:
      print("An error occurred:", str(e))
      


def clickuploadVisa(): 
     try:
          img_location = pg.locateOnScreen(r'image\insertvisaBtn.png', confidence=0.8) 
          if img_location:
               print("Image found at:", img_location)
               pg.moveTo(img_location)
               pg.move(600,0)
               pg.leftClick()
          else:
               print("Image not found.")
     except Exception as e:
      print("An error occurred:", str(e))


def clickuploadHouseDocument(): 
     try:
          img_location = pg.locateOnScreen(r'image\insertHousedocBtn.png', confidence=0.8) 
          if img_location:
               print("Image found at:", img_location)
               pg.moveTo(img_location)
               pg.move(600,0)
               pg.leftClick()
          else:
               print("Image not found.")
     except Exception as e:
      print("An error occurred:", str(e))


def clickuploadBT46(): 
    pg.moveTo(1215,757)
    pg.leftClick()


def typeWord(word):
     keyboard.write(word)

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
   


openAndLogin("3140900242144","242144","employer")
redirectTo("visa")
inserteEmpIdANDSelect("0023031078501")
insertAddressData()
insertPassportData(1,"T0776431","MIN PHNOM PENH","16/01/2023","16/01/2028")
insertVisaData("2994/67","12/1/2024","13/02/2025","CHACHOENGSAO IMMIGRATION OFFICE")
moveMouseandpressEnd()
time.sleep(0.3)

clickuploadPassport()
time.sleep(0.3)
clickonimage(r'image\documentsbtn.png')
clickChangePath(r'image\changepathbtn.png')
typeWord(r"C:\Users\Pond\Documents\งานต่างด้าว\ต่อวีซ่า\สุดาภรณ์")
pg.press('enter')
selectfolder(2)
pg.moveTo(979, 423)
SelectPassport()


time.sleep(0.3)
clickuploadVisa()
time.sleep(0.3)
clickonimage(r'image\documentsbtn.png')
clickChangePath(r'image\changepathbtn.png')
typeWord(r"C:\Users\Pond\Documents\งานต่างด้าว\ต่อวีซ่า\สุดาภรณ์")
pg.press('enter')
selectfolder(2)
pg.moveTo(979, 423)
SelectPassport()


time.sleep(0.3)
clickuploadHouseDocument()
time.sleep(0.3)
clickonimage(r'image\documentsbtn.png')
clickChangePath(r'image\changepathbtn.png')
typeWord(r"C:\Users\Pond\Documents\งานต่างด้าว\ต่อวีซ่า\สุดาภรณ์")
pg.press('enter')
pg.moveTo(979, 423)
SelectHouseDocument()


time.sleep(0.3)
clickuploadBT46()
time.sleep(0.3)
clickonimage(r'image\documentsbtn.png')
clickChangePath(r'image\changepathbtn.png')
typeWord(r"C:\Users\Pond\Documents\งานต่างด้าว\ต่อวีซ่า\สุดาภรณ์")
pg.press('enter')
pg.moveTo(979, 423)
selectfolder(2)
SelectBT46()

# time.sleep(0.3)
# clickuploadBT46()
# time.sleep(0.3)
# clickonimage(r'image\documentsbtn.png')
# clickChangePath(r'image\changepathbtn.png')
# typeWord(r"C:\Users\Pond\Documents\งานต่างด้าว\ต่อวีซ่า\สุดาภรณ์")
# pg.press('enter')
# selectfolder(1)
# pg.moveTo(979, 423)
# SelectBT46()


#SelectBT46()




