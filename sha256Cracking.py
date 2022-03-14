#!/usr/bin/env python3

from pwn import *
import sys

if len(sys.argv) != 2:
    print("Invalid arguments...")
    print(">>> {} <sha256sum>".format(sys.argv[0]))
    exit()
    
hash = sys.argv[1]
passFile = "top100.txt"
count = 0

with log.progress("Attempting to crack : {}".format(hash)) as p:
    with open(passFile, "r", encoding='latin-1') as passList:
        for passwd in passList:
            password = passwd.strip("\n").encode('latin1')
            password_hash = sha256sumhex(password)
            if password_hash == hash:
                p.success("\nPassword found => {} <= for given hash after {} attemps".format(password.decode("utf-8") , count))
                exit()
            count += 1
        p.failure("Password hash not found")
 
