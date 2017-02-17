#Have to initialize c to 1
#Wow, much challenge
registers ={"a":0, "b":0, "c":1, "d":0}
code=[]

def process_line(idx):
    while(idx<len(code)):
        cmd, *args=code[idx].split()
        offset=1
        if cmd== "cpy":
            registers[args[1]]=int(args[0]) if args[0].isdigit() else registers[args[0]]
        elif cmd=="inc":
            registers[args[0]]+=1
        elif cmd=="dec" :
            registers[args[0]]-=1
        elif cmd=="jnz":
            comp= int(args[0]) if args[0].isdigit() else registers[args[0]]
            if comp!=0:
                offset=int(args[1])
        idx+=offset

with open ('input.txt') as f:
    code=[l.rstrip('\n') for l in f.readlines()]
    process_line(0)
    print(registers)
