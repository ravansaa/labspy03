max = 0
while True:
    angka = int(input("Masukan Bilangan : "))
    if max < angka:
        max = angka
    if angka ==0:
        break
print("Bilangan yang Terbesar Adalah : ", max)