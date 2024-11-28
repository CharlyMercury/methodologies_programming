from machine import UART, Pin
import time

START_BYTE = 0xFF
SENSOR_ID = 0x01
COMMAND_READ = 0x86
COMMAND_SET_DETECTION_RANGE = 0x99

DETECTION_RANGE_2000 = 2000
DETECTION_RANGE_5000 = 5000

class MHZ19:
    def __init__(self, tx_pin, rx_pin):
        uart = UART(1, 9600)
        uart.init(9600, bits=8, parity=None, stop=1, tx=tx_pin, rx=rx_pin)

        self.uart = uart
        self.buf = bytearray(9)
        while uart.any() > 0:
            uart.readinto(self.buf, 9)
        
        self.co2 = 400
        self._next_read = 0
        self._cont_interval = 5000
        self._cont_measuring = False

    def get_co2(self):
        return self.co2

    def update(self):
        if self._cont_measuring and time.ticks_ms() > self._next_read:
            # print('measuring co2')
            self._next_read = time.ticks_ms() + self._cont_interval
            co2 = self.read_co2()
            if co2 != -1:
                self.co2 = co2

    def read_co2_continuous(self, interval):
        self._cont_measuring = True
        self._cont_interval = interval

    def read_co2(self):
        self._send_command(COMMAND_READ)
        start_read = time.ticks_ms()
        while self.uart.any() < 9:
            if time.ticks_ms() - start_read > 200:
                return -1
        self.uart.readinto(self.buf, 9)

        checksum = self._calc_sum(self.buf)
        # if checksum != self.buf[8]:
        #     print('checksum not correct')
        #     return -1
        
        ppm = self.buf[2]*256 + self.buf[3]
        return ppm
    
    def set_detection_range(self, range):
        range_high = int(range / 256)
        range_low = range % 256
        self._send_command(COMMAND_SET_DETECTION_RANGE, b3=range_high, b4=range_low)

    def _send_command(self, command, b3=0x00, b4=0x00, b5=0x00, b6=0x00, b7=0x00):
        command = [START_BYTE, SENSOR_ID, command, b3, b4, b5, b6, b7, 0x00]
        checksum = self._calc_sum(command)
        command[8] = checksum
        self.uart.write(bytearray(command))

    def _calc_sum(self, command):
        sum = 0
        for b in command[1:8]:
            sum += b
        sum = 0xff - sum 
        sum += 1
        return sum