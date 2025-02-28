# Supporting code and script for dissertation

## Pi 5 Files dir

### Python files to train the model, use the model and test the model

[chatbot_main.py](../main/Pi%205%20Files/chatbot_main.py)  
[chatbot_main_test.py](../main/Pi%205%20Files/chatbot_main_test.py)  
[chatbot_trainer.py](../main/Pi%205%20Files/chatbot_trainer.py)  

Need to install

nltk - pip install --user -U nltk

### json file of question & answers for training

[intents.json](../main/Pi%205%20Files/intents.json)  

### Question & answer files for accuracy test. Answers from chatbot

[intents_question.txt](../main/Pi%205%20Files/intents_question.txt)  
[intent_answers.txt](../main/Pi%205%20Files/intent_answers.txt)  
                   

### Python file to read json file and create questions & answers

[intents_question.py](../main/Pi%205%20Files/intents_question.py) 

### Output files from training model (kearas) classes and words (pkl)

[chatbotmodel.keras](../main/Pi%205%20Files/chatbotmodel.keras)   
[classes.pkl](../main/Pi%205%20Files/classes.pkl)   
[words.pkl](../main/Pi%205%20Files/words.pkl) 

## Teensy 4.1 dir

### Files on SD card for Teensy 4.1 to read for answers

[athletes.txt](../main/Teensy%204.1%20Files/athletes.txt)  
[coaches.txt](../main/Teensy%204.1%20Files/coaches.txt)  
[medallists.txt](../main/Teensy%204.1%20Files/medallists.txt) 

### Original csv files used to generate questions & answers

[athletes_cut_down.csv](../main/Teensy%204.1%20Files/athletes_cut_down.csv)  
[coaches_cut_down.csv](../main/Teensy%204.1%20Files/coaches_cut_down.csv)  
[medallists.csv](../main/Teensy%204.1%20Files/medallists.csv) 

### Python files to convert csv file into questions & answers

[athletes_conversion.py ](../main/Teensy%204.1%20Files/athletes_conversion.py)    
[coach_conversion.py](../main/Teensy%204.1%20Files/coach_conversion.py)   
[medallists_conversion.py](../main/Teensy%204.1%20Files/medallists_conversion.py) 

### Python file to convert question & answers into two files for accuracy testing

[olympic_test.py](../main/Teensy%204.1%20Files/olympic_test.py) 

### Question & answer files for accuracy testing

[athletes_answer.txt](../main/Teensy%204.1%20Files/athletes_answer.txt)  
[athletes_question.txt](../main/Teensy%204.1%20Files/athletes_question.txt) 

### Answers from chatbot from accuracy testing

[athletes_answers_chatbot.txt](../main/Teensy%204.1%20Files/athletes_answers_chatbot.txt) 

### Arduino code

[masters.ino](../main/Teensy%204.1%20Files/masters.ino) 

## TeensyFlow dir

### PlatformIO config  file

[platformio.ini](../main/TeensyFlow/platformio.ini) 

### Under lib dir is the files for TensorFlow Lite and required librairies
 
