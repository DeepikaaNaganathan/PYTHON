#sales program
#listing the values
months_per_year = 12  
sales_per_month = []  
salary_per_month = []
#printing the max of salary
max_salary = 25000    
no_of_sales = 0
phones_sold = 0
#using for getting each month's sold phones
for sale in range(months_per_year):    
    base_salary = 10000
    print("Enter the phone saled in this month : ",sale+1)
    phones_sold = int(input())
    print("Sales in this month : ",phones_sold)
    sales_per_month.append(phones_sold)
    base_salary += 1000
    #if the phones sold is greater than 5 then for each phone the incentive amount is 100
    if phones_sold > 5:
    #if the phones sold is greater than 10 then for each phone the incentive amount is 200    
        base_salary += phones_sold * 100
    elif phones_sold >= 10:
       base_salary += phones_sold * 200
       
    monthly_salary = base_salary
    #if monthly salary is greater than max salary then print max salary
    if monthly_salary>max_salary:          
        salary_per_month.append(max_salary)    
    else:                            
        salary_per_month.append(monthly_salary)  
#using for printing each month salary
for salary in range(months_per_year):  
    print("Salary for month ", salary+1, " : Rs. ", salary_per_month[salary])  
#calculating Average salary
sum_of_monthly_salaries = sum(salary_per_month)                        
average_of_monthly_per_year = sum_of_monthly_salaries / months_per_year
print("Average salary per year : Rs. ", average_of_monthly_per_year)



#output
Enter the phone saled in this month :  1
1
Sales in this month :  1
Enter the phone saled in this month :  2
2
Sales in this month :  2
Enter the phone saled in this month :  3
3
Sales in this month :  3
Enter the phone saled in this month :  4
4
Sales in this month :  4
Enter the phone saled in this month :  5
5
Sales in this month :  5
Enter the phone saled in this month :  6
6
Sales in this month :  6
Enter the phone saled in this month :  7
7
Sales in this month :  7
Enter the phone saled in this month :  8
8
Sales in this month :  8
Enter the phone saled in this month :  9
9
Sales in this month :  9
Enter the phone saled in this month :  10
10
Sales in this month :  10
Enter the phone saled in this month :  11
11
Sales in this month :  11
Enter the phone saled in this month :  12
12
Sales in this month :  12
Salary for month  1  : Rs.  11000
Salary for month  2  : Rs.  11000
Salary for month  3  : Rs.  11000
Salary for month  4  : Rs.  11000
Salary for month  5  : Rs.  11000
Salary for month  6  : Rs.  11600
Salary for month  7  : Rs.  11700
Salary for month  8  : Rs.  11800
Salary for month  9  : Rs.  11900
Salary for month  10  : Rs.  12000
Salary for month  11  : Rs.  12100
Salary for month  12  : Rs.  12200
Average salary per year : Rs.  11525.0
