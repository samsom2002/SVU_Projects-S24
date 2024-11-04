#defining Counters for right and wrong answers
i=0
j=0



# Main menu Function 
def Main(i,j):
    
        user_input0 = 0
       
   
    #start program
        print("To Play Enter Y")
        print("To End Game Enter N")

        #get user input
        user_input0=str(input("Enter a letter: "))
        
        #keep trying until user do what we want
        if user_input0 == "Y" or user_input0 == "y" :
            Learn(i,j)
        elif user_input0 == "N" or user_input0 == "n" :
            exit(1)
        else:
            print("there was an error please try again")
            Main(i,j)
                
                
               
        
        
      
def Learn(i,j):  
    
    
    # import random libary
    import random
    
# pick a random value from the list and saving them to variables x and y
    list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    x = int(random.choice(list1))
    y = int(random.choice(list1))

    # printing the numbers
    print("First Number is " + str(x))
    print("secound Number is " + str(y))
    
     #keep trying until user do what we want
    while True:
               try:
                    user_input =int(input("Enter The multiplication of the numbers: "))
                    if user_input>0 :
                         
                         break
                    else:
                        print("Please instert postive numbers only")
              # if input not number make the user try again until he puts a number
               except ValueError: 

                    print("Please input a number.")

    
    #adding to the counters after answering 
    if user_input == x*y:
        print ("This is correct")
        i=i+1
        
    elif user_input != x*y:
        print ("This is Not correct")
        j=j+1
    #else statment not necessery just for safty reasons    
    else:
        Main(i,j)
    
    
    
    print("Number of Correct Answers is " + str(i) + ", Number of Wrong Answers is " + str(j))

    Main(i,j)    
    
    return i,j




Main(i,j)
