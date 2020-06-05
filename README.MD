# Pokémon Mystery Dungeon Rescue Team DX Drop Logs

This is a personal database of all item drops in Pokémon Mystery Dungeon Rescue Team DX. 

All data is stored in plain text.

### Compiling Report

Compile the report from the logs by running `python3 reportgen.py`. This will build a report (`report.html`) in `/report` as well as prettified versions of each raw data file

### Storage Notes

Poké not shown. All items alphabetized by category

Treasure Box shown separately from dungeon drops.

Second part dungeons (e.g. Peaks) are treated separately

Pickup treated as Floor

Items not shown if:
- Tiny Apple + Food Finder  
- Monster House  
- Drop-only (e.g. Abra Max Ether, Pretty Box, Deluxe Box)  
- Delivery request item (they are always spawned on the floor of the request)  

### Notes on Specific Items

X-Ray Specs
- Shows items in walls as well
- Primarily used post Sky-Tower

### Other Notes

- Kecleon Shop in Pokémon Square seems to stock permenant stack upgrade items after clearing Murky Cave
- Boxes are not sorted by dungeon or acquisition method in logs  
- All rescue requests are aggregated regardless of dungeon or rank  
