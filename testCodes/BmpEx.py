import time, sys, signal, atexit
from upm import pyupm_bmpx8x as upmBmpx8x

def main():
    # Load Barometer module on i2c using default values
    sensor = upmBmpx8x.BMPX8X(6);

    ## Exit handlers ##

    # This function stops python from printing a stacktrace when you hit
    # control-C
    def SIGINTHandler(signum, frame):
        raise SystemExit

    # This function lets you run code on exit, including functions
    # from sensor
    def exitHandler():
        print("Exiting")
        sys.exit(0)

    # Register exit handlers
    atexit.register(exitHandler)
    signal.signal(signal.SIGINT, SIGINTHandler)

    # Print the pressure, altitude, sea level, and
    # temperature values every 0.1 seconds
    while(1):
        sensor.update()

        outputStr = ("Pressure: {0}"
        " Pa, Temperature: {1}"
        " C, Altitude: {2}"
        " m, Sea Level: {3} Pa".format(
        sensor.getPressure(),
        sensor.getTemperature(),
        sensor.getAltitude(),
        sensor.getSealevelPressure()))

        print(outputStr)
        time.sleep(.5)

if __name__ == '__main__':
    main()