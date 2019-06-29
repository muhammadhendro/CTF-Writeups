## Putar Tiga Belas

<p  align="center"><img src="img/crypto1.PNG"/></p>
Didapat sebuah chiper ROT13 coba decode didapat 
<img src="img/c1.png"

flag **TNet{r0taT3_By_13_Pl4c3s}**


## 64 1
<p  align="center"><img src="img/crypto2.PNG" /></p>
didapat base64, langsung decode saja
<img src="img/c2.png"

flag  **TNet{Base64_3nC0diNg}**

## 64 2
<p  align="center"><img src="img/crypto3.PNG"/></p>

didapat lagi base64 yg berulang, agar simple kita pake script ini simpan string base64 pada flag.txt
'''
import base64

f = open('flag.txt', 'r')
hasil = f.read()

while True:
  hasil = base64.b64decode(hasil).decode('utf-8')

  if '{' in hasil:
    print(hasil)
    break


'''

<img src="img/c4.png"/>
flag **TNet{bAsE64_3Nc0dIn6_B3ruL4ng}**
## XOR

<p  align="center"><img src="img/crypto4.PNG"/></p>
sesuai judul coba kita bruteforce pada single XORnya
<img src="img/c5.png"/>

flag **TNet{XOR_D3cryPt_M0d3rn}**
