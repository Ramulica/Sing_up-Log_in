import csv
import string

# with open("Log_in_data.csv", 'r') as fa:
#     reader = csv.reader(fa)
#     for line in reader:
#         print(line, len(line))
# print(dir(str))
# print(dir(string))
# print(string.punctuation)
# print('!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~')
#
#
# def get_correct_name() -> str:
#     """
#     If the name doesn't have unknown characters it returns the name
#     :return:
#     """
#     while True:
#         name = input(str("Enter your name:"))
#         x = 0
#         for ch in name:
#             if ch in string.punctuation + string.digits:
#                 x = 1
#         if x == 0:
#             break
#         else:
#             print(f"Error: name cannot contain any of these characters {string.punctuation + string.digits}")
#     return name
#
#
# # print(get_correct_name())
# email = input(str("Enter your email:"))
# print(email[email.find("@")::])


# def get_correct_mail() -> str:
#     """
#     email prefix formats
#     Allowed characters: letters (a-z), numbers, underscores, periods, points and dashes.
#     An underscore, period, or dash must be followed by one or more letter or number.
#
#     email domain formats
#     Allowed characters: letters, numbers, dashes.
#     The last portion of the domain must be at least two characters, for example: .com, .org, .cc
#     :return:
#     """
#     while True:
#         email = input(str("Enter your email:"))
#         condition = True
#         for ch in email[0:email.find("@")-1]:
#             if ch in '!"#$%&\'*+,/:;<=>?@[\\]^`{|}~':
#                 condition = False
#                 print(1)
#         if email[email.find("@") - 1] in string.punctuation:
#             condition = False
#             print(2)
#         if email[0] in string.punctuation:
#             condition = False
#             print(3)
#         for ch in email[email.find("@") + 1:email.rfind(".")]:
#             if ch in '!"#$%&\'()_*+,./:;<=>?@[\\]^`{|}~':
#                 condition = False
#                 print(4)
#         for ch in email[email.rfind(".") + 1::]:
#             if ch in string.punctuation:
#                 condition = False
#                 print(5)
#         if len(email[email.rfind(".") + 1::]) < 2:
#             condition = False
#             print(6)
#         if condition:
#             break
#         else:23456werwewqq1233223232323232333333333333333333333333333333333333333333333333333333344444
#             print(f"Error: Email is incorrect")
#     return email
#
#
# print(get_correct_mail())
# while True:
#     password = input(str("Enter your password"))
#     condition = True
#     if len(password) < 8:
#         condition = False
#     for ch in password:
#         if password.count(ch) > 2:
#             condition = False
#     ch_letter = 0
#     for ch in password:
#         if ch in string.ascii_letters:
#             ch_letter += 1
#     if ch_letter <= 4 or ch_letter == len(password):
#         condition = False
#     if condition:
#         while password != input(str("Enter your password confirmation")):
#             print("Error: password confirmation is wrong")
#         break
#     else:
#         print("Error: Your password is not strong enough. Try again!")
# def get_correct_age() -> int:
#     while True:
#         try:
#             age = int(input("What is your Age?:"))
#         except ValueError as e:
#             print(f'Your age must be written with')
#         else:
#             if age > 16:
#                 break
#             else:
#                 print("You are too yong for this app")
#     return age
#
# print(get_correct_age())
#
# l_genders = ['Female', 'Male', 'Intersex', 'Trans', 'Non-Conforming', 'Eunuch',
#              "trans-parent", 'Personal']
# print(f'Chose one gender from{l_genders}')
# gender = input(str("What is your gender?"))
#
# while gender not in l_genders:
#     print("Error: incorrect gender")
#     gender = input(str("What is your gender?"))

