import random

myRand = random.randrange(0,10)
charSexList = ["Male","Female"]
charSexChoice = random.randrange(0,len(charSexList))
charAlignList = ["Lawful Good",
                 "Neutral Good",
                 "Chaotic Good",
                 "Lawful Neutral",
                 "Neutral",
                 "Chaotic Neutral",
                 "Lawful Evil",
                 "Neutral Evil",
                 "Chaotic Evil"]
charAlignChoice = random.randrange(0,len(charAlignList))
charClassList = ["Blacksmith",
                 "Butcher",
                 "Baker"]
charClassChoice = random.randrange(0,len(charClassList))
charHeightList = ["5'5",
                  "5'6",
                  "20'7"]
charHeightChoice = random.randrange(0,len(charHeightList))
charBuildList = ["Fat",
                 "Chubby",
                 "Curved",
                 "Thin",
                 "Lithe",
                 "Athletic",
                 "Strong",
                 "Buff"]
charBuildChoice = random.randrange(0,len(charBuildList))
charAppearanceList = ["Distinctive Jewelry",
                      "Piercings",
                      "Flamboyant or outlandish clothing",
                      "Formal, clean clothes",
                      "Ragged, dirty clothes",
                      "Pronounced scar",
                      "Missing teeth",
                      "Missing fingers",
                      "Unusual eye color",
                      "Tattoos",
                      "Birthmark",
                      "Unusual skin color",
                      "Bald",
                      "Braided beard or hair",
                      "Unusual hair color",
                      "Nervous eye twitch",
                      "Distinctive nose",
                      "Distinctive posture",
                      "Exceptionally beautiful",
                      "Exceptionally ugly"]
charAppearanceChoice = random.randrange(0,len(charAppearanceList))
charTalentList = ["Plays a musical instrument",
                  "Speaks several languages fluently",
                  "Unbelievably lucky",
                  "Perfect memory",
                  "Great with animals",
                  "Great with children",
                  "Great at solving puzzles",
                  "Great at one game",
                  "Great at impersonations",
                  "Draws beautifully",
                  "Paints beautifully",
                  "Sings beautifully",
                  "Drinks everyone under the table",
                  "Expert carpenter",
                  "Expert cook",
                  "Expert dart thrower and rock skipper",
                  "Expert juggler",
                  "Skilled actor and master of disguise",
                  "Skilled dancer",
                  "Knows thieves' cant"]
charTalentChoice = random.randrange(0,len(charTalentList))
charMannerismList = ["Prone to singing, whistling, or humming quietly",
                     "Speaks in rhyme or some other peculiar way",
                     "Particularly low or high voice",
                     "Slurs words, lisps, or stutters",
                     "Enunciates overly clearly",
                     "Speaks loudly",
                     "Whispers",
                     "Uses flowery speech or long words",
                     "Frequently uses the wrong word",
                     "Uses colorful oaths and exclamations",
                     "Makes constant jokes or puns",
                     "Prone to predictions of doom",
                     "Fidgets",
                     "Squints",
                     "Stares into the distance",
                     "Chews something",
                     "Paces",
                     "Taps fingers",
                     "Bites fingernails",
                     "Twirls hair or tugs beard"]
charMannerismChoice = random.randrange(0,len(charMannerismList))
charInteractionList = ["Argumentative",
                       "Arrogant",
                       "Blustering",
                       "Rude",
                       "Curious",
                       "Friendly",
                       "Honest",
                       "Hot tempered",
                       "Irritable",
                       "Ponderous",
                       "Quiet",
                       "Suspicious"]
charInteractionChoice = random.randrange(0,len(charInteractionList))
charBondList = ["Dedicated to fulfilling a personal life goal",
                "Protective of close family members",
                "Protective of colleagues or compatriots",
                "Loyal to a benefactor, patron, or employer",
                "Captivated by a romantic interest",
                "Drawn to a special place",
                "Protective of a sentimental keepsake",
                "Protective of a valuable possession",
                "Out for revenge"]
charBondChoice = random.randrange(0,len(charBondList))
charFlawList = ["Forbidden love or susceptibility to romance",
                "Enjoys decadent pleasures",
                "Arrogance",
                "Envies another creature's possessions or station",
                "Overpowering greed",
                "Prone to rage",
                "Has a powerful enemy",
                "Specific phobia",
                "Shameful or scandalous history",
                "Secret crime or misdeed",
                "Possession of forbidden lore",
                "Foolhardy bravery"]
charFlawChoice = random.randrange(0,len(charFlawList))



print("Name: ")
print("Age: ")
print("Race: ")
print("Sex: " + charSexList[charSexChoice])
print("Alignment: " + charAlignList[charAlignChoice])
print("Class/Ocupation: " + charClassList[charClassChoice])
print("Height: " + charHeightList[charHeightChoice])
print("Build: " + charBuildList[charBuildChoice])
print("Appearance: " + charAppearanceList[charAppearanceChoice])
print("Stats: S+0 D+0 C+0 I+0 W+0 C+0")
print("Talent: " + charTalentList[charTalentChoice])
print("Mannerism: " + charMannerismList[charMannerismChoice])
print("Interaction: " + charInteractionList[charInteractionChoice])
print("Ideal: ")
print("Bond: " + charBondList[charBondChoice])
print("Flaw/Secret: " + charFlawList[charFlawChoice])
print("Description: ")
