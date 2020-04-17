echo All traffic to 192.168.10.1 is about to be redirect to localhost.
echo Please make sure to have ipv4 forwarding enabled.
echo "Are you sure you want to continue? (y / n)"
read inp
[ "$inp" == "y" ] || exit

sh redirect.sh
screen -S tellovideoscreen -d -m bash
screen -r tellovideoscreen -X stuff "sh startvideo.sh"
sh command.sh

screen -X -S tellovideoscreen kill
