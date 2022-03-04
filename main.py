grocery = ['banana', 'apple', 'melon', 'watermelon', 'TV', 'iPhone']
n = int(input('nechta mahsulot olganingizni kiriting: '))
z = 0
for i in range(n):
    a = input("mahsulot nomi: ")
    for q in range(len(grocery)):
        if grocery[q] == a:
            z += 1
            x = q
            grocery.pop(x)
            print(grocery)
            break
    if z == i:
        print("Mahsulot savatda yo'q")
        z+=1

# a = input()
# c = 0
# for i in range(0, len(a)):
#     c += int(a[i])
#
# print(c)

# a="Ravshan"
# b="Jumanazarov"
# c=f"{a} {b} bizning platformamizga xush"
# print(c)
# a=1_888_900.00
# b="%.5f" % a
# print(f"Men bugun bankdan {b} so'm pul qaytarib oldim")
#
# print(type(a))
