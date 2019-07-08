diberikan sebuah file zip recovery.7z, didalamnya terdapat file recovery.001 yang ketika dicek dengan file merupakan file DOS boot.
saya analisa dengan hexeditor didapat sebuah flag.apk, asumsi saya file ini berisi flagnya 
coba ekstrak dengan binwalk, saat di cek file flag.apk adalah file zip, unzip file tersebut didapat banyak file apk seperti ini . 
saya cek 1 per 1 file tsb, saya curiga dengan folder res/layout/main.xml. ketika di strings didapat flag flag={aplikasi_pertama_saya}
 
