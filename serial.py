"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, serial):
        "stores 2 copies of original serial, one to be incrimented and another for reset"
        self.serial = serial
        self.start = serial

    def generate(self):
        "incriments serial by 1 and returns serial"
        self.serial += 1
        return self.serial

    def reset(self):
        "resets serial to initial start number"
        self.serial = self.start
