class Item:
	def __init__(self, name, dropname, category, imagename):
		self.name = name # Name of item, including name to put in the report
		self.dropname = dropname # Name of item used in logs - often omits the ending (e.g. omits 'Orb' or 'Seed')
		self.category = category # Row ID used in logs
		self.imagename = imagename
		self.floordrops = []
		self.shopdrops = []
		self.tiledrops = []
		self.walldrops = []
		self.dungeonenddrops = []
		self.otherdrops = []
		if dropname == "": # If no drop name specified, use the provided name instead. This allows me to not have to rewrite all 100 TM names
			self.dropname = name

# Loads hardcoded information on items into a list and returns that list
def loadItems():
	itemlist = []
	# Consumables - Food
	itemlist.append(Item("Apple", "Apple", "Consumables", "apple"))
	itemlist.append(Item("Big Apple", "Big Apple", "Consumables", "bigapple"))
	itemlist.append(Item("Chestnut", "Chestnut", "Consumables", "chestnut"))
	itemlist.append(Item("Grimy Food", "Grimy Food", "Consumables", "grimyfood"))
	itemlist.append(Item("Perfect Apple", "Perfect Apple", "Consumables", "perfectapple"))
	itemlist.append(Item("Tiny Apple", "Tiny Apple", "Consumables", "tinyapple"))
	# Consumables - Stat Up + Recovery
	itemlist.append(Item("Accuracy Drink", "Accuracy Drink", "Consumables", "bluedrink"))
	itemlist.append(Item("Calcium", "Calcium", "Consumables", "calcium"))
	itemlist.append(Item("Carbos", "Carbos", "Consumables", "carbos"))
	itemlist.append(Item("Iron", "Iron", "Consumables", "iron"))
	itemlist.append(Item("Max Elixir", "Max Elixir", "Consumables", "greenbottle"))
	itemlist.append(Item("Max Ether", "Max Ether", "Consumables", "bluedrink"))
	itemlist.append(Item("Power Drink", "Power Drink", "Consumables", "powerdrink"))
	itemlist.append(Item("PP-Up Drink", "PP-Up Drink", "Consumables", "pp-updrink"))
	itemlist.append(Item("Protein", "Protein", "Consumables", "protein"))
	itemlist.append(Item("Zinc", "Zinc", "Consumables", "zinc"))
	# Berries
	itemlist.append(Item("Cheri Berry", "Cheri", "Berries", "cheriberry"))
	itemlist.append(Item("Chesto Berry", "Chesto", "Berries", "chestoberry"))
	itemlist.append(Item("Oran Berry", "Oran", "Berries", "oranberry"))
	itemlist.append(Item("Pecha Berry", "Pecha", "Berries", "pechaberry"))
	itemlist.append(Item("Rawst Berry", "Rawst", "Berries", "rawstberry"))
	itemlist.append(Item("Sitrus Berry", "Sitrus", "Berries", "sitrusberry"))
	# Projectiles
	itemlist.append(Item("Cacnea Spike", "Cacnea Spike", "Projectiles", "greenspike"))
	itemlist.append(Item("Corsola Twig", "Corsola Twig", "Projectiles", "purplespike"))
	itemlist.append(Item("Geo Pebble", "Geo Pebble", "Projectiles", "geopebble"))
	itemlist.append(Item("Golden Fossil", "Golden Fossil", "Projectiles", "goldenfossil"))
	itemlist.append(Item("Golden Spike", "Golden Spike", "Projectiles", "goldenspike"))
	itemlist.append(Item("Gravelerock", "Gravelerock", "Projectiles", "gravelerock"))
	itemlist.append(Item("Iron Spike", "Iron Spike", "Projectiles", "ironspike"))
	itemlist.append(Item("Silver Spike", "Silver Spike", "Projectiles", "silverspike"))
	# Seeds
	itemlist.append(Item("Ban Seed", "Ban", "Seeds", "seed"))
	itemlist.append(Item("Blast Seed", "Blast", "Seeds", "seed"))
	itemlist.append(Item("Blinker Seed", "Blinker", "Seeds", "seed"))
	itemlist.append(Item("Decoy Seed", "Decoy", "Seeds", "seed"))
	itemlist.append(Item("Doom Seed", "Doom", "Seeds", "seed"))
	itemlist.append(Item("Empowerment Seed", "Empowerment", "Seeds", "seed"))
	itemlist.append(Item("Energy Seed", "Energy", "Seeds", "seed"))
	itemlist.append(Item("Eyedrop Seed", "Eyedrop", "Seeds", "seed"))
	itemlist.append(Item("Heal Seed", "Heal", "Seeds", "seed"))
	itemlist.append(Item("Joy Seed", "Joy", "Seeds", "seed"))
	itemlist.append(Item("Life Seed", "Life", "Seeds", "seed"))
	itemlist.append(Item("Plain Seed", "Plain", "Seeds", "seed"))
	itemlist.append(Item("Pure Seed", "Pure", "Seeds", "seed"))
	itemlist.append(Item("Quick Seed", "Quick", "Seeds", "seed"))
	itemlist.append(Item("Reviver Seed", "Reviver", "Seeds", "seed"))
	itemlist.append(Item("Sleep Seed", "Sleep", "Seeds", "seed"))
	itemlist.append(Item("Stun Seed", "Stun", "Seeds", "seed"))
	itemlist.append(Item("Tiny Reviver Seed", "Tiny Reviver", "Seeds", "seed"))
	itemlist.append(Item("Totter Seed", "Totter", "Seeds", "seed"))
	itemlist.append(Item("Training Seed", "Training", "Seeds", "seed"))
	itemlist.append(Item("Violent Seed", "Violent", "Seeds", "seed"))
	itemlist.append(Item("Warp Seed", "Warp", "Seeds", "seed"))
	# Wands
	itemlist.append(Item("Confuse Wand", "Confuse", "Wand", "wand"))
	itemlist.append(Item("Guiding Wand", "Guiding", "Wand", "wand"))
	itemlist.append(Item("HP-Swap Wand", "HP-Swap", "Wand", "wand"))
	itemlist.append(Item("Petrify Wand", "Petrify", "Wand", "wand"))
	itemlist.append(Item("Pounce Wand", "Pounce", "Wand", "wand"))
	itemlist.append(Item("Slow Wand", "Slow", "Wand", "wand"))
	itemlist.append(Item("Slumber Wand", "Slumber", "Wand", "wand"))
	itemlist.append(Item("Stayaway Wand", "Stayaway", "Wand", "wand"))
	itemlist.append(Item("Surround Wand", "Surround", "Wand", "wand"))
	itemlist.append(Item("Switcher Wand", "Switcher", "Wand", "wand"))
	itemlist.append(Item("Tunnel Wand", "Tunnel", "Wand", "wand"))
	itemlist.append(Item("Two-Edged Wand", "Two-Edged", "Wand", "wand"))
	itemlist.append(Item("Warp Wand", "Warp", "Wand", "wand"))
	itemlist.append(Item("Whirlwind Wand", "Whirlwind", "Wand", "wand"))
	# Orbs
	itemlist.append(Item("All Dodge Orb", "All Dodge", "Orb", "orb"))
	itemlist.append(Item("All Power-Up Orb", "All Power-Up", "Orb", "orb"))
	itemlist.append(Item("All Protect Orb", "All Protect", "Orb", "orb"))
	itemlist.append(Item("Bank Orb", "Bank", "Orb", "orb"))
	itemlist.append(Item("Cleanse Orb", "Cleanse", "Orb", "orb"))
	itemlist.append(Item("Decoy Orb", "Decoy", "Orb", "orb"))
	itemlist.append(Item("Deluxe Ribbon", "Deluxe Ribbon", "Held Items", "goldband"))
	itemlist.append(Item("Drought Orb", "Drought", "Orb", "orb"))
	itemlist.append(Item("Escape Orb", "Escape", "Orb", "orb"))
	itemlist.append(Item("Evasion Orb", "Evasion", "Orb", "orb"))
	itemlist.append(Item("Foe-Hold Orb", "Foe-Hold", "Orb", "orb"))
	itemlist.append(Item("Foe-Seal Orb", "Foe-Seal", "Orb", "orb"))
	itemlist.append(Item("Gold Ribbon", "Gold Ribbon", "Held Items", "goldband"))
	itemlist.append(Item("Hail Orb", "Hail", "Orb", "orb"))
	itemlist.append(Item("Health Orb", "Health", "Orb", "orb"))
	itemlist.append(Item("Helper Orb", "Helper", "Orb", "orb"))
	itemlist.append(Item("Inviting Orb", "Inviting", "Orb", "orb"))
	itemlist.append(Item("Lasso Orb", "Lasso", "Orb", "orb"))
	itemlist.append(Item("Luminous Orb", "Luminous", "Orb", "orb"))
	itemlist.append(Item("Mobile Orb", "Mobile", "Orb", "orb"))
	itemlist.append(Item("Monster Orb", "Monster", "Orb", "orb"))
	itemlist.append(Item("Nullify Orb", "Nullify", "Orb", "orb"))
	itemlist.append(Item("One-Room Orb", "One-Room", "Orb", "orb"))
	itemlist.append(Item("One-Shot Orb", "One-Shot", "Orb", "orb"))
	itemlist.append(Item("Petrify Orb", "Petrify", "Orb", "orb"))
	itemlist.append(Item("Quick Orb", "Quick", "Orb", "orb"))
	itemlist.append(Item("Radar Orb", "Radar", "Orb", "orb"))
	itemlist.append(Item("Rainy Orb", "Rainy", "Orb", "orb"))
	itemlist.append(Item("Rare Quality Orb", "Rare Quality", "Orb", "orb"))
	itemlist.append(Item("Reset Orb", "Reset", "Orb", "orb"))
	itemlist.append(Item("Revive All Orb", "Revive All", "Orb", "orb"))
	itemlist.append(Item("Rollcall Orb", "Rollcall", "Orb", "orb"))
	itemlist.append(Item("Sandy Orb", "Sandy", "Orb", "orb"))
	itemlist.append(Item("Scanner Orb", "Scanner", "Orb", "orb"))
	itemlist.append(Item("See-Trap Orb", "See-Trap", "Orb", "orb"))
	itemlist.append(Item("Slow Orb", "Slow", "Orb", "orb"))
	itemlist.append(Item("Slumber Orb", "Slumber", "Orb", "orb"))
	itemlist.append(Item("Spurn Orb", "Spurn", "Orb", "orb"))
	itemlist.append(Item("Storage Orb", "Storage", "Orb", "orb"))
	itemlist.append(Item("Sunny Orb", "Sunny", "Orb", "orb"))
	itemlist.append(Item("Totter Orb", "Totter", "Orb", "orb"))
	itemlist.append(Item("Trapbust Orb", "Trapbust", "Orb", "orb"))
	itemlist.append(Item("Trawl Orb", "Trawl", "Orb", "orb"))
	itemlist.append(Item("Weather Lock Orb", "Weather Lock", "Orb", "orb"))
	itemlist.append(Item("Wigglytuff Orb", "Wigglytuff", "Orb", "orb"))
	# Held Items
	itemlist.append(Item("Big Eater Belt", "Big Eater Belt", "Held Items", "band"))
	itemlist.append(Item("Cover Band", "Cover Band", "Held Items", "band"))
	itemlist.append(Item("Defense Scarf", "Defense Scarf", "Held Items", "band"))
	itemlist.append(Item("Detect Band", "Detect Band", "Held Items", "band"))
	itemlist.append(Item("Efficient Bandanna", "Efficient Bandanna", "Held Items", "band"))
	itemlist.append(Item("Explosive Band", "Explosive Band", "Held Items", "band"))
	itemlist.append(Item("Fickle Specs", "Fickle Specs", "Held Items", "glasses"))
	itemlist.append(Item("Fierce Bandanna", "Fierce Bandanna", "Held Items", "band"))
	itemlist.append(Item("Friend Bow", "Friend Bow", "Held Items", "band"))
	itemlist.append(Item("Goggle Specs", "Goggle Specs", "Held Items", "glasses"))
	itemlist.append(Item("Heal Ribbon", "Heal Ribbon", "Held Items", "band"))
	itemlist.append(Item("Heavy Rotation Specs", "Heavy Rotation Specs", "Held Items", "glasses"))
	itemlist.append(Item("Insomniscope", "Insomniscope", "Held Items", "glasses"))
	itemlist.append(Item("Joy Ribbon", "Joy Ribbon", "Held Items", "band"))
	itemlist.append(Item("Lock-On Specs", "Lock-On Specs", "Held Items", "glasses"))
	itemlist.append(Item("Lucky Ribbon", "Lucky Ribbon", "Held Items", "band"))
	itemlist.append(Item("Mach Ribbon", "Mach Ribbon", "Held Items", "band"))
	itemlist.append(Item("Mobile Scarf", "Mobile Scarf", "Held Items", "band"))
	itemlist.append(Item("Munch Belt", "Munch Belt", "Held Items", "band"))
	itemlist.append(Item("No-Stick Cap", "No-Stick Cap", "Held Items", "band"))
	itemlist.append(Item("Nullify Bandanna", "Nullify Bandanna", "Held Items", "band"))
	itemlist.append(Item("Pass Scarf", "Pass Scarf", "Held Items", "band"))
	itemlist.append(Item("Pecha Scarf", "Pecha Scarf", "Held Items", "band"))
	itemlist.append(Item("Persim Band", "Persim Band", "Held Items", "band"))
	itemlist.append(Item("Phase Ribbon", "Phase Ribbon", "Held Items", "band"))
	itemlist.append(Item("Pierce Band", "Pierce Band", "Held Items", "band"))
	itemlist.append(Item("Power Band", "Power Band", "Held Items", "band"))
	itemlist.append(Item("Prosper Ribbon", "Prosper Ribbon", "Held Items", "band"))
	itemlist.append(Item("Recovery Scarf", "Recovery Scarf", "Held Items", "band"))
	itemlist.append(Item("Reunion Cape", "Reunion Cape", "Held Items", "band"))
	itemlist.append(Item("Scope Lens", "Scope Lens", "Held Items", "glasses"))
	itemlist.append(Item("Sneak Scarf", "Sneak Scarf", "Held Items", "band"))
	itemlist.append(Item("Special Band", "Special Band", "Held Items", "band"))
	itemlist.append(Item("Stamina Band", "Stamina Band", "Held Items", "band"))
	itemlist.append(Item("Tight Belt", "Tight Belt", "Held Items", "band"))
	itemlist.append(Item("Trap Scarf", "Trap Scarf", "Held Items", "band"))
	itemlist.append(Item("Twist Band", "Twist Band", "Held Items", "band"))
	itemlist.append(Item("Warp Scarf", "Warp Scarf", "Held Items", "band"))
	itemlist.append(Item("Weather Band", "Weather Band", "Held Items", "band"))
	itemlist.append(Item("X-Ray Specs", "X-Ray Specs", "Held Items", "glasses"))
	itemlist.append(Item("Zinc Band", "Zinc Band", "Held Items", "band"))
	# TMs
	itemlist.append(Item("Acrobatics", "", "TMs", "tm"))
	itemlist.append(Item("Aerial Ace", "", "TMs", "tm"))
	itemlist.append(Item("Attract", "", "TMs", "tm"))
	itemlist.append(Item("Aurora Veil", "", "TMs", "tm"))
	itemlist.append(Item("Blizzard", "", "TMs", "tm"))
	itemlist.append(Item("Brick Break", "", "TMs", "tm"))
	itemlist.append(Item("Brutal Swing", "", "TMs", "tm"))
	itemlist.append(Item("Bulk Up", "", "TMs", "tm"))
	itemlist.append(Item("Bulldoze", "", "TMs", "tm"))
	itemlist.append(Item("Calm Mind", "", "TMs", "tm"))
	itemlist.append(Item("Charge Beam", "", "TMs", "tm"))
	itemlist.append(Item("Confide", "", "TMs", "tm"))
	itemlist.append(Item("Dark Pulse", "", "TMs", "tm"))
	itemlist.append(Item("Dazzling Gleam", "", "TMs", "tm"))
	itemlist.append(Item("Double Team", "", "TMs", "tm"))
	itemlist.append(Item("Dragon Claw", "", "TMs", "tm"))
	itemlist.append(Item("Dragon Tail", "", "TMs", "tm"))
	itemlist.append(Item("Dream Eater", "", "TMs", "tm"))
	itemlist.append(Item("Earthquake", "", "TMs", "tm"))
	itemlist.append(Item("Echoed Voice", "", "TMs", "tm"))
	itemlist.append(Item("Embargo", "", "TMs", "tm"))
	itemlist.append(Item("Energy Ball", "", "TMs", "tm"))
	itemlist.append(Item("Explosion", "", "TMs", "tm"))
	itemlist.append(Item("Facade", "", "TMs", "tm"))
	itemlist.append(Item("False Swipe", "", "TMs", "tm"))
	itemlist.append(Item("Fire Blast", "", "TMs", "tm"))
	itemlist.append(Item("Flame Charge", "", "TMs", "tm"))
	itemlist.append(Item("Flamethrower", "", "TMs", "tm"))
	itemlist.append(Item("Flash Cannon", "", "TMs", "tm"))
	itemlist.append(Item("Fling", "", "TMs", "tm"))
	itemlist.append(Item("Fly", "", "TMs", "tm"))
	itemlist.append(Item("Focus Blast", "", "TMs", "tm"))
	itemlist.append(Item("Frost Breath", "", "TMs", "tm"))
	itemlist.append(Item("Frustration", "", "TMs", "tm"))
	itemlist.append(Item("Giga Impact", "", "TMs", "tm"))
	itemlist.append(Item("Grass Knot", "", "TMs", "tm"))
	itemlist.append(Item("Gyro Ball", "", "TMs", "tm"))
	itemlist.append(Item("Hail", "", "TMs", "tm"))
	itemlist.append(Item("Hidden Power", "", "TMs", "tm"))
	itemlist.append(Item("Hyper Beam", "", "TMs", "tm"))
	itemlist.append(Item("Ice Beam", "", "TMs", "tm"))
	itemlist.append(Item("Infestation", "", "TMs", "tm"))
	itemlist.append(Item("Leech Life", "", "TMs", "tm"))
	itemlist.append(Item("Light Screen", "", "TMs", "tm"))
	itemlist.append(Item("Low Sweep", "", "TMs", "tm"))
	itemlist.append(Item("Nature Power", "", "TMs", "tm"))
	itemlist.append(Item("Overheat", "", "TMs", "tm"))
	itemlist.append(Item("Payback", "", "TMs", "tm"))
	itemlist.append(Item("Poison Jab", "", "TMs", "tm"))
	itemlist.append(Item("Protect", "", "TMs", "tm"))
	itemlist.append(Item("Psych Up", "", "TMs", "tm"))
	itemlist.append(Item("Psychic", "", "TMs", "tm"))
	itemlist.append(Item("Psyshock", "", "TMs", "tm"))
	itemlist.append(Item("Quash", "", "TMs", "tm"))
	itemlist.append(Item("Rain Dance", "", "TMs", "tm"))
	itemlist.append(Item("Reflect", "", "TMs", "tm"))
	itemlist.append(Item("Rest", "", "TMs", "tm"))
	itemlist.append(Item("Return", "", "TMs", "tm"))
	itemlist.append(Item("Roar", "", "TMs", "tm"))
	itemlist.append(Item("Rock Polish", "", "TMs", "tm"))
	itemlist.append(Item("Rock Slide", "", "TMs", "tm"))
	itemlist.append(Item("Rock Tomb", "", "TMs", "tm"))
	itemlist.append(Item("Roost", "", "TMs", "tm"))
	itemlist.append(Item("Round", "", "TMs", "tm"))
	itemlist.append(Item("Safeguard", "", "TMs", "tm"))
	itemlist.append(Item("Sandstorm", "", "TMs", "tm"))
	itemlist.append(Item("Scald", "", "TMs", "tm"))
	itemlist.append(Item("Shadow Ball", "", "TMs", "tm"))
	itemlist.append(Item("Shadow Claw", "", "TMs", "tm"))
	itemlist.append(Item("Sky Drop", "", "TMs", "tm"))
	itemlist.append(Item("Sleep Talk", "", "TMs", "tm"))
	itemlist.append(Item("Sludge Bomb", "", "TMs", "tm"))
	itemlist.append(Item("Sludge Wave", "", "TMs", "tm"))
	itemlist.append(Item("Smack Down", "", "TMs", "tm"))
	itemlist.append(Item("Smart Strike", "", "TMs", "tm"))
	itemlist.append(Item("Snarl", "", "TMs", "tm"))
	itemlist.append(Item("Solar Beam", "", "TMs", "tm"))
	itemlist.append(Item("Steel Wing", "", "TMs", "tm"))
	itemlist.append(Item("Stone Edge", "", "TMs", "tm"))
	itemlist.append(Item("Substitute", "", "TMs", "tm"))
	itemlist.append(Item("Sunny Day", "", "TMs", "tm"))
	itemlist.append(Item("Surf", "", "TMs", "tm"))
	itemlist.append(Item("Swagger", "", "TMs", "tm"))
	itemlist.append(Item("Swords Dance", "", "TMs", "tm"))
	itemlist.append(Item("Taunt", "", "TMs", "tm"))
	itemlist.append(Item("Thief", "", "TMs", "tm"))
	itemlist.append(Item("Thunder", "", "TMs", "tm"))
	itemlist.append(Item("Thunder Wave", "", "TMs", "tm"))
	itemlist.append(Item("Thunderbolt", "", "TMs", "tm"))
	itemlist.append(Item("Torment", "", "TMs", "tm"))
	itemlist.append(Item("Toxic", "", "TMs", "tm"))
	itemlist.append(Item("Trick Room", "", "TMs", "tm"))
	itemlist.append(Item("U-turn", "", "TMs", "tm"))
	itemlist.append(Item("Venoshock", "", "TMs", "tm"))
	itemlist.append(Item("Volt Switch", "", "TMs", "tm"))
	itemlist.append(Item("Waterfall", "", "TMs", "tm"))
	itemlist.append(Item("Wild Charge", "", "TMs", "tm"))
	itemlist.append(Item("Will-O-Wisp", "", "TMs", "tm"))
	itemlist.append(Item("Work Up", "", "TMs", "tm"))
	itemlist.append(Item("X-Scissor", "", "TMs", "tm"))
	# Special
	itemlist.append(Item("Bronze Dojo Ticket", "Bronze Dojo Ticket", "Special", "ticket"))
	itemlist.append(Item("Silver Dojo Ticket", "Silver Dojo Ticket", "Special", "silverdojoticket"))
	itemlist.append(Item("Gold Dojo Ticket", "Gold Dojo Ticket", "Special", "golddojoticket"))
	itemlist.append(Item("Rainbow Gummi", "Rainbow Gummi", "Special", "rainbowgummi"))
	itemlist.append(Item("DX Gummi", "DX Gummi", "Special", "goldgummi"))
	itemlist.append(Item("Pretty Box", "Pretty Box", "Special", "prettybox"))
	itemlist.append(Item("Deluxe Box", "Deluxe Box", "Special", "box"))
	itemlist.append(Item("Evolution Crystal", "Evolution Crystal", "Special", "evolutioncrystal"))
	itemlist.append(Item("Invitation", "Invitation", "Special", "invitation"))
	itemlist.append(Item("Link Box", "Link Box", "Special", "linkbox"))

	return itemlist

