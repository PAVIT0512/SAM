import RPi.GPIO as GPIO
import time
# Disable GPIO warnings
GPIO.setwarnings(False)


# Define GPIO pins for control lines
ALE_PIN = 35
OE_PIN = 37
SC_PIN = 31
EOC_PIN = 33

# Define GPIO pins for data bus
DB_PINS = [16, 18, 22, 24, 26, 32, 36, 38]

# Sharp IR sensor output connected to ADC
SENSOR_CHANNEL = 3  # Change this if your sensor is connected to a different channel

# Set GPIO mode to BCM
GPIO.setmode(GPIO.BOARD)

# Configure control pins as outputs
GPIO.setup([ALE_PIN, OE_PIN, SC_PIN], GPIO.OUT)

# Configure EOC pin as input
GPIO.setup(EOC_PIN, GPIO.IN)

# Configure data bus pins as inputs
GPIO.setup(DB_PINS, GPIO.IN)

# Function to read data from the ADC
def read_adc(channel):
    GPIO.output(ALE_PIN, GPIO.LOW)  # Set ALE to low
    GPIO.output(SC_PIN, GPIO.HIGH)  # Set SC to high (start conversion)
    while not GPIO.input(EOC_PIN):  # Wait for EOC to go high (end of conversion)
        pass
    result = 0
    for i in range(8):
        result |= (GPIO.input(DB_PINS[i]) << i)
    return result

# Function to convert ADC reading to distance
def adc_to_distance(adc_value):
    # Replace this with your specific conversion formula
    # Example formula for a GP2Y0A21YK0F sensor:
    voltage = adc_value * (5.0 / 255.0)  # Convert ADC value to voltage (assuming 5V reference)
    distance = 20 / (voltage - 0.25)  # Replace with the correct formula for your sensor
    return distance

try:
    while True:
        adc_value = read_adc(SENSOR_CHANNEL)
        distance = adc_to_distance(adc_value)
        print(f"ADC Value: {adc_value}, Distance: {distance} cm")
        time.sleep(3)

except KeyboardInterrupt:
    pass

finally:
    GPIO.cleanup()
