import requests

# page_names = """Glenadine Brendadryl
# Horses940 Wiki
# Horses University
# Main Page
# Mark Spitz (Character)
# Matt
# Matt's mom
# Miranda
# The Titanic
# Trisha Paytas (Character)""".split("\n") #.replace(" ", "_").replace("'", "%27")


pages = {
'Glenadine Brendadryl': {"intro": """Glenadine is a recurring actor in the Horses940 universe. Dropped on her head many times as a child, Glenadine provides a unique point of view to Horses940's videos. 
Glenadine's interest in acting as a career began in 1945, after she accidentally attended the signing of the formal surrender documents that ended World War 2 aboard the U.S.S Missouri. Mistaking the ship for the Titanic, Glenadine boarded and was photographed in the background of the historic event. Glenadine, inspired by the boat she thought had inspired the movie Titanic, applied for the Julliard School of Arts, and was promptly accepted. This whirlwind of events led to her being cast in the lauded Horses940 production, <a href="https://www.youtube.com/watch?v=4us9qLVqgkI">Storage Wars</a>, based on The Storage Wars, an eruption of violence shortly after World War 2. Most people outside the storage locker community are not aware of this international conflict.
Glenadine also purports to have discovered the planet Jupiter. Although these claims have been <a href="https://www.google.com/search?safe=strict&rlz=1C5CHFA_enUS809US809&sxsrf=ALeKk03WGYkO6oNPf1REfsD4B-mt0ypIUg%3A1596470897293&ei=cTYoX4DDEaiFytMPtriImAQ&q=who+discovered+jupiter&oq=who+discovered+jupiter&gs_lcp=CgZwc3ktYWIQAzIECAAQQzICCAAyAggAMgIIADICCAAyAggAMgIIADICCAAyAggAMgcIABAUEIcCOgQIIxAnOgUIABCRAjoFCC4QkQJQwSxYvEZggUdoAnAAeACAAX6IAe8NkgEEMjAuMpgBAKABAaoBB2d3cy13aXrAAQE&sclient=psy-ab&ved=0ahUKEwjAv-jFtf_qAhWognIEHTYcAkMQ4dUDCAw&uact=5">disputed by the media</a>, it is still not clear if Glenadine is telling the truth, or what she is capable of when it comes to the science of the stars and the wide expanse of space that settles over Earth.
Glenadine's family members have been cited as working behind the scenes at Horses940 Incorporated. Most notable is her Auntie Hisstamean, who regulates the temperature of all Horses940 sets so as to suppress unwanted paranormal and paralegal activity.""", 
	"photo_alt": "Glenadine Brendadryl stands outside, hoping to discover a new planet in the sky above her.", "sections": {}, "comments": {}},
'Horses940 Wiki': {"intro": """<h2>Welcome to the Horses940 Wiki!</h2>
	We're a collaborative community website about Horses940 that anyone, including you, can build and expand. Wikis like this one depend on readers getting involved and adding content. Click the "ADD NEW PAGE" or "EDIT" button at the top of any page to get started!""", "photo_alt": "", 
	"sections": {"Important Pages": ""}, "comments": {}},
'Horses University': {"intro": """Horses University is an online not-for-education profit institution, based out of Yo Mama's Ass. The University excels in hobby-horse races, handily beating its main rivel in that arena, The University of Lorton.
	Originally founded in 1947 by runaway Nazi scientist Dr. Heinz Poopfentrousers, Horses University was at big risk of closing after its chemistry program was revealed to be nothing more than a charade. Many students complained that they were woefully unprepared for internships at such world-famous and prestigious chemistry labs as United Synthesis Acetate Inc., and Poopfentrousers Chemical Company. It turned out after an internal investigation that the chemistry program was more like alchemy and witchcraft than anything else, and that the pseudoscientific quest to turn lead into gold fizzled out several hundred years before the University's founding. This has been blamed on alchemists "giving up" and curing cholera instead.
	Witchcraft, however, continues to be a successful program at Horses University, and many warlock students find gainful employment selling their spells on Etsy. The program had the largest enrollment until June 23, 2013 when it was eclipsed by the Crocheting major / Selling Crocheted Goods on Etsy minor.
	""", 
	"photo_alt": "The Horses U schoolyard", 
	"sections": {"Notable classes": """Comedy 101: How to be Funny
	Witchcraft 102: The Magick of Sage""", "Notable instructors": """Matt
	Elinor
	Professor Glenadine Brendadryl (asstrology department)"""}, "comments": {}},
'Mark Spitz (Character)': {"intro": """Mark Spitz is well known for his brief romantic entanglement with Matt of Horses940, but their relationship started out professional. A profoundly gifted actor, Spitz was cast to portray Matt's house in zoey101 Season 5 Premiere. Starting from the ground floor, Spitz was an essential part of the launch of Horses940 productions, although he now is an uber driver in Springfield, Virginia, choosing to stay out of the spotlight.
	Matt and Mark's romance is one that fans have not forgotten about - and the two are often linked in the media, although Matt has sworn off dating ghosts for now - as it has only ever brought him trouble in the past.""", "photo_alt": "Mark Spitz poses with awards he won for his appearance in a Horses940 original production", "sections": {}, "comments": {}},
"Matt's mom": {"intro": """Contrary to the name, no one really knows who the woman known as "Matt's mom" is. She appeared on set one day during the filming of the <a href="https://www.youtube.com/watch?v=QRydzP97tVI&t=413s">Zoey 101 Season 5 horses940 Premiere</a>. While her suggestions to replace Trisha Paytas' character with a scarecrow and to not make the entire episode about ghosts were ignored in the creative process, the producers of the video admired her go-getter attitude.
	As this woman refused to identify herself, she was renamed to "Matt's MOM" which is an acrobat that stands for Mentions Only Miranda because she seems to ignore Matt for the most part. Some believe that due to their similar appearances, Matt's mom is actually Matt from the future, come to warn the talent at Horses940 of an impending tragedy. This theory has been discredited as she didn't say shit about the coronavirus.""", "photo_alt": "", "sections": {}, 
	"comments": {"User": 'Are you sure you didn\'t mean MOM is an "acronym" rather than an "acrobat?"', "Mirandahorse": "I think you mean antonym..."}},
'Matt': {"intro": """""", 
	"photo_alt": "Omg! Matt look so cute", 
	"sections": {
	"Accolades": """Matt of Horses940 is known and lauded within the film industry for being a wildly succesful spelling bee champion. Often brought in to spell check film titles for majer motion studios, Matt holds 53 titles in national spelling bees held across the United States. 50 of these were obtained during 2013, an odd coincidence which Matt tweeted about years later, saying "Yeah, in 2013 I spelled my way to the Wite [sic] House. Feelin' so famoussss." It was later revealed that Matt has never visited the White House, although his statement may have been some form of Gen-Z manifestation that has yet to come about.
	In 2018, a year before Horses940 coalesced, Matt entered the Mr. Kentucky pageant. It is widely believed that he did this to impress Donathan Hurley, a Kentuckian who shot to fame after his appearance on Survivor, Season 36, Ghost Island, a season in which contestants battled ghosts and demons. The season had historically low ratings as viewers could not see the ghosts, and assumed the events were faked. Matt, a known psychic, used his psychotic powers to actually see the ghosts and communicate through them to Donathan. When Donathan did not send any messages back, Matt hitchhiked to Kentucky to find him and ended up in the nationally acclaimed pageant. Matt was crowned the winner of the Mr. Kentucky pageant mere seconds after stepping onto stage, but he promptly surrendered the award to Donathan, and did not take public credit for his win.""",
	"Education": "N/A",
	"Health": """Matt has never been to a doctor, not even during his birth. He walks with a limp due to gout and lost all of his teeth in a claw machine accident."""
	}, "comments": {}},
'Miranda': {"intro": """""", "photo_alt": "Miranda caught enjoying a night on the Town. <i>Springfield, VA 2018</i>", 
	"sections": {
		"Health: Afflictions": """On March 3nd, 2020, Miranda issued a press release that she had contracted anemia. True to her form, Miranda managed to turn the news into a political issue, attacking the "liberal vegan elite" for "canceling" meat. In response, Democratic Party Vice President of Vegan Affairs Rhonda LaGoo blamed Miranda for being stupid, calling her a "silly imitation-goose-meat."
Miranda is also an avid sufferer of atopic dermatitis eczema on her hands, which causes flaky skin resembling asbestos or a snow globe. Miranda has joked that she has "handruff" and must use "Hand and Shoulders" "hand-poo" (referencing Head and Shoulders dandruff shampoo).
Miranda's doctors, in a strange violation of HIPAA protocol, announced on her behalf that she was the first female case of a his-nia, an affliction similar to a hernia but only for men. Miranda developed her his-nia while moving patio furniture onto her roof. Many[who?] have suggested this is related to her asstrological aspirations, and that Miranda was trying to get as high up as she could to try to touch the moon. """,
		"Health: Controversies": """Miranda has been criticized many times in the news for her treatment of debilitating conditions. On August 13, 2019, in the midst of The Feud, Miranda tweeted from her personal Twitter @69miranda69 that Matt "was all upset because he has his rectal veins in a knot. Did someone say roid rage?" Hemorrhoid activists and the general media criticized the term roid rage and even made calls to boycott Miranda's one-woman show on tour with the USO in Kuwait. As a defense, Miranda revealed that she too suffered from a hemorrhoid, brought on by attempting to pass a walnut that she had unknowingly ingested. Shortly after, Miranda began selling "Yes I Have Roid Rage" shirts and buttons in her online shop, Miranda Sells. """
	}, 
	"comments": {"User": "This girl stole my whole wheat bread out of my cart at Giant the grocery store. "}},

'The Titanic': {"intro": """<i>"This is a very large boat"</i>
	The Titanic is a fake ship invented by Matt and Miranda for their eponymous smash video. The idea of the Titanic is borrowed by fellow content creator, James Cameron for his eponymous flop video.
	Often confused by amateurs for a similar video by the name of <i>Remember the Titans</i>, a movie about football players, Titanic can be identified by it being about love and romance and drag. That is the plot for the most part.
	No one really knows what happened to The Titanic after filming; some say it was dismantled and put in Matt's backyard for storage, others swear they saw it sink in the North Atlantic in the early morning of April 15, 1912, and still other cast members and crew say the boat never existed in the first place. There is a division among this group; some claim the viewer was misled (an optional illusion so to speak) and others claim a small dinghy was used as the set and eaten by termites and beavers.
	Viewer viewership was so well-received (80 views as of August 8, 2020 at 12:05 AM) that the cast reunited for a sequel to this location: <i>The Titanic 2: Here We Go Again!</i> where luckily no one was injured because they knew the good ladyship would sink so they all had life jackets this time. <i>Titanic 2 prominently</i> features Matt's mom laughing at increasingly abstract footage of herself, apparently blissfully unaware of the carnality and agony yet to unfold in the rest of the film.""", "photo_alt": "", "sections": {}, "comments": {}},

'Trisha Paytas (Character)': {
	"intro": """<img src="math.svg"> Trisha Paytas is one of the first characters created by the founders of Horses940. Based on a popular youtube and onlyfans creator with the same name, Trisha Paytas is first introduced into the Horses940 universe in the smash hit video zoey101 SEASON 5 PREMIERE.
	The character's name is based on two qualities she espouses, that is, "Trisha" (short for nutrition), and Penis. Trisha's enemy is the Horses940 character Barack Obama, according to the Washington Post.
	Widely considered Horses940's first collab this character is contained within Matt's body, but controlled by the energy of Trisha Paytas - a feat achieved by supernatural means. When on set, Trisha Paytas designed her character's costume in the hopes of making Matt's physical form represent her own inner emotional one. While Matt has been said to "be built like a rack of ribs," the transformation was considered a success, and Trisha Paytas the character was born.""", 
	"photo_alt": "Trisha Paytas relaxing in plush leather chair", 
	"sections": {}, 
	"comments": {"User":"Omg I was always wondering about this. Trisha Oauras was a genius invention", "User2": "I was talking to my live-in swim instructor about this the other day... I said Clarence where do you think Horses 940 youtube channel came up with the character Trisha Paytas ... he said ... can you please not get so sweaty next time i stay the night ... fascinating article"}},
'index': {"sections": {}, "intro": "", "photo_alt":"", "comments": {}}
}

