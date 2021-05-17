#! /usr/bin/env python3

print('Content-type: text/html\n')

import cgi

form = cgi.FieldStorage()   

html = """<!doctype html>

<html>

<head><meta charset="utf-8">

<link rel="stylesheet" href="https://cgi.sice.indiana.edu/~dpierz/i211.css">

<title>PizzaNet Order [2]</title></head>


</body>
	
	<p>What do you want on your {size} pizza with {crust}-style crust? Each topping costs $2 to add.</p>
	
	<form action="pizza2.cgi" method="post">
	
	<input type="checkbox" name="toppings" value="pepperoni">
	Pepperoni
	
	<input type="checkbox" name="toppings" value="mushroom">
	Mushroom
	
	<input type="checkbox" name="toppings" value="onion">
	Onion
	
	<input type="checkbox" name="toppings" value="bell pepper">
	Bell Pepper
	
	<input type="checkbox" name="toppings" value="extra cheese">
	Extra Cheese
	
	<input type="hidden" name="size" value="{size}">
	<input type="hidden" name="crust" value="{crust}">
	
	<button type="submit">Next</button>
	
	</form>
	
</body>

</html>"""

#Make a variable to retrieve the size data
size = form.getvalue('size')

#Make a variable to retrieve the crust data 
crust = form.getvalue('crust')

#Place the values in the correct HTML spaces
print(html.format(size = size, crust = crust))