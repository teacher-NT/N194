
def calculate_discount(products: list) -> list:
    result = []
    for i in products:
        new_price = i['original_price'] * (1 - i['discount_percent'] / 100)
        result.append((i['name'], new_price))
    return result




# Test 1:
products = [
 {"name": "Laptop", "original_price": 5000000, "discount_percent": 20},
 {"name": "Telefon", "original_price": 2000000, "discount_percent": 10},
 {"name": "Planshet", "original_price": 1500000, "discount_percent": 0}
]
print(calculate_discount(products))
# Output:
# [
#  ("Laptop", 4000000.0),
#  ("Telefon", 1800000.0),
#  ("Planshet", 1500000.0)
# ]
# Test 2:
print(calculate_discount([]))
# Output:
# []
# Test 3:
print(calculate_discount([
 {"name": "Kitob", "original_price": 50000, "discount_percent": 50}
]))
# Output:
# [
#  ("Kitob", 25000.0)
# ]
# Test 4:
print(calculate_discount([
 {"name": "Stol", "original_price": 100000, "discount_percent": 100}
]))
# Output:
# [
#  ("Stol", 0.0)
# ]