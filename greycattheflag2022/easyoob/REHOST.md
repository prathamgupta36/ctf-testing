# REHOSTING

Files can be found here: [easyoob](https://github.com/NUSGreyhats/greyctf-2022-public/tree/main/challenges/ezpz/easyoob)

## Challenge Setup
There are no dependency files for `easyoob` or `easyoob.c` or `ld.so` or `libc.so.6`

## Flag Linking
This challenge calls a flag.txt file in the current directory so had to link the flag.txt with /flag which is the pwn.college text:
```
#!/bin/bash

# Attempt to create a symbolic link
ln -s /flag /challenge/ezflag.txt 2>/dev/null
```
This is kept in the .init file since the link should be made everytime a new challenge is run with a new environment.
