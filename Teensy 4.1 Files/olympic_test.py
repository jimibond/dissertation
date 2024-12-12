

out_questions = open("athletes_question.txt", "a")
out_answers = open("athletes_answer.txt", "a")

# Open the file in read mode
with open('athletes.txt', 'r') as file:
    # Read each line in the file
    for line in file:
        question, answer = line.split("=")
        out_questions.write(question)
        out_questions.write("\n")
        out_answers.write(answer)