# discovery.py
# given an EVE log file, write relevant data into a csv file where
# each row contains the ID of a discovered body, followed by relevant details
# about the body

# TODO import the json and csv libraries
import json
import csv

# TODO import the log file into a dictionary

discovered = []
with open('Journal.181006065557.01.log') as f:
    for line in f:
        discovered.append(json.loads(line))
        f.close()

# print(discovered) #debug line

# TODO store the "Discovered" data subset into a new list
# pseudocode: for each top level item, if item.event = SellExplorationData,
# {for each item in "Discovered", store item string}

# Then, for each discovered item stored, search the json data for exact matches
# and add matching item as sublist to the discovered item

# TODO initialize the output csv file
# csv_f= open("discovered.csv","w+")
# TODO write the csv headers line based on the new list
# TODO iterate over the discovered list and write the body name followed by
# each attribute, separated by commas and ending with a semi-colon

# TODO close the csv file
