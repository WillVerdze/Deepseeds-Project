import streamlit as st 
import time
import random

#To set up the page
st.title("AI Text Detector")
st.write("Paste your write-up below and click 'Analyze; to chack if it's AI-generated.")

#Getting input
write_up = st.text_area("Paste your write-up here: ", height= 300)

#Greate a trigger
if st.button("Analyzze"):
    #Checks if the user entered a text in the textbox
    if not write_up:
        st.warning("Please enter some text to analyse")
    else:
        #Adds a loading spinner
        with st.spinner("analysing text...This might take a moment."):
            time.sleep(2)#Simulate a 2 ssecond delay for the AI model
        
        ai_percentage = int(random.uniform
        (0.0, 100.0))
        if ai_percentage >= 50:
            st.error("This is likely AI generated")
            st.markdown(f"**Confidence:{ai_percentage: .2f}%")
        else:
            st.success("Likely human written")
            st.markdown(f"**Confidence:{100 - ai_percentage: .2f}% human written")