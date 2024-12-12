# importing the required modules. 
import random 
import json 
import pickle 
import numpy as np 
import nltk 

# need to download these once
#nltk.download('punkt_tab')
#nltk.download('punkt')
#nltk.download('wordnet')

from keras.models import Sequential 
from nltk.stem import WordNetLemmatizer 
from keras.layers import Dense, Activation, Dropout 
from keras.optimizers import SGD 
from tensorflow.keras.preprocessing.sequence import pad_sequences


lemmatizer = WordNetLemmatizer() 

# reading the json.intents file with quesstion/answers 
intents = json.loads(open("intents.json").read()) 

# creating empty lists to store data 
words = [] 
classes = [] 
documents = [] 
ignore_letters = ["?", "!", ".", ","]  # list of punctuation to ignore
for intent in intents['intents']: 
	for pattern in intent['patterns']: 
		# separating sentence into words
		# and adding them to words list 
		word_list = nltk.word_tokenize(pattern) 
		words.extend(word_list) 
		
		# associating words with respective tags (categrories) in json file
		documents.append(((word_list), intent['tag'])) 

		# appending the tags (categrories) to the class list 
		if intent['tag'] not in classes: 
			classes.append(intent['tag']) 

# storing the base words or lemma 
# walking, walks, walked all become walk
words = [lemmatizer.lemmatize(word) 
		for word in words if word not in ignore_letters] 
words = sorted(set(words)) 

# saving the words and classes list to binary files 
pickle.dump(words, open('words.pkl', 'wb')) 
pickle.dump(classes, open('classes.pkl', 'wb')) 


# we need numerical values of the 
# words because a neural network 
# needs numerical values to work with 
training = [] 
output_empty = [0]*len(classes) 
for document in documents: 
    bag = [] 
    word_patterns = document[0] 
    word_patterns = [lemmatizer.lemmatize( 
        word.lower()) for word in word_patterns] 
    for word in words: 
        bag.append(1) if word in word_patterns else bag.append(0) 
          
    # making a copy of the output_empty 
    output_row = list(output_empty) 
    output_row[classes.index(document[1])] = 1
    training.append([bag, output_row]) 
random.shuffle(training) 

# Separate the first and second lists
first_list = [x[0] for x in training]
second_list = [x[1] for x in training]

# Find the maximum length across both lists
max_len = max(max(len(seq) for seq in first_list), max(len(seq) for seq in second_list))

# Pad both sequences to ensure consistent shape
padded_first_list = pad_sequences(first_list, maxlen=max_len, padding='post', dtype='float32')
padded_second_list = pad_sequences(second_list, maxlen=max_len, padding='post', dtype='float32')

# Combine them into a single numpy array
training_np = np.array(list(zip(padded_first_list, padded_second_list)))
  
# splitting the data 
train_x = list(training_np[:, 0]) 
train_y = list(training_np[:, 1]) 

# creating a Sequential machine learning model with three layers (neural netowrok)
model = Sequential() 
# activation layer using rectified linear unit (relu)
model.add(Dense(128, input_shape=(len(train_x[0]), ), 
                activation='relu')) 
# dropout is when some neurons from the model are temporally ignored to harden the model training
model.add(Dropout(0.5)) 
# hidden layer, sits betweem input and output and is called hidden as we can't see what is going on
model.add(Dense(64, activation='relu')) 
model.add(Dropout(0.5)) 
# output layer with softmax, softmax ensures probabilities sum to 1
model.add(Dense(len(train_y[0]),  
                activation='softmax')) 
  
# compiling (configure) and training the model 
# Stochastic gradient descent (SGD) is an optimization method
sgd = SGD(learning_rate=0.01, momentum=0.9, nesterov=True) 
# sets up the model for optimization
model.compile(loss='categorical_crossentropy', 
              optimizer=sgd, metrics=['accuracy']) 
# two arrays is teh input training data, 200 iterations off the dataset, process 
# data in batches of 5. Turn verbose output on. 
hist = model.fit(np.array(train_x), np.array(train_y), 
                 epochs=200, batch_size=5, verbose=1) 

# saving the model 
model.save("chatbotmodel.keras") 
  
# print statement to show the  
# successful training of the Chatbot model 
print("Yay!") 