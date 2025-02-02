import streamlit as st 
from utils import generate_script

# Applying Styling
st.markdown("""
<style>
div.stButton > button:first-child {
    background-color: #4CAF50; /* Green */
    color: white;
    padding: 12px 20px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 16px;
    margin: 4px 2px;
    transition-duration: 0.4s;
    cursor: pointer;
    border: none;
    border-radius: 12px;
}

div.stButton > button:first-child:hover {
    background-color: white;
    color: black;
    border: 2px solid #4CAF50;
}
</style>""", unsafe_allow_html=True)


# Creating Session State Variable
if 'API_Key' not in st.session_state:
    st.session_state['API_Key'] =''


st.title('❤️ YouTube Script Writing Tool') 

# Sidebar to capture the OpenAi API key
st.sidebar.title("😎🗝️")
st.session_state['API_Key']= st.sidebar.text_input("What's your API key?",type="password")
st.sidebar.image('./Youtube.jpg',width=300, use_column_width=True)


# Captures User Inputs
prompt = st.text_input('Please provide the topic of the video',key="prompt")  # The box for the text prompt
video_length = st.text_input('Expected Video Length 🕒 (in minutes)',key="video_length")  # The box for the text prompt
creativity = st.slider('Creativity limit ✨ - (0 LOW || 1 HIGH)', 0.0, 1.0, 0.2,step=0.1)

submit = st.button("Generate Script for me")

if submit:
    if st.session_state['API_Key']:
        search_result,title,script = generate_script(prompt,video_length,creativity,st.session_state['API_Key'])
        #Let's generate the script
        st.success('Hope you like this script ❤️')
        
        #Display Title
        st.subheader("Title:🔥")
        st.write(title)

        #Display Video Script
        st.subheader("Your Video Script:📝")
        st.write(script)

        #Display Search Engine Result
        st.subheader("Check Out - DuckDuckGo Search:🔍")
        with st.expander('Show me 👀'): 
            st.info(search_result)
    else:
        st.error("Ooopssss!!! Please provide API key.....")