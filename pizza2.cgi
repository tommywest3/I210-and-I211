#! /usr/bin/env python3

print('Content-type: text/html\n')

import cgi

form = cgi.FieldStorage()   

html = """<!doctype html>

<html>

<head><meta charset="utf-8">

<link rel="stylesheet" href="https://cgi.sice.indiana.edu/~dpierz/i211.css">

<title>PizzaNet Order - Confirmation</title></head>

<body>

	<p>Your Order: A {size} {crust} pizza, with {toppings} toppings.</p>
	
	<p>Total Cost: ${total}</p>
	
</body>

</html>"""

#Make a variable to retrieve the size data
size = form.getvalue('size')

#Make a variable to retrieve the crust data 
crust = form.getvalue('crust')

#Make a variable to get a list of the toppings chosen
toppings = form.getlist('toppings')

#Count the number of toppings if any
if len(toppings) >= 1:
	toppings = len(toppings)
else:
	toppings = str('no')
	
#Find out the total of the order
#if form.getvalue('size') == 'small':
	#total += 8.5

#elif form.getvalue('size') == 'medium':
	#total += 10.5

#elif form.getvalue('size') == 'large':
	#total += 12.5

#Include the cost of toppings
#total = len(toppings) * 2

print(html.format(size = size, crust = crust, toppings = toppings, total = '0'))

