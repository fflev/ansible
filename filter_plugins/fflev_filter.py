#!/usr/bin/env python3

from netaddr import IPNetwork


class FilterModule:
    def filters(self):
        return {
            "getoctet": self.getoctet,
            "getquad": self.getquad,
            "getmacid": self.getmacid,
        }

    def getoctet(self, value, num):
        network = IPNetwork(value)

        if network.version == 4 and 1 < num > 4:
            raise ValueError("Queried octet must be between 0 and 4")

        if network.version == 6 and 1 < num > 8:
            raise ValueError("Queried quad must be between 0 and 8")

        return str(network).split("." if network.version == 4 else ":")[num - 1]

    def getquad(self, value, num):
        return self.getoctet(value, num)

    def getmacid(self, value, num):
        octet = int(self.getoctet(value, num))

        if octet > 99:
            return "%02x" % octet
        else:
            return octet
