import os
os.system("cls")

car = {
    "brand": "Mers",
    "model": "Gelik",
    "narx": 200_000,
    "yil": 2026,
    "max_speed": 200,
}

if "model" in car:
    print(car["model"])
else:
    print("No")
