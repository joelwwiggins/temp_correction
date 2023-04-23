import time
import board
import busio
import adafruit_bme280

# Create an I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Initialize the BME280 sensor
bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c)

# Set the temperature oversampling mode
bme280.sea_level_pressure = 1013.25
bme280.mode = adafruit_bme280.MODE_NORMAL
bme280.standby_period = adafruit_bme280.STANDBY_TC_500
bme280.iir_filter = adafruit_bme280.IIR_SIZE_16
bme280.overscan_temperature = adafruit_bme280.OVERSCAN_X16
bme280.overscan_humidity = adafruit_bme280.OVERSCAN_X1
bme280.overscan_pressure = adafruit_bme280.OVERSCAN_X16

while True:
    print("Temperature: %0.1f C" % bme280.temperature)
    print("Humidity: %0.1f %%" % bme280.relative_humidity)
    print("Pressure: %0.1f hPa" % bme280.pressure)
    print()
    time.sleep(2)