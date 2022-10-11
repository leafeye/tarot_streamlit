import streamlit as st
import pandas as pd
import numpy as np

import json
import random
import PIL
import datetime

import altair as alt

st.header('Tarot')

# Opening JSON file
f = open('tarot-images.json')
  
# returns JSON object as 
# a dictionary
data = json.load(f)
cards = data['cards']


if "session_cards" not in st.session_state:
    placeholder = st.empty()
    # button_trek_kaart = st.button('Trek kaarten')
    button_trek_kaart = placeholder.button('Trek kaarten')

if "session_cards" not in st.session_state and button_trek_kaart == True :
    nr_cards=3
    random_cards = random.sample(range(0, 77), nr_cards)

    st.session_state["session_cards"] = random_cards

    placeholder.empty()

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
    st.write('**Regarding your past**:')
    st.write(past_dict['fortune_telling'])

    st.write('**Regarding your present**:')
    st.write(present_dict['fortune_telling'])

    st.write('**Regarding your future**:')
    st.write(future_dict['fortune_telling'])

