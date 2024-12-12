import pandas as pd

# Load your CSV data into a DataFrame
df = pd.read_csv('athletes_cut_down.csv')

# create file for writing out
csv_outfile = open('athletes.txt', 'w')

# read each line
for index, row in df.iterrows():
        name = row['name']
        country = row['country']
        discipline = row['discipline']
        # remove unwanted characters
        discipline= discipline.replace('[', '') 
        discipline= discipline.replace(']', '')
        discipline= discipline.replace("'", '')
        question= (f"Tell me about {name}={name} is from {country} and competes in {discipline}\n")
        csv_outfile.write(question)

csv_outfile.close();