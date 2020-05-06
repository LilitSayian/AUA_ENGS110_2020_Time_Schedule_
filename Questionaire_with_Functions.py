def answer_question1():
    while True:
        Question1 = input("Does your child have difficulty talking? (yes/ no) ").lower()
        if Question1 == "yes":
            print('Register for a speech therapy session with the logopedic')
            break
        else:
            if Question1 == "no":
                print('Do not register for a speech therapy session with the logopedic')
                break


def answer_question2():
    while True:
        Question2 = input("Does your child have difficulty walking? (yes/ no) ").lower()
        if Question2 == "yes":
            print('Register for a physiotherapy session')
            break
        else:
            if Question2 == "no":
                print('Do not register for a physiotherapy session')
                break


def answer_question3():
    while True:
        Question3 = input("Does your child have developmental challenges? (yes/ no) ").lower()
        if Question3 == "yes":
            print('Register for a child psychology session')
            break
        else:
            if Question3 == "no":
                print('Do not register for a child psychology session')
                break


def main():

    answer_question1()
    answer_question2()
    answer_question3()

    print('Thank you. Now your appointments can be done.')


main()