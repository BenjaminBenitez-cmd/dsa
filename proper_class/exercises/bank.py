# account, user, bank,

class Bank:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def getDetails(self):
        print("======= " + self.name + " =========")
        print("======= " + self.address + " =======")


class Account:
    def __init__(self, name, amount, bank):
        self.name = name
        self.amount = amount
        self.bank = bank

    def getTotal(self):
        return self.amount

    def deposit(self, amount):
        self.amount += amount

    def withdraw(self, amount):
        self.amount = self.amount - amount

    def getDetails(self):
        print("=========Account Holder ===========")
        print("========== " + self.name + " =========")
        print("========== Total =========")
        print("==========" + str(self.amount) + "=========")


class Savings(Account):
    def __init__(self, name, amount, bank):
        super().__init__(name, amount, bank)
        self.interest = 0.5


class Checking(Account):
    def __init__(self, name, amount, bank):
        super().__init__(name, amount, bank)

    def withdraw(self, amount):
        if(amount > self.amount):
            print("Cannot withdraw funds greater than amount")
        else:
            self.amount = self.amount - amount


def main():
    bank1 = Bank("Belize Bank", "Orange Walk")
    bank1.getDetails()

    acc1 = Savings("John Doe", 500, bank1)
    acc1.getDetails()
    acc1.withdraw(400)
    acc1.getDetails()


main()
