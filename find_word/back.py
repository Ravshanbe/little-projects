from uzwords import words
import random
xarf=['й','ц','у','к','е','н','г','ш','ў',
   'з','х','ъ','ҳ','э','ж','д','л','о',
   'р','п','а','в','қ','ф','я','ч','с',
   'м','и','т','ь','б','ю']
def letter(word):
    l=len(word)
    found=[]
    entered_words = ''
    k=0
    for i in range(len(word)):
        found.append('_')
    while True:
        k+=1
        a = input("\nharf kiriting:").lower()
        if a not in entered_words:
            entered_words+=a
            xarf.remove(a)
            if a in word:
                for i in range(len(word)):
                    if a == word[i]:
                        print(f"{a.upper()} harfi to'g'ri kiritildi")
                        # print(i)
                        l -= 1
                        found[i] = a
                    else:

                        continue
                # print(found)
                for i in found:
                    print(i.upper(), end='')
            else:
                print("Xato! bunday harf so'zimizda mavjud emas mavjud emas")
                for i in found:
                    print(i.upper(), end='')
        else:
            print(entered_words)
            print("Bu harf avval kiritilgan.Iltimos boshqa xarf kiriting")
        print(f"\nShu vaqtgacha kiritilgan harflar {entered_words.upper()}"
              f"\nBisotingizdagi harflar {xarf}")
        if l == 0:
            break
    jovob=f"Siz {k} ta urinishda topdingiz"
    print(jovob)
    return k
def word():
    random_word = random.choice(words)
    while " " in random_word or " " in random_word:
        random_word=random.choice(words)
    print(random_word)
    size_word = len(random_word)
    print(size_word)
    print(f"Men {size_word} ta harfli so'z o'yladim topa olasizmi")

    for i in range(size_word):
        print('_',end='')
    letter(random_word)



word()