import streamlit as st
from groq import Groq

#initialize the api_key
client = Groq(api_key='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')


#create a function
def get_groq_response(user_input):
    completion = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role": "user",
            "content": user_input
        }
    ],
    temperature=1,
    max_tokens=1024,
    top_p=1,
    stream=True,
    stop=None,
)

    response_text = ""
    for chunks in completion:
        response_text += chunks.choices[0].delta.content or ""
    return response_text

#streamlit app layout
st.title("My GPT")
st.write("This web app will interact with Llama 3.3 llm model to generate the response")


#input the text
user_input = st.text_input("Enter your message : ")

#when the user clicks the button then, get the response from the groq
if st.button('Send'):
    with st.spinner("Generating Response..."):
        response = get_groq_response(user_input)

    st.success("response received.!")
    st.write(response)
st.markdown("***Made By Vatsa Joshi***", unsafe_allow_html=True)