# NANICA - baby monitor


## 1.First steps

- install raspbian lite
- on the boot partition include wpa config file and an empty ssh file
- sudo apt-get update
- sudo raspi-config. Under optio 5 enable camera, 
change internationalization option
- under 2.network options change the hostname
- The Raspberry Pi can be pinged and connected to via the
 hostname babypi.local or whatever name you chose 
in the last step (plus .local at the end). However, 
the IP address this defaults to is a long one (IPv6). 
Web browsers can have trouble connecting to the Pi with this enabled, 
so we need to disable IPv6 hostname resolution.

sudo nano /etc/avahi/avahi-daemon.conf

n the line use-ipv6=yes change yes to no.
- reboot 

## 2.
