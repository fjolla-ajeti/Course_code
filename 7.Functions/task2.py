#Task 2

#Creating a dictionary.

#Create a function called make_country, which takes in a country’s name and capital as parameters. 
#Then create a dictionary from those parameters, with ‘name’ and ‘capital’ as keys. Make the function print out the values of the dictionary to make sure that it works as intended.


def make_country(country_name, country_capital):
    country_info = {
        'name': country_name,
        'capital': country_capital
    }
    print(country_info)

make_country("Kosova", "Prishtine")
