# ffmpeg -r 25 -re -f lavfi -i testsrc=duration=30:size=960x720:rate=25 -vf "fps=30" -f h264 udp://0.0.0.0:11111 

# Video
ffmpeg -r 25 -re -f lavfi -i testsrc=duration=30:size=960x720:rate=25 -f h264 udp://0.0.0.0:11111 

# ffmpeg -r 25 -re -f lavfi -i testsrc=duration=3600:size=960x720:rate=25  -c:v libx265 -preset ultrafast -x265-params crf=23 -strict experimental -f h264 udp://0.0.0.0:11111 
