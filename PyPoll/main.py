#PYTHON HW #2 - PyPoll

# Import csv to read
import os
import csv

# define paths
cwd=os.getcwd()
print(cwd)

PyPollpath = os.path.join(cwd,"Resources","election_data.csv")
PyPolloutput = os.path.join(cwd,"analysis","election_analysis.txt")

# Lists to store data
Candidate_List =[]
Candidate_Votes =[]
Candidate_Votes_Pct =[]


# Read csvfile
with open(PyPollpath) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    print(csvreader)

    # Store header row
    csvheader = next(csvreader)

    # Assign initial values
    Init = 0
    Total_Votes=0

    for row in csvreader:

        # The total number of votes cast
        Total_Votes += 1

        # A complete list of candidates who received votes
        if row[2] not in Candidate_List:
            Candidate_List.append(row[2])
            Candidate_Votes.append(Init)
            Candidate_Votes_Pct.append(Init)

        # The total number of votes each candidate won   
        for i in range(len(Candidate_List)):
                
            if row[2] == Candidate_List[i]:
                Candidate_Votes[i] += 1
                  
    # The percentage of votes each candidate won
    for i in range(len(Candidate_List)):
        Candidate_Votes_Pct[i] = round((Candidate_Votes[i]/Total_Votes)*100,3)
    
    # The winner of the election based on popular vote.
    Winner= Candidate_List[Candidate_Votes.index(max(Candidate_Votes))]

    print(Candidate_List)
    print(Candidate_Votes)
    print(Candidate_Votes_Pct)
    print(Total_Votes)
    print(Winner)

# Summarise output 
summary = (
   f"Election Results\n"
   f"-------------------------\n"
   f"Total Votes: {Total_Votes}\n"
   f"-------------------------\n"
   f"{Candidate_List[0]}: {Candidate_Votes_Pct[0]:.3f}% ({Candidate_Votes[0]})\n"
   f"{Candidate_List[1]}: {Candidate_Votes_Pct[1]:.3f}% ({Candidate_Votes[1]})\n"
   f"{Candidate_List[2]}: {Candidate_Votes_Pct[2]:.3f}% ({Candidate_Votes[2]})\n"
   f"{Candidate_List[3]}: {Candidate_Votes_Pct[3]:.3f}% ({Candidate_Votes[3]})\n"
   f"-------------------------\n"
   f"Winner: {Winner}\n"
   f"-------------------------\n")

# output to terminal
print(summary)
    
# output to txt
with open(PyPolloutput, 'w') as txtfile:
    txtfile.write(summary)