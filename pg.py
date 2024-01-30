import time
import pyautogui as pg

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

selectfolder(2)