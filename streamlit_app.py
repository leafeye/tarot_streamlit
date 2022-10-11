import streamlit as st
import pandas as pd
import numpy as np

import json
import random
import PIL
import datetime

import altair as alt

st.header('Tarot Assistant')

# Opening JSON file
f = open('tarot-images.json')
  
# returns JSON object as 
# a dictionary
data = json.load(f)
cards = data['cards']


if "session_cards" not in st.session_state:
    button_placeholder = st.empty()
    # button_trek_kaart = st.button('Trek kaarten')
    button_trek_kaart = button_placeholder.button('Trek kaarten')

if "session_cards" not in st.session_state and button_trek_kaart == True :
    nr_cards=3
    random_cards = random.sample(range(0, 77), nr_cards)

    st.session_state["session_cards"] = random_cards

    button_placeholder.empty()

if "session_cards"  in st.session_state:
    current_card_numbers = st.session_state["session_cards"]
    past_dict = cards[current_card_numbers[0]]
    present_dict = cards[current_card_numbers[1]]
    future_dict = cards[current_card_numbers[2]]

    past_img = f"cards/{past_dict['img']}"
    present_img = f"cards/{present_dict['img']}"
    future_img = f"cards/{future_dict['img']}"

    images_on_page = [past_img,present_img, future_img]
    st.image(images_on_page, width=220, caption=[past_dict['name'],
                                                present_dict['name'],
                                                future_dict['name']])


    st.text('My dearest, your fortune reading is about your past, present and future.')

    expander_past = st.expander("Regarding your past")
    expander_past.write(f"""
        Your past card is {past_dict['name']}. 
    """)
    expander_past.write(random.choice(past_dict['fortune_telling']))
    
    expander_present = st.expander("Regarding your present")
    expander_present.write(f"""
        Your present card is {present_dict['name']}
    """)
    expander_present.write(random.choice(present_dict['fortune_telling']))


    expander_future = st.expander("Regarding your future")
    expander_future.write(f"""
        Your future card is {future_dict['name']}
    """)
    expander_future.write(random.choice(future_dict['fortune_telling']))


