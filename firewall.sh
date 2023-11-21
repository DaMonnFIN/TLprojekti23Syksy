#!/bin/bash

PATH="/usr/sbin:/sbin:/usr/bin:/bin"

#
# IPv4
#

# Clear old rules and set defaults
iptables -P INPUT ACCEPT
iptables -P OUTPUT ACCEPT
iptables -P FORWARD ACCEPT
iptables -F INPUT
iptables -F OUTPUT
iptables -F FORWARD
iptables -F -t nat
iptables -F -t mangle

# Local and trusted hosts and networks
iptables -A INPUT -i lo -j ACCEPT
iptables -A INPUT -s 192.168.0.0/24 -j ACCEPT # example how to allow whole IP network 192.168.0.xxx

# Backdoor for specific IP (students.oamk.fi)
iptables -A INPUT -s 193.167.100.97 -j ACCEPT # This rule is for backdoor access

# Completely open services
iptables -A INPUT -p tcp --dport 22 -j ACCEPT # SSH
iptables -A INPUT -p tcp --dport 80 -j ACCEPT # HTTP

# only allow or block ICMP traffic at the time, can't be used same time!
# Allow ICMP traffic
#iptables -A INPUT -p icmp -j ACCEPT
#iptables -A OUTPUT -p icmp -j ACCEPT

# Block ICMP traffic
iptables -A INPUT -p icmp -j DROP
iptables -A OUTPUT -p icmp -j DROP

# established traffic inbound (allow return traffic back which was originated from your server)
iptables -A INPUT -p ALL -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT

# Other SYN etc inbound

# Logging may generate too much log entries. This is commented now but left here as an example how to log:
# iptables -A INPUT -p ALL -m conntrack --ctstate NEW,INVALID -j LOG --log-prefix "DROP NEW "

# Drop all other new inbound but count dropped connections
iptables -A INPUT -p ALL -m conntrack --ctstate NEW,INVALID -j DROP 

# Dropping all example:
# iptables -A INPUT -p ALL -j DROP # This rule will drop all traffic, you should comment it out if you want to use the rules above

# Defaults - These default policies are quite permissive; adjust them as necessary for security
iptables -P INPUT DROP # Change default policy to DROP to secure the server
iptables -P OUTPUT ACCEPT
iptables -P FORWARD DROP

#
# IPv6 (same logic as with IPv4)
#

ip6tables -P INPUT DROP
ip6tables -P OUTPUT ACCEPT
ip6tables -P FORWARD DROP
ip6tables -F INPUT
ip6tables -F OUTPUT
ip6tables -F FORWARD

ip6tables -A INPUT -i lo -j ACCEPT
ip6tables -A INPUT -p tcp --dport 22 -j ACCEPT # SSH for IPv6
ip6tables -A INPUT -p tcp --dport 80 -j ACCEPT # HTTP for IPv6
# ip6tables -A INPUT -s 193.167.100.97 -j ACCEPT # Backdoor for IPv6 This needs to be IPv-6 addresss, not IPv4.
ip6tables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT
ip6tables -A INPUT -p icmpv6 -j ACCEPT # ICMPv6 autoconfig etc router advertisements

# Set default policies for IPv6
ip6tables -P INPUT DROP
ip6tables -P OUTPUT ACCEPT
ip6tables -P FORWARD DROP
