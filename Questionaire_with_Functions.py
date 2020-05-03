def main():

        Question1=input("Does your child have difficulty talking? (yes/ no) ").lower()
        if Question1 == "yes" :
            print('Register for a speech therapy session with the logopedic')
        else:
             if Question1 == "no" :
                 print('Do not register for a speech therapy session with the logopedic')

        Question2 = input("Does your child have difficulty walking? (yes/ no) ").lower()
        if Question2 == "yes":
            print('Register for a physiotherapy session')
        else:
            if Question2 == "no":
                print('Do not register for a physiotherapy session')

        Question3=input("Does your child have developmental challenges? (yes/ no) ").lower()
        if Question3 == "yes" :
            print('Register for a child psychology session')
        else:
            if Question3 == "no":
                print('Do not register for a child psychology session')

        print('Thank you. Now your appointments can be done.')


main()