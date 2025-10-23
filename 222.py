import streamlit as st

st.set_page_config(page_title='动物园', page_icon='🐒')
st.header("🤓震惊动物园运营只剩下最后三只动物......")

# 图片数组
images = ['https://cdn.pixabay.com/photo/2018/05/03/22/34/lion-3372720_1280.jpg',
          'https://dl0.creation.com/fpimages/11724.jpg',
          'https://breedingbusiness.com/wp-content/uploads/2021/07/cutest-small-white-dog-breeds.jpg']

captions = ['狮子🦁', '虎子🐯', '狗子🐕']
if 'a' not in st.session_state:
    st.session_state['a'] = 0
    
def nextimg():
    st.session_state['a'] =(st.session_state['a']+1) % len(images)
    
  
def next2mg():
    st.session_state['a'] =(st.session_state['a']-1) % len(images)


# st.image()总共两个参数，url：图片地址 caption:图片的备注
st.image(images[st.session_state['a']], captions[st.session_state['a']])



c1, c2 = st.columns(2)
with c1:
    st.button('上一张', on_click=next2mg, use_container_width=True)

with c2:
    st.button('下一张', on_click=nextimg, use_container_width=True)
