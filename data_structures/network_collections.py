import re
from ipaddress import IPv4Network, IPv4Address
from data_structures.entry import Entry

class NetworkCollection:
    def __init__(self, ipv4_network, raw_entry_list):
        """
        Constructor for NetworkCollection data structure.

        self.ipv4_network -> ipaddress.IPv4Network
        self.entries -> list(Entry)
        """

        self.ipv4_network = IPv4Network(ipv4_network)
        self.entries = [
            Entry(
                address=entry['address'],
                available=entry['available'],
                last_used=entry['last_used']
            )
            for entry in raw_entry_list
        ]

        self.remove_invalid_records()
        #self.sort_records()

    def remove_invalid_records(self):
        """
        Removes invalid objects from the entries list.
        """
        remove_records = []

        for entry in self.entries:
            digit_format = '[0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]'
            find_format = r'^({0})\.({0})\.({0})\.({0})$'.format(digit_format)
            pattern = re.compile(find_format)

            not_valid = False

            if not pattern.match(entry.address):
                not_valid = True
            if not_valid == False:
                if IPv4Address(entry.address) not in self.ipv4_network:
                    not_valid = True

            if not_valid :
                remove_records.append(entry.address)
                continue

        self.entries= [x for x in self.entries if x.address not in remove_records]

    #def sort_records(self):
        """
        Sorts the list of associated entries in ascending order.
        DO NOT change this method, make the changes in entry.py :)
        """
        #need to comaback here
        #self.entries = sorted(self.entries)
