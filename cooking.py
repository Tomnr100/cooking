import time
import random
import pyautogui
import keyboard

fishselection = input("What fish should we use?\n")
randsleep = random.normalvariate(0.8, 0.3)
time.sleep(2)
run = True

# Slower drag dur for items far away
dragdur1 = random.normalvariate(1, 0.2)

# Faster drag dur for items closer
dragdur2 = random.normalvariate(0.8, 0.2)

# Creating a list for random.choice later
draglist = [dragdur1, dragdur2]

def banking():
    print("Opening the bank...")
    bankdimensions = pyautogui.locateOnScreen('E:\\Desktop\\pycodes - kopie\\cooking\\bank.jpg', confidence=0.8)
    print(bankdimensions)
    bankx = random.uniform(bankdimensions[0]+(0.1*bankdimensions[2]), (bankdimensions[0]+(bankdimensions[2])*0.9))
    banky = random.uniform(bankdimensions[1]+(0.1*bankdimensions[3]), (bankdimensions[1]+(bankdimensions[3])*0.9))
    # dragdur1 = random.normalvariate(1, 0.2)
    print("Moving to " + str(bankx) + " " + str(banky))
    pyautogui.moveTo(bankx, banky, dragdur1)
    pyautogui.click()
    time.sleep(randsleep)


def depositall():
    print("Depositing items...")
    depositdimensions = pyautogui.locateOnScreen(
        'E:\\Desktop\\pycodes - kopie\\cooking\\depositall.jpg', confidence=0.8)
    print(depositdimensions)
    depositx = random.uniform(depositdimensions[0]+(0.1*depositdimensions[2]), depositdimensions[0]+(depositdimensions[2])*0.9)
    deposity = random.uniform(depositdimensions[1]+(0.1*depositdimensions[3]), depositdimensions[1]+(depositdimensions[3])*0.9)
    # dragdur1 = random.normalvariate(1, 0.2)
    pyautogui.moveTo(depositx, deposity, dragdur2)
    pyautogui.click()
    time.sleep(randsleep)


def withdrawfish():
    print("Withdrawing...")
    fishdimensions = pyautogui.locateOnScreen(
        f'E:\\Desktop\\pycodes - kopie\\cooking\\{fishselection}.jpg', confidence=0.9)
    fishx = random.uniform(
        fishdimensions[0]+(fishdimensions[2]*0.1), fishdimensions[0]+(fishdimensions[2])*0.9)
    fishy = random.uniform(
        fishdimensions[1]+(fishdimensions[3]*0.1), fishdimensions[1]+(fishdimensions[3])*0.9)
    # dragdur2 = random.normalvariate(1, 0.2)
    randomdrag = random.choice(draglist)
    pyautogui.moveTo(fishx, fishy, randomdrag)
    pyautogui.click()
    time.sleep(randsleep)
    pyautogui.hotkey('esc')


def startcook():
    # click on fish
    print('Clicking on the fish...')
    invfishdimensions = pyautogui.locateOnScreen(
        f'E:\\Desktop\\pycodes - kopie\\cooking\\inv{fishselection}.jpg', confidence=0.8)
    invfishx = random.uniform(
        invfishdimensions[0]+(invfishdimensions[2]*0.1), invfishdimensions[0]+(invfishdimensions[2])*0.9)
    invfishy = random.uniform(
        invfishdimensions[1]+(invfishdimensions[3]*0.1), invfishdimensions[1]+(invfishdimensions[3])*0.9)
    # dragdur1 = random.normalvariate(1, 0.2)
    pyautogui.moveTo(invfishx, invfishy, dragdur1)
    pyautogui.click()
    time.sleep(randsleep+0.5)

    # click on fire
    print('Clicking on the fire...')
    fireplace = pyautogui.locateOnScreen(
        'E:\\Desktop\\pycodes - kopie\\cooking\\fire.jpg', confidence = 0.8)
    firex = random.uniform(
        fireplace[0]+(0.1*fireplace[2]), fireplace[0]+(fireplace[2])*0.9)
    firey = random.uniform(
        fireplace[1]+(0.1*fireplace[3]), fireplace[1]+(fireplace[3])*0.9)
    # dragdur1 = random.normalvariate(1, 0.2)
    pyautogui.moveTo(firex, firey, dragdur2)
    pyautogui.click()
    time.sleep(randsleep)
    # confirm last object
    pyautogui.hotkey('space')
    # Waiting for inventory to complete
    print("Sleeping...")
    time.sleep(random.uniform(67, 70))

def startbot():
    try:
        banking()
        depositall()
        withdrawfish()
        startcook()
    except:
        pyautogui.hotkey('esc')
        return


while run:
    startbot()
    if keyboard.is_pressed('q'):
        run = False
