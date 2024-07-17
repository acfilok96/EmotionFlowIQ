import streamlit as st
from chatBot import ChatBot

st.set_page_config(page_title="FlowIQ", layout="wide", page_icon = 'image/flowIQ8-1.png', initial_sidebar_state = 'auto')

st.markdown("""
<style>
.big-font-1 {
    font-size:30px !important;
    text-align: center; 
    color: yellow
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>
    [data-testid=stSidebar] {
        background-color: #20200F;
    }
</style>
""", unsafe_allow_html=True)

def main(): 
    # st.sidebar.markdown('<p class="big-font-1">FlowIQ</p>', unsafe_allow_html = True)
    
    st.sidebar.image("image/flowIQ5-1.png")
    # st.sidebar.write(":#65E83B[Hello]")
    st.sidebar.info("""
    
    :rainbow[**Welcome to FlowIQ !**] \n
    :blue[It has a memory so it speaks with emotion.]
    
    """)
    # st.sidebar.success("It talks emotionally and has a memory.")
    
    ChatBot()

    show_advanced_info_1 = st.sidebar.toggle(":blue[*Application Details*]", value = False)
    
    if show_advanced_info_1:
        st.sidebar.info("""

                    :rainbow[**AI Chatbot**]
                    
                    :blue[**Model:** *Llama3*]
                    
                    :blue[**Language:** *English*]
                    
                    :blue[**Release Date:** *July, 2024*]
                    
                    """)
        
    show_advanced_info_2 = st.sidebar.toggle(":blue[*Developer Details*]", value = True)
    
    if show_advanced_info_2:
        st.sidebar.info("""
                    
                    :rainbow[**This appplication has been created by [:blue[Dipankar Porey]](https://www.linkedin.com/in/dipankar-porey-403320259/),
                    BluWebMedia Pvt. Ltd., Ernst & Young.**] 
                    
                    """)

       
if __name__ == '__main__':
    main()
