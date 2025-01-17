import time
import streamlit as st
from streamlit_extras.streaming_write import write

st.title("🎈 This is the app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/). This will be very useful for sure!!!"
)
st.write(
    "This shall be the start of something fruitful!"
)

write(
    "Have you heard of the critically acclaimed MMORPG Final Fantasy XIV? With an expanded free trial which you can play through the entirety of A Realm Reborn and the award-winning Heavensward, and thrilling Stormblood expansions up to level 70 for free with no restrictions on playtime."
)