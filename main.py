import os
os.system("cls")

ismlar = ['Ibrohim', "Begzod", "Abdulhamid"]

ismlar.append("Nurmuhammad")
# print(ismlar)

ismlar.insert(1, "Muhammadsobir")
# print(ismlar)

ismlar2 = ["Asalxon", "Pariza"]
ismlar.extend(ismlar2)
# print(ismlar)

ismlar.remove("Ibrohim")
# print(ismlar)

# ism = ismlar.pop(3)
# print(ismlar)
# print(ism)

# ismlar.clear()
# print(ismlar)

# print(ismlar)
# ismlar.sort(reverse=True)
# print(ismlar)

ismlar3 = ismlar.copy()
ismlar3.append("Ibrohim")
print(ismlar3)
print(ismlar)
