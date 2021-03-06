import re
import json
import os


def openuserinformation(name, surname, birthMonth, birthDay, birthYear, condition):
    if not os.path.exists("user_information.json"):
        with open("user_information.json", "w+") as file:
            initial_dict = {
                "user_information": []
            }
            json.dump(initial_dict, file) #, indent=True

    with open("user_information.json", "r") as file:
        data_json = json.load(file)
    user_information = {'name': name,
                        'surname': surname,
                        'birthMonth': birthMonth,
                        'birthDay': birthDay,
                        'birthYear': birthYear,
                        'condition': condition
                        }
    data_json["user_information"].append(user_information)
    with open("user_information.json", "w+") as f:
        json.dump(data_json, f, indent=True)
    return user_information


def name():
    while True:
        name = input("Please Enter Name: ")
        if not re.match("^[a-z]*$", name):
            print("Error! Only letters a-z allowed!")
        else:
            return name


def surname():
    while True:
        surname = input("Please Enter Surname: ")
        if not re.match("^[a-z]*$", surname):
            print("Error! Only letters a-z allowed!")
        else:
            return surname


def birthMonth():
    while True:
        try:
            birthMonth = int(input("Enter your birth month :"))
            if 0 < birthMonth <= 12:
                return birthMonth
        except:
            print("That's not a valid option!")


def birthDay():
    while True:
        try:
            birthday = int(input("Enter your birth day :"))
            if 0 < birthday <= 31:
                return birthday
        except:
            print("That's not a valid option!")


def birthYear():
    while True:
        try:
            birthYear = input("Enter the year you were born (4 digits):")
            birthYear=int(birthYear)
            if 1919 < int(birthYear) <= 2020:
                return birthYear
        except:
            print("That's not a valid option!")


def condition():
    while True:
        try:
            condition = input("Please Enter the Condition from 1-5: ")
            condition= int(condition)
            if 0 < condition <= 5:
                return condition
        except:
            print("That's not a valid option!")


def data():
    # info = {}
    with open("read_user_info.json") as file_data:
        info = json.load(file_data)
        return info


def displayCurrentDicValue(currentValue, step=0):
    if (type(currentValue) == list):
        for item in currentValue:
            displayCurrentDicValue(item, step+1)
            print(", ", end="")
        print("\n", end="")

    elif (type(currentValue) == dict):
        for key in currentValue:
            print("\n", "\t"*step, key, ": ", end="")
            displayCurrentDicValue(currentValue[key], step+1)

    else:
        print(currentValue, end="")


def main():
    user_name = name()
    user_surname = surname()
    birth_month = birthMonth()
    day = birthDay()
    year = birthYear()
    _condition = condition()
    openuserinformation(user_name, user_surname, birth_month, day, year, _condition)
    print("\nThank you for registering. Here is a list of our health specialists.")
    data()
    specialists_info = data()
    displayCurrentDicValue(specialists_info)
    print("\nPlease answer the upcoming questions to make future appointments. Thank you.")


main()