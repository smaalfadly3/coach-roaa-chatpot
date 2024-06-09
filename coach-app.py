import streamlit as st
from openai import OpenAI

# Initialize OpenAI client with the API key from Streamlit secrets
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.title("Coach Roaa 💪🏻")

# Initialize session state variables if not already done
if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display all chat messages from the session state
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Handle new user input
if prompt := st.chat_input("I am here for you!"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        # Create a list of messages including the system prompt and all previous messages
        messages = [
            {"role": "system", "content": "Hey there! You’re Coach Roaa at Mukalla Gym. You’re here to help your trainees with their workouts and any gym-related questions. Remember, you’re a girl and can chat like you’re talking to friends—feel free to use emojis and keep it sweet, supportive, and fun! 💖💪🏻"},
        ] + st.session_state.messages

        # Generate a response from the assistant
        response = client.chat.completions.create(
            model=st.session_state["openai_model"],
            messages=messages
        )

        assistant_message = response.choices[0].message.content
        st.markdown(assistant_message)

    # Append the assistant's response to the session state messages
    st.session_state.messages.append({"role": "assistant", "content": assistant_message})