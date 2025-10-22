"""
Group D Members
Jack Phillips
Sewon Ra
Kara Morgan
weldezgi fisshaye

This is a program converting Candian dollars to U.S dollars.
"""

#First, it will prompt the user to input the amount they are looking to transfer from CAN to USD.
CAN = float(input(" Enter your amount in CAN $ "))

# This variable is the active rate you can multiply CAN dollars by to get the conversion $1 CAN == $0.74 USD
CANtoUSD = 0.74 # Live rate is actually $0.72 as of 10/20/25

# Next it will run the input through a simple algorithm to get the amount in USD
CANtoUSDConversion = CAN * CANtoUSD

# This function will round the amount to the 100ths place
roundedBalance = round(CANtoUSDConversion, 2)

# This function will convert the number value into a string and add '$' to the front to make the answer work in a sentence.
finalBalance = "$" + str(roundedBalance)

# Finally it prints the answer to give the user their new balance.
print("You balance in USD is", finalBalance)
