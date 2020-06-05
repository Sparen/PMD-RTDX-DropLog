# Python 3 Report Generator
# For every item, generates a list of drop locations in HTML format

import dxutil

items = dxutil.loadItems()
dungeons = dxutil.getDungeons()

# Initialize Report File
report = open("report/report.html", "w")
report.write("<!DOCTYPE html><title>DX Drop Logs - Drop Report</title>")
report.write('<link href="https://fonts.googleapis.com/css2?family=PT+Sans&display=swap" rel="stylesheet">')
report.write('<link href="itemdb.css" rel="stylesheet">')
report.write("<body><nav id='nav'></nav>\n")
report.write("<table><thead><tr><th>Icon</th><th>Art</th><th>Name</th><th>Drops</th></tr></thead><tbody>\n")

# Read data from all logs and load data into item objects
dividerline = "- - - - - - - - - - - - - - - -"
footerline = "----------------------------------------------------------------"
for dname in dungeons:
	with open(dname + ".txt") as log:
		print("Now Analyzing - " + dname)
		currmode = "Floor" # Mode defines drop mode, noting how to parse and which item field to insert into
		currflag = "NONE" # Current flag notes if we are currently switching mode, or which category/row we are on
		# Initialize dungeon report file
		dname_stripped = dname.split("/")[1]
		dungeonreport = open("report/" + dname_stripped + ".html", "w") # RHS of the dungeon/<name> dname
		dungeonreport.write("<!DOCTYPE html><title>DX Drop Logs - Drops by Dungeon - " + dname_stripped + "</title>")
		dungeonreport.write('<link href="https://fonts.googleapis.com/css2?family=PT+Sans&display=swap" rel="stylesheet">')
		dungeonreport.write('<link href="itemdb.css" rel="stylesheet">')
		dungeonreport.write("<body><nav id='nav'></nav>\n")
		dungeonreport.write("<h1>" + dname_stripped + "</h1><div class='flexcontainer'>")
		# Begin analysis
		for line in log:
			line = line.strip()
			if (currflag == "NONE" and line == dividerline): # End of header
				currflag = "MODECHANGE"
			elif currflag == "NONE": # Currently in header, do nothing
				pass 
			elif (currflag != "MODECHANGE" and line == dividerline): # Switching to a mode change
				currflag = "MODECHANGE"
				dungeonreport.write("</div></div>")
			elif (currflag == "MODECHANGE" and line != dividerline): # Mode Label
				currmode = line.strip() # Now Floor, Shop, Tile, Wall, or Dungeon End
				dungeonreport.write("<div><h2 class='dropmode'>" + currmode + "</h2><div class='flexcontainer-inner'>")
			elif (currflag == "MODECHANGE" and line == dividerline): # Preparing for shift to Consumables
				currflag = "STASIS"
			elif (line != footerline): # Category line. Need to make sure we're not at the footer (edge case)
				currflag = line.split("|")[0].strip()
				# Now parse. Remember special case for Dungeon End mode
				splitdropline = line.split("|")
				if (splitdropline[1].strip() == ""): # This is the case when there are no drops in the category
					drops = []
				else:
					drops = splitdropline[1].strip().split(", ")
				if (len(drops) > 0): # Don't write to the dungeon report if there are no drops for this category
					dungeonreport.write("<div><table><tr><th colspan='3'>" + currflag + "</th></tr>")
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
					# Write the item drop to the dungeon report
					dungeonreport.write("<tr><td style='text-align:center'><img src='../img/" + curritem.imagename + ".png' class='reportimg-sm'></td><td style='text-align:center'><img src='../itemart/" + curritem.artname + ".png' class='reportimg-sm'></td><td>" + curritem.name + "</td></tr>")
				if (len(drops) > 0): # Don't write to the dungeon report if there are no drops for this category
					dungeonreport.write("</table></div>")
		# Finalize dungeon report
		dungeonreport.write("</div></body>\n")
		dungeonreport.write("<footer id='footer'></footer>\n")
		dungeonreport.write("<script src='itemdb.js'></script>")
		dungeonreport.close()

# Write table using items
print("Now generating report...")
for item in items:
	report.write("<tr><td style='text-align:center'><img src='../img/" + item.imagename + ".png' class='reportimg'></td><td style='text-align:center'><img src='../itemart/" + item.artname + ".png' class='reportimg'></td><td>" + item.name + "</td><td>")
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
report.write("</body>\n")
report.write("<footer id='footer'></footer>\n")
report.write("<script src='itemdb.js'></script>")
report.close()