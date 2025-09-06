from gradio_client import Client
import streamlit as st

def predict(text: str):
    client = Client("Rez2318/Spam_Classifier_Model")
    return client.predict(
        text=text,
        api_name="/predict"
    )

st.set_page_config(page_title='Spam Classifier API Call',
                   page_icon='🤖',
                   initial_sidebar_state='expanded',
                   layout='wide')

st.title('Spam Classifier API Interface')

with st.sidebar:
    st.info("""
        The Application is using a trained classifier model (made by me)
        deployed on Hugging Face Spaces and called via API 
        to classify the given text.
    """)
    st.info("""
        You can use it as well by using the given code snippet.
        Check out my LinkedIn for more projects:
        LinkedIn: http://www.linkedin.com/in/muhammad-umar-3b7b7b378
    """)
    
    # Container for the code snippet
    with st.expander("Spam Classifier Prediction Snippet"):
        st.code("""
from gradio_client import Client

def predict(text: str):
    client = Client("Rez2318/Spam_Classifier_Model")
    return client.predict(
        text=text,
        api_name="/predict"
    )

print(predict("Congratulations!, you've won a prize"))
        """, language="python")

st.info('It might take 15 seconds for the prediction so be patient')

# Initialize chat history
if 'history' not in st.session_state:
    st.session_state.history = []

# Display chat history
for msg in st.session_state.history:
    with st.chat_message(msg['role']):
        st.markdown(msg['content'])

# User input
if user_input := st.chat_input('Your Spam/Ham Message'):
    with st.chat_message('user'):
        st.markdown(user_input)
    st.session_state.history.append({'role':'user','content':user_input})
    with st.chat_message('assistant'):
        with st.spinner(text='Thinking...',show_time=True):
            result = predict(text=user_input)
        with st.spinner("Thinking..."):
            result = predict(text=user_input)

        # Create a readable Markdown string
        output_text = f"""
        ### 📨 Spam Classifier Result

        **Message:** {user_input}

        **Prediction:** {'Spam' if result['label'] == 1 else 'Ham'}

        **Probability:** {result['probability']:.2f}
        """

        # Display the formatted output
        st.markdown(output_text)

        # Store the formatted output in history
        st.session_state.history.append({
            'role': 'assistant',
            'content': output_text
        })
