from pwn import xor

flag = "ASGama{ga"
flag2 = "mpang_to}"
cipher = ',#&\x0f\n>\x0f\x08\x1c'

a = xor(cipher[:15], flag)
b = xor(cipher[-15:], flag2)

print b +a

