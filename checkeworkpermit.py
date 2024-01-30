import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
myoptions = webdriver.ChromeOptions()
myoptions.add_experimental_option("detach",True)
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

bt50_O3 = driver.find_element(By.XPATH, "/html/body/form/div[2]/div[2]/div/div/div/div[2]/div/div/div/div[4]/div[2]/select/option[4]")
searchBtn = driver.find_element(By.XPATH, "/html/body/form/div[2]/div[2]/div/div/div/div[2]/div/div/div/div[7]/div[2]/a/button")

bt50_O3.click()
searchBtn.click()

