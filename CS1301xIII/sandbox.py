phrase = "HULK MAD"
phrase = phrase.lower()
phrase = phrase.title()
cut_phrase = phrase[:5]
new_phrase = ""
 
for char in phrase[5:]:
    if char == "m":
         new_phrase = cut_phrase + "Hungry"
    elif char == "a":
        new_phrase = cut_phrase + "Angry"
    elif char == "d":
         new_phrase = cut_phrase + "Smash"
    print(new_phrase)