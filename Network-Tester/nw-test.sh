#!/bin/bash
#experiment duration in minutes
duration=1
#interval between experiments in minutes
interval=1

for i in $( eval echo {0..$duration..$interval} )
do
echo "run "$i >> script.log
date >> script.log
GATEWAY=`ip route | grep default | cut -d' ' -f3`
echo $GATEWAY >> script.log
echo >> script.log
echo "`dig +short myip.opendns.com @resolver1.opendns.com`" >> script.log
echo >> script.log
ping -s 1400 -c 10 $GATEWAY >> script.log
echo >> script.log
echo >> script.log
ping -s 1400 -c 10 10.250.200.3 >>script.log
echo >> script.log
echo >> script.log
mtr -s 1400 -c 30 -r 10.250.209.251 >>script.log
echo >> script.log
mtr -s 1400 -c 30 -r google.com >>script.log
echo >> script.log
mtr -s 1400 -c 30 -r facebook.com >>script.log
echo >> script.log
dig @10.250.200.3 A www.iitb.ac.in >>script.log
echo >> script.log
dig @10.250.200.3 A www.mit.edu >>script.log
echo >> script.log
dig @10.250.200.3 A www.iitdh.ac.in >>script.log
echo >> script.log
traceroute google.com >>script.log
echo >> script.log
traceroute facebook.com >>script.log
echo >> script.log
wget -a script.log http://ports.ubuntu.com/ubuntu-ports/dists/bionic-updates/main/installer-arm64/current/images/netboot/netboot.tar.gz
echo >> script.log
wget -a script.log http://ftp.iitdh.ac.in/os/ubuntu/archives/ubuntu/dists/bionic-updates/main/installer-amd64/current/images/hwe-netboot/netboot.tar.gz
echo >> script.log
sleep $interval"m"
done
