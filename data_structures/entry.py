class Entry:
    def __init__(self, address, available, last_used):
        """
        Constructor for Entry data structure.

        self.address -> str
        self.available -> bool
        self.last_used -> datetime
        """

        self.address = address
        self.available = available
        self.last_used = last_used

    def ip_to_decimal(self):

        ip_address_digits = self.address.split('.')
        ip_address_decimal = 0
        for index, digit in enumerate(ip_address_digits):
            ip_address_decimal += int(digit) * 256**(3-index)
        return ip_address_decimal
