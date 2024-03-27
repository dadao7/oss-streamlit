import streamlit as st
import numpy as np
import pandas as pd
import altair as alt

# Page title
st.set_page_config(page_title='Interactive Data Explorer', page_icon='📊')
st.title('📊 Interactive Data Explorer')
st.header('this is the markdown')
st.markdown('this is the header')
st.subheader("this is the subheader")
st.caption("this is the caption")
st.code("x=2023")
st.latex(r"""a+ar^1+ar^2+ar^3""")
st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ0Innq72YTXnDr5APcW_40jEoPJNa-LlQXG7FYhWxk1erNG7BVPm53f4h8ZnxQJjy22z4&usqp=CAU")

st.checkbox('yes')
st.button('Click')
st.radio('Pick your gender',['Male','Female'])
st.selectbox('Pick your gender',['Male','Female'])
st.multiselect('choose a planet',['Jupiter','Mars','neptune'])
st.select_slider('Pick a mark',['Bad','Good','Exellent'])
x=st.slider('Pick a number',0,50)
st.write(x)
