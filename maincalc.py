import add_work
import sub_work
import mul_work
import div_work

 print("Select Operation:")
 print("1.ADDITION:")
 print("2.SUBTRACTION:")
 print("3.MULTIPLICATION:")
 print("4.DIVISION:")

 while(True):
     choice=input("Enter your choice(1/2/3/4):")
     if choice in ('1','2','3','4'):
         num1=float(input("Enter First Number:"))
         num2=float(input("Enter Second Number:"))

         if choice == '1' :
             print(num1,'+',num2,"=",add_work)
        elif choice == '2' :
            print(num1,'-',num2,"=",sub_work)
        elif choice == '3' :
            print(num1,"*",num2,'=',mul_work)
        elif choice == '4' :
            print(num1,'/',num2,'=',div_work)


        next_calculation = input("Let's do next calculation?(yes/No) :")
        if next_calculation == "No" :
            break
        else:
            print("Invalid input")

    

        
        
             
