# REHOSTING

Link to files: [0x41414141 CTF](https://github.com/sajjadium/ctf-archives/blob/main/ctfs/0x41414141/2021/crypto/Delegate-wallet/wallet.py)

## Challenge Setup
This challenge just has a file called `wallet.py` which do not have any dependencies.

## Flag Permissions
This challenge officially uses `flag.txt` file in the current working directory for the flag but as [`pwn.college`](https//:pwn.college.com) uses `/flag`, we changed the file to use that custom flag instead which made us provide python and the source file the permissions to open the flag. The restriction on python was it can only run the source file as sudo to open the flag. This is the bash script written for it and we make sure it is run before every new challenge is started:
```
#!/bin/bash
echo "hacker ALL=(ALL:ALL) NOPASSWD: /challenge/wallet.py" > /etc/sudoers.d/hacker
echo "hacker ALL=(ALL:ALL) NOPASSWD: /usr/bin/python wallet.py" > /etc/sudoers.d/hacker

chmod 0440 /etc/sudoers.d/hacker

chmod 4755 /usr/bin/sudo

sudo -u root /challenge/wallet.py

sudo chmod +x wallet.py
```