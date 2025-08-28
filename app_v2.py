import streamlit as st
import requests

API_KEY = "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"

st.set_page_config(page_title="A's Delulu Chatbot")
st.title("🤖 A's Delulu Chatbot")

# add a sidebar
if st.sidebar.button("Clear Chat"):
    st.session_state.messages = []
    st.rerun()

st.sidebar.markdown("This chatbot uses Llama 3.3 70B")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Function to call Groq API
def get_groq_response(messages):
    url = "https://api.groq.com/openai/v1/chat/completions"
    
    headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}

    data = {
        "model": "llama-3.3-70b-versatile",
        "messages": messages ,
        # "temperature": 0.7,
        # "max_tokens": 512,
    }

    
    response = requests.post(url, headers=headers, json=data, verify=False)  # Disable SSL verification
    # print("DEBUG:", response.status_code, response.text)  # see what Groq sends back
    response.raise_for_status()
    
    return response.json()["choices"][0]["message"]["content"]

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Delulu is the only solulu! Ask me anything..."):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate assistant response
    with st.chat_message("assistant"):
        with st.spinner("Delusionally thinking..."):
            response = get_groq_response(st.session_state.messages)
            st.markdown(response)

    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
  

