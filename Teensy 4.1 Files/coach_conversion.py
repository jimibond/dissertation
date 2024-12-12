import pandas as pd

# Load your CSV data into a DataFrame
df = pd.read_csv('coaches_cut_down.csv')

# create file for writing out
csv_outfile = open('coaches.txt', 'w')

# read each line
for index, row in df.iterrows():
        name = row['name']
        country = row['country']
        function = row['function']
        discipline = row['discipline']
        question= (f"Coach {name}?={name} is from {country} and is a {function} in {discipline}\n")
        csv_outfile.write(question)

csv_outfile.close();