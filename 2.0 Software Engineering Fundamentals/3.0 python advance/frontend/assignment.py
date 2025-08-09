import streamlit as st
#Tabs (st.tabs)
#Separate content into multiple pages without navigating
# #Adding sidebars
st.sidebar.title("🌱DEEPSEED")
st.sidebar.markdown("one seed at a time")
st.sidebar.divider()
st.sidebar.write("🚇Session Skills")
col1, col2 = st.sidebar.columns(2)
with col1:
    st.write("Messages")
    st.markdown("2")
    
with col2:
    st.write("Total")
    st.markdown("2")
st.sidebar.divider()
st.sidebar.header("🗼Quick Action")
st.sidebar.button("⚡Tell me a joke")
st.sidebar.button("⚡Explain AI", use_container_width=True)
st.sidebar.button("⚡Help Brainstorm", use_container_width=True)
st.sidebar.button("⚡Writing tips", use_container_width=True)
st.sidebar.button("⚡Book recommendations", use_container_width=True)
st.sidebar.divider()
st.sidebar.write("🤞Controls")
# st.sidebar.selectbox("Choose the model", ["Gemini", "Chatgpt", "Poe", "Midjourney"])
# st.sidebar.select_slider("Choose temperature", [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 1])
st.header("😁 Chat with DEEPSEED")
box = st.container(height = 500, border=True)
with box:
    with st.chat_message("user", avatar="😒"):
        st.write("Welcome to the world of Deepseeds")

    with st.chat_message("assistant", avatar="🤦‍♂️"):
        st.write("Based on your message, I can provide some insights on this")

st.divider()
with st.form(key="Message DEEPSEED"):
    #st.markdown("Message DEEPSEED:")
    col1, col2 = st.columns(2)
    with col1:
        message = st.text_input("Message DEEPSEED:", placeholder = "Type your message here...")
     #st.text_input("Enter prompt: ")
    
    with col2:
        submit = st.form_submit_button("Send🗼")
    #st.write("AI result goes here")
    #message = st.text_input("Message DEEPSEED:", placeholder = "Type your message here...")
    #submit = st.form_submit_button("Send🗼")
    #st.chat_input("Type your message here...")
st.markdown("'2 messages in this conversation'")

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
    