# while True:
#     p_code: str = input(str("Enter your postal code:"))
#     codition = True
#     digits = 0
#     if len(p_code) != 6:
#         codition = False
#         print('Error: Postal code has 6 characters')
#     else:
#         for ch in p_code:
#             if ch in string.digits:
#                 digits += 1
#     if digits != 6:
#         codition = False
#         print("Error: Postal contains just digits")
#     if codition:
#         break
# print(type([p_code]))
#
# def get_correct_address_postal_code():
#     """
#     returns a list with the address and postal code
#     :return:
#     """
#     address = input(str("Enter your home address:"))
#     while True:
#         p_code = input(str("Enter your postal code:"))
#         condition = True
#         digits = 0
#         if len(p_code) != 6:
#             condition = False
#             print('Error: Postal code has 6 characters')
#         else:
#             for ch in p_code:
#                 if ch in string.digits:
#                     digits += 1
#         if digits != 6:
#             condition = False
#             print("Error: Postal contains just digits")
#         if condition:
#             break
#     return [address, p_code]
# #
# # print(type(get_correct_address_postal_code()))
# l_values = {'🅰', '🅱', '🆎', '🆑', '🅾', '🆘', '🅿', '🆖', '🆗',
#             '🔟', '🔞', '💤', '⁉', '❗', '❓', '❎', 'Ⓜ', '✳',
#             '💯', '❌', '⭕', '🚾'}
#
# d_values = {"A": "🅰", "B" : "🅱", 'AB': "🆎", 'CL': "🆑", 'o': "🅾",
#             'SOS': "🆘", "P": "🅿", "NG": "🆖", "OK": "🆗", "10": "🔟",
#             "18": "🔞", "zzz": "💤", "!?": "⁉", "!": "❗", "?": "❓",
#             "x": "❎", "M": "Ⓜ", "*": "✳", "100": "💯", "X": "❌",
#             "O": "⭕", "WC": "🚾"}
# print("Robot Verification:")
# while True:
#     t_1 = tuple(l_values)
#     print("".join(t_1[0:4]))
#     s_final = ""
#     for ch in "".join(t_1[0:4]):
#         for k, v in d_values.items():
#             if ch == v:
#                 s_final += k
#         # print(ch)
#     if input(str("Write what do you see:")) == s_final:
#         print("You are not a Robot.")
#         break
# # print(s_final)
def get_correct_mail() -> str:
    """
    email prefix formats
    Allowed characters: letters (a-z), numbers, underscores, periods, points and dashes.
    An underscore, period, or dash must be followed by one or more letter or number.

    email domain formats
    Allowed characters: letters, numbers, dashes.
#     The last portion of the domain must be at least two characters, for example: .com, .org, .cc
#     :return:
#     """
#     while True:
#         email = input(str("Enter your email:"))
#         condition = True
#         if "@" not in email:
#             condition = False
#         for ch in email[0:email.find("@")-1]:
#             if ch in '!"#$%&\'*+,/:;<=>?@[\\]^`{|}~':
#                 condition = False
#         if email[email.find("@") - 1] in string.punctuation:
#             condition = False
#         if email[0] in string.punctuation:
#             condition = False
#         for ch in email[email.find("@") + 1:email.rfind(".")]:
#             if ch in '!"#$%&\'()_*+,./:;<=>?@[\\]^`{|}~':
#                 condition = False
#         for ch in email[email.rfind(".") + 1::]:
#             if ch in string.punctuation:
#                 condition = False
#         if len(email[email.rfind(".") + 1::]) < 2:
#             condition = False
#         if condition:
#             break
#         else:
#             print(f"Error: Email is incorrect")
#     return email
# print(get_correct_mail())

#
# with open("Log_in_data.csv", "r") as fr:
#     reader = csv.reader(fr)
#     for row in reader:
#         print(row)
#
#
# def log_in():
#     """
#     If You enter your data correctly u will have access to your
#     information and u will have the right to move them
#     :return:
#     """
#     name = input(str("enter your username or your email:"))
#     password = input(str("enter your password:"))
#     # row = 0
#     access = False
#     if "@" in name:
#         with open("Log_in_data.csv", "r") as fr:
#             reader = csv.reader(fr)
#             for row in reader:
#                 if row[2] == name and row[4] == password:
#                     print("Log in successful")
#                 # row += 1
#             else:
#                 print("Error: you are not singed in")
#     else:
#         with open("Log_in_data.csv", "r") as fr:
#             reader = csv.reader(fr)
#             for row in reader:
#                 if row[3] == name and row[4] == password:
#                     print("Log in successful")
#                 # row += 1
#             else:
#                 print("Error: you are not singed in")
#
# log_in()

# print(verify_robot())


import csv
#
#
# with open("Log_in_data.csv", "r") as fr:
#     reader = csv.reader(fr)
#     for row in reader:
#         print(row)


