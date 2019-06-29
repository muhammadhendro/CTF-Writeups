## Password
<p  align="center"><img src="img/rev1.PNG"/></p>
diberikan sebuah file soal reverse, coba dulu dengan strings didapat key yang diduga sebuah flag
<img src="img/r1.png"/>

flag **TNet{M1nt4_Fl4gnY4_D0nK}**

## Tebak Kata 2
<p  align="center"><img src="img/rev2.PNG"/></p>
didapat sebuah file py yg berisi script python

<img src="img/r3.png"/>
dari situ terlihat jika flag sudah ada namun terpecah, dan tinggal menyusunnya
berikut solver yang saya coba sendiri

```
data =[None] *30
data[::5] = 'TRstiZ'
data[15:-7] = 'th0n_i5_'
data[6::2] = '33s_Yhni_4zy'
data[8:15] = '3rs3_pY'
data[::-7] = '}_t3N'
data[2::5] = 'ev_0_Z'
data[23] = 'e'
data[-29:-25]  = 'Net{'

data = data[30:] +data[:30]
print(''.join(data))

```
jalankan...
<img src="img/r2.png"/>

flag **TNet{R3v3rs3_pYth0n_i5_e4ZzZy}**

## PIN
<p  align="center"><img src="img/rev3.PNG"/></p>
diberikan sebuah binary ELF64 buka file tsb dengan IDA pro
<img src="img/r4.png"/>
didapat sebuah fungsi pengecekan pin, cek pada fungsi valid_pin
<img src="img/r5.png"/>
didapat sebuah string hexa yg merupakan pin valid, ubah kedesimal menjadi 17081945 
, inputkan pin tsb
<img src="img/r6.png"/>

flag **TNet{17081945}**

## Password 2
<p  align="center"><img src="img/rev4.PNG"/></p>
diberikan sebuah binary ELF64 buka file tsb dengan IDA pro
<img src="img/r7.png"/>
dilakukan pengecekan inputan variabel s harus sama dengan key agar v5 tetap bernilai true
cek pada fungsi key tsb didapat sebuah key yang sudah di XOR,
<img src="img/r8.png"/>
 bruteforce key tersebut didapat string ini
 <img src="img/r9.png"/>
 
 ketika di run..
 
 <img src="img/r10.png"/>
 
 flag **TNet{In1_P4ssw0rD_Ganzz}**

