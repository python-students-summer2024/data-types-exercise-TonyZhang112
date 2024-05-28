"""
Practice problems to get the hang of converting among data types.
In this case, we focus on converting numeric data types to strings and vice-versa.
"""


def calculate_profit():
    """
    Imagine this scenario: a company has determined that its annual profit is typically 23 percent of total sales.
    Complete this function so that it asks the user to enter in the projected amount of total sales and then displays the profit that will be made from that amount.
    You can assume the user will enter only numeric characters, e.g. "3000", not "$3,000.00"
    The output should match the format of the following examples: "Profit: $690.00" for sales of $3,000, or "Profit: $2,300.00" for sales of $10,000, etc.
    """
    total_sales = float(input('what is your amount of total sales? '))
    annual_profit = total_sales * 0.23
    x = format(annual_profit, ',.2f')
    print('Profit: $' + x+'\n')


def calculate_quotient_and_remainder():
    """
    Complete this function so that it asks the user to input two integers.
    You program should calculate and output the quotient and remainder when the first number is divided by the second.
    Here's an example run of the function:
      Enter number #1: 5
      Enter number #2: 2
      2 goes into 5 a total of 2 times with a remainder of 1
    """
    number1 = int(input("What is your first number? "))
    number2 = int(input('What is your second number? '))
    quotient = number1 // number2
    remainder = number1 % number2
    print(str(number2) + ' goes into ' + str(number1) + " a total of "+ str(quotient)+ ' times with a remainder of '+ str(remainder)+'\n')


def calculate_miles_per_gallon():
    """
    A car's Miles Per Gallon (MPG) can be calculated using the following formula:
      MPG = Miles driven / Gallons of Gas Used
    Complete this function so that it asks the user for the number of miles driven and the gallons of gas used.
    It should calculate the car's MPG and display the result in the format indicated in this example run of the program:

      Miles driven: 100
      Gas used (gallons): 25
      Miles per gallon: 2.2
    """
    print('This is a Miles Per Gallon (MPG) calculator.')
    miles_driven= int(input("How many miles have you driven? "))
    gas_used= int(input('How many gallons of gas you used? '))
    mpg=int(miles_driven) / int(gas_used)
    #print('Miles driven: '+ str(miles_driven) +'\nGas used (gallon): '+ str(gas_used) + '\nMiles per gallon: '+ str(mpg)+'\n')
    x = format(miles_driven, '>25,.2f')
    y = format(gas_used, '>20,.2f')
    z = format(mpg, '>21,.2f')
    a = format('Miles driven:', '<10')
    b = format('Gas used (gallon):', '<10')
    c = format('Miles per gallon:', '<10')

    c1="{0}{1}".format(a,x)
    c2="{0}{1}".format(b,y)
    c3="{0}{1}".format(c,z)
    
    print(c1)
    print(c2)
    print(c3+'\n')


def align_text():
    """
    Complete this function such that it asks the user to enter in 3 price values (as floating point numbers).
    The print out the price values so that they are formatted to two decimal places. Also make sure that the price values are right aligned and line up at the decimal point.
    Here's a sample running of the program:

      Enter price #1: 1.55
      Enter price #2: 10
      Enter price #3: 9532.6

      Here are your prices!

      Price #1: $    1.55
      Price #2: $   10.00
      Price #3: $ 9532.60
    """
    p1 = float(input("Please input 1st price value "))
    p2 = float(input("Please input 2nd price value "))
    p3 = float(input("Please input 3rd price value "))
    x = format(p1, '>20,.2f')
    y = format(p2, '>20,.2f')
    z = format(p3, '>20,.2f')
    a = format('price #1:', '<10')
    b = format('price #2:', '<10')
    c = format('price #3:', '<10')

    c1="{0}{1}{2}".format(a,"$",x)
    c2="{0}{1}{2}".format(b,"$",y)
    c3="{0}{1}{2}".format(c,"$",z)
    
    print("Here are your prices!\n")
    print(c1)
    print(c2)
    print(c3)


      
