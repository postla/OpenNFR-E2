#!/bin/sh
################################
#####  Persian HD Project  #####
#######  Persian Prince  #######
#### info.bermoodateam.com  ####
################################

echo ""
echo "SatSharing.net SoftCam Downloader"
echo "Downloading SoftCam , Please Wait"
cd /var
mkdir keys > /dev/null 2>&1
cd 
wget http://www.satsharing.net/files/SoftCam.Key -O /var/keys/SoftCam.Key > /dev/null 2>&1
cd /var/keys
chmod 644 * > /dev/null 2>&1
cd
echo "Done"
sleep 2
exit 0
