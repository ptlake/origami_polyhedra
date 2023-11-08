import math
t=[]
for den in range(5):
    for num in range(-den+1,den):
        if math.gcd(num,den) == 1:
            for x in range(1,5):
                y = x/4 * math.tan(0.5 * math.acos(num/den))
                t.append((num, den, x, y))
t.sort(key=lambda x:x[3])
for a in t:
    print(f"{a[0]:2d} {a[1]:2d} {a[2]:2d}:    {a[3]:.4f}")
