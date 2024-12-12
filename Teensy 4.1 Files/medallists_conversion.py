import pandas as pd

# Load your CSV data into a DataFrame
df = pd.read_csv('medallists.csv')

# create file for writing out
csv_outfile = open('medallists.txt', 'w')

# read each line
for index, row in df.iterrows():
        medal_type = row['medal_type']
        name = row['name']
        country = row['country']
        discipline = row['discipline']
        event = row['event']
        question= (f"Who won {medal_type} in {discipline} {event}?={name} won the  {medal_type} in {event}\n")
        csv_outfile.write(question)

csv_outfile.close();