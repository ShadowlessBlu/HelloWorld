""""price of house is 1M
If buyer has good credit
    they need to put down 10%
otherwise
    they need to put down 20%
print the down payment"""

price = 1000000
has_good_credit = True
if has_good_credit:
    down_payment = price * 0.10
    print("The Down payment of house is ", down_payment)
else:
    down_payment = price * 0.20
    print("The Down payment of house is ", down_payment)
