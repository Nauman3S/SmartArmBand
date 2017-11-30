import time

from upm import pyupm_led

led=pyupm_led.Led(13)

print(led.name())

while True:
    led.on()
    time.sleep(1)
    led.off()
    time.sleep(1)