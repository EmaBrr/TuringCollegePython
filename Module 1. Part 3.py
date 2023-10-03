# Lesson 6: Applying Cluster Analysis to a Real Dataset (C2, 1.5)

# We will analyse congressional dataset with key means

from typing import NamedTuple, DefaultDict
import csv
# from means import k_means, assign_data
from collections import defaultdict # namedtuple - removed when added above with capital letters, defaultdict for data accumulation
from pprint import pprint
import glob

# Senator = namedtuple('Senator', ['name', 'party', 'state'])

Senator = NamedTuple('Senator', [('name', str), ('party', str), ('state', str)])
VoteValue = int
# Load the votes which were arranges by topic and acumulate votes by senator
vote_value= {'Yea': 1, 'Nay' : -1, 'Not Voting' : 0}   #Type: Dict[str, VoteValue]
accumulated_record = defaultdict(list)                  #Type: DefaultDict[Senator, List[VoteValue]]
for filename in glob.glob('congress_vot*.csv'):
    # with open('congress_votes_118-2023_h515.csv', encoding='utf-8') as f:
    with open(filename, encoding='utf-8') as f:  
        reader = csv.reader(f)
        vote_topic = next(reader)
        headers = next(reader)
        for person, state, district, vote, name, party in reader:
            senator = Senator(name, party, state)
            accumulated_record[senator].append(vote_value[vote]) # vote_value is a list, but we will need a tuple since we will use keys

# Transform the record into plain dict that maps to tuple of votes

record = {senator: tuple(votes) for senator, votes in accumulated_record.items()} # Type: Dict[Senator, VoteHistory]]
pprint(record, width=500)

# Use k-means to locate the cluster centroids from pattern of votes, asssign each senator to the nearest cluster
# centroids = k_means(record.values())
# pprint(accumulated_record, width=500)

# ['person', 'state', 'district', 'vote', 'name', 'party'] headers

# print(senator[0]) # Rep. Jennifer McClellan [D]
# print(senator.name) # Rep. Jennifer McClellan [D]

