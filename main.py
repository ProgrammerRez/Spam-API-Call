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
                   initial_sidebar_state='expanded')

with st.sidebar:
    st.info("""
            The Application is using a trained classifier model
            which is deployed in hugging face spaces
            
            """)