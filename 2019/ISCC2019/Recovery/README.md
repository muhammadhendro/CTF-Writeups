# Recovery Me
diberikan sebuah file zip recovery.7z, didalamnya terdapat file recovery.001 yang ketika dicek dengan file merupakan file DOS boot.

<img src="../img/1.png"/>

saya analisa dengan hexeditor didapat sebuah file rar dan flag.apk, <img src="../img/5.png"/> asumsi saya file ini berisi flagnya 
coba ekstrak dengan binwalk <img src="../img/2.png"/>, saat di cek file flag.apk adalah file zip, unzip file tersebut didapat banyak file didalam apk seperti ini <img src="../img/3.png"/>. 
saya cek 1 per 1 file tsb, saya curiga dengan folder res/layout/main.xml. ketika di strings didapat flag <img src="../img/4.png"/>  **flag={aplikasi_pertama_saya}**
 
