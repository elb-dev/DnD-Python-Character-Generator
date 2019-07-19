import random

def bellChoice():
    #This whole thing is a fricken hack.
    #It returns 0-13, on a bell curve. Chances are highest you'll get 6 or 7, being the center of the bell curve.
    i = random.randrange(0,1000)
    i += 1
    if i == 1:
        return 0
    if i > 1 and i <= 6:
        return 1
    if i > 6 and i <= 23:
        return 2
    if i > 23 and i <= 67:
        return 3
    if i > 67 and i <= 159:
        return 4
    if i > 159 and i <= 309:
        return 5
    if i > 309 and i <= 500:
        return 6
    if i > 500 and i <= 691:
        return 7
    if i > 691 and i <= 841:
        return 8
    if i > 841 and i <= 933:
        return 9
    if i > 933 and i <= 977:
        return 10
    if i > 977 and i <= 994:
        return 11
    if i > 994 and i <= 999:
        return 12
    if i > 999:
        return 13


charAlphList = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",]
charFirstAlphChoice = random.randrange(0,len(charAlphList))
charLastAlphChoice = random.randrange(0,len(charAlphList))

charSexList = ["Male","Female"]
charSexChoice = random.randrange(0,len(charSexList))

charGoodOrEvilList = ["Good", "Neutral", "Evil"]
charGoodOrEvilChoice = random.randrange(0,len(charGoodOrEvilList))

charLawfulOrChaoticList = ["Lawful", "Neutral", "Chaotic"]
charLawfulOrChaoticChoice = random.randrange(0,len(charLawfulOrChaoticList))

charClassList = ["Blacksmith",
                 "Butcher",
                 "Baker"]
charClassChoice = random.randrange(0,len(charClassList))

charHeightList = ["Insanely Short",
                  "Very Short",
                  "Short",
                  "Somewhat Short",
                  "Shorter Than Average",
                  "Slightly Below Average",
                  "Average-",
                  "Average+",
                  "Slightly Above Average",
                  "Taller Than Average",
                  "Somewhat Tall",
                  "Very Tall",
                  "Insanely Tall",]
charHeightChoice = bellChoice()

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

#Ideal would go here

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



print("Name: " + charAlphList[charFirstAlphChoice] + " " + charAlphList[charLastAlphChoice])
print("Age: ")
print("Race: ")
print("Sex: " + charSexList[charSexChoice])
print("Alignment: " + charLawfulOrChaoticList[charLawfulOrChaoticChoice] + " " + charGoodOrEvilList[charGoodOrEvilChoice])
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
