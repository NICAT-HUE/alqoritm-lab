import random

n = int(input("n daxil et: "))
a = [random.randint(-3, 10) for _ in range(n)]
print("Siyahı:", a)

for i in range(n):
    if a[i] < 0:
        if i == 0:
            print("İlk ədəd mənfidir.")
        else:
            orta = sum(a[:i]) / i
            print("Ədədi orta:", orta)
        break
else:
    print("Mənfi ədəd yoxdur.")
