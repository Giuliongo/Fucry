#Created by Giuliongo

import time
import os
import requests

#Name of the Crypto

name_crypto = input("What is the name of your crypto? : ")

while name_crypto.isalpha() != True:
	print("Enter a valid crypto!")
	name_crypto = input("What is the name of your crypto? : ")

name_crypto = name_crypto.upper()
crypto_name = name_crypto + "USDT"

#Binance API

marketprice = 'https://api.binance.com/api/v1/ticker/24hr?symbol=' + crypto_name
res = requests.get(marketprice)
data = res.json()
lastprice = float(data['lastPrice'])

#Number of crypto

number_crypto = input("How much crypto do you have? : ")

while number_crypto == "":
	print("Please enter a number!")
	number_crypto = input("How much crypto do you have? : ")

while number_crypto.isalpha() != False:
    print("Please enter a number!")
    number_crypto = input("How much crypto do you have? : ")

number_crypto = float(number_crypto)

#Price Request

price_request = input("What price do you want to set? : ")

while price_request == "":
	print("Please enter a number!")
	price_request = input("What price do you want to set? : ")

while price_request.isalpha() != False:
    print("Please enter a number!")
    price_request = input("What price do you want to set? : ")

price_request = float(price_request)

#Value of Crypto

value_of_the_crypto = number_crypto * lastprice
value_of_the_crypto = float(value_of_the_crypto)

#Profit

actual = value_of_the_crypto

one = value_of_the_crypto / lastprice
two = one * price_request
profit = two - actual

if profit > 0:
	gainorlose = "gain"
	profitorloss = "profit"

elif profit < 0:
	gainorlose = "lose"
	profitorloss = "loss"


print(f"The future price will be {price_request}$/{name_crypto}")
print(f"{number_crypto} {name_crypto} is currently worth {value_of_the_crypto}$")
print(f"You will {gainorlose} precisely {profit}$ in {profitorloss}")
