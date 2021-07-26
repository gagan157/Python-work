import pygame
import time
import datetime
import math
#Healthy program Reminder
#time duration 9am - 5pm
# water - water.mp3 (3.5liter) off to input drank - create log with time and date
# Eye -eye.mp3 Every 30 min play - of eydone - log
# physical activity - phicical.mp3 every 45min exdone-log
#1liter=1000ml
"""pending complete first"""
def play_music():
    file="retro-game-emergency-alarm.wav"
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
    while True:
        a=input()
        if a=='stop':
            pygame.mixer.music.stop()
            print("Thank you")
            break

def user_log(total_drank,glass):    
    with open("userreminder.txt","a") as f:        
        f.write(f"{time.asctime()}= your water intake left : {total_drank}ml you Drank {glass}ml and now ml\n")

def caldurationtime(s1,s2):    
    FMT='%I %p'
    tdelta= datetime.datetime.strptime(s2,FMT)-datetime.datetime.strptime(s1,FMT)    
    tdeltatystr=str(tdelta).split(":")[0]
    tdeltatyint=int(tdeltatystr)    
    return tdeltatyint

  

if __name__=="__main__":#calculate second   60sec 60min  1hour*60min*60sec = 1hour(sec3600)      40min*60sec = 40min(2400sec)
    def main():
        user_wktime=input("Enter the wakeup time AM or PM: ")
        user_sltime=input("Enter the sleep time AM or PM: ") 
        total_time=caldurationtime(user_wktime,user_sltime)       
        total_drank=3500
        glass=300        
        asume_user=60
        water_drank=time.time()
        eye_exe= time.time()
        pyc_exe=time.time()
        total_glass=round(total_drank/glass)
        gap_sec=asume_user/total_glass        
        water_sec=gap_sec
          
        # glass,left=user_water(total_drank)       
           
        eye_sec=5
        pyc_sec=20 
        i=1      
        while True:                
            int_water=time.time()
            int_eye=time.time()
            int_pyc=time.time()
            if i<=total_drank:
                if int_water-water_drank > water_sec: 
                    print("Drink water")                    
                    play_music()                    
                    user_log(total_drank,glass)
                    total_drank-=glass
                    water_drank=time.time()
            else:
                print("Finish your today water intake")        
                break
                 
            # if int_eye-eye_exe > eye_sec: 
            #     print("Eye Excercise")
            #     play_music()
            #     user_log("Done Eye Exerice")
            #     eye_exe=time.time()
            # if int_pyc-pyc_exe > pyc_sec: 
            #     print("Pysical Exersice")
            #     play_music()
            #     user_log("Done Pysical Exersice")
            #     pyc_exe=time.time()         
        
    
main()