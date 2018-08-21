#from picamera import PiCamera
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
PWM_PINr = 18
PWM_PINl = 12
GPIO.setup(PWM_PINr, GPIO.OUT)
GPIO.setup(PWM_PINl, GPIO.OUT)

pwmr = GPIO.PWM(PWM_PINr, 500)
pwml = GPIO.PWM(PWM_PINl, 500)

pwmr.start(0)
pwml.start(0)


PWM_PINrb = 17
PWM_PINlb = 6
GPIO.setup(PWM_PINrb, GPIO.OUT)
GPIO.setup(PWM_PINlb, GPIO.OUT)

pwmrb = GPIO.PWM(PWM_PINrb, 500)
pwmlb = GPIO.PWM(PWM_PINlb, 500)

pwmrb.start(0)
pwmlb.start(0)
#camera = PiCamera()
#camera.start_preview()
def init():
        pwmr.ChangeDutyCycle(0)
        pwml.ChangeDutyCycle(0)
        pwmrb.ChangeDutyCycle(0)
        pwmlb.ChangeDutyCycle(0)
#60
def go_60():
        init()
        pwmr.ChangeDutyCycle(90)
        pwml.ChangeDutyCycle(90)
#30
def go_30():
        init()
        pwmr.ChangeDutyCycle(80)
        pwml.ChangeDutyCycle(80)

def left():
        init()
        pwmr.ChangeDutyCycle(70)
        pwml.ChangeDutyCycle(30)

def right():
        init()
        pwmr.ChangeDutyCycle(30)
        pwml.ChangeDutyCycle(70)
def left1():
        init()
        pwmr.ChangeDutyCycle(100)
        pwmlb.ChangeDutyCycle(30)

def right1():
        init()
        pwmrb.ChangeDutyCycle(30)
        pwml.ChangeDutyCycle(100)

def stop():
        init()
        pwmr.ChangeDutyCycle(0)
        pwml.ChangeDutyCycle(0)
#traffic sign use (Peter

def SP_60():
        init()
        pwmr.ChangeDutyCycle(95)
        pwml.ChangeDutyCycle(95)

def SP_30():
        init()
        pwmr.ChangeDutyCycle(40)
        pwml.ChangeDutyCycle(40)

def SP_60R():
        init()
        pwmrb.ChangeDutyCycle(30)
        pwml.ChangeDutyCycle(100)
def SP_30R():
        init()
        pwmrb.ChangeDutyCycle(30)
        pwml.ChangeDutyCycle(50)
def SP_60L():
        init()
        pwmr.ChangeDutyCycle(100)
        pwmlb.ChangeDutyCycle(30)
def SP_30L():
        init()
        pwmr.ChangeDutyCycle(50)
        pwmlb.ChangeDutyCycle(30)
#traffic sign use (Peter
def foo():
        print('good')

# try:
    # while True:
        # key = input('in:')
        # if key == 'w':
            # init()
            # pwmr.ChangeDutyCycle(90)
            # pwml.ChangeDutyCycle(90)
            # print(key)

        # if key == 's':
            # init()
            # pwmrb.ChangeDutyCycle(90)
            # pwmlb.ChangeDutyCycle(90)
            # print(key)

        # if key == 'a':
            # init()
            # pwmr.ChangeDutyCycle(90)
            # pwml.ChangeDutyCycle(30)
            # print(key)

        # if key == 'd':
            # init()
            # pwmr.ChangeDutyCycle(30)
            # pwml.ChangeDutyCycle(90)
            # print(key)

        # if key == 'p':
            # init()
            # pwmr.ChangeDutyCycle(0)
            # pwml.ChangeDutyCycle(0)
            # print(key)
        # # if key == 'l':
            # # #camera.rotation = 180
            # # #camera.start_preview(alpha=200)
            # # camera.start_preview()
            # # time.sleep(3)
            # # camera.stop_preview()
        # if key =='k':
            # camera.stop_preview()


#except KeyboardInterrupt:
    #print ("Exception: KeyboardInterrupt")

#finally:
    #pwmr.stop()
    #pwml.stop()
    #pwmrb.stop()
    #pwmlb.stop()


    #GPIO.cleanup()

