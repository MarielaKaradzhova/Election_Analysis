# Election_Analysis

## Project Overview
A Colorado Board of Elections employee has given me the tasks outlined below with the purpose of completing the election audit of a recent local congressional election.


1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.

## Resources
- Data Source: election_results.csv
- Software: Python 3.7.6, Visual Studio Code, 1.52.1

## Summary
The analysis of the election show that:
- There were 369,711 votes cast in the election.
- The candidates were:
    - Charles Casper Stockham
    - Diana DeGette
    - Raymon Anthony Doane
- The candidate results were:
    - Charles Casper Stockham received 23.0% of the vote and 85,213 number of votes.
    - Diana DeGette received 73.8% of the vote and 272,892 number of votes.
    - Raymon Anthony Doane received 3.1% of the vote and 11,606 number of votes.
- The winner of the election was:
    - Diana DeGette, who received 73.8% of the vote and 272,892 number of votes.

## Challenge Overview
After submitting the election audit results to the election commission, the employee requested some additional data to complete the audit. 

# Additional Data Request:
1.Calculate the voter turnout for each county.
2.Calculate the percentage of votes from each county out of the total count.
3.Determine the county with the highest turnout.

### Resources
- Data Source: election_results.csv
- Software: Python 3.7.6, Visual Studio Code, 1.52.1

## Challenge Summary
### Overview of Election Aduit
The purpose of the Election Aduit analysis was to determine the important outcomes associated with the data collected from the local congressional election. The dat source used to perform the analysis is located above in "Resources". Specifically, the important outcomes were:
1. To calculate the total number of votes cast in the election.
2. Gather a complete list of candidates who received votes in the election.
3. Calculate the total number of votes each candidate received in the election.
4. Calculate the percentage of votes each candidate won in the election.
5. Determine the winner of the election based on popular vote, (determine the highest vote count for that candidate).

In addition, using the data provided it was important to find out some geographic information based on location and vote turnout. Where the following questions were answered:
6. What was the voter turnout for each county?
7. What was the percentage of votes from each county out of the total count?
8. Which county had the highest turnout?

### Election Audit Results
- How many votes were cast in this congressional election?
    There were 369,711 votes cast in tis congressional election.
- Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.
    Below is a breakdown of the total votes cast in the election based on county name with respective percentages of votes and number of Votes:
    Jefferson county accounted for 10.5% of the total votes, with 38,855 votes.
    Denver county accounted for 82.8% of the total votes, with 306,055 votes.
    Arapahoe county accounted for just 6.7%  of the total votes, with only 4,801 votes.


- The county with the largest number of votes was Denver, with 82.8% percent of the total votes cast and total votes amounting to 306,055.

- Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.

    The candidates in the congressional election were:
    - Charles Casper Stockham
    - Diana DeGette
    - Raymon Anthony Doane

    Results with number of votes and percentage of total votes for each candidate in the congresional election are displayed below:
    - Charles Casper Stockham received 23.0% of the vote and 85,213 number of votes.
    - Diana DeGette received 73.8% of the vote and 272,892 number of votes.
    - Raymon Anthony Doane received 3.1% of the vote and 11,606 number of votes.
    
- Which candidate won the election, what was their vote count, and what was their percentage of the total votes?

The winner of the election was Diane Degette, who won the election with 272,892, equivalent to 73.8% of the vote.

### Election Audit Results
In a summary statement, provide a business proposal to the election commission on how this script can be used—with some modifications—for any election. Give at least two examples of how this script can be modified to be used for other elections.

####Summary Statement 
The code used to analyze the results of the local congressional election can be used with other election results using simple modifications of variables to yield the results needed to complete an election audit. 

For example, simply accessing a different data source in the code can set up the analysis for another election. See the image below:
![](https://github.com/MarielaKaradzhova/Election_Analysis/blob/main/Resources/path_modification.png) 

Specifically, instead of accessing the "election_results.csv", another file can be accessed to easily answer the same questions we did with the local congressional election (See: Summary and Challenge Summary).

If there were other questions that needed analyzing, then we can simply modify variable names to determine the answers we are trying to find. See sample from code below before further explanation.

![](https://github.com/MarielaKaradzhova/Election_Analysis/blob/main/Resources/modifications_variables.png) 

In this image we can see that a list  "county_options", was created to store all the county names available from the data source. In another election this variable can be modified to fit the description of the location where ballots were collected. For example, there may be a provincial election that includes States or Provinces. Therefore, we would modify the variable as "province_options" or, "state_options" to yield the results we are looking for and organize them in a list to further analyze.

These simple yet powerful modifications make our code incredibly useful and versatile, while providing a solid foundation and code structure that can yield accurate results with minimal errors when executed.


