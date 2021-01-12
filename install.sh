#! /bin/sh

pip3 install paramiko
sudo mkdir /usr/share/
sudo cp sshpython.py /usr/share/
sudo cp sshpython /bin
sudo chmod +x /bin/sshpython
