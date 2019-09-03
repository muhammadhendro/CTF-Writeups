# sabe64

```
import base64
import random

#socat TCP-LISTEN:6000,fork,reuseaddr EXEC:"python3 app.py"

def main():
    e = Encoder()
    with open('flag.txt', "rb") as f:
        flag = f.read()
    while True:
        command = input("Enter command: ").split(" ", 1)
        if not command:
            print("Please enter a command.")
            continue
        elif command[0] == "ENCODE":
            if len(command) < 2:
                print("Please enter text to encode.")
                continue
            print(e.encode(command[1].encode()))
        elif command[0] == "ENCODEFLAG":
            print(e.encode(flag))
        else:
            print("Invalid command")


def shuffle_string(s):
    s = list(s)
    random.shuffle(s)
    return "".join(s)


class Encoder(object):
    std = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'

    def __init__(self):
        self.perm = shuffle_string(self.std)
        self.enc = str.maketrans(self.std, self.perm)

    def encode(self, s):
        return base64.b64encode(s).decode().translate(self.enc)


if __name__ == "__main__":
    main()
```
<br>

script solver
<br>
```
from pwn import *
from string import printable
from random import choice

char = printable.strip()
tmp = ''.join(choice(char) for i in range(1000))
string = tmp.encode('base64').replace('\n','')

def kirim(isi):
	r.recvuntil(': ')
	r.sendline('ENCODE' + isi)
	return r.recvline().strip('\n')

cmpr = lambda x,y : dict(zip(x,y))
r = remote('127.0.0.1', 6000)
#r = process('python app.py')
flag = kirim('FLAG')
enc = kirim(' ' + tmp)
dic = cmpr(enc,string)

print ''.join(dic[i] for i in flag).decode('base64')
```