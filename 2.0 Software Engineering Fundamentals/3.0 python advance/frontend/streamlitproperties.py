# import streamlit as st

# print("run")
# pressed1 = st.button("click me")

# #When ever something is changed from the application, strealit runs the whole application again.

import streamlit as st
#To display an image
st.image("roseflower.png", caption= "A rose flower", use_container_width= True)

#To upload an image
uploaded_image = st.file_uploader("Upload your profile picture", type=["png", "jpg", "jpeg"])
if uploaded_image:
    st.image(uploaded_image, caption="Uploaded image", use_container_width= True)