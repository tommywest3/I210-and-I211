#Place a table in html code using Python
#Thomas West

output = open("list.html", "w")

html = """<!doctype html>

<html lang="en">
<head>
      <meta charset="utf-8">
      <title>HTML table list practice</title>
</head>

<body>
      {content}
</body>
</html>"""

data = ["Item", "Cost", "Type", "Coke", "$2", "Drink",

        "Water", "$0", "Drink", "Fries", "$4", "Appetizer",

        "Onion Rings", "$3", "Appetizer", "Steak", "$12", "Entree",

        "Chicken", "$8", "Entree", "Caesar Salad", "$7", "Entree"]
table = "<table>" + "<tr>" + "<td>"
row1 = data[0] + "," + data[1] + "," + data[2] + "</td>"
row2 = "<td>" + data[3] + "," + data[4] + "," + data[5] + "</td>"
row3 = "<td>" + data[6] + "," + data[7] + "," + data[8] + "</td>"
row4 = "<td>" + data[9] + "," + data[10] + "," + data[11] + "</td>"
row5 = "<td>" + data[12] + "," + data[13] + "," + data[14] + "</td>"
row6 = "<td>" + data[15] + "," + data[16] + "," + data[17] + "</td>"
row7 = "<td>" + data[18] + "," + data[19] + "," + data[20] + "</td>"
row8 = "<td>" + data[21] + "," + data[22] + "," + data[23] + "</td>"

rows = row1 + row2 + row3 + row4 + row5 + row6 + row7 + row8
table += rows + "</tr>" + "</table>"

output.write(html.format(content=table))
output.close
