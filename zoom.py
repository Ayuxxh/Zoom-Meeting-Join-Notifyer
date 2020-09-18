import datetime
import sys
import pyautogui
import os, winsound

class ZoomMeeting:
    def __init__(self):
        pass

    def get_time (self):
        current_time = datetime.datetime.now().time()
        current_time = str(current_time)
        current_hour = current_time[0] + current_time[1]
        return current_hour

    def get_date(self):
        today_day = datetime.date.today().strftime("%A")
        return today_day

    def open_password(self):
        #credential imported from schedule.py directly because of circular import might try later to solve this problem for curcular import :(
        pass

    def open_zoom(self):
        zoom_url = "C:\\Users\\Aayush\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe"
        os.startfile(zoom_url)

    def join_meeting(self):
       #this part simulates clicking join meeting, entering meeting id and pressing enter to join
        ##Make sure the joinButton.png file is located in the same folder as the python file or else it will not work
        ##this tells the script where to click to join the meeting
        x = None
        while x == None:
            x = pyautogui.locateCenterOnScreen('join.png', confidence=0.9)
            print(x)
        pyautogui.click(x)


    def logging(self,token,password):
        #token
        pyautogui.press('enter',interval=1)
        ## the interval of 1 second is important, if not there, then the meeting id will not be inputted
        pyautogui.write(token)
        pyautogui.press('enter',interval=1)

        #password
        pyautogui.press('enter',interval=1)
        ## the interval of 1 second is important, if not there, then the meeting password will not be inputted
        pyautogui.write(password)
        pyautogui.press('enter',interval=1)

#See If we Are Connected 
    def notify_by_ring(self,token,password):
        x = None
        while x == None:
            x = pyautogui.locateCenterOnScreen('mic.png', confidence=0.9)
            print(x)
            #token
            pyautogui.press('enter',interval=1)
            ## the interval of 1 second is important, if not there, then the meeting id will not be inputted
            pyautogui.write(token)
            pyautogui.press('enter',interval=1)

            #password
            pyautogui.press('enter',interval=1)
            ## the interval of 1 second is important, if not there, then the meeting password will not be inputted
            pyautogui.write(password)
            pyautogui.press('enter',interval=1)
            if x != None:
                break
        winsound.PlaySound("music.wav",winsound.SND_ASYNC | winsound.SND_ALIAS |winsound.SND_LOOP )        

    def stop_ring_byUser(self):
        winsound.PlaySound(None, winsound.SND_ASYNC)