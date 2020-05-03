import json

def main():
    name = input(" Please Enter Name: ")
    surname = input(" Please Enter Surname: ")
    birthMonth = int(input("Enter your birth month (2 digits):"))
    birthDay = int(input("Enter the day of your birth:"))
    birthYear = int(input("Enter the year you were born (4 digits):"))
    condition = int(input(" Please Enter the Condition from 1-5: "))

    print("Thank you for registering.")

    user_information = {'name': name,
                        'surname': surname,
                        'birthMonth': birthMonth,
                        'birthDay': birthDay,
                        'birthYear': birthYear,
                        'condition': condition
                        }
    json_dump = json.dumps(user_information, indent=2)

    print(json_dump)
    file = open("user_information.json", 'w+')
    file.write(json_dump)
    file.close()
    with open("user_information.json", "r") as f:
        f.close()


main()
