import streamlit as st
from multiapp import MultiApp
from content import portifolio, streamlitEEG 

app = MultiApp()

# Add your app pages here
app.add_app("Portofilio ", content\pyportifolio.app)
app.add_app("EEG Eye State Classification Project ", content\streamlitEEG.app)

# Run the app
app.run()
