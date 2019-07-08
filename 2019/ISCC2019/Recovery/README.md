# Recovery Me
diberikan sebuah file zip recovery.7z
yang didalamnya terdapat file recovery.001, ketika dicek dengan format file merupakan file DOS boot.

<img src="../img/1.png"/>

saya analisa dengan hexeditor didapat sebuah file rar dan flag.apk, 

<img src="../img/5.png"/> 
asumsi saya file ini berisi flagnya 
coba ekstrak dengan binwalk 

<img src="../img/2.png"/>
saat di cek format flag.apk adalah file zip, unzip file tersebut didapat banyak file seperti ini

<img src="../img/3.png"/>. 
saya cek 1 per 1 file tsb, saya curiga dengan folder res/layout/main.xml. 
ketika di strings didapat flag 

<img src="../img/4.png"/>  

**flag={aplikasi_pertama_saya}**
 
