#n or num = number to convert
#c = convertion base

#main functions
def hex(n, c):
    if c == 16:
        if n.isnumeric():
            if n == 10: return "a"
            elif n == 11: return "b"
            elif n == 12: return "c"
            elif n == 13: return "d"
            elif n == 14: return "e"
            elif n == 15: return "f"
        else:
            if n.upper() == "A": return 10
            elif n.upper() == "B": return 11
            elif n.upper() == "C": return 12
            elif n.upper() == "D": return 13
            elif n.upper() == "E": return 14
            elif n.upper() == "F": return 15
    return str(n)

def DecimalToAll(n, c):
    if n < c: return hex(n, c)
    return DecimalToAll(n // c, c) + hex(n % c, c)

def BinarioDecimal(n):
    if len(n) == 1: return int(n)
    return 2 * BinarioDecimal(n[:-1]) + int(n[-1])

def OctalBinario(n):
    try:
        octal = {'0': '000', '1': '001', '2': '010', '3': '011', '4': '100', '5': '101', '6': '110', '7': '111'}
        bin = str(''.join(octal[num] for num in n))
        return bin.lstrip('0')
    except:
        raise "invalid octal num"
    
def AllToDecimal(num, c):
    result = 0; count = len(num)-1
    for n in num:
        result += int(hex(n, c))*((c)**count)
        count -= 1
    return result

def HexBin(n):
    num=""; n = list(n.upper())
    for i in n:
        if i.isnumeric():
            num += (bin(int(i))[2:].zfill(4))
        else:   
            num += (bin(int(hex(i, 16)))[2:].zfill(4))
    return num

#derived from main functions
def BinarioOctal(n):
    return DecimalToAll(BinarioDecimal(n), 8)
    
def BinarioHex(n):
    return DecimalToAll(BinarioDecimal(n), 16)

def BinarioTer(n):
    return DecimalToAll(BinarioDecimal(n), 3)

def BinarioCuar(n):
    return DecimalToAll(BinarioDecimal(n), 4)

def OctalDecimal(n):
    return BinarioDecimal(OctalBinario(n))

def OctalHex(n):
    return DecimalToAll(OctalDecimal(n), 16)

def OctalTer(n):
    return DecimalToAll(OctalDecimal(n), 3)

def OctalCuar(n):
    return DecimalToAll(OctalDecimal(n), 4)

def HexDecimal(n):
    return BinarioDecimal(HexBin(n))

def HexOctal(n):
    return BinarioOctal(BinarioDecimal(HexBin(n)))

def HexTer(n):
    return BinarioTer(BinarioDecimal(HexBin(n)))

def HexCuar(n):
    return BinarioCuar(BinarioDecimal(HexBin(n)))

def TerDecimal(num):
    return AllToDecimal(num, 3)

def TerBin(num):
    return DecimalToAll(TerDecimal(num), 2)

def TerOctal(num):
    return DecimalToAll(TerDecimal(num), 8)

def TerHex(num):
    return DecimalToAll(TerDecimal(num), 16)

def TerCuar(num):
    return DecimalToAll(TerDecimal(num), 4)

def CuarDecimal(num):
    return AllToDecimal(num, 4)

def CuarBin(num):
    return DecimalToAll(CuarDecimal(num), 2)

def CuarOctal(num):
    return DecimalToAll(CuarDecimal(num), 8)

def CuarHex(num):
    return DecimalToAll(CuarDecimal(num), 16)

def CuarTer(num):
    return DecimalToAll(CuarDecimal(num), 3)

print(HexBin('8Ab'))