# Returns a list of filenames (without the .txt) to look into.
# This is necessary since we don't necessarily want to scan every file in the repo
def getDungeons():
	dungeonlist = []
	dungeonlist.append("dungeon/Buried Relic")
	dungeonlist.append("dungeon/Darknight Relic")
	dungeonlist.append("dungeon/Desert Region")
	dungeonlist.append("dungeon/Fantasy Strait")
	dungeonlist.append("dungeon/Far-Off Sea")
	dungeonlist.append("dungeon/Fiery Field")
	dungeonlist.append("dungeon/Frosty Forest")
	dungeonlist.append("dungeon/Heart of the Frosty Forest")
	dungeonlist.append("dungeon/Grand Sea")
	dungeonlist.append("dungeon/Great Canyon")
	dungeonlist.append("dungeon/Howling Forest")
	dungeonlist.append("dungeon/Joyous Tower")
	dungeonlist.append("dungeon/Lapis Cave")
	dungeonlist.append("dungeon/Lightning Field")
	dungeonlist.append("dungeon/Magma Cavern Pit")
	dungeonlist.append("dungeon/Magma Cavern")
	dungeonlist.append("dungeon/Marvelous Sea")
	dungeonlist.append("dungeon/Meteor Cave")
	dungeonlist.append("dungeon/Mt. Blaze")
	dungeonlist.append("dungeon/Mt. Blaze Peak")
	dungeonlist.append("dungeon/Mt. Faraway")
	dungeonlist.append("dungeon/Mt. Freeze")
	dungeonlist.append("dungeon/Mt. Freeze Peak")
	dungeonlist.append("dungeon/Mt. Steel")
	dungeonlist.append("dungeon/Mt. Thunder")
	dungeonlist.append("dungeon/Mt. Thunder Peak")
	dungeonlist.append("dungeon/Murky Cave")
	dungeonlist.append("dungeon/Northern Range")
	dungeonlist.append("dungeon/Northwind Field")
	dungeonlist.append("dungeon/Oddity Cave")
	dungeonlist.append("dungeon/Pitfall Valley")
	dungeonlist.append("dungeon/Purity Forest")
	dungeonlist.append("dungeon/Remains Island")
	dungeonlist.append("dungeon/Rock Path")
	dungeonlist.append("dungeon/Silent Chasm")
	dungeonlist.append("dungeon/Silver Trench")
	dungeonlist.append("dungeon/Sinister Woods")
	dungeonlist.append("dungeon/Sky Tower")
	dungeonlist.append("dungeon/Sky Tower Summit")
	dungeonlist.append("dungeon/Snow Path")
	dungeonlist.append("dungeon/Solar Cave")
	dungeonlist.append("dungeon/Southern Cavern")
	dungeonlist.append("dungeon/Stormy Sea")
	dungeonlist.append("dungeon/Thunderwave Cave")
	dungeonlist.append("dungeon/Tiny Woods")
	dungeonlist.append("dungeon/Unown Relic")
	dungeonlist.append("dungeon/Uproar Forest")
	dungeonlist.append("dungeon/Waterfall Pond")
	dungeonlist.append("dungeon/Western Cave")
	dungeonlist.append("dungeon/Wish Cave")
	dungeonlist.append("dungeon/Wyvern Hill")

	# Non-dungeons with potentially hardwired inventories
	dungeonlist.append("other/Square - Kecleon Shop")
	dungeonlist.append("other/Square - Kecleon Wares")
	dungeonlist.append("other/Square - Felicity Bank")
	dungeonlist.append("other/Square - Mailbox")
	dungeonlist.append("other/Square - Munchlax")
	dungeonlist.append("other/Rescue - Pokémon Square")
	dungeonlist.append("other/Rescue - Regular")
	dungeonlist.append("other/Rescue - Special")
	dungeonlist.append("other/Rescue - Deluxe")

	dungeonlist.append("other/Box - Pretty Box")
	dungeonlist.append("other/Box - Deluxe Box")
	
	return dungeonlist

# Returns the item object based on the DROP NAME
# Intended use is mapping text in the drop logs to the item objects
def getItemByName(name, itemlist):
	for item in itemlist:
		if item.dropname == name:
			return item
	print("Unable to find item " + name + " in item list")
	return None
	
