class Sensor:

    serial = ""
    text = ""

    retryLimit = 5

    def __init__(self, serial):
        self.serial = serial

    def get_temp(self, times=0):

        if times == self.retryLimit:
            return False

        self.read_file()
        if self.is_error():
            times += 1
            return self.get_temp(times)

        return self.get_temperature_float()

    def read_file(self):
        tfile = open("/sys/bus/w1/devices/" + self.serial + "/w1_slave")
        self.text = tfile.read()
        tfile.close()

        print(self.text)

        return True

    def is_error(self):
        return self.text.split("\n")[0].split(" ")[11] == "NO"

    def get_temperature_float(self):
        raw_temp = self.text.split("\n")[1].split(" ")[9]

        return float(raw_temp[2:]) / 1000
