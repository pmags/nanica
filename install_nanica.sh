#! /bin/bash

set -e

# install dependencies
sudo apt-get install libharfbuzz0b libfontconfig1

# make dirs executable
# FIXME: carefull if sudo access is given
chmod +x make_dirs.sh
./make_dirs.sh

# install picam
tar xvf picam-1.4.7-binary.tar.xz
# copies files to be available at picam
cp picam-1.4.7-binary/picam ~/picam/

# make run_picam executable
chmod +x run_picam.sh

# copy file to initial and make it executable
sudp cp picam_tmp /etc/init.d/picam
sudo chmod +x /etc/init.d/picam

# Register at startup
sudo update-rc.d picam defaults

echo "Nanica available"