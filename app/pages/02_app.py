import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image, ImageDraw


# 입력
st.title('1. 입력 버튼들')


# data_editor
df = pd.DataFrame(
    [
       {"command": "st.selectbox", "rating": 4, "is_widget": True},
       {"command": "st.balloons", "rating": 5, "is_widget": False},
       {"command": "st.time_input", "rating": 3, "is_widget": True},
   ]
)
edited_df = st.data_editor(df)
favorite_command = edited_df.loc[edited_df["rating"].idxmax()]["command"]
st.markdown(f"Your favorite command is **{favorite_command}** 🎈")


# download_button
# data에 str 넣으면 str 적혀있는 streamlit_download.txt 만들어서 다운로드
# data = 'data'
st.download_button(
    label='On the dl', 
    data=df.to_csv(),
    file_name='app_df.csv',
    mime='text/scv'
    )

# print: T/F log print
button_result = st.button('Hit me')
print(button_result)
if button_result:  
    st.write(df)
# button_result

check_result = st.checkbox('Check me out')
if check_result:
    st.write(df)


# img search
cat_list = ['고양이1', '고양이2','고양이3']
img_list = ['https://imgur.com/ULlcUR9.jpg', 
            'https://imgur.com/zPfODOH.jpg', 
            'https://imgur.com/b61thYx.jpg']

search = st.text_input('검색할 사진 이름 입력')
for i in cat_list:
    if search in i:
        idx = cat_list.index(i)
        link = img_list[idx]
if search != '':
    st.image(link)




st.radio('Pick one:', ['nose','ear'])
st.selectbox('Select', [1,2,3])
st.multiselect('Multiselect', [1,2,3])
st.slider('Slide me', min_value=0, max_value=10)
st.select_slider('Slide to select', options=[1,2,3])
st.text_input('Enter some text')
st.number_input('Enter a number')
st.text_area('Area for textual entry')
st.date_input('Date input')
st.time_input('Time entry')
st.file_uploader('File uploader')
st.camera_input("一二三,茄子!")
st.color_picker('Pick a color')


# 출력
st.title('2. 출력')
st.text('Fixed width text')
st.markdown('_Markdown_') # see #*
st.caption('Balloons. Hundreds of them...')
st.latex(r''' e^{i\pi} + 1 = 0 ''') # 수식 작성
st.write('Most objects') # df, err, func, keras!
st.write(['st', 'is <', 3]) # see *
st.title('My title')
st.header('My header')
st.subheader('My sub')
st.code('for i in range(8): foo()') # 코드 작성



