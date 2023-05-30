# vmops2x86

https://velog.io/@msh1307/Wacon-VM

root@ed1ff428eb33 ~/Desktop/CTF/wacon_VM
❯ python3 vmops2x86.py
256it [00:00, 124506.24it/s]
261632it [00:31, 8273.33it/s]
1it [00:00, 7319.90it/s]
261632it [00:00, 384716.08it/s]
256it [00:00, 7445.63it/s]
256it [00:00, 20044.84it/s]
256it [00:00, 336913.03it/s]
261632it [00:00, 385433.06it/s]
261632it [00:34, 7605.85it/s]
261632it [00:21, 11922.89it/s]
261632it [00:34, 7580.34it/s]
--- Candidates ---
xchg
add
or
syscall
clts
sysret
invd
wbinvd
ud2
femms
wrmsr
rdtsc
rdmsr
rdpmc
sysenter
sysexit
getsec
emms
push
pop
cpuid
rsm
ud2b
bswap
ud0
adc
sbb
and
insb
insd
outsb
outsd
nop
cwde
cdq
wait
pushfq
popfq
sahf
lahf
movsb
movsd
cmpsb
cmpsd
stosb
stosd
lodsb
lodsd
scasb
scasd
ret
leave
retf
int3
iretd
xlatb
in
out
int1
hlt
cmc
clc
stc
cli
sti
cld
std
sub
xor
cmp
cdqe
cqo
movsq
cmpsq
stosq
lodsq
scasq
retfq
iretq
movsxd
insw
outsw
cbw
cwd
pushf
popf
movsw
cmpsw
stosw
lodsw
scasw
iret
jo
jno
jb
jae
je
jne
jbe
ja
js
jns
jp
jnp
jl
jge
jle
jg
test
mov
lea
int
rol
ror
rcl
rcr
shl
shr
sal
sar
fadd
fmul
fcom
fcomp
fsub
fsubr
fdiv
fdivr
fld
fst
fstp
fldenv
fldcw
fnstenv
fnstcw
fxch
fnop
fstpnce
fchs
fabs
ftst
fxam
fld1
fldl2t
fldl2e
fldpi
fldlg2
fldln2
fldz
f2xm1
fyl2x
fptan
fpatan
fxtract
fprem1
fdecstp
fincstp
fprem
fyl2xp1
fsqrt
fsincos
frndint
fscale
fsin
fcos
fiadd
fimul
ficom
ficomp
fisub
fisubr
fidiv
fidivr
fcmovb
fcmove
fcmovbe
fcmovu
fucompp
fild
fisttp
fist
fistp
fcmovnb
fcmovne
fcmovnbe
fcmovnu
feni8087_nop
fdisi8087_nop
fnclex
fninit
fsetpm
fucomi
fcomi
frstor
fnsave
fnstsw
ffree
fucom
fucomp
faddp
fmulp
fcompp
fsubrp
fsubp
fdivrp
fdivp
fbld
fbstp
ffreep
fucomip
fcomip
loopne
loope
loop
jrcxz
jmp
repne insb
repne insd
repne outsb
repne outsd
repne movsb
repne cmpsb
repne cmpsd
repne stosb
repne stosd
repne lodsb
repne lodsd
repne scasb
repne scasd
bnd ret
bnd retf
rep insb
rep insd
rep outsb
rep outsd
pause
rep movsb
rep movsd
repe cmpsb
repe cmpsd
rep stosb
rep stosd
rep lodsb
rep lodsd
repe scasb
repe scasd
not
neg
mul
imul
div
idiv
inc
dec
call
lcall
ljmp


>
---------------------------------------------------------
> jmp
jmp   3  // [145, 235, 0]
jmp   4  // [145, 235, 1]
jmp   5  // [145, 235, 2]
jmp   6  // [145, 235, 3]
jmp   7  // [145, 235, 4]
jmp   8  // [145, 235, 5]
jmp   9  // [145, 235, 6]
jmp   0xa  // [145, 235, 7]
jmp   0xb  // [145, 235, 8]
jmp   0xc  // [145, 235, 9]
jmp   0xd  // [145, 235, 10]
jmp   0xe  // [145, 235, 11]
jmp   0xf  // [145, 235, 12]
jmp   0x10  // [145, 235, 13]
jmp   0x11  // [145, 235, 14]
jmp   0x12  // [145, 235, 15]
jmp   0x13  // [145, 235, 16]
jmp   0x14  // [145, 235, 17]
jmp   0x15  // [145, 235, 18]
jmp   0x16  // [145, 235, 19]
jmp   0x17  // [145, 235, 20]
jmp   0x18  // [145, 235, 21]
jmp   0x19  // [145, 235, 22]
jmp   0x1a  // [145, 235, 23]
jmp   0x1b  // [145, 235, 24]
jmp   0x1c  // [145, 235, 25]
jmp   0x1d  // [145, 235, 26]
jmp   0x1e  // [145, 235, 27]
jmp   0x1f  // [145, 235, 28]
jmp   0x20  // [145, 235, 29]
jmp   0x21  // [145, 235, 30]
jmp   0x22  // [145, 235, 31]
jmp   0x23  // [145, 235, 32]
jmp   0x24  // [145, 235, 33]
jmp   0x25  // [145, 235, 34]
jmp   0x26  // [145, 235, 35]
jmp   0x27  // [145, 235, 36]
jmp   0x28  // [145, 235, 37]
jmp   0x29  // [145, 235, 38]
jmp   0x2a  // [145, 235, 39]
jmp   0x2b  // [145, 235, 40]
jmp   0x2c  // [145, 235, 41]
jmp   0x2d  // [145, 235, 42]
jmp   0x2e  // [145, 235, 43]
jmp   0x2f  // [145, 235, 44]
jmp   0x30  // [145, 235, 45]
jmp   0x31  // [145, 235, 46]
jmp   0x32  // [145, 235, 47]
jmp   0x33  // [145, 235, 48]
jmp   0x34  // [145, 235, 49]
jmp   0x35  // [145, 235, 50]
jmp   0x36  // [145, 235, 51]
jmp   0x37  // [145, 235, 52]
jmp   0x38  // [145, 235, 53]
jmp   0x39  // [145, 235, 54]
jmp   0x3a  // [145, 235, 55]
jmp   0x3b  // [145, 235, 56]
jmp   0x3c  // [145, 235, 57]
jmp   0x3d  // [145, 235, 58]
jmp   0x3e  // [145, 235, 59]
jmp   0x3f  // [145, 235, 60]
jmp   0x40  // [145, 235, 61]
jmp   0x41  // [145, 235, 62]
jmp   0x42  // [145, 235, 63]
jmp   0x43  // [145, 235, 64]
jmp   0x44  // [145, 235, 65]
