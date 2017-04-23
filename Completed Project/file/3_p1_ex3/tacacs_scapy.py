#! /usr/bin/env python

# Set log level to benefit from Scapy warnings
import logging
import random
logging.getLogger("scapy").setLevel(1)

from scapy.all import *

class Tacacs(Packet):
	name = "Tacacs+"
	fields_desc=[ XByteField("major_version", 12),
			XByteField("minor_version", 0),
			ByteEnumField("type", 1, {1:"Authentication", 2:"Authorization", 3:"Accounting"}),
			ByteField("seq_no", 1),
			ByteEnumField("flags", 1, {1:"TAC_PLUS_UNENCRYPTED_FLAG", 4:"TAC_PLUS_SINGLE_CONNECT_FLAG"}),
			IntField("session_id", random.SystemRandom().randint(1, 4294967295)),
			IntField("length", 43)]

if __name__ == "__main__":
    interact(mydict=globals(), mybanner="Test add-on v3.14")
