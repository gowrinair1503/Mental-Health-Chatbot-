import streamlit as st
import json
import torch
import random
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Load model
class MentalHealthBot(torch.nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(MentalHealthBot, self).__init__()
        self.fc1 = torch.nn.Linear(input_size, hidden_size)
        self.fc2 = torch.nn.Linear(hidden_size, output_size)
    
    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = self.fc2(x)
        return x

# Load trained model
model = MentalHealthBot(10, 8, 9)
model.load_state_dict(torch.load("mental_health_model.pth"))
model.eval()

# Load self-care suggestions
with open("self_care_suggestions.json", "r") as file:
    self_care_suggestions = json.load(file)

# Set up Streamlit UI
st.set_page_config(page_title="Mental Health Chatbot", layout="centered", initial_sidebar_state="expanded")
st.title("🧘 Mental Health Chatbot")
st.write("💙 Let’s talk. Tell me how you’re feeling.")

# Mood Tracking Section
st.subheader("📊 Track Your Mood")

# Define moods
moods = ["Happy 😊", "Calm 🌿", "Anxious 😟", "Sad 😢", "Stressed 😰", "Overwhelmed 😵", "Neutral 😐"]

# User selects their mood
user_mood = st.selectbox("How are you feeling today?", ["Select"] + moods)

# Save the mood to a CSV file
if user_mood != "Select":
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    mood_data = pd.DataFrame([[timestamp, user_mood]], columns=["Timestamp", "Mood"])
    
    try:
        # Append to existing file
        mood_data.to_csv("mood_history.csv", mode='a', header=False, index=False)
    except:
        # Create a new file if it doesn't exist
        mood_data.to_csv("mood_history.csv", mode='w', header=True, index=False)
    
    st.success(f"✅ Mood recorded: {user_mood}")

# Display mood history
if st.button("📈 Show Mood History"):
    try:
        df = pd.read_csv("mood_history.csv")
        df["Timestamp"] = pd.to_datetime(df["Timestamp"])
        
        # Count occurrences of each mood
        mood_counts = df["Mood"].value_counts()
        
        # Plot mood trend
        fig, ax = plt.subplots()
        mood_counts.plot(kind="bar", color=["green", "blue", "orange", "red", "purple", "brown", "gray"])
        plt.xlabel("Mood")
        plt.ylabel("Frequency")
        plt.title("Your Mood History")
        plt.xticks(rotation=45)
        st.pyplot(fig)
    except:
        st.warning("No mood data available yet. Record your mood first!")

# User Input Section
st.subheader("💬 Chat with Me")
user_input = st.text_input("Type here...")

if user_input:
    mental_health_issues = list(self_care_suggestions.keys())
    issue_detected = random.choice(mental_health_issues)
    
    st.write(f"💡 You might be experiencing {issue_detected}. Here's a suggestion:")
    st.success(random.choice(self_care_suggestions[issue_detected]))

    # Offer alternative suggestion
    if st.button("Not helpful? Show another."):
        st.success(random.choice(self_care_suggestions[issue_detected]))

    # Suggest professional help if needed
    if st.button("I need more help."):
        st.warning("💙 It might be helpful to talk to a mental health professional.")

# Meditation & Music Section
st.subheader("🎧 Need some calm?")
meditation_option = st.selectbox("Choose an option:", ["Select", "Guided Meditation", "Breathing Exercise"])
if meditation_option == "Guided Meditation":
    st.info(random.choice(self_care_suggestions["Meditation"]))
elif meditation_option == "Breathing Exercise":
    st.info("Try this: Inhale for 4 seconds, hold for 4, exhale for 6. 🌬️")

st.subheader("🎶 Relaxing Music Suggestions")
music_option = st.selectbox("Choose a type of calming music:", ["Select", "Rain Sounds", "Soft Piano", "Ocean Waves", "Nature Sounds"])
if music_option != "Select":
    st.info(random.choice(self_care_suggestions["Calm Music"]))

# Light/Dark Mode Toggle
if st.checkbox("🌙 Dark Mode"):
    st.markdown("""
        <style>
        body { background-color: #222; color: white; }
        </style>
    """, unsafe_allow_html=True)
