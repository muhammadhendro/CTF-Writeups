
## Meowing 2
<p  align="center"><img src="img/forensic1.PNG"/></p>
diberikan sebuah gambar nekovoi lagi, cek gambar tsb dengan gabungan antara strings dan grep untuk mencari string 'tnet'
<img src="img/f1.png"/>

flag **TNet{MeoWwW_5uAr4_Kuc1Ng}**

## Tanda Tangan
<p  align="center"><img src="img/forensic2.PNG"/></p>
didapat sebuah file yang diduga merupakan sebuah file gambar, cek dengan hex editor dan memang file signature tsb salah.

<img src="img/f2.png"/>

**TNet{H3adeR_Si6Natur3_FiL3}**

## Kode Tiket
<p  align="center"><img src="img/forensic3.PNG"/></p>
diberikan sebuah file pcapng, buka dengan wireshark. pada POST /upload.html didapat sebuah biner.
<img src="img/f3.png"/>

decode didapat flag **TNet{N3tw0rk_F0r3nSic}**

