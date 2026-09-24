import streamlit as st
from main import ask_question

if "messages" not in st.session_state:
    st.session_state.messages = []

st.title("Azure AI Python Project")
st.write("Chatbot")

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

user_input = st.chat_input("Ask your question: ")

if user_input:
    with st.chat_message("user"):
        st.write(user_input)

    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    messages = st.session_state.messages[-4:]

    answer = ask_question(messages)

    with st.chat_message("assistant"):
        st.write(answer)

    st.session_state.messages.append(
        {"role": "assistant", "content": answer}
    )