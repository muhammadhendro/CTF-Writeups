# Lucky Number

function main

```
int __fastcall main(int argc, const char **argv, const char **envp)
{
  __int64 v4; // [rsp+8h] [rbp-18h] BYREF
  __int64 v5[2]; // [rsp+10h] [rbp-10h] BYREF

  v5[1] = __readfsqword(0x28u);
  v4 = 0LL;
  puts(" _                _            _   _                 _                ");
  puts("| |              | |          | \\ | |               | |               ");
  puts("| |    _   _  ___| | ___   _  |  \\| |_   _ _ __ ___ | |__   ___ _ __  ");
  puts("| |   | | | |/ __| |/ / | | | | . ` | | | | '_ ` _ \\| '_ \\ / _ \\ '__| ");
  puts("| |___| |_| | (__|   <| |_| | | |\\  | |_| | | | | | | |_) |  __/ |    ");
  puts("\\_____/\\__,_|\\___|_|\\_\\__, | \\_| \\_/\\__,_|_| |_| |_|_.__/ \\___|_|    ");
  puts("                        __/ |                                         ");
  puts("                       |___/                                          ");
  puts(" ");
  printf("Enter a number to check if its a lucky number: ");
  __isoc99_scanf("%llu", v5);
  v5[0] = doSomething(v5[0]);
  luckyNumberGen(&v4);
  if ( v4 == v5[0] )
  {
    puts("Wow ! You guessed the lucky number.");
    puts("Now submit the lucky number to get your points");
  }
  else
  {
    puts("Damn ! You are unlucky like me :( ");
  }
  return 0;
}
```

function doSomething

```
unsigned __int64 __fastcall doSomething(unsigned __int64 a1)
{
  unsigned __int64 v3; // [rsp+10h] [rbp-8h]

  v3 = 0LL;
  while ( a1 )
  {
    v3 = 10 * v3 + a1 % 0xA;
    a1 /= 0xAuLL;
  }
  return v3;
}
```

function luckyNumberGen

```
_QWORD *__fastcall luckyNumberGen(_QWORD *a1)
{
  _QWORD *result; // rax
  __int64 v2; // [rsp+8h] [rbp-20h]
  __int64 v3; // [rsp+10h] [rbp-18h]
  unsigned __int64 i; // [rsp+18h] [rbp-10h]
  __int64 v5; // [rsp+20h] [rbp-8h]

  v2 = 0LL;
  v3 = 1LL;
  result = a1;
  *a1 = 0LL;
  for ( i = 0LL; i <= 0x31; ++i )
  {
    *a1 += v2;
    v5 = v2 + v3;
    v2 = v3;
    result = (_QWORD *)v5;
    v3 = v5;
  }
  return result;
}
```

berikut solver yang dibuat:

```
def doSomething(a1):
    v3 = 0
    while a1:
        v3 = 10 * v3 + a1 % 10
        a1 //= 10
    return v3

def luckyNumberGen():
    v2 = 0
    v3 = 1
    result = 0
    for i in range(50):
        result += v2
        v2, v3 = v3, v2 + v3
    return result

def main():
    right_number_sum = luckyNumberGen()
    right_number = doSomething(right_number_sum)

    print("The right number is:", right_number)

if __name__ == "__main__":
    main()


```
