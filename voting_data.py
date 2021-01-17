#SKILL DRILL 
#Print each county and registered voter from the dictionary. The output should look like the following:
#Arapahoe county has 422,829 registered voters.
#Denver county has 463,353 registered voters.
#Jefferson county has 432,438 registered voters.

#Solution
voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, {"county":"Denver", "registered_voters": 463353}, {"county":"Jefferson", "registered_voters": 432438}]
voting_data = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county, voters in voting_data.items():
    print(f"{county} county has {voters:,} registered voters.")

#How to check what commands are available to use for each data type
dir(str)
dir(int)
dir(float)
dir(bool)
dir(list)
dir(tuple)
dir(dict)
dir(datetime)
