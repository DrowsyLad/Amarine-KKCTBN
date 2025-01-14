import RPi.GPIO as GPIO
from time import sleep
from adafruit_servokit import (
    ServoKit,
)  # https://circuitpython.readthedocs.io/projects/servokit/en/latest/

class Controller:
    def __init__(
        self,
        thrusterPinConfig,
        mainThrusterPinConfig,
        allServoPinConfig,
        mainThrusterSpeed
    ) -> None:
        self.thrusterPinConfig = thrusterPinConfig
        self.mainThrusterPinConfig = mainThrusterPinConfig
        self.allServoPinConfig = allServoPinConfig
        self.mainThrusterSpeed = mainThrusterSpeed
        
    def staticThruster(self, percentage):
        percentage /= 100
        self.thrusterPinConfig[0].throttle = percentage * -1
        sleep(0.002)
        self.thrusterPinConfig[1].throttle = percentage 
        sleep(0.002)
        self.thrusterPinConfig[2].throttle = percentage 
        sleep(0.002)
        self.thrusterPinConfig[3].throttle = percentage * -1
        sleep(0.002)

    def mainThruster(self):        
        self.mainThrusterPinConfig.throttle = self.mainThrusterSpeed / 100
        sleep(0.002)

    def initMainThruster(self):        
        self.mainThrusterPinConfig.throttle = 0.0
        sleep(0.002)

    def forward(self):
        self.allServoPinConfig[0].set_pulse_width_range(500, 2500)
        sleep(0.002)
        self.allServoPinConfig[0].angle = 90
                
    def left(self):
        self.allServoPinConfig[0].set_pulse_width_range(500, 2500)
        sleep(0.002)
        self.allServoPinConfig[0].angle = 150
        
    def right(self):
        self.allServoPinConfig[0].set_pulse_width_range(500, 2500)
        sleep(0.002)
        self.allServoPinConfig[0].angle = 30

    def cleanup(self):
        GPIO.output(self.stepperPinConfig[3], GPIO.LOW)
        GPIO.output(self.stepperPinConfig[2], GPIO.LOW)
        GPIO.output(self.stepperPinConfig[1], GPIO.LOW)
        GPIO.output(self.stepperPinConfig[0], GPIO.LOW)

