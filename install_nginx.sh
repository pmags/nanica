sudo apt-get install nginx
#sudo nano /etc/nginx/sites-available/default

sudo sed -i '/location/a/ location /hls/ {root /run/shm;}' /etc/nginx/sites-available/default
#location /hls/ {
#root /run/shm;
#}

sudo /etc/init.d/nginx start