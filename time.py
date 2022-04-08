import time

remainder = int(time.time()) % (ord("Z") - ord("A") + 1)

randomChr = chr(remainder + ord("A"))

print(randomChr)
print(remainder)