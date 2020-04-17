iptables -t nat -A OUTPUT -p all -d 192.168.10.1 -j DNAT --to-destination 127.0.0.1

