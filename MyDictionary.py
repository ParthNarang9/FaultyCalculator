d1 = {"Mutable":"Items that can be changed", 
      "Immutable":"Items that can't be changed", 
      "Affiliate":"Officially attached or connected to an organization", 
      "Beginner":"A person just starting to learn a skill or take part in an activity", 
      "Bitcoin":"https://en.wikipedia.org/wiki/Bitcoin" }

print("Welcome to our Dictionary")
print("Type the word you want to search")
a = input()
print("Your word meaning is here")
print(d1.get(a))