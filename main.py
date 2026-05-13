import os
os.system('cls')

import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='1234',
    database='dars_baza'
)

cursor = mydb.cursor()

# _id = input("Id: ")
# username = input("Username: ")
# first = input("First name: ")
# last = input("Last name: ")
# posts = int(input("Posts count: "))
# followers = int(input("Followers: "))
# following = int(input("Followings: "))
# joined = input("Joined date: ")

# sql = f"""
#     INSERT INTO users(user_id,username,first_name,last_name,posts_count,followers,followings,joined_date)
#     VALUES
#     ({_id}, '{username}', '{first}', '{last}', {posts}, {followers}, {following}, '{joined}');
# """


# sql2 = """
#     UPDATE users SET followers = 7000000
#     WHERE user_id = 31;
# """

sql3 = """
    DELETE FROM users WHERE user_id = 30;
"""

cursor.execute(sql3)
mydb.commit()

print(f"{cursor.rowcount} rows affected")