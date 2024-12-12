Supporting code and script for dissertation


Pi 5 Files dir

Python files to train the model, use the model and test the model

chatbot_main.py 
chatbot_main_test.py 
chatbot_trainer.py

Need to install

nltk - pip install --user -U nltk

json file of question/answers for training

intents.json

question answer files for accuracy test

intents_question.txt
intents_answers.txt

Python file to read jsopn file and create questiosn/answers

intents_question.py

output files from training model (kearas) classes and words (pkl)

chatbotmodel.keras 
classes.pkl
words.pkl

Teensy 4.1 dir

Files on SD card for Teensy 4.1 to read for answers

athletes.txt
coaches.txt
medalistes.txt

Original csv files used to generate questions/answers

athletes_cut_down.csv
coaches_cut_down.csv
medallists.csv

Python files to convert csv file into questions/answers

athletes_conversion.py 
coach_conversion.py 
medallists_conversion.py 

Python file to convert question/answers into two files for accuracy testing

olympic_test.py

Question/answer files for accuracy testing

athletes_answer.txt
athletes_question.txt

Answers from chatbot from accuracy testing

athletes_answer_chatbot.txt

Arduino code

masters.ino 

TeensyFlow dir

PlatformIO config  file

platformio.ini

Under lib dir is the files for TensorFlow Lite and required librairies 




