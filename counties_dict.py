#Make a dictionary called counties_dict
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

#to get only keys from dict using for loop:To get only the keys from a dictionary using a for loop, the loop can be written like we are iterating over a list or tuple.
for county in counties_dict:
    print(county)

#can also use the keys method to get the same result 
for county in counties_dict.keys():
    print(county)

#GET THE VALUES OF A DICTIONARY
#To get the values of a dictionary, we iterate over the dictionary using the values() method, just like we used the keys() method.

#For the counties list, modify the for loop and use the key, county to reference the value.
for voters in counties_dict.values():
    print(voters)

#For the counties list, modify the for loop and use the key, county to reference the value.
for county in counties_dict:
    print(counties_dict[county])

#Another method we can use to get the values of a key is to use the get() method on the dictionary in the for loop.
for county in counties_dict:
    print(counties_dict.get(county))


#GET THE KEY VALUE PAIRS
#Finally, if we want to print the key-value pair of the dictionary, we use the items() method in the for loop

for county, voters in counties_dict.items():
    print(county, voters)
#SKILL DRILL 
#Print each county and registered voter form the counties dictionary so that the output looks like this:
#Arapahoe county has 422829 registered voters.
#Denver county has 463353 registered voters.
#Jefferson county has 432438 registered voters.

#SOLUTION:
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county, voters in counties_dict.items():
    print(f"{county} county has {voters:,} registered voters.")

#The solution is using the f-strings to 
#LISTS OF DICTIONARIES
#First, create an empty list called voting_data:
voting_data = []
voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
voting_data.append({"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Jefferson", "registered_voters": 432438})

print(voting_data)

#GET EACH DICTIONARY IN A LIST OF DICTIONARIES
#To print each dictionary in voting_data, use the standard format for iterating over the list of dictionaries with a for loop:
for county_dict in voting_data:
    print(county_dict)

#Since this is a list of dictionaries, use the range() function to iterate over the list

#How would you use the range() function to iterate over the list of dictionaries and print the counties in voting_data?
#Answer:
for i in range(len(voting_data)):

      print(voting_data[i])

#GET THE VALUES FROM A LIST OF DICTIONARIES
#To retrieve only the values we need to use a nested for loop with voting_data
#First, use the for loop: for county_dict in voting_data: to retrieve each dictionary. Then, in the second for loop, use the values() method on the variable county_dict to reference the data in the second for loop in order to get each value:

for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

#HHow would you retrieve the number of registered voters from each dictionary?

#Answer:

for county_dict in voting_data:

     print(county_dict['registered_voters'])

#To print just tje county name from each dictionary, we can use county_dict['county'] in the print statement for the 'for loop':
for county_dict in voting_data:
    print(county_dict['county'])

#PRINTING FORMATS
#1. Printing a string displayed between quotes
print("Arapahoe and Denver are not in the list of counties.")

#2. Printing A string with integer values converted to a string using concatenation with the "+" sign:
#print("Your interest for the year is $" + str(interest))

#F-strings: Formatted String Literals
# EXAMPLE code we wrote to calculate the percentage of votes using f-string literals.
#Original code

#Code edited with f-strings


#3.2.8. Decision Statements
#Retrieving data based on a condition is known as a decision statement. Used to retrieve data from large dataset that meets certain criteria

#3.2.8. Decision Statements: Algorithm calculating the precentage of votes a candidate recieves in an election:
# How many votes did you get?

#  Total votes in the election

# Calculate the percentage of votes you received.


#If we want to use a floating point decimal we have to sub int() with float()

#3.2.11. Using Multiline F-Strings as Printing Format: Used to print multiple lines and create a message to be printed to screen
candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes:,} number of votes. "
    f"The total number of votes in the election was {total_votes:,}. "
    f"You received {candidate_votes / total_votes * 100:.f2}% of the total votes.")

print(message_to_candidate)

#Format floating point decimals

#SKILL DRILL 
voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, {"county":"Denver", "registered_voters": 463353}, {"county":"Jefferson", "registered_voters": 432438}]
voting_data = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county, voters in voting_data.items():
    print(f"{county} county has {voters:,} registered voters.")

# 3.4.1. The CSV Module
#A variable, like a dictionary {'key':'value'}, for example the counties_dict dictionary. The dir() function will return all the functions available on that variable.
#run code into interperter to see available functions
>>> dir({"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438})