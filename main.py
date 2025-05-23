import random
import pickle
import numpy as np
import nltk
from nltk.stem import WordNetLemmatizer
from tensorflow.keras.models import load_model
from pymongo import MongoClient

nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')

lemmatizer = WordNetLemmatizer()

# Connect to MongoDB and load intents
client = MongoClient("mongodb://localhost:27017/")
db = client["chatbotdb"]
collection = db["intents"]
intents_cursor = collection.find()
intents = {"intents": list(intents_cursor)}

words = pickle.load(open('words.pkl', 'rb'))
classes = pickle.load(open('classes.pkl', 'rb'))
model = load_model('chatbotmodel.h5')

global res
res = None

def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word) for word in sentence_words]
    return sentence_words

def bag_of_words(sentence):
    sentence_words = clean_up_sentence(sentence)
    bag = [0] * len(words)
    for w in sentence_words:
        for i, word in enumerate(words):
            if word == w:
                bag[i] = 1
    return np.array(bag)

def predict_class(sentence):
    bow = bag_of_words(sentence)
    global res
    res = model.predict(np.array([bow]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({'intent': classes[r[0]], 'probability': str(r[1])})
    return return_list

def get_response(intents_list, intents_json):
    tag = intents_list[0]['intent']
    list_of_intents = intents_json['intents']
    result = ""
    for i in list_of_intents:
        if i['tag'] == tag:
            result = random.choice(i['responses'])
            break
    return result

print("|============= Welcome to Basic Banking Chatbot System! =============|")
print("|============================== Feel Free ============================|")
print("|================================== To ===============================|")
print("|=============== Ask your any query about Banking proccesses ================|")
while True:
    message = input("| You: ")
    if message.lower() in ["bye", "goodbye"]:
        ints = predict_class(message)
        res = get_response(ints, intents)
        print("| Bot:", res)
        print("|===================== The Program End here! =====================|")
        exit()
    else:
        ints = predict_class(message)
        res = get_response(ints, intents)
        print("| Bot:", res)
