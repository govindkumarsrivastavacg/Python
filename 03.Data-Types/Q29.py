#Create a small Python program that stores information about a product:

#Product name as a string
#Product quantity as an integer
#Product price as a floating-point number
#Whether the product is available as a Boolean
#Product discount information as None
#Use type() to identify every value.

product_name = "Laptop"      # <class 'str'>
quantity = 5                 # <class 'int'>
price = 799.99               # <class 'float'>
is_available = True          # <class 'bool'>
discount = None              # <class 'NoneType'>

print("Name:", type(product_name))
print("Quantity:", type(quantity))
print("Price:", type(price))
print("Available:", type(is_available))
print("Discount:", type(discount))