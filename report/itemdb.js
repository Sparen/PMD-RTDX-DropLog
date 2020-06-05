"use strict";

// This is the JavaScript source for menus and other common elements in the PMD Drop Log + Item Database

function setNav () {
	let navbar = "<ul><li class='navitem'><a href='./report.html'>Item Drop Locations</a></li></ul>";
	document.getElementById("nav").innerHTML = navbar;
}

function setFooter () {
	let footer = `
		<div id="footernav"><div id="footernavheader">Main Story Dungeons</div><ul>
		<li class="navitem"><a href="Tiny Woods.html">Tiny Woods</a></li>
		<li class="navitem"><a href="Thunderwave Cave.html">Thunderwave Cave</a></li>
		<li class="navitem"><a href="Mt. Steel.html">Mt. Steel</a></li>
		<li class="navitem"><a href="Oddity Cave.html">Oddity Cave</a></li>
		<li class="navitem"><a href="Sinister Woods.html">Sinister Woods</a></li>
		<li class="navitem"><a href="Silent Chasm.html">Silent Chasm</a></li>
		<li class="navitem"><a href="Mt. Thunder.html">Mt. Thunder</a></li>
		<li class="navitem"><a href="Mt. Thunder Peak.html">Mt. Thunder Peak</a></li>
		<li class="navitem"><a href="Great Canyon.html">Great Canyon</a></li>
		<li class="navitem"><a href="Lapis Cave.html">Lapis Cave</a></li>
		<li class="navitem"><a href="Rock Path.html">Rock Path</a></li>
		<li class="navitem"><a href="Mt. Blaze.html">Mt. Blaze</a></li>
		<li class="navitem"><a href="Mt. Blaze Peak.html">Mt. Blaze Peak</a></li>
		<li class="navitem"><a href="Frosty Forest.html">Frosty Forest</a></li>
		<li class="navitem"><a href="Heart of the Frosty Forest.html">Heart of the Frosty Forest</a></li>
		<li class="navitem"><a href="Snow Path.html">Snow Path</a></li>
		<li class="navitem"><a href="Mt. Freeze.html">Mt. Freeze</a></li>
		<li class="navitem"><a href="Mt. Freeze Peak.html">Mt. Freeze Peak</a></li>
		<li class="navitem"><a href="Uproar Forest.html">Uproar Forest</a></li>
		<li class="navitem"><a href="Magma Cavern.html">Magma Cavern</a></li>
		<li class="navitem"><a href="Magma Cavern Pit.html">Magma Cavern Pit</a></li>
		<li class="navitem"><a href="Sky Tower.html">Sky Tower</a></li>
		<li class="navitem"><a href="Sky Tower Summit.html">Sky Tower Summit</a></li>
		</ul>
		<div id="footernavheader">Postgame Dungeons</div><ul>
		<li class="navitem"><a href="Waterfall Pond.html">Waterfall Pond</a></li>
		<li class="navitem"><a href="Remains Island.html">Remains Island</a></li>
		<li class="navitem"><a href="Desert Region.html">Desert Region</a></li>
		<li class="navitem"><a href="Southern Cavern.html">Southern Cavern</a></li>
		<li class="navitem"><a href="Wyvern Hill.html">Wyvern Hill</a></li>
		<li class="navitem"><a href="Darknight Relic.html">Darknight Relic</a></li>
		<li class="navitem"><a href="Unown Relic.html">Unown Relic</a></li>
		<li class="navitem"><a href="Grand Sea.html">Grand Sea</a></li>
		<li class="navitem"><a href="Far-Off Sea.html">Far-Off Sea</a></li>
		<li class="navitem"><a href="Howling Forest.html">Howling Forest</a></li>
		<li class="navitem"><a href="Stormy Sea.html">Stormy Sea</a></li>
		<li class="navitem"><a href="Buried Relic.html">Buried Relic</a></li>
		<li class="navitem"><a href="Solar Cave.html">Solar Cave</a></li>
		<li class="navitem"><a href="Fiery Field.html">Fiery Field</a></li>
		<li class="navitem"><a href="Lightning Field.html">Lightning Field</a></li>
		<li class="navitem"><a href="Northwind Field.html">Northwind Field</a></li>
		<li class="navitem"><a href="Mt. Faraway.html">Mt. Faraway</a></li>
		<li class="navitem"><a href="Western Cave.html">Western Cave</a></li>
		<li class="navitem"><a href="Northern Range.html">Northern Range</a></li>
		<li class="navitem"><a href="Pitfall Valley.html">Pitfall Valley</a></li>
		<li class="navitem"><a href="Joyous Tower.html">Joyous Tower</a></li>
		<li class="navitem"><a href="Purity Forest.html">Purity Forest</a></li>
		<li class="navitem"><a href="Wish Cave.html">Wish Cave</a></li>
		<li class="navitem"><a href="Murky Cave.html">Murky Cave</a></li>
		<li class="navitem"><a href="Silver Trench.html">Silver Trench</a></li>
		<li class="navitem"><a href="Meteor Cave.html">Meteor Cave</a></li>
		<li class="navitem"><a href="Marvelous Sea.html">Marvelous Sea</a></li>
		<li class="navitem"><a href="Fantasy Strait.html">Fantasy Strait</a></li>
		</ul>
		<div id="footernavheader">Other</div><ul>
		<li class="navitem"><a href="Square - Kecleon Shop.html">Square - Kecleon Shop</a></li>
		<li class="navitem"><a href="Square - Kecleon Wares.html">Square - Kecleon Wares</a></li>
		<li class="navitem"><a href="Square - Feliity Bank.html">Square - Felicity Bank</a></li>
		<li class="navitem"><a href="Square - Mailbox.html">Square - Mailbox</a></li>
		<li class="navitem"><a href="Square - Munchlax.html">Square - Munchlax</a></li>
		<li class="navitem"><a href="Rescue - Pokémon Square.html">Rescue - Pokémon Square</a></li>
		<li class="navitem"><a href="Rescue - Regular.html">Rescue - Regular</a></li>
		<li class="navitem"><a href="Rescue - Special.html">Rescue - Special</a></li>
		<li class="navitem"><a href="Rescue - Deluxe.html">Rescue - Deluxe</a></li>
		<li class="navitem"><a href="Box - Pretty Box.html">Box - Pretty Box</a></li>
		<li class="navitem"><a href="Box - Deluxe Box.html">Box - Deluxe Box</a></li>
		</ul></div>
	`;
	document.getElementById("footer").innerHTML = footer;
}

setNav();
setFooter();