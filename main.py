import time
from PIL import Image,ImageGrab
import pyautogui

def iscollide(data):

    if data[342,262]>160:
        for i in range(455,560):
            for j in range(230,265):
                if data[i,j]<160:
                    pyautogui.keyDown('up')
                    return True
    elif data[342,262]<160:
        for i in range(455, 560):
            for j in range(230, 265):
                if data[i, j] > 160:
                    pyautogui.keyDown('up')
                    return True

    return False



if __name__ == '__main__':
    print("Here we go")
    pyautogui.keyDown('up')
    time.sleep(2)
    while True:
        image=ImageGrab.grab().convert('L')
        data=image.load()
        iscollide(data)
    #
    # for i in range(455,576):
    #     for j in range(230,265):
    #         data[i,j]=0

    # image.show()


