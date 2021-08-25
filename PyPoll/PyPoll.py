import os
import csv

filepath = os.path.join('resources', 'election_data.csv')

total_votes = 0

votes_per_candidate = {}

with open(filepath, 'r') as f:
    csv_reader = csv.reader(f, delimiter=',')
    next(csv_reader)

    for row in csv_reader:
        total_votes += 1
        if row[2] not in votes_per_candidate:
            votes_per_candidate[row[2]] = 1
        else:
            votes_per_candidate[row[2]] += 1   

print("Election Results")
print("-------------------------")
print("Total Votes: " + str(total_votes))
print("-------------------------")

for candidate, votes in votes_per_candidate.items():
    print(candidate + ": " + "{:.3%}".format(votes/total_votes) + "   (" +  str(votes) + ")")
    
print("-------------------------") 

winner = max(votes_per_candidate, key=votes_per_candidate.get)

print(f"Winner: {winner}")

f = open("election_results.txt", "w")
f.write("Election Results")
f.write('\n')
f.write("-------------------------")
f.write('\n')
f.write("Total Votes: " + str(total_votes))
f.write('\n')
f.write("-------------------------")
f.write('\n')

for candidate, votes in votes_per_candidate.items():
    f.write(candidate + ": " + "{:.3%}".format(votes/total_votes) + "   (" +  str(votes) + ")")
    f.write('\n')
  
f.write("-------------------------") 
f.write('\n')
f.write(f"Winner: {winner}")
f.write('\n')
