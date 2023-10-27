
#Task2
#Input data:
#stock = {
  #  "banana": 6,
   # "apple": 0,
   # "orange": 32,
    #"pear": 15
#}
#prices = {
  #  "banana": 4,
   # "apple": 2,
   # "orange": 1.5,
   # "pear": 3
#}
#Create a function which takes as input two dicts with structure mentioned above, then computes and returns the total price of stock.




stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

total_price = 0

for item, quantity in stock.items():
    if item in prices:
        total_price += prices[item] * quantity

print(f"Total price of stock: {total_price:.2f}")
