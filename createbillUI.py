import tkinter as tk
from tkinter import ttk
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pyautogui as pg

def clickonimage(path):
    print("Wait Page Load")
    time.sleep(1.5)
    try:
        img_location = pg.locateOnScreen(path, confidence=0.9)
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

def run_script():
    # Get values from the entry widgets
    username = username_entry.get()
    password = password_entry.get()

    # Your existing script here
    myoptions = webdriver.ChromeOptions()
    myoptions.add_experimental_option("detach", True)
    myoptions.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=myoptions)

    # Open a website
    driver.get("https://e-workpermit.doe.go.th/")

    radioemployer = driver.find_element(By.XPATH, "/html/body/div[1]/center/table/tbody/tr/td[3]/div/form/div[1]/table/tbody/tr[1]/td[2]/div/label[1]")
    radioemployer.click()

    employerUsername = driver.find_element(By.XPATH, "/html/body/div[1]/center/table/tbody/tr/td[3]/div/form/div[1]/table/tbody/tr[2]/td[2]/input")
    employerPassword = driver.find_element(By.XPATH, "/html/body/div[1]/center/table/tbody/tr/td[3]/div/form/div[1]/table/tbody/tr[3]/td[2]/input")
    loginbtn = driver.find_element(By.XPATH, "/html/body/div[1]/center/table/tbody/tr/td[3]/div/form/div[2]/a")

    employerUsername.send_keys(username)
    employerPassword.send_keys(password)
    loginbtn.click()

    # Redirect to document
    driver.get("https://e-workpermit.doe.go.th/CLMV-WEB/main.php?menu=paymentext&smenu=s1")

    # Uncomment the next line if needed
    # checkallBtn = driver.find_element(By.XPATH, "/html/body/form/div[2]/div[2]/div/div/div/div[2]/div/div/div/div[7]/div/div/table/thead/tr/th[1]/label")
    # checkallBtn.click()
    # time.sleep(0.5)
    #clickonimage(r'image\checkall.png')
    checkallBTN = driver.find_element(By.XPATH, "/html/body/form/div[2]/div[2]/div/div/div/div[2]/div/div/div/div[7]/div/div/table/thead/tr/th[1]/label/span")
    
    checkallBTN.click();

# Create main window
root = tk.Tk()
root.title("Script Automation UI")

# Create and place UI elements
frame = ttk.Frame(root, padding="10")
frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Username Label and Entry
ttk.Label(frame, text="Username:").grid(column=0, row=0, sticky=tk.W)
username_entry = ttk.Entry(frame, width=20)
username_entry.grid(column=1, row=0, sticky=(tk.W, tk.E))

# Password Label and Entry
ttk.Label(frame, text="Password:").grid(column=0, row=1, sticky=tk.W)
password_entry = ttk.Entry(frame, show="*", width=20)
password_entry.grid(column=1, row=1, sticky=(tk.W, tk.E))

# Run Button
run_button = ttk.Button(frame, text="Create Bill", command=run_script)
run_button.grid(column=0, row=2, columnspan=2, pady=10)

# Start GUI event loop
root.mainloop()
