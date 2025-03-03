import streamlit as st
import random

# Streamlit UI Setup
st.set_page_config(page_title="Mental Health Chatbot", layout="wide")

# Set up the title and introduction
st.title("🌿 Calm Mind")
st.markdown("A calm and supportive chatbot to help with your mental well-being.")

# Sidebar Settings
st.sidebar.title("Settings")
light_mode = st.sidebar.checkbox("Light Mode", value=True)

# Function to set theme based on light/dark mode
def set_theme(light_mode):
    if light_mode:
        # Light mode
        theme = """
            <style>
                body {
                    background-color: #f8f1f1;
                    color: #000000;
                }
                .stTextInput input, .stTextArea textarea {
                    background-color: #ffffff;
                    color: #000000;
                }
                .stButton>button {
                    background-color: #f0f0f0;
                    color: #000;
                }
                .stMarkdown {
                    color: #000;
                }
            </style>
        """
    else:
        # Dark mode
        theme = """
            <style>
                body {
                    background-color: #2c2c2c;
                    color: #ffffff;
                }
                .stTextInput input, .stTextArea textarea {
                    background-color: #444444;
                    color: #ffffff;
                }
                .stButton>button {
                    background-color: #555;
                    color: #fff;
                }
                .stMarkdown {
                    color: #ffffff;
                }
            </style>
        """
    st.markdown(theme, unsafe_allow_html=True)

# Apply the selected theme
set_theme(light_mode)

# Actions and suggestions for different emotions
actions = {
    "Depression": ["Try going for a short walk.", "Listen to soft music.", "Break your day into tiny tasks."],
    "Anxiety": ["Try deep breathing.", "Imagine a peaceful place.", "Hold something soft."],
    "Panic Attacks": ["Place your hand on your chest and feel your heartbeat slow.", "Focus on an object and describe it in detail.", "Splash cold water on your face."],
    "Overthinking": ["Write your thoughts in a journal.", "Set a 5-minute timer for overthinking.", "Distract yourself with music or puzzles."],
    "PTSD": ["Hold a grounding object.", "Listen to calming sounds.", "Take deep, slow breaths."],
    "Stress": ["Stretch your body.", "Drink water mindfully.", "Listen to your favorite song."],
    "OCD": ["Try guided meditation.", "Hold a grounding object.", "Breathe deeply and remind yourself: 'I am in control.'"]
}

# Initialize session state for conversation if it doesn't exist
if 'conversation_history' not in st.session_state:
    st.session_state['conversation_history'] = []

# Function to generate chatbot response
def generate_response(user_input):
    return "I'm here to listen and support you."

# Function to determine sentiment (for simplicity, placeholder logic)
def get_sentiment(text):
    # Add more sophisticated sentiment analysis if required
    if "sad" in text.lower():
        return "Negative"
    return "Positive"

# Function to get a suggestion based on sentiment
def get_suggestion(emotion):
    if emotion in actions:
        suggestion = random.choice(actions[emotion])
        return suggestion, emotion
    return "Stay strong, you're not alone!", "Neutral"

# Function to handle user input and chatbot response
def handle_conversation(user_input):
    sentiment = get_sentiment(user_input)
    response = generate_response(user_input)
    st.session_state['conversation_history'].append(f"You: {user_input}")
    st.session_state['conversation_history'].append(f"🤖 Chatbot: {response}")
    
    # Sentiment-based suggestion (if negative sentiment)
    if sentiment == "Negative":
        emotion = random.choice(list(actions.keys()))
        suggestion, _ = get_suggestion(emotion)
        st.session_state['conversation_history'].append(f"💡 Suggestion: {suggestion}")
    
    # Update conversation history in the UI
    for message in st.session_state['conversation_history']:
        st.write(message)

# Display the conversation history
with st.container():
    for message in st.session_state['conversation_history']:
        st.write(message)

# Input field at the bottom for user input
input_container = st.empty()
user_input = input_container.text_input("How are you feeling today?", "")

# Handle conversation when user inputs text
if user_input:
    handle_conversation(user_input)
    input_container.text_input("How are you feeling today?", "", key="next_message")
