import calendar

def decide_Day(possible_days, used_days, available_days) :
    for item in possible_days.keys():
        if item not in used_days:
            available_days.append(item)

def chooseDay(used_days, available_days):
    while True:
        user_day = input("Please choose a suitable day for you, Saturday or Sunday").lower()
        if (user_day in used_days):
            print("Sorry that day is not available at this moment")
        else:
            if (user_day in available_days):
                print("The day is confirmed.")
                break

def decide_Time(possible_options,used_options,available_options) :
    for item in possible_options.keys():
        if item not in used_options:
            available_options.append(item)

def chooseTime(used_options,available_options,possible_options,not_available_options):
    while True:
        user_time = int(input("Please choose a suitable time for you, each appointment takes an hour."))
        if (user_time in used_options):
            print("Sorry the time is taken")
        if (user_time in available_options):
            print(possible_options[str(user_time)])
            used_options.append(user_time)
            break
        if (user_time in not_available_options):
            print(possible_options[str(user_time)])

def main():

    year = 2020
    month = int(input("Enter month in numbers: "))
    print(calendar.month(year, month))

    print("The Logopedic only works on Sundays and Saturdays from 10-4")

    not_available_options = [1, 4]
    used_options = [3, 2]
    available_options = [10, 11, 12]
    used_days = ['sunday']
    available_days = ['saturday','sunday']

    possible_days = {
        "Saturday" : "Thank you. Your appointment is made",
        "Sunday" : "Thank you. Your appointment is made",
    }

    decide_Day(possible_days, used_days, available_days)
    chooseDay(used_days, available_days)
    
    possible_options = {
        "10": "Thank you. Your appointment is made.",
        "11": "Thank you. Your appointment is made.",
        "12": "Thank you. Your appointment is made.",
        "2": "Thank you. Your appointment is made.",
        "3": "Thank you. Your appointment is made.",
        "1": "From 1-2 there is lunch break, please choose another suitable time.",
        "4": "Sorry, by that time the appointments would have ended. Try another suitable time."
    }

    decide_Time(possible_options,used_options,available_options)
    chooseTime(used_options,available_options,possible_options,not_available_options)


main()

