from  zoom import ZoomMeeting

def Schedule():
    zoom_meeting = ZoomMeeting() 
    current_hour = zoom_meeting.get_time()
    today_day = zoom_meeting.get_date()
    #Password For Monday
    if today_day == "Monday": 
        #Hour English
        if current_hour == '10':
            token = '3r79767378'
            password = "dreamland"
            return token, password
            
        #Hour SST
        if current_hour == '11':
            token = '3r79767378'
            password = "dreamland" 
            return token, password

    #Password For Tuesday
    if today_day == "Tuesday": 
        #Hour English
        if current_hour == '10':
            token = '3r79767378'
            password = "dreamland"
            return token, password
            
        #Hour SST
        if current_hour == '11':
            token = '3r79767378'
            password = "dreamland" 
            return token, password

    #Password For Wednesday 
    if today_day == "Wednesday": 
        #Hindi
        if current_hour == '9':
            token = '3r79767378'
            password = "dreamland"
            return token, password

        #Maths
        if current_hour == '11':
            token = '3r79767378'
            password = "dreamland" 
            return token, password
        #SOPAN SIR LESSON
        if current_hour == '17':
            token = '3r79767378'
            password = "dreamland" 
            return token, password        

    #Password For Thursday
    if today_day == "Thursday": 
        #Hindi
        if current_hour == '9':
            token = '3r79767378'
            password = "dreamland"
            return token, password

        #Maths
        if current_hour == '11':
            token = '3r79767378'
            password = "dreamland" 
            return token, password
        #SOPAN SIR LESSON
        if current_hour == '17':
            token = '3r79767378'
            password = "dreamland" 
            return token, password



    #Password For Friday
    if today_day == "Friday": 
        if current_hour == '18':
            token = '7251288343'
            password = "12345678"
            return token, password

        if current_hour == '10':
            token = '3r79767378'
            password = "dreamland" 
            return token, password

