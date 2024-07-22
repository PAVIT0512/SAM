import RPi.GPIO as GPIO
import time

# Set the GPIO pin numbering mode to BOARD mode (physical pin numbers)
GPIO.setmode(GPIO.BOARD)

# Define the GPIO pins for TRIG and ECHO
TRIG_PIN = 16
ECHO_PIN = 18
caliberation_factor=1.06

# Set up the GPIO pins
GPIO.setup(TRIG_PIN, GPIO.OUT)
GPIO.setup(ECHO_PIN, GPIO.IN)

# Function to measure distance
def measure_distance():
    # Send a 10us pulse to trigger the sensor
    GPIO.output(TRIG_PIN, True)
    time.sleep(0.00001)
    GPIO.output(TRIG_PIN, False)

    # Initialize variables
    pulse_start = time.time()
    pulse_end = pulse_start

    # Wait for the ECHO pin to go high
    while GPIO.input(ECHO_PIN) == 0:
        pulse_start = time.time()

    
    # Wait for the ECHO pin to go low or timeout
    while GPIO.input(ECHO_PIN) == 1:
        pulse_end = time.time()
        
        if (pulse_end - pulse_start) > 0.1:  # Timeout after 0.1 seconds
            break

    # Calculate the pulse duration
    pulse_duration = pulse_end - pulse_start

    # Check for timeout
    if pulse_duration >= 0.1:
        return None  # Indicates a timeout

    # Calculate the distance in millimeters
    distance_mm = (pulse_duration * 34300 * 10) / 2 
    distance_mm=distance_mm+(20*caliberation_factor)
    return distance_mm

try:
    while True:
        # Measure distance and print it
        dist = measure_distance()
        if dist is not None:
            print(f"Distance: {dist:.2f} mm")
        else:
            print("Distance measurement timed out")
        time.sleep(1)

except KeyboardInterrupt:
    GPIO.cleanup()
