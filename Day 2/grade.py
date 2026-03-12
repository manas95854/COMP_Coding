#write a program if percentage is greater than 90 then print grade A, if percentage is greater than 80 and less than or equal to 90 then print grade B, if percentage is greater than 70 and less than or equal to 80 then print grade C, if percentage is greater than 60 and less than or equal to 70 then print grade D, if percentage is less than or equal to 60 then print grade F.

percentage = float(input("Enter percentage: ")) 

if percentage > 90:
    print("Grade A")

elif percentage > 80 and percentage <= 90:
    print("Grade B")

elif percentage > 70 and percentage <= 80:  
    print("Grade C")

elif percentage > 60 and percentage <= 70:
    print("Grade D")

else:    
    print("Grade F")    