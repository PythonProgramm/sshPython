#! /bin/sh

pip3 install paramiko
sudo mkdir /usr/share/sshpython/
sudo cp sshpython.py /usr/share/sshpython/
sudo cp sshpython /bin/
sudo chmod +x /bin/sshpython
