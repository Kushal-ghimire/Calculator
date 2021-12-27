
import add_work
import sub_work
import mul_work
import div_work


print("Select Operation:")
print("1.ADDITION:")
print("2.SUBTRACTION:")
print("3.MULTIPLICATION:")
print("4.DIVISION:")

while True :

     choice=input("Enter your choice(1/2/3/4):")
     if choice in ('1','2','3','4'):
         a=float(input("Enter First Number:"))
         b=float(input("Enter Second Number:"))

         if choice == '1' :
             print(a,"+",b,"=",add(a,b))
         elif choice == '2' :
             print(a,"-",b,"=",sub(a,b))
         elif choice == '3' :
             print(a,"*",b,'=',mul(a,b))
         elif choice == '4' :
             print(a,"/",b,'=',div(a,b))


         next_calculation = input("Let's do next calculation?(yes/No) :")
         if next_calculation == "No" :
            break
         else:
            print("Invalid input")

    

        
        
             
