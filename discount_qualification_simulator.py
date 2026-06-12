#Enmanuel Perez
#Lab 3 Decision Structures
#Complete

#This program determines whether the customer qualifys
#for a discount based on packages purchased

#Original price

original_price= 149.00

#Ask user to enter number of packages purchased

packages_purchased= int(input('Enter the amount of packages purchased: '))

#determine whether the customer qualifies for the discount

total_amount= packages_purchased * original_price

if packages_purchased >=10 and packages_purchased <=49:
    discount=10

elif packages_purchased >=50 and packages_purchased <=99:
    discount=20

elif packages_purchased >=100 and packages_purchased <= 149:
    discount=30

elif packages_purchased >=150: 
    discount=40        

# calculate discount amount

discount_amount=(total_amount*discount)/100
final_price=total_amount-discount_amount

print(f'Discount Amount:${discount_amount: ,.2f} ')
print(f'Total Amount:${final_price: ,.2f} ')


