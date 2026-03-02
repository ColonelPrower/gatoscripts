#script for an idea of a project
import random

vocals = "aeiou"
consonants = "bcdfghjklmnpqrstvwxyz"
wordsize = random.randrange(3,15)
word = ""
for x in range(0,wordsize):
    if random.choice(['vocal','consonant']) == 'vocal':
        word += random.choice(vocals)
    else:
        word += random.choice(consonants)

print(f"your word is: {word}, u like it???")
