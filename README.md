# 🏦 Banking Chatbot

This is a simple chatbot built using Python, TensorFlow, and Streamlit. It helps users with common banking-related queries using a trained neural network. Intents are stored in **MongoDB**, making it easy to manage and scale the conversation database.

## 🚀 Features

- NLP-based classification of user queries
- Pre-trained deep learning model using Keras
- MongoDB integration for dynamic intents management
- Command-line and Web UI using Streamlit

---

🛠️ Setup Instructions
1. Install Dependencies:
    pip install -r requirements.txt
Or install manually:
    pip install numpy nltk tensorflow pymongo streamlit
Also, install NLTK datasets (automatically handled in scripts):
    import nltk
    nltk.download('punkt')
    nltk.download('wordnet')
    nltk.download('omw-1.4')
2. Start MongoDB Server
Make sure MongoDB is installed and running on your system. Example:
    mongod
Create and populate your database:
# In Python shell or script
  from pymongo import MongoClient
  import json
  
  client = MongoClient("mongodb://localhost:27017/")
  db = client["chatbotdb"]
  collection = db["intents"]
  
  with open("intents.json") as f:
      data = json.load(f)
      collection.insert_many(data["intents"])
      
3. Train the Model
    python trainingData.py
This will generate:
chatbotmodel.h5
words.pkl
classes.pkl

4. Run the Chatbot (CLI)
    python main.py
5. Run the Chatbot (Web Interface)
    streamlit run main2.py
📄 License
This project is for educational purposes. Feel free to fork and extend it!

👤 Author
Abhinayana Vanaparthi
B.Tech (CSE - AI), Pragati Engineering College
GitHub: Abhinayana16
