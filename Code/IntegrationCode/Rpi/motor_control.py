import RPi.GPIO as GPIO
import time

# Define GPIO pins
dirPinMX = 3 
stepPinMX = 5  
dirPinMY = 8  
stepPinMY = 10  
dirPinMZ = 11 
stepPinMZ = 13  
dirPinMZ1 = 38 
stepPinMZ1 = 40  
dirPinMZ2 = 35 
stepPinMZ2 = 37 
relay_pin = 15

GPIO.setmode(GPIO.BOARD)
GPIO.setup(dirPinMX, GPIO.OUT)
GPIO.setup(stepPinMX, GPIO.OUT)
GPIO.setup(dirPinMY, GPIO.OUT)
GPIO.setup(stepPinMY, GPIO.OUT)
GPIO.setup(dirPinMZ, GPIO.OUT)
GPIO.setup(stepPinMZ, GPIO.OUT)
GPIO.setup(dirPinMZ1, GPIO.OUT)
GPIO.setup(stepPinMZ1, GPIO.OUT)
GPIO.setup(dirPinMZ2, GPIO.OUT)
GPIO.setup(stepPinMZ2, GPIO.OUT)
GPIO.setup(relay_pin, GPIO.OUT)


def move_stepper_motor_MX(distance_mm, direction):
    steps_to_move = int((distance_mm / 2) * 24.945)
    if direction > 0:
        GPIO.output(dirPinMX, GPIO.HIGH)
    else:
        GPIO.output(dirPinMX, GPIO.LOW)

    for _ in range(2 * steps_to_move):
        GPIO.output(stepPinMX, GPIO.HIGH)
        time.sleep(0.0005)  # Sleep for 500 microseconds
        GPIO.output(stepPinMX, GPIO.LOW)
        time.sleep(0.0005)  # Sleep for 500 microseconds

    GPIO.output(dirPinMX, GPIO.LOW)
    time.sleep(1)
    global motorXMoving
    motorXMoving = False

def move_stepper_motor_MY(distance_mm, direction):
    steps_to_move = int((distance_mm / 2) * 24.945)
    if direction > 0:
        GPIO.output(dirPinMY, GPIO.HIGH)
    else:
        GPIO.output(dirPinMY, GPIO.LOW)

    for _ in range(2 * steps_to_move):
        GPIO.output(stepPinMY, GPIO.HIGH)
        time.sleep(0.0005)  # Sleep for 500 microseconds
        GPIO.output(stepPinMY, GPIO.LOW)
        time.sleep(0.0005)  # Sleep for 500 microseconds

    GPIO.output(dirPinMY, GPIO.LOW)
    time.sleep(1)
    global motorYMoving
    motorYMoving = False

def move_stepper_motor_MZ(distance_mm, direction):
    steps_to_move = int((distance_mm / 2) * 24.945)
    if direction > 0:
        GPIO.output(dirPinMZ, GPIO.HIGH)
    else:
        GPIO.output(dirPinMZ, GPIO.LOW)

    for _ in range(2 * steps_to_move):
        GPIO.output(stepPinMZ, GPIO.HIGH)
        time.sleep(0.0001)  # Sleep for 500 microseconds
        GPIO.output(stepPinMZ, GPIO.LOW)
        time.sleep(0.000001)  # Sleep for 500 microseconds

    GPIO.output(dirPinMZ, GPIO.LOW)
    time.sleep(1)
    global motorXMoving
    motorXMoving = False

def move_stepper_motor_MZ1(distance_mm, direction):
    steps_to_move = int((distance_mm / 2) * 24.945)
    if direction > 0:
        GPIO.output(dirPinMZ1, GPIO.HIGH)
    else:
        GPIO.output(dirPinMZ1, GPIO.LOW)

    for _ in range(2 * steps_to_move):
        GPIO.output(stepPinMZ1, GPIO.HIGH)
        time.sleep(0.0001)  # Sleep for 500 microseconds
        GPIO.output(stepPinMZ1, GPIO.LOW)
        time.sleep(0.0001)  # Sleep for 500 microseconds

    GPIO.output(dirPinMZ1, GPIO.LOW)
    time.sleep(1)
    global motorXMoving
    motorXMoving = False

def move_stepper_motor_MZ2(distance_mm, direction):
    steps_to_move = int((distance_mm / 2) * 24.945)
    if direction > 0:
        GPIO.output(dirPinMZ2, GPIO.HIGH)
    else:
        GPIO.output(dirPinMZ2, GPIO.LOW)

    for _ in range(2 * steps_to_move):
        GPIO.output(stepPinMZ2, GPIO.HIGH)
        time.sleep(0.001)  # Sleep for 500 microseconds
        GPIO.output(stepPinMZ2, GPIO.LOW)
        time.sleep(0.001)  # Sleep for 500 microseconds

    GPIO.output(dirPinMZ2, GPIO.LOW)
    time.sleep(1)
    global motorXMoving
    motorXMoving = False



# move_stepper_motor_MX(10, -5)
# move_stepper_motor_MY(50, -5)
# move_stepper_motor_MZ(400, -5)                                
# move_stepper_motor_MZ1(200, -5)
# move_stepper_motor_MZ2(200, -5)
# GPIO.output(relay_pin, GPIO.LOW)
# GPIO.output(relay_pin, GPIO.HIGH)



