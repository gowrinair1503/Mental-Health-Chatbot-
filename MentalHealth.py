
# Streamlit UI Setup
st.set_page_config(page_title="Mental Health Chatbot", layout="centered")
st.title("🌿 Calm Mind")
st.markdown("A calm and supportive chatbot to help with your mental well-being.")

# Sidebar Settings
st.sidebar.title("Settings")
light_mode = st.sidebar.checkbox("Light Mode", value=True)

theme = "#f8f1f1" if light_mode else "#2c2c2c"
st.markdown(f"<style>body {{background-color: {theme};}}</style>", unsafe_allow_html=True)

# Chat Input
user_input = st.text_input("How are you feeling today?", "")
if user_input:
    response = generate_response(user_input)
    st.write(f"🤖 Chatbot: {response}")
    sentiment = get_sentiment(user_input)
    if sentiment == "Negative":
        emotion = random.choice(list(actions.keys()))
        suggestion, _ = get_suggestion(emotion)
        st.write(f"💡 Suggestion: {suggestion}")