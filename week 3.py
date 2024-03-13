# Define the functions to calculate the discount
def calculate_discount(price, discount_percent):
    if discount_percent >=20:  #This checks to see if the discount is 20% or higher
        discounted_price = price - (price * (discount_percent/100)) #calculates the discounted price
        return discounted_price #It will return the discounted price
    else:
        return price # if discount is less than 20% original price is returned


#Prompt the user to enter original and discounted price of the item
original_price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

#Calculate the final price after applying the discount
final_price = calculate_discount(original_price, discount_percent)

# Print the final price after applying discount, or if no discount was applied print the original price
if final_price != original_price:
    print("Final price after applying the discount: $", final_price)
else:
    print("No discount applied. Final price remains: $", final_price)