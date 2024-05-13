def HexConvertion(n, c):
    if c == 16:
        if str(n).isnumeric():
            if n == 10: return "A"
            elif n == 11: return "B"
            elif n == 12: return "C"
            elif n == 13: return "D"
            elif n == 14: return "E"
            elif n == 15: return "F"
        else:
            if n.upper() == "A": return 10
            elif n.upper() == "B": return 11
            elif n.upper() == "C": return 12
            elif n.upper() == "D": return 13
            elif n.upper() == "E": return 14
            elif n.upper() == "F": return 15
    return str(n)

def DecimalToAll(n, c):
    if n < c: return HexConvertion(n, c)
    return DecimalToAll(n // c, c) + HexConvertion(n % c, c)
    
def AllToDecimal(num, c):
    result = 0; count = len(num)-1
    for n in num:
        result += int(HexConvertion(n, c))*((c)**count)
        count -= 1
    return result

def AllToAll(num, base, ToBase):
    return DecimalToAll(AllToDecimal(str(num), int(base)), int(ToBase))