pages["index"]["sections"]["Pages"] = "\n".join([f'<a href="{page}">{page}</a>' for page in pages])


for page, data in pages.items():
# 	url = f"https://horses940.fandom.com/wiki/{page}"
# 	response = requests.get(url)
# ALIGN="right" HSPACE="50" VSPACE="50""

	# make body
	# look for links
	body = "\n".join([f"<h2>{title}</h2><p>{text}</p>" for title, text in data["sections"].items()]).replace("\n", "<br><br>")
	intro = data["intro"].replace("\n", "<br><br>")
	
	for other_page_name in pages:
		if other_page_name == page: continue
		html_name = other_page_name.replace(" ", "%20")
		body = body.replace(other_page_name, f'<a href={html_name}.html>{other_page_name}</a>', 2)
		intro = intro.replace(other_page_name, f'<a href={html_name}.html>{other_page_name}</a>', 2)
	
	
	pic = page.replace(" ", "")
	photo_alt = data["photo_alt"]
	comments = "\n".join([f"<h5>{poster}</h5>\n<p>{text}</p>" for poster, text in data["comments"].items()])
	
	with open("template.html") as t:
		html = t.read().format(page=page, body=body, intro=intro, pic=pic, photo_alt=photo_alt, comments=comments)
	
	with open(f"{page}.html", "w") as f:
		f.write(html)