from scapy.all import *
# Ask user for input
user_input = input("Enter filter expression: ")

# Define filter expression and sniff packets
result = sniff(filter=user_input, prn=lambda x: x.summary())
wrpcap('sniff.pcap', result)
