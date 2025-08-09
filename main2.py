import random
import json
import pickle
import numpy as np
import streamlit as st
import nltk
from nltk.stem import WordNetLemmatizer
from tensorflow.keras.models import load_model
from googletrans import Translator
from langdetect import detect

lemmatizer = WordNetLemmatizer()

# Load intents and model
intents = json.loads(open('intents.json', encoding='utf-8').read())
words = pickle.load(open('words.pkl', 'rb'))
classes = pickle.load(open('classes.pkl', 'rb'))
model = load_model('chatbotmodel.h5')

# Translator setup
translator = Translator()

def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
    return sentence_words

def bow(sentence, words):
    sentence_words = clean_up_sentence(sentence)
    bag = [0] * len(words)
    for s in sentence_words:
        for i, w in enumerate(words):
            if w == s:
                bag[i] = 1
    return np.array(bag)

def predict_class(sentence):
    ERROR_THRESHOLD = 0.25  # lowered for better matching
    p = bow(sentence, words)
    res = model.predict(np.array([p]))[0]
    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]

    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({"intent": classes[r[0]], "probability": str(r[1])})
    return return_list

def get_response(intents_list, intents_json):
    if not intents_list:
        return "Sorry, I didn't understand that. Could you rephrase?"
    tag = intents_list[0]['intent']
    list_of_intents = intents_json['intents']
    for i in list_of_intents:
        if i['tag'] == tag:
            return random.choice(i['responses'])
    return "I'm not sure about that. Can you try asking differently?"

# Streamlit UI
st.title("Basic Banking Chatbot System")
st.write("Feel free to ask any queries about banking processes in **any Indian language**.")

user_input = st.text_input("You:")

if st.button("Send") and user_input.strip() != "":
    try:
        # 1. Detect user language
        user_lang = detect(user_input)

        # 2. Translate to English if needed
        if user_lang != 'en':
            translated_input = translator.translate(user_input, src=user_lang, dest='en').text
        else:
            translated_input = user_input

        # 3. Get bot response in English
        response_intents = predict_class(translated_input)
        bot_response_en = get_response(response_intents, intents)

        # 4. Translate back to user’s language if needed
        if user_lang != 'en':
            bot_response = translator.translate(bot_response_en, src='en', dest=user_lang).text
        else:
            bot_response = bot_response_en

        st.text_area("Bot:", value=bot_response, height=100)

    except Exception as e:
        st.error(f"Error: {e}")



# import streamlit as st
# import random
# import json
# import pickle
# import numpy as np

# import nltk
# from nltk.stem import WordNetLemmatizer

# from tensorflow.keras.models import load_model

# lemmatizer = WordNetLemmatizer()

# intents = json.loads(open('intents.json').read())

# words = pickle.load(open('words.pkl', 'rb'))
# classes = pickle.load(open('classes.pkl', 'rb'))
# model = load_model('chatbotmodel.h5')

# def clean_up_sentence(sentence):
# sentence_words = nltk.word_tokenize(sentence)
# sentence_words = [lemmatizer.lemmatize(word) for word in sentence_words]
# return sentence_words

# def bag_of_words(sentence):
# sentence_words= clean_up_sentence(sentence)
# bag = [0] * len(words)
# for w in sentence_words:
# for i, word in enumerate(words):
# if word == w:
# bag[i] = 1
# return np.array(bag)

# def predict_class(sentence):
# bow = bag_of_words(sentence)
# res = model.predict(np.array([bow]))[0]
# ERROR_THRESHOLD = 0.25
# results = [[i,r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]

# results.sort(key=lambda x:x[1], reverse=True)
# return_list = []
# for r in results:
# return_list.append({'intent': classes[r[0]], 'probability': str(r[1])})
# return return_list

# def get_response(intents_list, intents_json):
# if not intents_list: # no match found
# return "Sorry, I didn't understand that. Could you rephrase?"
# tag = intents_list[0]['intent']
# list_of_intents = intents_json['intents']
# result = ""
# for i in list_of_intents:
# if i['tag'] == tag:
# result = random.choice(i['responses'])
# break
# return result

# st.title("Basic Banking Chatbot System")
# st.write("Feel free to ask any queries about banking processes.")

# user_input = st.text_input("You:")
# if st.button("Send"):
# if user_input.lower() == "bye" or user_input.lower() == "goodbye":
# response_intents = predict_class(user_input)
# bot_response = get_response(response_intents, intents)
# st.write("Bot:", bot_response)
# st.write("The program ends here!")
# else:
# response_intents = predict_class(user_input)
# bot_response = get_response(response_intents, intents)
# st.write("Bot:", bot_response)