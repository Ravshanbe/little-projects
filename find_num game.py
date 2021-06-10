x = int(input("Son o'ylang"))
low, high = map(int, input("o'ylangan son oralig'i:").split())
k = 0
while low <= high:
    k += 1
    m = (low + high) // 2
    q = input(f"Siz o'ylagan son {m}, shundaymi?+(katta),-(kichik),=(ha)")
    if q == '=':
        print(f"Siz o'ylagan son {m}, {k} ta urinishda topildi")
        break
    elif q == '-':
        high = m - 1
    else:
        low = m + 1
