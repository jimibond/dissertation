import random 
import json 
import pickle 
import numpy as np 
import nltk 
from keras.models import load_model 
from nltk.stem import WordNetLemmatizer 

lemmatizer = WordNetLemmatizer() 
  
# loading pre-trained files trainesd with chatbot_trainer.py
intents = json.loads(open("intents.json").read())   # json file with questions/answers
words = pickle.load(open('words.pkl', 'rb'))        # list of words used in training in model
classes = pickle.load(open('classes.pkl', 'rb'))    # classes used to classify questions (intents)
model = load_model('chatbotmodel.keras')            # trained model


# breaks up the sentence into individual words (tokens)
# and lemmatizes each word ( walking, walks, walked all become walk)
def clean_up_sentences(sentence): 
    sentence_words = nltk.word_tokenize(sentence) 
    sentence_words = [lemmatizer.lemmatize(word)  
                      for word in sentence_words] 
    return sentence_words 

# takes the input question, breaks it into words and checks against predefined list
# in words.pkl. Outputs a binary representation of the input 1 = known word 0 = unknown word 
def bag_of_words(sentence): 
    
    # takes the input and returns an array of words from the input
    sentence_words = clean_up_sentences(sentence) 
    # create an array the same length as the input, zero filled
    bag = [0]*len(words) 
    # check to see if word is known (in words.pkl) if it is known
    # set the corresponding bit in array to 1
    for w in sentence_words: 
        for i, word in enumerate(words): 
            if word == w: 
                bag[i] = 1
  
    # return a numpy array 
    return np.array(bag) 

# Uses model to try and understand the question (intent)
def predict_intent(sentence): 

    bow = bag_of_words(sentence) 
    # takes array and tries to predict intent
    # returns a list of possiblities with probablity of each being correct
    res = model.predict(np.array([bow]))[0] 
    # changing error threshold can narrow or widen possible answers
    ERROR_THRESHOLD = 0.2
    # iterate through results and find results with probabilty higher
    # than the error threshold
    results = [[i, r] for i, r in enumerate(res)  
               if r > ERROR_THRESHOLD] 
    results.sort(key=lambda x: x[1], reverse=True) 
    return_list = [] 
    # get a list of possible intents and probability 
    for r in results: 
        return_list.append({'intent': classes[r[0]], 
                            'probability': str(r[1])}) 
        return return_list 

# looks up predicted intent in json file and picks 
# one of the correct answers randomly  
def get_response(intents_list, intents_json): 
    
    # if not possible answers have been found return
    if not ints:
        return "Sorry, I don't understand."

    tag = intents_list[0]['intent'] 
    list_of_intents = intents_json['intents'] 
    result = "" 
    # find intent in json file
    for i in list_of_intents: 
        if i['tag'] == tag: 
              # prints a random answer 
            result = random.choice(i['responses'])   
            break
    return result 
  
print("Chatbot is up!")

# keep reading inputs
while True: 
    message = input("") 
    ints = predict_intent(message) 
    res = get_response(ints, intents) 
    print(res) 