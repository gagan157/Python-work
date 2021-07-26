import time
import datetime
import pygame
#Set alram 
def cur_time():
    current_t=datetime.datetime.now()
    hours=int(current_t.strftime("%I"))  
    mins=int(current_t.strftime("%M"))
    secs=current_t.strftime("%S")
    a_pm=current_t.strftime("%p")        
    c_time=f"{hours}:{mins} {a_pm}"
    return c_time

def set_alarm(user_hours,user_mins,user_a_pm):
    current_t=datetime.datetime.now()
    hours=int(current_t.strftime("%I"))   
    mins=int(current_t.strftime("%M"))
    secs=current_t.strftime("%S")
    a_pm=current_t.strftime("%p")
    user_hours-=hours
    user_mins-=mins
    hours+=user_hours
    mins+=user_mins
    user_a_pm    
    cu_time=f"{hours}:{mins} {user_a_pm}"
    return cu_time

def remind_me(): 
    try:
        print("Set Alarm")
        alarm_msg=input("Enter your Alarm Msg: ")
        alarm_msg=alarm_msg.upper()
        user_ho=int(input("Enter the Hour : "))
        user_mi=int(input("Enter the minit : "))
        am_pm=str(input("Enter AM||PM : "))
        user_am_pm=am_pm.upper()
        #get one line time input
        # alltime=input("Enter Time format hour:min : ")
        # user_am_pm=input("Enter AM||PM: ")
        # user_am_pm=user_am_pm.upper()
        # user_ho,user_mi=[int(n) for n in alltime.split(":")]
        se_a=set_alarm(user_ho,user_mi,user_am_pm)
        set_alarms=se_a
        while True:   
        
            file="retro-game-emergency-alarm.wav"
            pygame.init()
            pygame.mixer.init()
            pygame.mixer.music.load(file)        
     
        
            current_time=cur_time() 
            # i=1      
            # if i<=10:
            if current_time==set_alarms:
                
                pygame.mixer.music.play()        
                print(f"\n{alarm_msg}")
                alarm_stop=input("Enter to 'S' stop alaram: ")  
                query=alarm_stop.upper()                          
                if query == 'P':
  
                        # Pausing the music
                    pygame.mixer.music.pause()     
                elif query == 'R':
  
                        # Resuming the music
                    pygame.mixer.music.unpause()
                elif query == 'S':
  
                        # Stop the mixer
                    pygame.mixer.music.stop()
                    break

    except Exception as e:
        print(e)

remind_me()                