# Encang Maman Belajar Ngoding

pesan1 diencode dengan utf-16<br>

pesan2 diencode dengan utf-32<br>

Cheers.


hint 2 :
2 file tersebut adalah 2 file yang ditulis dengan encoding tertentu, dengan penanda encoding yang dihapus
<br>

```
iconv -t UTF-16 -t UTF-8 pesan1 | strings
iconv -t UTF-32 -t UTF-8 pesan2 | strings
```