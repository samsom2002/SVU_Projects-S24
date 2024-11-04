#Making Functions for better design
#Calcultor Function
def calc():
    #Input number of hours
    NH=float(input("Enter an Number of Hours: "))
    #Input Money for 1 Hour of work
    MH=float(input("Enter an Money per hour: "))
    #Outpt Money
    OM = 0
    #Chech if number of hours is bigger than 40 and print result
    if NH < 0 or MH < 0:
        print("Please Input Postive Numbers")
        calc()
    elif NH > 40:
        #Doing Math
        X = NH - 40
        Y = X * 1.5
        Z = 40 + Y
        OM = Z * MH
        print(OM)
    #checking if number of hours and money per hour are postive numbers
    elif NH <= 40:
       #Doing Math
        OM= MH*NH
        print(OM)
    #calculating for user error
    else: 
         print("Something went wrong")
         calc()
#Main Menu Function 
def Main():
    #start program
    user_input = 0
    #keep trying until user do what we want
    while user_input == 0: 
        print("To Start program Enter 1")
        print("To End program Enter -1")
       #Getting A number from user
        while True :
            #If user didnt input number keep trying
            try:
                user_input=int(input("Enter a Number: "))
                break
            #If user didnt input number keep trying
            except ValueError: 
                print("Please input a number.")

        #start program if user input = 1
        if user_input == 1 :
            calc()
        #Exit program if user input = -1
        elif user_input == -1:
            exit(1)
        #calculating for user error
        else: 
            user_input = 0
            print("Try Again Please")
            Main()

#start the program
Main()