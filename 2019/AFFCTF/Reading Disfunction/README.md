diberikan koneksi nc 165.22.22.11 9999<br>

<img src="ok.png">
dimana flag terdapat pada setiap cell nya.<br>

```
#!/bin/bash
a='>'
for i in {1..200}
do
 echo "$a." | nc 165.22.22.11 9999
 a+=">"
done
```

