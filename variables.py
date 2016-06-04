'''
Edit this file to contain the variable assignments.
To get you started the first one is done for you.
The quotes are necessary for storing text in a
variable, but not for numbers.
'''

name = "Lee Cardholder" 

balance = 120.50

percent_apr = 20
from fractions import Fraction
Fraction(percent_apr, 100)

monthly_interest = balance * Fraction(percent_apr, 100)/12
print(monthly_interest)
