# Python 3 Report Generator
# For every item, generates a list of drop locations in HTML format

import dxutil

items = dxutil.loadItems()
dungeons = dxutil.getDungeons()

# Initialize Report File
report = open("report.html", "w")
report.write("<!DOCTYPE html><title>DX Drop Logs - Drop Report</title>")
report.write('<link href="https://fonts.googleapis.com/css2?family=PT+Sans&display=swap" rel="stylesheet">')
report.write("<style>body {font-family: 'PT Sans'} table, th, td {border: 1px solid black;} p {margin: 0 0.25em;}</style>")
report.write("<body><table><thead><tr><th></th><th>Name</th><th>Drops</th></tr></thead><tbody>")

# Read data from all logs and load data into item objects
dividerline = "- - - - - - - - - - - - - - - -"
for dname in dungeons:
	with open(dname + ".txt") as log:
		print("Now Analyzing - " + dname)
		currmode = "Floor" # Mode defines drop mode, noting how to parse and which item field to insert into
		currflag = "NONE" # Current flag notes if we are currently switching mode, or which category/row we are on
		for line in log:
			line = line.strip()
			if (currflag == "NONE" and line == dividerline): # End of header
				currflag = "MODECHANGE"
			elif currflag == "NONE": # Currently in header, do nothing
				pass 
			elif (currflag != "MODECHANGE" and line == dividerline): # Switching to a mode change
				currflag = "MODECHANGE"
			elif (currflag == "MODECHANGE" and line != dividerline): # Mode Label
				currmode = line.strip() # Now Floor, Shop, Tile, Wall, or Dungeon End
			elif (currflag == "MODECHANGE" and line == dividerline): # Preparing for shift to Consumables
				currflag = "STASIS"
			else: # Category line
				currflag = line.split("|")[0].strip()
				# Now parse. Remember special case for Dungeon End mode
				splitdropline = line.split("|")
				if (len(splitdropline) == 1): # This is the case for the footer line at the end of each log
					drops = []
				elif (splitdropline[1].strip() == ""): # This is the case when there are no drops in the category
					drops = []
				else:
					drops = splitdropline[1].strip().split(", ")
				for drop in drops:
					if currmode == "Dungeon End":
						drop = drop.split(" x ")[0].strip()
					curritem = dxutil.getItemByName(drop, items)
					# Based on the current mode, add to the correct category
					# If None, an error message has already been output to console; we will just ignore it
					if curritem != None:
						if currmode == "Floor":
							curritem.floordrops.append(dname)
						elif currmode == "Shop":
							curritem.shopdrops.append(dname)
						elif currmode == "Tile":
							curritem.tiledrops.append(dname)
						elif currmode == "Wall":
							curritem.walldrops.append(dname)
						elif currmode == "Dungeon End":
							curritem.dungeonenddrops.append(dname)

# Write table using items
print("Now generating report...")
for item in items:
	report.write("<tr><td style='text-align:center'><img src='img/" + item.imagename + ".png'></td><td>" + item.name + "</td><td>")
	report.write("<p><b>Floor</b>: " + ', '.join(item.floordrops) + "</p>")
	if len(item.shopdrops) > 0:
		report.write("<p><b>Shop</b>: " + ', '.join(item.shopdrops) + "</p>")
	if len(item.tiledrops) > 0:
		report.write("<p><b>Tile</b>: " + ', '.join(item.tiledrops) + "</p>")
	if len(item.walldrops) > 0:
		report.write("<p><b>Wall</b>: " + ', '.join(item.walldrops) + "</p>")
	if len(item.dungeonenddrops) > 0:
		report.write("<p><b>Dungeon End</b>: " + ', '.join(item.dungeonenddrops) + "</p>")
	report.write("</td></tr>")

# Finalize Report File
report.write("</tbody></table>")
report.write("</body>")
report.close()