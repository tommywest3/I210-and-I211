#Creating a table in html with the help of CGI
#Thomas West

#! /usr/bin/env python3
print('Content-type: text/html\n')

#Make sure those are the first lines for a CGI script ^
#Create HTML setup
html = """<!doctype html>

<html lang="en">
<head>
      <meta charset="utf-8">
      <title>HTML table practice</title>
</head>

<body>
      {content}
</body>
</html>"""
#Start making the table 
table = "<table>" + "<tr>"
#include row 1
row1 = ("<td>" + "Row 1, Col 1" + "</td>"
        + "<td>" + "Row 1, Col 2" + "</td>"
        + "<td>" + "Row 1, Col 3" + "</td>"
        + "<td>" + "Row 1, Col 4" + "</td>"
        + "<td>" + "Row 1, Col 5" + "</td>"
        + "<td>" + "Row 1, Col 6" + "</td>"
        + "<td>" + "Row 1, Col 7" + "</td>"
        + "<td>" + "Row 1, Col 8" + "</td>"
        + "<td>" + "Row 1, Col 9" + "</td>"
        + "<td>" + "Row 1, Col 10" + "</td>" + "</tr>")
#include row 2
row2 = ("<td>" + "Row 2, Col 1" + "</td>"
        + "<td>" + "Row 2, Col 2" + "</td>"
        + "<td>" + "Row 2, Col 3" + "</td>"
        + "<td>" + "Row 2, Col 4" + "</td>"
        + "<td>" + "Row 2, Col 5" + "</td>"
        + "<td>" + "Row 2, Col 6" + "</td>"
        +"<td>" + "Row 2, Col 7" + "</td>"
        + "<td>" + "Row 2, Col 8" + "</td>"
        +"<td>" + "Row 2, Col 9" + "</td>"
        + "<td>" + "Row 2, Col 10" + "</td>" + "</tr>")
#include row 3
row3 = ("<td>" + "Row 3, Col 1" + "</td>"
        + "<td>" + "Row 3, Col 2" + "</td>"
        + "<td>" + "Row 3, Col 3" + "</td>"
        + "<td>" + "Row 3, Col 4" + "</td>"
        +"<td>" + "Row 3, Col 5" + "</td>"
        + "<td>" + "Row 3, Col 6" + "</td>"
        +"<td>" + "Row 3, Col 7" + "</td>"
        + "<td>" + "Row 3, Col 8" + "</td>"
        +"<td>" + "Row 3, Col 9" + "</td>"
        + "<td>" + "Row 3, Col 10" + "</td>" + "</tr>")
#include row 4
row4 = ("<td>" + "Row 4, Col 1" + "</td>"
        + "<td>" + "Row 4, Col 2" + "</td>"
        + "<td>" + "Row 4, Col 3" + "</td>"
        + "<td>" + "Row 4, Col 4" + "</td>"
        +"<td>" + "Row 4, Col 5" + "</td>"
        + "<td>" + "Row 4, Col 6" + "</td>"
        +"<td>" + "Row 4, Col 7" + "</td>"
        + "<td>" + "Row 4, Col 8" + "</td>"
        +"<td>" + "Row 4, Col 9" + "</td>"
        + "<td>" + "Row 4, Col 10" + "</td>" + "</tr>")
#include row 5
row5 = ("<td>" + "Row 5, Col 1" + "</td>"
        + "<td>" + "Row 5, Col 2" + "</td>"
        + "<td>" + "Row 5, Col 3" + "</td>"
        + "<td>" + "Row 5, Col 4" + "</td>"
        +"<td>" + "Row 5, Col 5" + "</td>"
        + "<td>" + "Row 5, Col 6" + "</td>"
        +"<td>" + "Row 5, Col 7" + "</td>"
        + "<td>" + "Row 5, Col 8" + "</td>"
        +"<td>" + "Row 5, Col 9" + "</td>"
        + "<td>" + "Row 5, Col 10" + "</td>" + "</tr>")
#include row 6
row6 = ("<td>" + "Row 6, Col 1" + "</td>"
        + "<td>" + "Row 6, Col 2" + "</td>"
        + "<td>" + "Row 6, Col 3" + "</td>"
        + "<td>" + "Row 6, Col 4" + "</td>"
        +"<td>" + "Row 6, Col 5" + "</td>"
        + "<td>" + "Row 6, Col 6" + "</td>"
        +"<td>" + "Row 6, Col 7" + "</td>"
        + "<td>" + "Row 6, Col 8" + "</td>"
        +"<td>" + "Row 6, Col 9" + "</td>"
        + "<td>" + "Row 6, Col 10" + "</td>" + "</tr>")
#include row 7
row7 = ("<td>" + "Row 7, Col 1" + "</td>"
        + "<td>" + "Row 7, Col 2" + "</td>"
        + "<td>" + "Row 7, Col 3" + "</td>"
        + "<td>" + "Row 7, Col 4" + "</td>"
        +"<td>" + "Row 7, Col 5" + "</td>"
        + "<td>" + "Row 7, Col 6" + "</td>"
        +"<td>" + "Row 7, Col 7" + "</td>"
        + "<td>" + "Row 7, Col 8" + "</td>"
        +"<td>" + "Row 7, Col 9" + "</td>"
        + "<td>" + "Row 7, Col 10" + "</td>" + "</tr>")
#include row 8
row8 = ("<td>" + "Row 8, Col 1" + "</td>"
        + "<td>" + "Row 8, Col 2" + "</td>"
        + "<td>" + "Row 8, Col 3" + "</td>"
        + "<td>" + "Row 8, Col 4" + "</td>"
        +"<td>" + "Row 8, Col 5" + "</td>"
        + "<td>" + "Row 8, Col 6" + "</td>"
        +"<td>" + "Row 8, Col 7" + "</td>"
        + "<td>" + "Row 8, Col 8" + "</td>"
        +"<td>" + "Row 8, Col 9" + "</td>"
        + "<td>" + "Row 8, Col 10" + "</td>" + "</tr>")
#include row 9
row9 = ("<td>" + "Row 9, Col 1" + "</td>"
        + "<td>" + "Row 9, Col 2" + "</td>"
        + "<td>" + "Row 9, Col 3" + "</td>"
        + "<td>" + "Row 9, Col 4" + "</td>"
        +"<td>" + "Row 9, Col 5" + "</td>"
        + "<td>" + "Row 9, Col 6" + "</td>"
        +"<td>" + "Row 9, Col 7" + "</td>"
        + "<td>" + "Row 9, Col 8" + "</td>"
        +"<td>" + "Row 9, Col 9" + "</td>"
        + "<td>" + "Row 9, Col 10" + "</td>" + "</tr>")
#include row 10
row10 = ("<td>" + "Row 10, Col 1" + "</td>"
         + "<td>" + "Row 10, Col 2" + "</td>"
         + "<td>" + "Row 10, Col 3" + "</td>"
         + "<td>" + "Row 10, Col 4" + "</td>"
         +"<td>" + "Row 10, Col 5" + "</td>"
         + "<td>" + "Row 10, Col 6" + "</td>"
         +"<td>" + "Row 10, Col 7" + "</td>"
         + "<td>" + "Row 10, Col 8" + "</td>"
         +"<td>" + "Row 10, Col 9" + "</td>"
         + "<td>" + "Row 10, Col 10" + "</td>" + "</tr>")
#Put all the pieces together
table += row1 + row2 + row3 + row4 + row5 + row6 + row7 + row8 + row9 + row10 + "</table>"
print(html.format(content = table))

