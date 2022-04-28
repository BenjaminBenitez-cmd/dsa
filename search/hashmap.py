import math


def isPrime(n):

    # Corner cases
    if(n <= 1):
        return False
    if(n <= 3):
        return True

    # This is check so that we can skip
    # middle five numbers in below loop
    if(n % 2 == 0 or n % 3 == 0):
        return False

    for i in range(5, int(math.sqrt(n) + 1), 6):
        if(n % i == 0 or n % (i + 2) == 0):
            return False

    return True


def nextPrime(N):
    # base case
    if(N <= 1):
        return 2

    prime = N
    found = False

    # Loop continously until isPrime returns
    # True for a number greater than n
    while(not found):
        prime = prime + 1

        if(isPrime(prime) == True):
            found = True

    return prime


class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size
        self.tomb = 'TOMB'

    def put(self, key, data):
        hashvalue = self.hashfunction(key, len(self.slots))
        tombhash = None

        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        else:
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data  # replace
            else:
                count = 0

                if self.slots[hashvalue] == self.tomb:
                    tombhash = hashvalue

                nextslot = self.rehash(hashvalue, count, len(self.slots))
                count += 1

                while self.slots[nextslot] != None and \
                        self.slots[nextslot] != key:
                    # set tomb if no previous Tombhash
                    if self.slots[nextslot] == self.tomb and not tombhash:
                        tombhash = nextslot

                    nextslot = self.rehash(nextslot, count, len(self.slots))
                    count += 1

                if self.slots[nextslot] == None and tombhash == None:
                    self.slots[nextslot] = key
                    self.data[nextslot] = data
                elif self.slots[nextslot] == key and tombhash != None:
                    self.slots[tombhash] = key
                    self.data[tombhash] = data

                    self.slots[nextslot] = None
                    self.slots[nextslot] = None
                elif self.slots[nextslot] == None and tombhash != None:
                    self.slots[tombhash] = key
                    self.slots[tombhash] = data

        # check load factor
        if(self.loadfactor() > 0.7):
            self.resize()

    def resize(self):
        self.size = nextPrime(len(self) * 2)

        tempslots = self.slots
        tempdata = self.data

        self.data = [None] * self.size
        self.slots = [None] * self.size

        for i in range(len(tempslots)):
            print(i)
            if tempslots[i] != None and tempslots[i] != self.tomb:
                self.put(tempslots[i], tempdata[i])

    def hashfunction(self, key, size):
        return key % size

    def rehash(self, oldhash, i, size):
        return (oldhash + i ^ 2) % size

    def loadfactor(self):
        return len(self) / self.size

    def get(self, key):
        startslot = self.hashfunction(key, len(self.slots))

        data = None
        stop = False
        found = False
        position = startslot
        while self.slots[position] != None and  \
                not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position, len(self.slots))
                if position == startslot:
                    stop = True
        return data

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)

    def __len__(self):
        count = 0
        for i in self.slots:
            if i != None:
                count = count + 1
        return count

    def __contains__(self, key):
        hashvalue = self.hashfunction(key, len(self.slots))

        if self.slots[hashvalue] == key:
            return True
        else:
            nextslot = self.rehash(hashvalue, len(self.slots))
            while self.slots[nextslot] != None and self.slots[nextslot] != key:
                nextslot = self.rehash(nextslot, len(self.slots))

            if self.slots[nextslot] == None:
                return False
            else:
                return True

    # Tombstone delete method
    def __delitem__(self, key):
        hashvalue = self.hashfunction(key, len(self.slots))

        if self.slots[hashvalue] == key:
            self.slots[hashvalue] = self.tomb
        else:
            count = 0
            nextslot = self.rehash(hashvalue, count, len(self.slots))
            count += 1

            while self.slots[nextslot] != None and self.slots[nextslot] != key:
                nextslot = self.rehash(nextslot, count, len(self.slots))
                count += 1
            if self.slots[nextslot] == key:
                self.slots[nextslot] = self.tomb


H = HashTable()
H[54] = "cat"
H[26] = "dog"
H[93] = "lion"
H[17] = "tiger"
H[77] = "bird"
H[31] = "cow"
H[44] = "goat"
H[55] = "pig"
H[20] = "chicken"


print(H.slots)

del H[77]

print(H.slots)

print(H[44])
H[44] = "Chihuaha"
print(H[44])
print(H.slots)
