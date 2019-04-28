
import RPi.GPIO as GPIO
import time
import os
import random

GPIO.setmode(GPIO.BCM)

GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    input_state = GPIO.input(23)
    if input_state == False:
		os.system("sudo killall -s 9 omxplayer.bin")
		dir = "/home/pi/Documents/videoscreen/vidFolder1"
		video = random.choice(os.listdir(dir))
		path = os.path.join(dir, video)
		os.system("omxplayer -o alsa  "+"'"+path+"'")
		time.sleep(0.2)
			if input_state == False:
				os.system("sudo killall -s 9 omxplayer.bin")


    input_state = GPIO.input(17)
    elif input_state == False:
		os.system("sudo killall -s 9 omxplayer.bin")
		dir = "/home/pi/Documents/videoscreen/vidFolder2"
		video = random.choice(os.listdir(dir))
		path = os.path.join(dir, video)
		os.system("omxplayer -o alsa "+"'"+path+"'")
		time.sleep(0.2)
			if input_state == False:
				os.system("sudo killall -s 9 omxplayer.bin")

    input_state = GPIO.input(16)
    else input_state == False:
		os.system("sudo killall -s 9 omxplayer.bin")
		time.sleep(0.2)
	
	





"""

if input_state = GPIO.input(23):
    if input_state == False:
        dir = "/home/pi/Documents/vidFolder1"
        video = random.choice(os.listdir(dir))
        path = os.path.join(dir, video)
        os.system("omxplayer -o local "+"'"+path+"'")
        time.sleep(0.2)

elif input_state = GPIO.input(17):
    if input_state == False:
        dir = "/home/pi/Documents/vidFolder1"
        video = random.choice(os.listdir(dir))
        path = os.path.join(dir, video)
        os.system("omxplayer -o local "+"'"+path+"'")
        time.sleep(0.2)
"""

"""
import RPi.GPIO as GPIO
import time
import os

GPIO.setmode(GPIO.BCM)   # Declaramos que los pines seran llamados como numeros
GPIO.setwarnings(False)

GPIO.setup(23, GPIO.IN)  # GPIO  7 como entrada
GPIO.setup(17, GPIO.IN) # GPIO 17 como entrada
GPIO.setup(12, GPIO.IN) # GPIO 27 como entrada
GPIO.setup(22, GPIO.IN) # GPIO 22 como entrada

pathVideos = "/home/pi/VideoHD/Belen"                   # Directorio donde se encuentran los videos en HD

def reproducirVideos(nameVideo):
    command1 = "sudo killall -s 9 omxplayer.bin"
    os.system(command1)
    command2 = "omxplayer -p -o hdmi %s/%s.mp4 &" % (pathVideos,nameVideo)
    os.system(command2)
    
    

def programaPrincipal():
    

    while True:
        if (GPIO.input(4)):
            
            reproducirVideos("amanecer")
        elif (GPIO.input(17)):
            
            reproducirVideos("dia")
        elif (GPIO.input(27)):
            
            reproducirVideos("atardecer")
        elif (GPIO.input(22)):
           
            reproducirVideos("anochecer")
        else:
            pass
    
    GPIO.cleanup() #Limpiar los GPIO  


programaPrincipal()   
"""