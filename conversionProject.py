"""
Group D Members
Jack Phillips
Sewon Ra
Kara Morgan
weldezgi fisshaye

This is a program converting Candian dollars to U.S dollars 
"""
CAN = float(input(" Enter your amount in CAN $ "))
CANtoUSD = 0.74 # Live rate is actually $0.72
CANtoUSDConversion = CAN * CANtoUSD
roundedBalance = round(CANtoUSDConversion, 2)

finalBalance = "$" + str(roundedBalance)
print("You balance in USD is", finalBalance)
