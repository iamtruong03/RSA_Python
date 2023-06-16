import MyMath
import MyBase

def getPrivateKey(file):
    fi = open(file, "r")
    n = int(fi.readline())
    d = int(fi.readline())
    fi.close()
    return n, d

def getCiphertextDecode(file):
    fi = open(file, "r", encoding="utf8")
    C = fi.readline()
    C = C.split(" ")
    C = C[:-1]
    fi.close()
    return C

def decode(n, d, C, base, fileOut):
    fo = open(fileOut, "w", encoding="utf8")
    P = ""
    for i in C:
        m = MyMath.powMod(MyBase.toInt(i, 64), d, n)
        c = str(m)
        while len(c) % base != 0:
            c = '0' + c
        x = 0
        while x != len(c):
            a = c[x:x+base]
            x += base
            P += chr(int(a))
            fo.write(chr(int(a)))
    fo.close()
    return P

def main():
    n, d = getPrivateKey("Data/PrivateKey.txt")
    C = getCiphertextDecode("Data/CiphertextDecode.txt")
    C = decode(n, d, C, 4, "Data/PlaintextDecode.txt")
    return C

main()