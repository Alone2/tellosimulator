# Template from: https://pythontic.com/modules/socket/udp-client-server-example
import socket
import os
import sys

questions={
    "speed?":"100",
    "battery?":"80",
    "time?":"12",
    "wifi?":"10",
    "sdk":"2.0",
    "sn?":"1234"
}

canreceivecommands = False

commands=["command","takeoff","land","emergency","up","down","left","right","forward","back","cw","ccw","flip","go","stop","curve","jump","speed","rc","wifi","mon","moff","mdirection","ap"]

localIP     = "0.0.0.0"
localPort   = 8889
bufferSize  = 1024

print("All traffic to 192.168.10.1 is about to be redirect to localhost.")
print("Please make sure to have ipv4 forwarding enabled.")
print("Are you sure you want to continue? (y / n)")
a = input()
if a != "y":
    sys.exit()

os.system("sudo iptables -t nat -A OUTPUT -p all -d 192.168.10.1 -j DNAT --to-destination 127.0.0.1")

UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
UDPServerSocket.bind((localIP, localPort))

def streamon():

    os.system('screen -S tellovideoscreen -d -m bash && screen -r tellovideoscreen -X stuff "ffmpeg -r 25 -re -f lavfi -i testsrc=duration=999999:size=960x720:rate=25 -f h264 udp://0.0.0.0:11111\n"')

def streamoff():
    os.system('screen -X -S tellovideoscreen kill')

try:
    print("started tello simulator...")
    while(True):

        bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)

        messageoriginal = bytesAddressPair[0].decode("utf-8")
        message = messageoriginal.split(" ")[0]
        address = bytesAddressPair[1]
        response = "";
        if (canreceivecommands):
            response ="error";

        if ("command" == message):
            response = "ok"
            canreceivecommands = True

        if (canreceivecommands and message in commands):
            response = "ok"

        if (canreceivecommands and message == "streamon"):
            streamon()
            response = "ok"

        if (canreceivecommands and message == "streamoff"):
            streamoff()
            response = "ok"

        try:
            if(canreceivecommands):
                response = questions[message]
        except:
            pass

        print("in: " + messageoriginal)
        print("out: " + response)

        UDPServerSocket.sendto(str.encode(response), address)

except KeyboardInterrupt:
    streamoff()
    # Removing entry
    os.system("sudo iptables -t nat -D OUTPUT -p all -d 192.168.10.1 -j DNAT --to-destination 127.0.0.1")

