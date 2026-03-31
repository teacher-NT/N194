import os
os.system("cls")

car = {
    "brand": "Mers",
    "model": "Gelik",
    "narx": 200_000,
    "yil": 2026,
    "max_speed": 200,
}

# print(car.get("mode", "Bunday kalit yo'q"))
# print(car["mode"])

# print(car.keys())
# print(car.values())

# m = car.pop("yil")
# print(m)
# print(car)


# for k, q in car.items():
#     print(k, q)

# n = car.copy()
# n['model'] = "Damas"
# print(n, car)

# car.clear()
# print(car)

# k = car.popitem()
# print(k)
# print(car)

car.update({"yil": 2023,"narx":150000, "rang":"Qora"})
# car['yil'] = 2023
# car["narx"] = 150000
# car['rang'] = "Qora"
print(car)


# for i in car:
#     print(i, car[i])


# if "model" in car:
#     print(car["model"])
# else:
#     print("No")
