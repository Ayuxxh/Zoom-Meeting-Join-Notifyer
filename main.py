
#Importing 
from zoom import ZoomMeeting
import sys , time, schedule
from signal import signal, SIGINT

#listen for ctrl + c to exit program 
def handler(signal_received, frame):
    # Handle any cleanup here
    print('Exit Detected, Thanks for using me')
    print('Exiting Gracefully...')
    exit(0)

#Logging Console With Caption 
print("""Zoom Notify v0.1 2020,
Running... /n Waiting For Meeting,
Press Ctrl + C to EXIT PROGRAM !""")

# #Assigning Class duh!
zoom_meeting = ZoomMeeting() 

#Running file
if __name__ == '__main__':
    # Tell Python to run the handler() function when SIGINT is recieved
    signal(SIGINT, handler)

while True:
    #Getting Time 
    current_hour = zoom_meeting.get_time()

    #Cheaking Time 
    if current_hour == '18':
        print("Listening when meeting starts")
        #Getting Date 
        today_day = zoom_meeting.get_date()  
        # Compareing Dates
        if today_day == 'Saturday' or today_day == 'Sunday':
            print("*"  * 50)
            print("Umm....")
            print("*Gulp*")
            print("Yikes! Theres No Class Today Because Today Is " + today_day + " I guess :)")
            print("*"  * 50)
            print("Exiting...")
            sys.exit()


        try:
            #collecting credentials
            token, password = schedule.Schedule()
        except:
            print("Join Metting Credential Not Found!")
            print("For Time: "+ current_hour)
            print("For Day: " + today_day)

        #opening zoom 
        zoom_meeting.open_zoom()


        #joining meeting 
        zoom_meeting.join_meeting()
        
        #time delay to factor for zoom app to load up, good buffer is like 15 sec but its case specific
        time.sleep(15)

        # entering into meeting 
        zoom_meeting.logging(token,password)

        time.sleep(15)

        zoom_meeting.notify_by_ring(token, password)
        alram =input("Press Enter or type 'q' To Stop Alram ")
        if  alram == '' or alram == 'q':
            zoom_meeting.stop_ring_byUser()
            print("Stopped Alram")
        
        over = input("If Class Is Over Press Enter! :")
        time.sleep(60)
    else:
        # Cheaking IF exceeded The Time Limit
        if current_hour == '1':
            print("*"  * 50)
            print("Looks Like There Aren't Any Class Today")
            print("*"  *  50)
            sys.exit()
        
        #Sleeping for 5 minutes
        time.sleep(300)


