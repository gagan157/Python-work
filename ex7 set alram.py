import time
import datetime
import pygame
import math
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
           
            if current_time==set_alarms:
                
                pygame.mixer.music.play(-1)        
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


def playmusic():
    file="retro-game-emergency-alarm.wav"
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play(-1)
    obj=input("Enter S to stop alarm: ")
    if obj=="S":
        pygame.mixer.music.stop()
        


class Timer():    
    def timer():
        user_inp=input("Enter timmer EX: 00h 00m 00s: ")
        
        userdata=user_inp.split(" ")
        hour= int(userdata[0])
        mins= int(userdata[1])
        sec= int(userdata[2])
        usercopy = userdata.copy()
        
        currenttime=datetime.datetime.now()
        h=int(currenttime.strftime("%I"))
        m=int(currenttime.strftime("%M"))
        s=int(currenttime.strftime("%S"))
        hour+=h
        mins+=m
        sec+=s                 
        if sec>=60:
            sec-=60           
            mins+=1   

        if mins>=60:
            mins-=60
            hour+=1

        if hour>=12:
            hour-=12    
        usertim = f"{hour} {mins} {sec}"
        hr=int(usercopy[0])
        mn=int(usercopy[1])
        se=int(usercopy[2])
        #hours,minuits,seconds
        h=hr*3600
        m=mn*60
        s=se   
        seconds=h+m+s
        while True:
            current_t=datetime.datetime.now()
            hours=int(current_t.strftime("%I"))   
            minss=int(current_t.strftime("%M"))
            secs=int(current_t.strftime("%S"))
            tim = f"{hours} {minss} {secs}"           
            time.sleep(1)

            h=int(seconds/3600)
            m=int(seconds//60)
            if m > 60:
                 m = (m % 60)
                
            s=seconds%60
            timer = '{:02d}:{:02d}:{:02d}'.format(h, m, int(s))
            print(timer, end="\r")
            # time.sleep(1)
            seconds-=1

            if tim == usertim:
                playmusic()
                break   






class countdown():
    @staticmethod
    def timer(hr,mn,se):
        h=hr*3600
        m=mn*60
        s=se   
        seconds=h+m+s     
        while True:      
            # h=int(seconds/12)
            h=int(seconds/3600)
            m=int(seconds//60)
            if m > 60:
                 m = (m % 60)
            s=seconds%60
            timer = '{:02d}:{:02d}:{:02d}'.format(h, m, int(s))
            # min, sec = divmod(seconds, 60)
            # hour, min = divmod(min, 60)
            # timer="%d:%02d:%02d" % (hour, min, sec)
            print(timer, end="\r")
            time.sleep(1)
            seconds-=1
            
           



if __name__=="__main__":
    # remind_me()                
    Timer.timer()
    # t = input("Enter the time in seconds: ")
  
   
   
    # co = countdown()
    # co.timer(0,0,10)