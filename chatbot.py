import streamlit as st
import google.generativeai as genai

# --- Streamlit Page Setup ---
st.set_page_config(page_title=" Chatbot", page_icon="🤖")
st.title("🔥FlashChat")

# --- Input API Key from User ---
api_key = st.text_input("🔑 Enter your Gemini API Key:", type="password")

# --- Check for API Key before continuing ---
if api_key:
    try:
        # Configure the Gemini API
        genai.configure(api_key=api_key)

        # Load the model
        model = genai.GenerativeModel(model_name="models/gemini-1.5-flash-latest")

        # Initialize chat session
        if "chat" not in st.session_state:
            st.session_state.chat = model.start_chat(history=[])
        if "messages" not in st.session_state:
            st.session_state.messages = []

        # Display previous messages
        for msg in st.session_state.messages:
            with st.chat_message(msg["role"]):
                st.markdown(msg["content"])

        # User input
        user_input = st.chat_input("Ask anything...")

        if user_input:
            # Show user message
            st.chat_message("user").markdown(user_input)
            st.session_state.messages.append({"role": "user", "content": user_input})

            # Get response from Gemini
            response = st.session_state.chat.send_message(user_input)

            # Show Gemini's response
            with st.chat_message("assistant"):
                st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})

    except Exception as e:
        st.error(f"❌ Error: {e}")
else:
    st.warning("⚠️ Please enter your Gemini API key to start chatting.")
