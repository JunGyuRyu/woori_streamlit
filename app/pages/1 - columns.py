import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image, ImageDraw

cat_list = ['고양이1', '고양이2','고양이3']
img_list = ['https://imgur.com/ULlcUR9.jpg', 
            'https://imgur.com/zPfODOH.jpg', 
            'https://imgur.com/b61thYx.jpg']

add_selectbox = st.sidebar.selectbox(
    'title1',
    ['a', 'b', 'c']
)
with st.sidebar:
    add_radio = st.radio(
        'title2',
        [1,2,3,4]
    )
    st.write(add_selectbox)
    st.write(add_radio)

# st.columns
col1, col2 = st.columns(2)
col1, col2, col3 = st.columns([3,1,1])

# 순서 알아서 맞춤
col3.write('Column 3')
col1.write('Column 1')
col2.write('Column 2')

#웹 width에 맞춰 image 간격 알아서 조정해줌
with col1:
    st.image(img_list[0])
with col2:
    st.image(img_list[1])
with col3:
    st.image(img_list[2])


