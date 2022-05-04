# Import math for compound interest formula 
import math 

#Create open statment for user to  to select "innvestment" or "bond"
calculator_type = str(input("\nChoose either 'investment' or 'bond' from the menu below to proceed:\n \ninvestment \t - To calculate the amount of interest you'll earn on interest. \nbond \t \t - To calculate the amount you'll have to pay on a home loan\nEnter here: "))

# Create an if statment for user to select investment or bond option
# Create money variable to determine initial investment amount
# Create interest_rate variable to determine interest earned then divide that variable by 100 to convert it to decimal for interest formulas and make decimal = r. 
# Create time variable to determine the length of the investment
# Create interest variable to prompt user to select "simple" or "compound" interest

if calculator_type in ["investment","Investment","INVESTMENT"]:
    money = float(input("How much money are you depositing into the investment account: R"))
    interest_rate = float(input("Please enter the percentage (as a number) of your interest rate: "))
    r = interest_rate / 100
    time = float(input("How many years are you planning on investing for: "))
    interest = input("Would you be earning simple or compound interest: ")
    
    # Create if else statment based on users input to select either simple or compound interest
    # If "simple" is selected then run the simple interest formula with variables from above and print it.
    # If "compound" is selected then run the compound interest formula with variables from above and print it.
    # Else print a fail statment.
   
    if interest in ["simple", "Simple","SIMPLE","simple interest","Simple Interest","SIMPLE INTEREST"]:
        a = money*(1 + r * time)
        print("Your investment will total R{}".format(a))
    elif interest in ["compound","Compound","COMPOUND","Compound Interest","compound interest","COMPOUND INTEREST"] :
        a = money * (math.pow((1+r),time))
        print("Your investment will total R{}".format(a))
    else :
        print("Failed to understand instructons, please try again.")    

# Create an if statment for user to select bond option
# Create variable called house_value to determine the value of the house
# Create interest_rate variable too determine the interest rate of the user then divide it by 100 to get decimal value and then divide it by 12 to convert it to monthly interest  
# Create variable to determine how long the user plans to take paying back the loan
# Calculate the bond repayment using the bond repayment formula 
# Print the final payment amount
 
if calculator_type in ["Bond","bond","BOND"]:
    house_value = float(input("What is the current value of your house? R"))
    interest_rate = float(input("Please enter the percentage (as a number) of your interest rate: "))
    interest_decimal = interest_rate/100
    i = interest_decimal/12
    repayment = float(input("Over how many months do you plan on repaying your bond: "))
    x = (i * house_value) / (1 - (1 + i)**(-repayment))
    print("Your monthly bond repayent will total R{}".format(x))
