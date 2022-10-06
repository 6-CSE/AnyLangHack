#!/bin/sh
echo Hello!
echo This script will help automate post-installation setup of minix3
passwd
echo export TZ=Asia/Kolkata > /etc/rc.timezone
pkgin update
pkgin install openssh
mkdir /etc/rc.d/
cp /usr/pkg/etc/rc.d/sshd /etc/rc.d/
printf 'sshd=YES\n' >> /etc/rc.conf
/etc/rc.d/sshd start
pkgin update
pkgin_sets
echo That's all! You're ready to rock!
