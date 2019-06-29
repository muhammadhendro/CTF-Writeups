## Felis Catus
<p  align="center"><img src="img/web1.PNG"/></p>
didapat link tentang SQL injection, coba view page source terdapat md5 hash
<img src="img/web1a.PNG"/>

didapat flag **TNet{kucing}**

## Login
<p  align="center"><img src="img/web2.PNG"/></p>
didapat form login ini
<img src="img/web2b.png"/>
mencoba dengan berbagai SQL injection namun gagal semua

<img src="img/web2a.png"/>
 akhirnya coba dengan curl pada flag.php curl -i http://ctf.technet.id:9004/flag.php
didapat 
  <img src="img/web2c.png"/>
  
 flag **TNet{SQL_Inj3ct10n_EZZ}**
 
 thx to gayu n rizky
 
## Tebak Kata
<p  align="center"><img src="img/web3.PNG"/></p>
<img src="img/web3a.PNG"/>
terdapat form berupa inputan text, coba view page source dan didapat hex 
<img src="img/web3b.png"/>

flag **TNet{J5_0bfuc4st0R}**

## Login 2
<p  align="center"><img src="img/web4.PNG"/></p>
sama seperti soal Login pertama dengan curl
<img src="img/web4b.png"/>

flag **TNet{SQL_Inj3ct10n_L1m1Tzz}**

## Kepala Saya Dimana?
<p  align="center"><img src="img/web5.PNG"/></p>
sesuai clue cek pada header terdapat sebuah chipertext
<img src="img/web5b.png"/>
cek juga pada page source didapat key berupa HEADER

<img src="img/web5a.PNG"/>
langsung cus decrypt dengan vigener chiper
<img src="img/web5c.png"/>

flag 
**TNet{B3rM4!n_CTF_1tu_A5y1k}**


## Javascript Membingungkan
<p  align="center"><img src="img/web6.PNG"/></p>
lihat page sourcenya terdapat file js.txt
<img src="img/web6a.PNG"/>
didapat string berupa jsfuck dan decode di http://codertab.com/JsUnFuck
<img src="img/web6b.PNG"/>

flag **TNet{JS_Pr0gr4mMin6_5tYl3}**






