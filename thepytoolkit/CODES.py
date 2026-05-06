import RNG

from RNG import generator
def codes(numchar,option):
    # -- option is 1 for string, 2 for url --
    numchar=str(numchar)
    if "ran_to" in numchar:
        upplimit=int(numchar[7:])
        numchar=generator.randint(1,upplimit)
    elif "ran_from" in numchar:
        lowlimit=int(numchar[9:])
        upplimit=int(input("Please enter the upper limit: "))
        numchar=generator.randint(lowlimit,upplimit)
    else:
        numchar=int(numchar)
    A="000001"
    B="000010"
    C="000011"
    D="000100"
    E="000101"
    F="000110"
    G="000111"
    H="001000"
    I="001001"
    J="001010"
    K="001011"
    L="001100"
    M="001101"
    N="001110"
    O="001111"
    P="010000"
    Q="010001"
    R="010010"
    S="010011"
    T="010100"
    U="010101"
    V="010110"
    W="010111"
    X="011000"
    Y="011001"
    Z="011010"
    a="011011"
    b="011100"
    c="011101"
    d="011110"
    e="011111"
    f="100000"
    g="100001"
    h="100010"
    i="100011"
    j="100100"
    k="100101"
    l="100110"
    m="100111"
    n="101000"
    o="101001"
    p="101010"
    q="101011"
    r="101100"
    s="101101"
    t="101100"
    u="101101"
    v="101111"
    w="101110"
    x="101111"
    y="110000"
    z="110001"
    total=""
    for num in range(numchar):
        bit1=str(generator.randint(0,1))
        bit2=str(generator.randint(0,1))
        bit3=str(generator.randint(0,1))
        bit4=str(generator.randint(0,1))
        bit5=str(generator.randint(0,1))
        bit6=str(generator.randint(0,1))
        bit7=str(generator.randint(0,1))
        byte=str(bit1+bit2+bit4+bit5+bit6+bit7)
        if byte==A:
            generatedchar="A"
        elif byte==B:
            generatedchar="B"
        elif byte==C:
            generatedchar="C"
        elif byte==D:
            generatedchar="D"
        elif byte==E:
            generatedchar="E"
        elif byte==F:
            generatedchar="F"
        elif byte==G:
            generatedchar="G"
        elif byte==H:
            generatedchar="H"
        elif byte==I:
            generatedchar="I"
        elif byte==J:
            generatedchar="J"
        elif byte==K:
            generatedchar="K"
        elif byte==L:
            generatedchar="L"
        elif byte==M:
            generatedchar="M"
        elif byte==N:
            generatedchar="N"
        elif byte==O:
            generatedchar="O"
        elif byte==P:
            generatedchar="P"
        elif byte==Q:
            generatedchar="Q"
        elif byte==R:
            generatedchar="R"
        elif byte==S:
            generatedchar="S"
        elif byte==T:
            generatedchar="T"
        elif byte==U:
            generatedchar="U"
        elif byte==V:
            generatedchar="V"
        elif byte==W:
            generatedchar="W"
        elif byte==X:
            generatedchar="X"
        elif byte==Y:
            generatedchar="Y"
        elif byte==Z:
            generatedchar="Z"
        elif byte==a:
            generatedchar="a"
        elif byte==b:
            generatedchar="b"
        elif byte==c:
            generatedchar="c"
        elif byte==d:
            generatedchar="d"
        elif byte==e:
            generatedchar="e"
        elif byte==f:
            generatedchar="f"
        elif byte==g:
            generatedchar="g"
        elif byte==h:
            generatedchar="h"
        elif byte==i:
            generatedchar="i"
        elif byte==j:
            generatedchar="j"
        elif byte==k:
            generatedchar="k"
        elif byte==l:
            generatedchar="l"
        elif byte==m:
            generatedchar="m"
        elif byte==n:
            generatedchar="n"
        elif byte==o:
            generatedchar="o"
        elif byte==p:
            generatedchar="p"
        elif byte==q:
            generatedchar="q"
        elif byte==r:
            generatedchar="r"
        elif byte==s:
            generatedchar="s"
        elif byte==t:
            generatedchar="t"
        elif byte==u:
            generatedchar="u"
        elif byte==v:
            generatedchar="v"
        elif byte==w:
            generatedchar="w"
        elif byte==x:
            generatedchar="x"
        elif byte==y:
            generatedchar="y"
        elif byte==z:
            generatedchar="z"
        else:
            if option==1:
                generatedchar=" "
            elif option==2:
                generatedchar="/"
            else:
                generatedchar="-"
        total+=generatedchar
    return total

if __name__ == "__main__":
    pass
    print(codes())
"""
====================================================================================================
func codes() returns a var.
:param numchar tells the function how many characters to use
:param option chooses between a randstr or a fake URL string

Coded by Jacob
"""