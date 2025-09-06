# [📨 Spam Classifier API Interface]
## Streamlit Deployment: [Link](https://spam-api-call-interface.streamlit.app)

[![Python](https://img.shields.io/badge/Python-3.10+-blue)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.25+-green)](https://streamlit.io/)
[![Hugging Face](https://img.shields.io/badge/Hugging%20Face-Model-orange)](https://huggingface.co/)

A **Streamlit web application** to classify text as **Spam** or **Ham** using a pre-trained model deployed on **Hugging Face Spaces**. The app provides a chat interface, shows predictions with probabilities, and includes a ready-to-use code snippet for developers.

---

## 🚀 Features

- **Interactive Chat Interface:** Enter text and receive Spam/Ham classification instantly.  
- **Readable Output:** Displays the original message, predicted label, and probability clearly.  
- **Persistent Chat History:** Keeps track of all messages during the session.  
- **Developer Code Snippet:** Learn to call the model directly using Gradio client.  
- **Sidebar Info:** Includes model details and a link to the developer's LinkedIn profile.

---

## 💻 Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/spam-classifier-app.git
cd spam-classifier-app
````

2. Install required packages:

```bash
pip install streamlit gradio_client
```

---

## ⚡ Usage

Run the Streamlit app:

```bash
streamlit run app.py
```

1. Enter your text in the chat input box.
2. Wait for the prediction (may take \~15 seconds for the first request).
3. See the formatted result:

* **Message:** Your input text
* **Prediction:** Spam or Ham
* **Probability:** Confidence score

---

## 📌 Code Snippet

You can call the model directly using the Gradio client:

```python
from gradio_client import Client

def predict(text: str):
    client = Client("Rez2318/Spam_Classifier_Model")
    return client.predict(
        text=text,
        api_name="/predict"
    )

print(predict("Congratulations!, you've won a prize"))
```

---

## 👤 Author

**Muhammad Umar**
[LinkedIn Profile](http://www.linkedin.com/in/muhammad-umar-3b7b7b378)

---

## ⚠ Notes

* The first prediction may take a few seconds to load.
* All messages and results are stored in **session state** for easy tracking.
* Make sure your Python environment has **Streamlit ≥1.25** and **Gradio client installed**.


