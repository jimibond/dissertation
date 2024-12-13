# Supporting code and script for dissertation

## Pi 5 Files dir

### Python files to train the model, use the model and test the model

[chatbot_main.py](https://github.com/jimibond/dissertation/blob/main/Pi%205%20Files/chatbot_main.py)  
[chatbot_main_test.py](https://github.com/jimibond/dissertation/blob/main/Pi%205%20Files/chatbot_main_test.py)  
[chatbot_trainer.py](https://github.com/jimibond/dissertation/blob/main/Pi%205%20Files/chatbot_trainer.py)  

Need to install

nltk - pip install --user -U nltk

### json file of question & answers for training

[intents.json](https://github.com/jimibond/dissertation/blob/main/Pi%205%20Files/intents.json)  

### Question & answer files for accuracy test. Answers from chatbot

[intents_question.txt](https://github.com/jimibond/dissertation/blob/main/Pi%205%20Files/intents_question.txt)  
[intents_answers.txt](https://github.com/jimibond/dissertation/blob/main/Pi%205%20Files/intents_answers.txt)  

### Python file to read json file and create questions & answers

[intents_question.py](https://github.com/jimibond/dissertation/blob/main/Pi%205%20Files/intents_question.py) 

### Output files from training model (kearas) classes and words (pkl)

[chatbotmodel.keras](https://github.com/jimibond/dissertation/blob/main/Pi%205%20Files/chatbotmodel.keras)   
[classes.pkl](https://github.com/jimibond/dissertation/blob/main/Pi%205%20Files/classes.pkl)   
[words.pkl](https://github.com/jimibond/dissertation/blob/main/Pi%205%20Files/words.pkl) 

## Teensy 4.1 dir

### Files on SD card for Teensy 4.1 to read for answers

[athletes.txt](https://github.com/jimibond/dissertation/blob/main/Teensy%204.1%20Files/athletes.txt)  
[coaches.txt](https://github.com/jimibond/dissertation/blob/main/Teensy%204.1%20Files/coaches.txt)  
[medalistes.txt](https://github.com/jimibond/dissertation/blob/main/Teensy%204.1%20Files/medalistes.txt) 

### Original csv files used to generate questions & answers

[athletes_cut_down.csv](https://github.com/jimibond/dissertation/blob/main/Teensy%204.1%20Files/athletes_cut_down.csv)  
[coaches_cut_down.csv](https://github.com/jimibond/dissertation/blob/main/Teensy%204.1%20Files/coaches_cut_down.csv)  
[medallists.csv](https://github.com/jimibond/dissertation/blob/main/Teensy%204.1%20Files/medallists.csv) 

### Python files to convert csv file into questions & answers

[athletes_conversion.py ](https://github.com/jimibond/dissertation/blob/main/Teensy%204.1%20Files/athletes_conversion.py)    
[coach_conversion.py](https://github.com/jimibond/dissertation/blob/main/Teensy%204.1%20Files/coach_conversion.py)   
[medallists_conversion.py](https://github.com/jimibond/dissertation/blob/main/Teensy%204.1%20Files/medallists_conversion.py) 

### Python file to convert question & answers into two files for accuracy testing

[olympic_test.py](https://github.com/jimibond/dissertation/blob/main/Teensy%204.1%20Files/olympic_test.py) 

### Question & answer files for accuracy testing

[athletes_answer.txt](https://github.com/jimibond/dissertation/blob/main/Teensy%204.1%20Files/athletes_answer.txt)  
[athletes_question.txt](https://github.com/jimibond/dissertation/blob/main/Teensy%204.1%20Files/athletes_question.txt) 

### Answers from chatbot from accuracy testing

[athletes_answer_chatbot.txt](https://github.com/jimibond/dissertation/blob/main/Teensy%204.1%20Files/athletes_answer_chatbot.txt) 

### Arduino code

[masters.ino](https://github.com/jimibond/dissertation/blob/main/Teensy%204.1%20Files/masters.ino) 

## TeensyFlow dir

### PlatformIO config  file

[platformio.ini](https://github.com/jimibond/dissertation/blob/main/TeensyFlow/platformio.ini) 

### Under lib dir is the files for TensorFlow Lite and required librairies
 
