# Python 3 Report Generator
# For every item, generates a list of drop locations in HTML format

import dxutil

items = dxutil.loadItems()
dungeons = dxutil.getDungeons()

# Initialize Report File
report = open("report.html", "w")
report.write("<!DOCTYPE html><title>DX Drop Logs - Drop Report</title>")
report.write('<link href="https://fonts.googleapis.com/css2?family=PT+Sans&display=swap" rel="stylesheet">')
report.write("<style>body {font-family: 'PT Sans'} table, th, td {border: 1px solid #AAAAAA; border-collapse: collapse; padding: 0.25em;} p {margin: 0 0.25em;} img {max-height: 32px}</style>\n")
report.write("<body><table><thead><tr><th>Icon</th><th>Art</th><th>Name</th><th>Drops</th></tr></thead><tbody>\n")

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
					fullname = drop
					if (currflag == "Berries"):
						fullname = fullname + " Berry"
					if (currflag == "Seeds"):
						fullname = fullname + " Seed"
					if (currflag == "Orbs"):
						fullname = fullname + " Orb"
					if (currflag == "Wands"):
						fullname = fullname + " Wand"
					curritem = dxutil.getItemByName(fullname, items)
					# Based on the current mode, add to the correct category
					# If None, an error message has already been output to console; we will just ignore it
					if curritem != None:
						if currmode == "Floor":
							curritem.floordrops.append(dname.split("/")[1])
						elif currmode == "Shop":
							curritem.shopdrops.append(dname.split("/")[1])
						elif currmode == "Tile":
							curritem.tiledrops.append(dname.split("/")[1])
						elif currmode == "Wall":
							curritem.walldrops.append(dname.split("/")[1])
						elif currmode == "Dungeon End":
							curritem.dungeonenddrops.append(dname.split("/")[1])
						elif currmode == "Other":
							curritem.otherdrops.append(dname.split("/")[1])

# Write table using items
print("Now generating report...")
for item in items:
	report.write("<tr><td style='text-align:center'><img src='img/" + item.imagename + ".png'></td><td style='text-align:center'><img src='itemart/" + item.artname + ".png'></td><td>" + item.name + "</td><td>")
	if len(item.floordrops) > 0:
		report.write("<p><b>Floor</b>: " + ', '.join(item.floordrops) + "</p>")
	if len(item.shopdrops) > 0:
		report.write("<p><b>Shop</b>: " + ', '.join(item.shopdrops) + "</p>")
	if len(item.tiledrops) > 0:
		report.write("<p><b>Tile</b>: " + ', '.join(item.tiledrops) + "</p>")
	if len(item.walldrops) > 0:
		report.write("<p><b>Wall</b>: " + ', '.join(item.walldrops) + "</p>")
	if len(item.dungeonenddrops) > 0:
		report.write("<p><b>Dungeon End</b>: " + ', '.join(item.dungeonenddrops) + "</p>")
	if len(item.otherdrops) > 0:
		report.write("<p><b>Other</b>: " + ', '.join(item.otherdrops) + "</p>")
	report.write("</td></tr>\n")

# Finalize Report File
report.write("</tbody></table>")
report.write("</body>")
report.close()