Jika karakter yang dimasukkan tidak sesuai, maka program akan keluar. Jika karakter yang diinput benar, maka program akan meminta karakter selanjutnya.  kami mencoba brute force karakter yang diminta satu per satu
<br>

```
from subprocess import Popen, PIPE
import string
 
charset = string.letters + string.digits + '_'
param = '01'
flag = ''
x = 0
 
while x < len(charset):
    proc = Popen('./nani-the-fuk', stdin=PIPE, stdout=PIPE)
    char = flag + '%s\n' %charset[x]
    result = proc.communicate(input=char)[0]
    current = result[len(result)-13:len(result)-11]
    print charset[x]
    if current > param:
        flag += charset[x] + '\n'
        param = current
        x = 0
        print 'Flag : hacktoday{' + flag.replace('\n', '') + '}'
        continue
    x += 1
```
<br>

bisa juga <br>

```
from pwn import *

m = []

while(1):

   for i in range(0x20,0x7f):

       r = process('./nani-the-fuk')

       for x in m:

           r.sendlineafter('????', chr(x))

       try:

           r.sendlineafter('????', chr(i))

           a = r.recvuntil('????')

           print(i)

           m.append(i)

           print ''.join([chr(n) for n in m])

           if(len(m) >= 20):

               exit()

           break

       except EOFError:

           r.close()
```