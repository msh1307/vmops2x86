from capstone import *
from tqdm import tqdm
import itertools
import struct
#vm_opcodes_args = [[0x81,1],[0x91,2],[0x9F,0],[0xA1,2],[0xAA,1],[0x3,1],[0x6,1],[0xD,2],[0x24,2],[0xd8,2],[0x73,2]]
vm_opcodes_args = [[0x91,2]]
cs = Cs(CS_ARCH_X86, CS_MODE_64)
OPS = []
for oa in vm_opcodes_args:
    a = [i for i in range(0x100)]
    a *= oa[1]
    op = oa[0].to_bytes(1,byteorder='little')
    for tp in tqdm(itertools.permutations(a,oa[1])):
        code = op + bytes(tp)
        for k in cs.disasm(code,0x0):
            flag = 1
            for i in OPS:
                if i[0] == k.mnemonic:
                    flag = 0
            if flag:
                OPS.append([k.mnemonic,oa[1],oa[0]])
def print_candi(OPS):
    print("--- Candidates ---")
    for i in OPS:
        print(i[0])
if __name__ == "__main__":
    print_candi(OPS)
    while True:
        print("\n> ",end='')
        opcode = input()
        if opcode == 'exit':
            exit()
        elif opcode == 'candidates':
            print_candi(OPS)
            continue
        elif opcode.startswith('['):
            for k in cs.disasm(bytes(eval(opcode)),0x0):
                print("%d | %s   %s"%(k.address, k.mnemonic,k.op_str))
            continue
        flag = 0
        for i,j in enumerate(OPS):
            if j[0] == opcode:
                flag=1
                idx=i
                break
        if flag:
            a = [i for i in range(0x100)]
            a *= OPS[idx][1]
            op = OPS[idx][2].to_bytes(1,byteorder='little')
            for i in itertools.permutations(a,OPS[idx][1]):
                code = op + bytes(i)
                for k in cs.disasm(code,0x0):
                    if k.mnemonic == opcode:
                        print("%s   %s"%(k.mnemonic,k.op_str),end='')
                        arr = [x for x in code]
                        print('  // '+str(arr))
        else:
            print("Not found")