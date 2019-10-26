sudo bash /home/pi/make_dirs.sh
sudo /home/pi/picam/picam -o /run/shm/hls --time --alsadev hw:1,0 > /var/log/picam.log 2&>1