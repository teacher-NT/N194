import os
os.system('cls')

# def even_squares(numbers: list[int]) -> list[int]:
#     result = []
#     for i in numbers:
#         if i % 2 == 0:
#             result.append(i**2)
#     return result

# numbers = [1, 2, 3, 4, 5, 6]
# print(even_squares(numbers))
# Output: [4, 16, 36]


# def find_longest_word(words: list[str]) -> str:
#     if not words:
#         return ""
#     return max(words, key=len)

# words = ["apple", "banana", "kiwi",'applejoice', "strawberry", ]
# print(find_longest_word([]))
# Output: strawberry


# def count_above_average(scores: list[int]) -> int:
#     if not scores:
#         return 0
#     avg = sum(scores)/len(scores)
#     res = list(filter(lambda x: x>avg, scores))
#     return len(res)

    # count  = 0
    # for i in scores:
    #     if i > avg:
    #         count+=1
    # return count

# scores = [50, 70, 80, 40, 90, 60]
# print(count_above_average([]))
# Output: 3  (o'rtacha: 65, undan yuqori: 70, 80, 90)



# def filter_by_prefix(words: list[str], prefix: str) -> list[str]:
#     res  = filter(lambda x:x.lower().startswith(prefix.lower()), words)
#     return list(res)

# words = ["Python", "java", "javascript", "Pycharm", "ruby"]
# prefix = "PY"
# print(filter_by_prefix(words, prefix))
# Output: ['Python', 'Pycharm']



import json

def manage_library(input_file: str, genre: str, output_file: str) -> int:
    with open(input_file) as file:
        books = json.load(file)
    res = list(filter(lambda x:x.get('genre').lower()==genre.lower(), books))
    res2 = res.copy()
    with open(output_file, "w") as f:
        json.dump(list(res), f, indent=2)
    return len(res2)

# Sinov uchun:
count = manage_library("books.json", "FANTASY", "fantasy_books.json")
print(count)
# Output: 2
# fantasy_books.json faylida faqat fantasy kitoblar yozilgan bo'lishi kerak

input_file="books.json"
genre="dystopia"
output_file="out.json"
count = manage_library(input_file, genre, output_file)
print(count)