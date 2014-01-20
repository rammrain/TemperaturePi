class Sensor:

    serial = ""
    text = ""

    retryLimit = 5

    def __init__(self, serial):
        self.serial = serial

    def getTemp(self, times = 0):

        if (times == self.retryLimit):
            return False

        self.readFile()
        if (self.isError()):
            times += 1
            return self.getTemp(times)

        return self.getTemperatureFloat()

    def readFile(self):
        tfile = open("/sys/bus/w1/devices/" + self.serial + "/w1_slave")
        self.text = tfile.read()
        tfile.close()

        return True

    def isError(self):
        if (self.text.split("\n")[0].split(" ")[11] == "NO"):
            return True
        return False

    def getTemperatureFloat(self):
        rawTemp = self.text.split("\n")[1].split(" ")[9]

        return float(rawTemp[2:]) / 1000