# def log_in() -> int:
#     """
#     If You enter your data correctly this function
#     will return the row where your data is
#     :return:
#     """
#     name = input(str("enter your username or your email:"))
#     password = input(str("enter your password:"))
#     row_final = 0
#     if "@" in name:
#         with open("Log_in_data.csv", "r") as fr:
#             reader = csv.reader(fr)
#             for row in reader:
#                 if row[2] == name and row[4] == password:
#                     print("Log in successful")
#                     break
#                 row_final += 1
#             else:
#                 print("Error: you are not singed in")
#                 row_final = -1
#     else:
#         with open("Log_in_data.csv", "r") as fr:
#             reader = csv.reader(fr)
#             for row in reader:
#                 if row[3] == name and row[4] == password:
#                     print("Log in successful")
#                     break
#                 row_final += 1
#             else:
#                 print("Error: you are not singed in")
#                 row_final = -1
#     return row_final

# import pandas as pd

#
# def show_info(row: int):
#     """
#     It reads a certain row
#     :param row:
#     :return:
#     """
#     with open("Log_in_data.csv", "r") as fr:
#         reader = csv.reader(fr)
# #         reader = list(reader)
# #         print(reader[row])
# #         return reader[row]
#
#
# # l_1 = show_info(2)
# # def modify_data():
# #     """
# #     It modifies data from csv file
# #     :return:
# #     """
# #     lines = list()
# #     remove = [2]
# #     new_data = ['Mihai', 'Popescu', 'Mihai.Popescu@yahoo.com', 'Mihaita', 'Mihai2432', 32, "Male",
# #                 ['5, Ion Ghica Street, Sector 3', '030044']]
# #
# #     with open('Log_in_data.csv', 'r') as read_file:
# #         reader = csv.reader(read_file)
# #         for row_number, row in enumerate(reader, start=0):
# #             if row_number not in remove:
# #                 lines.append(row)
# #             else:
# #                 if len(row) == 5:
# #                     lines.append(row + [32, "Male", ['5, Ion Ghica Street, Sector 3', '030044']])
# #
# #     with open('Log_in_data.csv', 'w', newline="") as write_file:
# #         writer = csv.writer(write_file)
# #         writer.writerows(lines)
# #
# # modify_data()
#
# import csv
# import string
#
#
# def get_answer() -> bool:
#     """
#     functions gets an answer which decides if
#     some actions will be done
#     :return:
#     """
#     x = input(str("press y for yes or n for no:"))
#     while x != "y" and x != "n":
#         print("you have entered a wrong answer")
#         x = input(str("press y for yes or n for no:"))
#     return x == "y"
#
#
# def get_correct_name() -> str:
#     """
#     If the name doesn't have unknown characters it returns the name
#     :return:
#     """
#     while True:
#         name = input(str("Enter your name:"))
#         x = 0
#         for ch in name:
#             if ch in string.punctuation + string.digits:
#                 x = 1
#         if x == 0:
#             break
#         else:
#             print(f"Error: name cannot contain any of these characters {string.punctuation + string.digits}")
#     return name
#
#
# def get_correct_first_name() -> str:
#     """
#     If the first_name doesn't have unknown characters it returns the name
#     :return:
#     """
#     while True:
#         first_name = input(str("Enter your first_name:"))
#         x = 0
#         for ch in first_name:
#             if ch in string.punctuation + string.digits:
#                 x = 1
#         if x == 0:
#             break
#         else:
#             print(f"Error: first name cannot contain any of these characters {string.punctuation + string.digits}")
#     return first_name
#
#
# def get_correct_mail() -> str:
#     """
#     email prefix formats
#     Allowed characters: letters (a-z), numbers, underscores, periods, points and dashes.
#     An underscore, period, or dash must be followed by one or more letter or number.
#
#     email domain formats
#     Allowed characters: letters, numbers, dashes.
#     The last portion of the domain must be at least two characters, for example: .com, .org, .cc
#     :return:
#     """
#     while True:
#         email = input(str("Enter your email:"))
#         condition = True
#         if "@" not in email:
#             condition = False
#         for ch in email[0:email.find("@")-1]:
#             if ch in '!"#$%&\'*+,/:;<=>?@[\\]^`{|}~':
#                 condition = False
#         if email[email.find("@") - 1] in string.punctuation:
#             condition = False
#         if email[0] in string.punctuation:
#             condition = False
#         for ch in email[email.find("@") + 1:email.rfind(".")]:
#             if ch in '!"#$%&\'()_*+,./:;<=>?@[\\]^`{|}~':
#                 condition = False
#         for ch in email[email.rfind(".") + 1::]:
#             if ch in string.punctuation:
#                 condition = False
#         if len(email[email.rfind(".") + 1::]) < 2:
#             condition = False
#         if condition:
#             break
#         else:
#             print(f"Error: Email is incorrect")
#     return email
#
#
# def get_correct_username() -> str:
#     """
#     If the username doesn't have unknown characters it returns the name
#     :return:
#     """
#     while True:
#         username = input(str("Enter your username:"))
#         x = 0
#         for ch in username:
#             if ch in '!"#$%&\'*()+,/:;<=>?@[\\]^`{|}~':
#                 x = 1
#         if x == 0:
#             break
#         else:
#             print("Error: username cannot contain any of these characters !\"#$%&\'*+,/:;<=>?@[\\]^`{|}~")
#     return username
#
#
# def get_correct_password() -> str:
#     """
#     You enter a password with at least 8 characters and if
#     you enter your password correct again it returns the password
#     conditions:
#     Not valid: must contain at least 8 characters.
#     Not valid: contains more than two repeated characters.
#     :return:
#     """
#     while True:
#         password = input(str("Enter your password"))
#         condition = True
#         if len(password) < 8:
#             condition = False
#         for ch in password:
#             if password.count(ch) > 2:
#                 condition = False
#         ch_letter = 0
#         for ch in password:
#             if ch in string.ascii_letters:
#                 ch_letter += 1
#         if ch_letter <= 4 or ch_letter == len(password):
#             condition = False
#         if condition:
#             while password != input(str("Enter your password confirmation")):
#                 print("Error: password confirmation is wrong")
#             break
#         else:
#             print("Error: Your password is not strong enough. Try again!")
#     return password
#
#
# def get_correct_age() -> int:
#     """
#     This function ensures that your age is written
#     in digits and it s above 16
#     :return:
#     """
#     while True:
#         try:
#             age = int(input("What is your Age?:"))
#         except ValueError:
#             print(f'Your age must be written with')
#         else:
#             if age > 16:
#                 break
#             else:
#                 print("You are too yong for this app")
#     return age
#
#
# def get_correct_gender() -> str:
#     """
#
#     :return:
#     """
#     l_genders = ['Female', 'Male', 'Intersex', 'Trans', 'Non-Conforming', 'Eunuch',
#                  "trans-parent", 'Personal', "Gender bender"]
#     print(f'Chose one gender from{l_genders}')
#     gender = input(str("What is your gender?"))
#
#     while gender not in l_genders:
#         print("Error: incorrect gender")
#     return gender
#
#
# def get_correct_address_postal_code() -> list:
#     """
#     returns a list with the address and postal code
#     :return:
#     """
#     address = input(str("Enter your home address:"))
#     while True:
#         p_code = input(str("Enter your postal code:"))
#         condition = True
#         digits = 0
#         if len(p_code) != 6:
#             condition = False
#             print('Error: Postal code has 6 characters')
#         else:
#             for ch in p_code:
#                 if ch in string.digits:
#                     digits += 1
#         if digits != 6:
#             condition = False
#             print("Error: Postal contains just digits")
#         if condition:
#             break
#     return [address, p_code]
#
#
# def verify_robot() -> bool:
#     """
#     It verifies if you are a robot
#     :return:
#     """
#     l_values = {'🅰', '🅱', '🆎', '🆑', '🅾', '🆘', '🅿', '🆖', '🆗',
#                 '🔟', '🔞', '💤', '⁉', '❗', '❓', '❎', 'Ⓜ', '✳',
#                 '💯', '❌', '⭕', '🚾'}
#
#     d_values = {"A": "🅰", "B": "🅱", 'AB': "🆎", 'CL': "🆑", 'o': "🅾",
#                 'SOS': "🆘", "P": "🅿", "NG": "🆖", "OK": "🆗", "10": "🔟",
#                 "18": "🔞", "zzz": "💤", "!?": "⁉", "!": "❗", "?": "❓",
#                 "x": "❎", "M": "Ⓜ", "*": "✳", "100": "💯", "X": "❌",
#                 "O": "⭕", "WC": "🚾"}
#     while True:
#         t_1 = tuple(l_values)
#         print("".join(t_1[0:4]))
#         s_final = ""
#         for ch in "".join(t_1[0:4]):
#             for k, v in d_values.items():
#                 if ch == v:
#                     s_final += k
#             # print(ch)
#         if input(str("Write what do you see:")) == s_final:
#             print("You are not a Robot.")
#             bol = True
#             break
#         else:
#             print("Error: You have entered the wrong characters")
#     return bol
#
#
# def sign_up():
#     """
#     This will add your information in a csv file
#     :return:
#     """
#     l_info = [get_correct_name(), get_correct_first_name(), get_correct_mail(), get_correct_username(),
#               get_correct_password()]
#     if verify_robot():
#
#         print("Do you want to complete all the information?(you can complete them later")
#         if get_answer():
#             l_info.append(get_correct_age())
#             l_info.append(get_correct_gender())
#             l_info.append(get_correct_address_postal_code())
#     with open("Log_in_data.csv", "a+", newline="") as fw:
#         writer = csv.writer(fw, delimiter=';')
#         writer.writerow(l_info)
#
#
# def log_in() -> int:
#     """
#     If You enter your data correctly this function
#     will return the row where your data is
#     :return:
#     """
#     name = input(str("enter your username or your email:"))
#     password = input(str("enter your password:"))
#     row_final = 0
#     if "@" in name:
#         with open("Log_in_data.csv", "r") as fr:
#             reader = csv.reader(fr)
#             for row in reader:
#                 if row[2] == name and row[4] == password:
#                     print("Log in successful")
#                     break
#                 row_final += 1
#             else:
#                 print("Error: you are not singed in")
#                 row_final = -1
#     else:
#         with open("Log_in_data.csv", "r") as fr:
#             reader = csv.reader(fr)
#             for row in reader:
#                 if row[3] == name and row[4] == password:
#                     print("Log in successful")
#                     break
#                 row_final += 1
#             else:
#                 print("Error: you are not singed in")
#                 row_final = -1
#     return row_final
#
#
# def show_info(row: int):
#     """
#     It reads a certain row
#     :param row:
#     :return:
#     """
#     with open("Log_in_data.csv", "r") as fr:
#         reader = csv.reader(fr)
#         reader = list(reader)
#         print(reader[row])
#
#
# def modify_data(modied_row: int):
#     """
#     It modifies data from csv file
#     :return:
#     """
#     lines = list()
#     remove = [modied_row]
#     new_data = ['Mihai', 'Popescu', 'Mihai.Popescu@yahoo.com', 'Mihaita', 'Mihai2432', 32, "Male",
#                 ['5, Ion Ghica Street, Sector 3', '030044']]
#
#     with open('Log_in_data.csv', 'r') as read_file:
#         reader = csv.reader(read_file)
#         for row_number, row in enumerate(reader, start=0):
#             if row_number not in remove:
#                 lines.append(row)
#             else:
#                 if len(row) == 5:
#                     print("complete all information about you")
#                     lines.append(row + [get_correct_age(), get_correct_gender(), get_correct_address_postal_code()])
#                 else:
#                     while True:
#                         print("What is the information you want to change?")
#                         answer_3 = input(str("Choose between:Name, First Name, Email, Username, "
#                                              "password, age, gender, address_postal_code, exit"))
#                         if answer_3 == "Name":
#                             row = [get_correct_name()] + row[1::]
#                         if answer_3 == "First Name":
#                             row = row[0:1] + [get_correct_first_name()] + row[2::]
#                         if answer_3 == "Email":
#                             row = row[0:2] + [get_correct_mail()] + row[3::]
#                         if answer_3 == "Username":
#                             row = row[0:3] + [get_correct_username()] + row[4::]
#                         if answer_3 == "password":
#                             row = row[0:4] + [get_correct_password()] + row[5::]
#                         if answer_3 == "age":
#                             row = row[0:5] + [get_correct_age()] + row[6::]
#                         if answer_3 == "gender":
#                             row = row[0:6] + [get_correct_gender()] + row[7::]
#                         if answer_3 == "address_postal_code":
#                             row = row[0:7] + [get_correct_address_postal_code()]
#                         if answer_3 == "exit":
#                             break
#                     lines.append(row)
#     print(lines)
#     with open('Log_in_data.csv', 'w', newline="") as write_file:
#         writer = csv.writer(write_file)
#         writer.writerows(lines)
#
#
# modify_data(2)

with open("Log_in_data.csv", "r") as fr:
        reader = csv.reader(fr)
        for item in reader:
            print(len(item))