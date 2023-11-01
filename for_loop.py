# for i in (1,2,3,4,5,6,7,8,9):
#     print(i)
    
# d=[]
# for i in range(1,20):
#     if i%2 ==0:
#         d.append(i)
#         # print(d)
# print(d)
# print(len(d))

good_guess=10
number_of_try=0
while number_of_try <=2:
    number_of_try+=1
    print(number_of_try)
    try:
        choice = int(input("Please enter a number between 1 and 20:"))
        if choice not in range(1,21):
            print("Invalid entry")
        elif choice == good_guess:
            print("Good job you win!!!")
            break
        elif choice < good_guess:
            print("Sorry your number is lower")
        elif choice > good_guess:
            print("Sorry your number is bigger")
            
    except:
        print("Something went wrong please try again")
        # continue
        
if number_of_try == 3:
    print("Out of attempts. The correct number was")