# A Few Bits of Modern Crypto

```
import base64
from itertools import cycle

def decrypt(encrypted, passphrase):
    data = base64.b64decode(encrypted)
    key = base64.b64decode(passphrase)
    return "".join(chr(ord(a)^ord(b)) for a, b in zip(data, cycle(key)))

def flintz(encrypted, passphrase):
    return "".join(chr(ord(a)^ord(b)) for a, b in zip(encrypted, cycle(passphrase)))

flag = open("flag_encrypted.txt", "r")
chiper = open("greeting_encrypted.txt", "r")
message = open("greeting.txt","r")

key =  decrypt(chiper.read(),flag.read())
print flintz(message.read(),key)



```