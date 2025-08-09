🏦 Banking Chatbot System
An AI-powered chatbot designed to answer banking-related queries in multiple Indian languages.
This project uses Natural Language Processing (NLP) and Deep Learning to provide fast, accurate, and user-friendly responses for various banking services such as deposits, loans, investment services, payment systems, and more.

🚀 Features
💬 Conversational Banking Support – Handles a wide range of banking queries from deposits to loans.

🌏 Multi-language Support – Accepts queries in any Indian language and responds in the same language using Google Translate API.

🤖 AI & NLP Powered – Uses NLTK for text preprocessing and TensorFlow for intent classification.

🖥 Two Versions Available:

Command-line version (main.py) for quick testing.

Web-based version (main2.py) using Streamlit for a clean, interactive UI.

🔄 Real-time Translation – Automatically detects the input language and translates both input & output.

📂 Customizable Intents – Modify intents.json to train the chatbot on new services.

🛠 Tech Stack
Programming Language: Python

NLP: NLTK (tokenization, lemmatization)

Deep Learning: TensorFlow / Keras

Translation: Googletrans & Langdetect

Frontend: Streamlit

Model Storage: Pickle (words.pkl, classes.pkl) & H5 (chatbotmodel.h5)

📂 Project Structure
bash
Copy
Edit
├── intents.json         # Banking services intents & responses
├── main.py              # CLI chatbot version
├── main2.py             # Streamlit web chatbot version with multi-language support
├── trainingData.py      # Model training script
├── words.pkl            # Preprocessed vocabulary
├── classes.pkl          # Intent classes
├── chatbotmodel.h5      # Trained deep learning model
├── .gitignore           # Ignored files & virtual env
⚙️ Installation & Setup
1️⃣ Clone the repository

bash
Copy
Edit
git clone https://github.com/Abhinayana16/Banking-Chatbot.git
cd Banking-Chatbot
2️⃣ Create & activate virtual environment

bash
Copy
Edit
python -m venv venv
source venv/bin/activate      # Linux/Mac
venv\Scripts\activate         # Windows
3️⃣ Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
4️⃣ Train the model (optional, if modifying intents)

bash
Copy
Edit
python trainingData.py
5️⃣ Run the chatbot

CLI Version:

bash
Copy
Edit
python main.py
Web Version (Streamlit):

bash
Copy
Edit
streamlit run main2.py
📊 How It Works
User Input → Detect language using langdetect.

Translate (if not English) using Googletrans API.

Preprocess input (tokenization, lemmatization).

Predict intent with trained neural network (chatbotmodel.h5).

Select Response from intents.json.

Translate Back to user’s language (if needed).

Output Response in chosen interface.

💡 Example Queries
"How to do ATM deposits?"

"Tell me about personal loans"

"क्रेडिट कार्ड कैसे लें?" (Hindi)

"சேமிப்பு வைப்புகள் என்னென்ன?" (Tamil)

📌 Future Improvements
🔐 Integrate with secure banking APIs for real-time account queries.

🧠 Implement context-aware conversation memory.

📱 Deploy as a WhatsApp / Telegram banking assistant.

🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

📜 License
This project is licensed under the MIT License – you’re free to use, modify, and distribute it.
