# Guess The Number

<p  align="center"><img src="img/1.png"/></p>


didapat link sebuah web > http://18.136.167.108:18030/  dan file index.php
dimana web tsb meminta sebuah inputan,

<img src="img/3.png"/>

buka file index.php tersebut,
diketahui dilakukan pengecekan apabila pada $guess sama dengan $number akan menghasilkan flag.

<img src="img/2.png"/>

berarti apapun bisa dimasukan asal valuenya sama.
disini saya coba dengan curl untuk melakukan post data tsb

> curl -d "guess=123&number=123" http://18.136.167.108:18030/

<img src="img/4.png"/>

**COMPFEST11{u53r_1npu7_1s_3v1l}**
