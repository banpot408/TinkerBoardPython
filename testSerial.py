# sudo nano /boot/config.txt
# dmesg | grep tty
# https://python-periphery.readthedocs.io/en/latest/serial.html
# https://tinker-board.asus.com/images/doc/download/Getting_Started_202003.pdf


from periphery import GPIO
import time

from periphery import Serial
# Open /dev/ttyUSB0 with baudrate 115200, and defaults of 8N1, no flow control
# serial = Serial("/dev/ttyUSB0", 115200)

uart1 = Serial("/dev/ttyS0", 115200)

LED_Pin = 123 #Physical Pin-32 is GPIO 146

BUZ_PIN = 150
RY1_PIN = 123
RY2_PIN = 127

PWM_DIS_PIN = 125

LTE_WDIS_PIN = 71
LTE_RST_PIN = 126

CFCI_PIN = 121
CAR_PIN = 149
RFID_IRQ_PIN = 8

CFCI_GPIO = GPIO(CFCI_PIN, "in")
CAR_GPIO = GPIO(CAR_PIN, "in")
RFID_IRQ_GPIO = GPIO(RFID_IRQ_PIN, "in")


# Open GPIO /sys/class/gpio/gpio73 with output direction
LED_GPIO = GPIO(LED_Pin, "out")
BUZ_GPIO = GPIO(BUZ_PIN, "out")
RY1_GPIO = GPIO(RY1_PIN, "out")
RY2_GPIO = GPIO(RY2_PIN, "out")

PWM_DIS_GPIO = GPIO(PWM_DIS_PIN, "out")
LTE_WDIS_GPIO = GPIO(LTE_WDIS_PIN, "out")
LTE_RST_GPIO = GPIO(LTE_RST_PIN, "out")

BUZ_GPIO.write(False)
PWM_DIS_GPIO.write(False)
LTE_WDIS_GPIO.write(False)
LTE_RST_GPIO.write(False)

print("Init System . . . .")





uart1.write(b"Hello World!")

# Read up to 128 bytes with 500ms timeout
# buf = serial.read(128, 0.5)
# print("read {:d} bytes: _{:s}_".format(len(buf), buf))

# uart1.close()





while True:
    try:
        print("RFID_IRQ_GPIO.read() ---> ", RFID_IRQ_GPIO.read(), "  CFCI_GPIO.read() ---> ", CFCI_GPIO.read())
        uart1.write(b"Hello World! True")
        LTE_RST_GPIO.write(True)
        time.sleep(1)
        LTE_RST_GPIO.write(False)
        uart1.write(b"Hello World! False")
        time.sleep(1)
    except KeyboardInterrupt:
        LTE_RST_GPIO.write(False)
        uart1.close()
        print("Error KeyboardInterrupt")
        break
    except IOError:
        uart1.close()
        print("Error IOError")

while True:
    try:
        BUZ_GPIO.write(True)
        print("True")
        time.sleep(1)
        BUZ_GPIO.write(False)
        print("False")
        time.sleep(1)
    except KeyboardInterrupt:
        BUZ_GPIO.write(False)
        break
    except IOError:
        print("Error")
BUZ_GPIO.close()
