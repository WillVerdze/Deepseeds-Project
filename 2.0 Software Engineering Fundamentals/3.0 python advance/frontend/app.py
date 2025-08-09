import streamlit as st 
# # import pandas as pd 
# # import numpy as np
# # # st.title("Welcome to Germini frontend ")
# # # st.subheader("Thanks for attending")
# # # st.write("Hello, Streamlit! This is my first web app")

# # # st.sidebar.title("my sidebar")
# # # st.sidebar.subheader("Profile")
# # # An interactive data explorer with streamlit

# # st.title("Interactive Data Explorer")
# # #Add a text input for user's name
# # name = st.text_input("Please enter your name: ")
# # #Create a slider for a random number seed
# # seed = st.slider("Slect a random number", 0, 100, 42)

# # st.markdown("* Item 1")
# # st.markdown("* Item 2")
# # st.markdown("* Item 3")

# # st.success("Done")
# # st.info("This is info")

# # st.warning("warn")
# # st.error("error")
# # #create a button
# # # if st.button("Generate Data"):
# # #     st.write(f"Hello, {name}! Generating some data for you.")
    
    
# #     #Generate a random datafram based on seed
# #     # np.random.seed(seed)
# #     # data = pd.DataFrame(
# #     #     np.random.randn(10,3),
# #     #     columns = ['a', 'b', 'c']
    
# #     # )
    
# #     # #Display the data frame and a chart
# #     # st.write("Here is your data: ")
# #     # st.dataframe(data)
    
# #     # st.header("Data chart")
# #     # st.line_chart(data)
    
    
    
# # import streamlit as st
# # from profile import markdown_code

# # st.markdown(markdown_code)
    

# #Working with forma and dorm inputs
# import streamlit as st
# import time

# #Adding sidebars
# st.sidebar.title("my sidebar")
# st.sidebar.subheader("Profile")
# st.sidebar.selectbox("Choose the model", ["Gemini", "Chatgpt", "Poe", "Midjourney"])
# st.sidebar.select_slider("Choose temperature", [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 1])
# st.write("Please fill out the form below to register.")

# #Creating the form conatainer
# with st.form(key = "registration_form"):
#     #With brings in context management. Allowing python to manage your code.
#     #with here stops streamlit for continuously running.
#     #so, instead of it running as you enter each letter, putting it all in the with will allow the code to run only after the register button has been clicked.
#     st.subheader("Personal informtion")
#     username = st.text_input("Enter your username")
#     email = st.text_input("Enter email")
#     password = st.text_input("Enter your password", type= "password")
#     st.subheader("Preferences")
#     fav_color = st.selectbox("what is your favourite color?", ["Red", "Blue", "Green", "Yellow"])
    
#     agree_to_terms = st.checkbox("I agree t the terms and conditions")
    
#     submitted = st.form_submit_button("Register")
#     if submitted:
#         registration_data = {
#             "username" : username,
#             "email" : email,
#             "Fav_color" : fav_color
#         }
#         if not username:
#             st.error("User name required")
#         elif not email:
#             st.error("Email is required")
#         elif not agree_to_terms:
#             st.error("You must gree to terms")
#         else:
#             st.success("Registration successful")
            
#             st.write("Here are your details: ")
#             st.write(f"**Username:** {username}")
#             st.write(f"**email:** {email}")
#             st.write(f"**Favourite color:** {fav_color}")
#             st.balloons()
#             # with st.spinner("analysing text...This might take a moment."):
#             #     time.sleep(2)
#             #     st.json(registration_data)

# # progress = st.progress(0)
# # for i in range(100):
# #      time.sleep(0.2)  # Simulate some work being done
# #      progress.progress(i + 1)  # Update the progress bar
     
# # st.success("Generation complete!!")

# #Tabs (st.tabs)
# #Separate content into multiple pages without navigating

# tab1, tab2 = st.tabs(["Prompt", "Output"])
# with tab1:
#     st.text_area("Enter your prompt: ")
    
# with tab2:
#     st.write("Generated result apperas here")

# #Columns
# #Place elements side by side (e.g. inputs on the left, results on the right)

# col1, col2 = st.columns(2)
# with col1:
#     st.text_input("Enter prompt: ")
    
# with col2:
#     st.write("AI result goes here")
    
    
# #Container (st.container)
# #Groups related elements and allows for dynamic updates inside the group

# container = st.container()

# container.write("Generated text area")
# btn = container.button("Generate Text")


# #Expander(st.expander)
# #Hide/show details on demand- useful for advanced settings or explanations
# with st.expander("Advanced Options"):
#     st.slider("Max Tokens", 100, 1000)
#     st.checkbox("Stream Output")
    

# #Empty(st.empty)
# #REserves a space that updates later (eg, dynamic results area)

# placeholder = st.empty()

# if st.button("Generate"):
#     placeholder.write("Generating...")
#     placeholder.write("Done, here is the result.")
    


#Combine laybouts for GenAI app

st.title("GenAI Prompt Generator")

#Sidebar settings
st.sidebar.title("Settings")
temp = st.sidebar.slider("Creativity (temperature)", 0.0, 1.0, 0.7)

#tabs
tab1, tab2 = st.tabs(["Prompts", "Output"])

with tab1:
    prompt = st.text_area("Enter your prompt")
    
with tab2:
    st.write("**AI Output**")
    if st.button("Generate"):
        st.success(f"Response from model (temp = {temp}) for : {prompt}")
