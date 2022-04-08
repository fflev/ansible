#!/usr/bin/env python3

from netaddr import IPNetwork
import subprocess
import re


class FilterModule:
    def filters(self):
        return {
            "getoctet": self.getoctet,
            "getquad": self.getquad,
            "getmacid": self.getmacid,
            "fastd_pubkey": self.fastd_pubkey,
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

    def fastd_pubkey(self, value):
        r = re.compile('^[0-9a-f]{64}$')
        key = str(value)
        if not r.match(key):
            raise ValueError("Input does not look like a fastd key")
        proc = subprocess.Popen(
            ['ecdsakeygen', '-p'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        output, _ = proc.communicate(input=key.encode('utf-8'))
        return output.strip().decode('utf-8')
