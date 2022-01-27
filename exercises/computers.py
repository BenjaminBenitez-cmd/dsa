class Computer:
    def __init__(self, name, cpu, storage):
        self.name = name
        self.cpu = cpu
        self.storage = storage

    def getStorage(self):
        print("Total Storage", self.storage)


class MobileComputer(Computer):
    def __init__(self, name, cpu, storage, opersystem):
        Computer.__init__(self, name, cpu, storage)

        self.opersystem = opersystem

    def getDetails(self):
        print("------System Properties --------")
        print("--------", self.cpu, "--------")
        print("--------", self.storage, "--------")
        print("--------", self.opersystem, "---------")


def main():
    comp1 = MobileComputer("Joe's computer", "ryzen9000", 4000, "linux")
    comp1.getDetails()


main()
