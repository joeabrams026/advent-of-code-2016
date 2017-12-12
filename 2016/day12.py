import re
from util import Input

def run(instructions):
    registers = {'a':0,'b':0,'c':0,'d':0}
    
    i = 0
    j = 0
    while i < len(instructions) and j < 1000000:
        j += 1
        inst = instructions[i]
        #print registers, inst

        cpy = re.match('cpy (-?\d+|[abcd]) ([abcd])', inst)
        inc = re.match('inc ([abcd])', inst)
        dec = re.match('dec ([abcd])', inst)
        jnz = re.match('jnz (-?\d+|[abcd]) (-?\d)', inst)
        
        if cpy:
            val,reg = cpy.groups()
            if val in 'abcd':
                registers[reg] = registers[val]
            else:
                registers[reg] = int(val)
        elif inc:
            reg = inc.groups()[0]
            registers[reg] += 1
        elif dec:
            reg = dec.groups()[0]
            registers[reg] -= 1
        elif jnz:
            reg, jmp = jnz.groups()
            if not (reg == 0 or (reg in registers and registers[reg] == 0)):
                i += int(jmp)
                continue
        else:
            print 'unrecognized instruction', inst
            assert False
        
        i+=1
        
    return registers
    
print (run('''cpy 41 a
inc a
inc a
dec a
jnz a 2
dec a'''.split('\n'))['a'] == 42)

print run(Input("12").read().strip().split('\n'))