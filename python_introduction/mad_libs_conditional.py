print("Welcome to Conditional Mad Libs!")
print("Please provide the following words:")

adjective1 = input("Enter an adjective (e.g., 'beautiful', 'gloomy'): ").strip().lower()
noun_plural = input("Enter a plural noun (e.g., 'trees', 'flowers'): ").strip().lower()
verb_past_tense = input("Enter a verb in past tense (e.g., 'ran', 'jumped'): ").strip().lower()
adjective2 = input("Enter another adjective (e.g., 'sparkling', 'muddy'): ").strip().lower()
animal = input("Enter an animal (e.g., 'monkey', 'lion', 'elephant'): ").strip().lower()
verb_ing = input("Enter a verb ending in -ing (e.g., 'singing', 'running'): ").strip().lower()
adjective3 = input("Enter a final adjective (e.g., 'amazing', 'terrible'): ").strip().lower()

story = f"\n--- Your Wild Adventure ---\n"
story += f"On a {adjective1} day, a peculiar adventure began.\n"

if adjective1 == "beautiful":
    story += "The sun was shining brightly, and everything felt perfect. "
elif adjective1 == "gloomy":
    story += "Heavy clouds hung low, hinting at a mystical journey. "
else:
    story += "It was an ordinary day, but about to become extraordinary. "

story += f"I packed my bags and {verb_past_tense} to a hidden forest filled with {noun_plural}. "

story += f"Deep inside, I spotted a {adjective2} {animal} {verb_ing} freely.\n"
if animal == "lion":
    story += "Its roar echoed through the jungle, sending shivers down my spine! "
elif animal == "monkey":
    story += "It chattered excitedly, inviting me to play. "
elif animal == "elephant":
    story += "Its massive size was awe-inspiring, and it gently trumpeted a greeting. "
else:
    story += "What a unique creature to encounter in the wild! "

story += f"What an absolutely {adjective3} experience!\n"
story += f"-------------------------\n"

print(story)