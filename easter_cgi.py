#!/usr/bin/env python3
import cgi
import calendar

def find_easter_date(year):
    # Formula to find the date of Easter
    a = year % 19
    b = year // 100
    c = year % 100
    d = b // 4
    e = b % 4
    f = (b + 8) // 25
    g = (b - f + 1) // 3
    h = (19 * a + b - d - g + 15) % 30
    i = c // 4
    k = c % 4
    l = (32 + 2 * e + 2 * i - h - k) % 7
    m = (a + 11 * h + 22 * l) // 451
    month = (h + l - 7 * m + 114) // 31
    day = ((h + l - 7 * m + 114) % 31) + 1
    return day, month

# Get form data
form = cgi.FieldStorage()

# Get the year and format from the form
year = int(form.getvalue("year"))
date_format = form.getvalue("format")

# Find Easter date
day, month = find_easter_date(year)

# Format the date
if date_format == "numeric":
    date = "{}/{}/{}".format(day, month, year)
elif date_format == "verbose":
    date = "{}th {} {}".format(day, calendar.month_abbr[month], year)
elif date_format == "both":
    date = "{}/{}/{} - {}th {} {}".format(day, month, year, day, calendar.month_abbr[month], year)

# Display the Easter date
print("Content-type: text/html")
print("")
print("<html>")
print("<head>")
print("    <title>Easter Date Finder</title>")
print("</head>")
print("<body>")
print("    <h1>Easter Date Finder</h1>")
print("    <p>Easter date for {}:</p>".format(year))
print("    <p>{}</p>".format(date))
print("    <p><a href=\"index.html\">Calculate again</a></p>")
print("</body>")
print("</html>")
