# Demi masa

<img src="demimasa.png"><br>
```
from pwn import *

import time r=remote('34.87.0.60', 2057)
waktu= int(time.time()) % 255 
x = r.recvline().strip()


ans = ""
for i in range(len(x)):
	ans += chr(ord(x[i]) ^ waktu)
print ans
r.sendline(ans)
r.interactive()

```