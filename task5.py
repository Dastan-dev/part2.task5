name = int(input("skoliko ychenikov? : "))
name2 = int(input("skoliko ychenikov? : "))
name3 = int(input("skoliko ychenikov? : "))

desk = name // 2
ost = name % 2
if ost != 0:
    desk += 1
print(desk)
desk1 = name2 // 2
ost1 = name2 % 2
if ost1 != 0:
    desk1 += 1
print(desk1)
desk2 = name3 // 2
ost2 = name3 % 2
if ost2 != 0:
    desk2 += 1
print(desk2)
part = round(desk2) + round(desk1) + round(desk)
print("Nuzhno " + str(part) + " part")