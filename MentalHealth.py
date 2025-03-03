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

# Apply the theme dynamically
if light_mode:
    # Light mode: Background light, text dark
    theme = """
        <style>
            body {
                background-color: #f8f1f1;
                color: #000000;
            }
            .stTextInput input {
                background-color: #ffffff;
                color: #000000;
            }
            .stTextArea textarea {
                background-color: #ffffff;
                color: #000000;
            }
        </style>
    """
else:
    # Dark mode: Background dark, text light
    theme = """
        <style>
            body {
                background-color: #2c2c2c;
                color: #ffffff;
            }
            .stTextInput input {
                background-color: #444444;
                color: #ffffff;
            }
            .stTextArea textarea {
                background-color: #444444;
                color: #ffffff;
            }
        </style>
    """

# Add the theme to the app
st.markdown(theme, unsafe_allow_html=True)

# Action and suggestion functions
actions = {
    "Depression": ["Try going for a short walk.", "Listen to soft music.", "Break your day into tiny tasks."],
    "Anxiety": ["Try deep breathing.", "Imagine a peaceful place.", "Hold something soft."],
    "Panic Attacks": ["Place your hand on your chest and feel your heartbeat slow.", "Focus on an object and describe it in detail.", "Splash cold water on your face."],
    "Overthinking": ["Write your thoughts in a journal.", "Set a 5-minute timer for overthinking.", "Distract yourself with music or puzzles."],
    "PTSD": ["Hold a grounding object.", "Listen to calming sounds.", "Take deep, slow breaths."],
    "Stress": ["Stretch your body.", "Drink water mindfully.", "Listen to your favorite song."],
    "OCD": ["Try guided meditation.", "Hold a grounding object.", "Breathe deeply and remind yourself: 'I am in control.'"]
}

# Initialize session state for storing conversation history if not already present
if 'conversation_history' not in st.session_state:
    st.session_state['conversation_history'] = []

# Function to generate chatbot response
def generate_response(user_input):
    # Simple response generation based on input, can be replaced with actual model-based generation
    return "I'm here to listen and support you."

# Function to determine sentiment (placeholder for actual sentiment analysis logic)
def get_sentiment(text):
    # Here, you would process the text to get sentiment (positive, negative, etc.)
    if "sad" in text.lower():
        return "Negative"
    return "Positive"

# Function to provide suggestions based on the emotion
def get_suggestion(emotion):
    if emotion in actions:
        suggestion = random.choice(actions[emotion])
        return suggestion, emotion
    return "Stay strong, you're not alone!", "Neutral"

# Display previous conversation if it exists (Scrollable history)
conversation_container = st.container()
with conversation_container:
    for message in st.session_state['conversation_history']:
        st.write(message)

# Input field at the bottom of the page (fixed position)
input_container = st.empty()
user_input = input_container.text_input("How are you feeling today?", "")

if user_input:
    # Generate chatbot response
    response = generate_response(user_input)
    
    # Add user input and response to the conversation history
    st.session_state['conversation_history'].append(f"You: {user_input}")
    st.session_state['conversation_history'].append(f"🤖 Chatbot: {response}")
    
    # Sentiment-based actions
    sentiment = get_sentiment(user_input)
    if sentiment == "Negative":
        emotion = random.choice(list(actions.keys()))
        suggestion, _ = get_suggestion(emotion)
        st.session_state['conversation_history'].append(f"💡 Suggestion: {suggestion}")
    
    # Display updated conversation history (auto-scroll down)
    for message in st.session_state['conversation_history']:
        st.write(message)

    # Reset the input field to be empty
    input_container.text_input("How are you feeling today?", "", key="next_message")
