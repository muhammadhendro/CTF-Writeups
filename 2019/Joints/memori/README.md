dilakukan identifikasi OS profile
dengan plugin kdbgscan.<br>

```
volatility -f memory.dmp kdbgscan
```

diperoleh Win7SP1x86 sebagai opsi profile
<br>
``` volatility -f memory.dmp --profile=Win7SP1x86 pslist ``` <br>

Berbicara mengenai notepad, hal yang pertama muncul di perspektif
penulis adalah informasi yang disembunyikan pada TXT file, dengan kata
lain sebuah plain-text. Berbekal pemahaman tersebut, dilakukan pencarian
file dengan ekstensi *.txt menggunakan plugin filescan.<br>

``` volatility -f memory.dmp --profile=Win7SP1x86 filescan | grep txt ``` <br>

diperoleh file hekelmensecret.txt yang kemungkinan memuat salah
satu dari flag.<br>

``` volatility -f memory.dmp --profile=Win7SP1x86 dumpfiles -Q 0x000000003e1d4e70 --name -D ``` <br>

Berdasarkan penelusuran sebelumnya, diketahui bahwa terdapat satu
suspect user, yaitu hekelmen, yang diduga melakukan eksploitasi pada
sistem. Selanjutnya, untuk menelusuri activity log yang ia lakukan, dilakukan
penelusuran dengan plugin chromehistory.<br>

``` volatility -f memory.dmp --profile=Win7SP1x86 chromehistory ```

<br>
Hasilnya, diketahui bahwa terdapat history log yang mengarah ke URL
https://ctf.asgama.web.id. Untuk memperkecil scope pencarian, dilakukan proses
memdump terlebih dahulu untuk process dengan PID 2552 (chrome.exe)<br>


 ``` volatility -f memory.dmp --profile=Win7SP1x86 memdump -p 2552 -D ``` <br>


```  strings 2552.dmp | egrep -i 'asgama.web.id' -A 25 | grep -i 'hekel' | head -5 ``` <br>

dilakukan proses ekstraksi kembali dengan plugin hashdump<br>

```  volatility -f memory.dmp --profile=Win7SP1x86 hashdump ``` <br>



