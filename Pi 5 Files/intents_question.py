import json 

# reading the json.intense file 
intents = json.loads(open("intents.json").read()) 
out_file = open("intents_question.txt", "a")

for intent in intents['intents']: 
	for pattern in intent['patterns']: 
            out_file.write(pattern)
            out_file.write("\n")
		

out_file.close()