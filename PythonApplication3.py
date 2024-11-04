
from ast import Global

#Definig Varibles to None Because 0 is A number and i dont want to start comparing just yet.
Bigger1 = None
Bigger2 = None
Bigger3 = None

#Definig function so i dont repeat code too many times.
def big(num):
   #making local varibles global so thet can be used outside function
   global Bigger1,Bigger2,Bigger3 
    #comparing the number i input to the first number and if there isnt a number store the first number i input in it.
   if Bigger1 == None or num > Bigger1:
        Bigger3 = Bigger2
        Bigger2 = Bigger1
        Bigger1 = num
   #comparing the number i input to the secound number and if there isnt a number store the first number i input in it.
   elif Bigger2 == None or num > Bigger2:
        Bigger3 = Bigger2
        Bigger2 = num
   #comparing the number i input to the third number and if there isnt a number store the first number i input in it.
   elif Bigger3 == None or num> Bigger3:
        Bigger3 = num

#ask for input 10 times and call the main function
for i in range(10):
    try:
        num = float(input("Enter A Number:"))
        big(num)
        
    except ValueError:
        print("not a number. try again")
        break
        
     
   
              


# printing results.
print("1st : ", Bigger1)
print("2nd : ", Bigger2)
print("3rd : ", Bigger3)

















