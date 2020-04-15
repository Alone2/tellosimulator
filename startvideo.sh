# Video
ffmpeg -f lavfi -i testsrc=duration=100:size=1280x720:rate=60  -f mpegts udp://0.0.0.0:11111
