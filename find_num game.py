import random


def sontop(x=10):
    taxminlar = 0
    randomnum = random.randint(1, x)
    print(f"Men 1 dan {x} gacha son o'yladim")
    while True:
        taxminlar += 1
        taxmin = int(input(">>>"))
        if taxmin < randomnum:
            print("Xato. Men o'ylagan son bundan kattaroq.")
        elif taxmin > randomnum:
            print("Xato. Men o'ylagan son bundan kichikroq.")
        else:
            print(f"Tabriklaymiz {taxminlar} ta taxminlar topdingiz!")
            break
    return taxminlar


def sontopPc(x=10):
    input(f"1 dan {x} gacha son o'ylang va istalgan tugmani bosing Men topaman")
    quyi = 1
    yuqori = x
    taxminlar=0
    while True:
        taxminlar+=1
        if quyi != yuqori:
            taxmin = random.randint(quyi, yuqori)
        else:
            taxmin = quyi
        javob = input(f"Siz {taxmin} sonini o'yladingiz: to'g'ri(t),"
                      f"men o'ylagan son bundan kattaroq(+), yoki kichikroq(-) ".lower())
        if javob == '-':
            yuqori = taxmin - 1
        elif javob == '+':
            quyi = taxmin + 1
        else:
            break
    print(f"Topdim!{taxminlar} ta urinish bilan topdim" )
    return taxminlar
def play(x=10):
    again=True
    while True:
        taxminlar_user=sontop(x)
        taxminlar_px=sontopPc(x)
        if taxminlar_user>taxminlar_px:
            print("Men yutdim")
        elif taxminlar_px>taxminlar_user:
            print("Siz yutdingiz")
        else:
            print("Durrang")
        again=int(input("yana o'ynaysizmi:(1)ha,(0)yo'q"))

play()
