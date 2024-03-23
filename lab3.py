def carno(code: dict)->None:
    rc = ['00', '01', '11', '10'];
    for i in range(len(rc)):
        print("================")
        print(f"C{len(rc) - i - 1}")
        print("a3a2", end=' ');
        for c in rc:
            print(c, end=' ')
        print();
        print("a1a0");
        for r in rc:
            print(" ".join(str(r)), end=' ')
            for c in rc:
                print("{:>2}".format(code[c+r][i]), end=' ');
            print();
        print("================")
    
def table(f: dict)->None:
    print("Число |  8421     |  функция ")
    print("      +===========+==========")
    print("======|a3|a2|a1|a0|c3|c2|c1|c0")
    for _src, _code in f.items():
        print("{:<6}|".format(int(_src)), end='');
        print(' |'.join(str(_src)), end='');
        print(' |', end='')
        print(' |'.join(str(_code)));

    
codes1 = ['1101',
         '1110',
         '1111',
         '0000',
         '0001',
         '0010',
         '0011',
         '0100',
         '0101',
         '0110',
         'XXXX',
         'XXXX','XXXX','XXXX','XXXX','XXXX','XXXX','XXXX','XXXX','XXXX','XXXX','XXXX']
f1 = {f'{i:04b}': codes1[i] for i in range(16)};

codes2 = ['1111',
         '0000',
         '0001',
         '0010',
         '0011',
         '0100',
         '0101',
         '0110',
         '0111',
         '1000',
         'XXXX',
         'XXXX','XXXX','XXXX','XXXX','XXXX','XXXX','XXXX','XXXX','XXXX','XXXX','XXXX']
f2 = {f'{i:04b}': codes2[i] for i in range(16)};
#carno(f1);
table(f1);
print("===================================================")
print("===================================================")
print("===================================================")
#carno(f2);
table(f2);

