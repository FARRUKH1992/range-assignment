# using random module 
# create list of moods
# mood for each day selct randomly
# print mood for each day in a single line string

import random

# List of moods
moods = ["Happy", "Sad", "Energetic", "Calm"]

# List of days of the week
days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# Loop through each day of the week
for day in days_of_week:
    # Randomly select a mood
    mood = random.choice(moods)
    # Print the mood for the day
    print(f"On {day}, you were feeling {mood.lower()}.")




# simulate mood tracker three different moods for each time of the day
# and for each time of the week 
# use random to select mood from the list and print it
# using random module again  


import random

# List of moods
moods = ["Happy", "Sad", "Energetic", "Calm", "Tired", "Excited"]

# List of times of the day
times_of_day = ["morning", "afternoon", "evening"]

# List of days of the week
days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# Loop through each day of the week
for day in days_of_week:
    # Loop through each time of the day
    for time in times_of_day:
        # Randomly select a mood
        mood = random.choice(moods)
        # Print the mood for the specific time of day
        print(f"On {day} {time} you were feeling {mood.lower()}.")