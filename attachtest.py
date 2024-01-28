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

myoptions = webdriver.ChromeOptions()
myoptions.add_experimental_option("detach",True)
myoptions.add_argument("--start-maximized")

driver = webdriver.Chrome(options = myoptions)


# Open a website
driver.get("https://e-workpermit.doe.go.th/")

radioemployer = driver.find_element(By.XPATH, "/html/body/div[1]/center/table/tbody/tr/td[3]/div/form/div[1]/table/tbody/tr[1]/td[2]/div/label[1]")
radioemployer.click()

employerUsername = driver.find_element(By.XPATH, "/html/body/div[1]/center/table/tbody/tr/td[3]/div/form/div[1]/table/tbody/tr[2]/td[2]/input")
employerPassword = driver.find_element(By.XPATH, "/html/body/div[1]/center/table/tbody/tr/td[3]/div/form/div[1]/table/tbody/tr[3]/td[2]/input")
loginbtn = driver.find_element(By.XPATH, "/html/body/div[1]/center/table/tbody/tr/td[3]/div/form/div[2]/a")

employerUsername.send_keys("1101401499748")
employerPassword.send_keys("499748")
loginbtn.click()

#redirect to document
driver.get("https://e-workpermit.doe.go.th/CLMV-WEB/main.php?menu=manageemp")

deleteEmployerdocbtn = driver.find_element(By.XPATH, "/html/body/form/div[2]/div[2]/div/div/div/div[2]/div/div/div/div[7]/div/div/table/tbody/tr/td[3]/table/tbody/tr/td/div/span[2]/div[2]")
deleteEmployerdocbtn.click()
time.sleep(2)
clickonimage(r'image\fileuploadbtn.png')
clickonimage(r'image\documentsbtn.png')


clickChangePath(r'image\changepathbtn.png')

typeWord(r'C:\Users\Pond\Documents\Python\eworkpermitSelenium\image')
pg.press('enter')

doubleclickonimage(r'image\employer.png')


time.sleep(1.5)
savebtn = driver.find_element(By.XPATH, "/html/body/form/div[2]/div[2]/div/div/div/div[2]/div/div/div/div[8]/div[3]/button")
savebtn.click()
print("saved")


