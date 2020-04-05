# Python 3 Report Generator
# For every item, generates a list of drop locations in HTML format

import dxutil

items = dxutil.loadItems()
dungeons = dxutil.getDungeons()

# Initialize Report File
report = open("report.html", "w")



report.close()