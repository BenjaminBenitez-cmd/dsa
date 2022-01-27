def gcd(m, n):
    while m % n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm % oldn
    return n


class Fraction:
    def __init__(self, top, bottom):
        if isinstance(top, int) and isinstance(bottom, int):
            common = gcd(top, bottom)
            self.num = top // common
            self.den = bottom // common
        else:
            raise Exception("Top and Bottom should be type int")

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def __add__(self, otherfraction):
        newNum = self.num * otherfraction.den + otherfraction.num * self.den
        newDen = self.den * otherfraction.den
        common = gcd(newNum, newDen)
        return Fraction(newNum // common, newDen // common)

    def __iadd__(self, otherfraction):
        self.num = self.num * otherfraction.den + otherfraction.num * self.den
        self.den = self.den * otherfraction.den

        return Fraction(self.num, self.den)

    def __sub__(self, otherfraction):
        newNum = self.num * otherfraction.den - otherfraction.num * self.den
        newDen = self.den * otherfraction.den
        common = gcd(newNum, newDen)
        return Fraction(newNum // common, newDen // common)

    def __eq__(self, otherfraction):
        newNum = self.num * otherfraction.den
        newDen = otherfraction.num * self.den
        return newDen == newNum

    def __mul__(self, otherfraction):
        newNum = self.num * otherfraction.num
        newDen = self.den * otherfraction.den
        common = gcd(newNum, newDen)
        return Fraction(newNum // common, newDen // common)

    def __truediv__(self, otherfraction):
        newNum = self.num * otherfraction.den
        newDen = self.den * otherfraction.num
        common = gcd(newNum, newDen)
        return Fraction(newNum // common, newDen // common)

    def __lt__(self, otherfraction):
        left = self.num / self.den
        right = otherfraction.num / otherfraction.den
        return left < right

    def __le__(self, otherfraction):
        left = self.num / self.den
        right = otherfraction.num / otherfraction.den
        return left <= right

    def __ge__(self, otherfraction):
        left = self.num / self.den
        right = otherfraction.num / otherfraction.den
        return left >= right

    def __gt__(self, otherfraction):
        left = self.num / self.den
        right = otherfraction.num / otherfraction.den
        return left > right

    def __ne__(self, otherfraction):
        left = self.num / self.den
        right = otherfraction.num / otherfraction.den
        return left != right

    def getNum(self):
        return self.num

    def getDen(self):
        return self.den

    def __radd__(self, otherfraction):
        newNum = self.num * otherfraction.den + otherfraction.num * self.den
        newDen = self.den * otherfraction.den
        common = gcd(newNum, newDen)
        return Fraction(newNum // common, newDen // common)

    def __repr__(self):
        return 'Fraction(%s, %s)' % (str(self.num), str(self.den))


myfraction = Fraction(2, 3)
otherfraction = Fraction(1, 2)


def main():
    print(repr(myfraction))


main()
