import streamlit as st
from excuses import Excuses
from streamlit_chat import message
from functions import ChatModel
from avatars import Avatar


def ChatBot():
    
    # container_11 = st.container(height = 350, border = False)
    
    if "messages_show" not in st.session_state:
        st.session_state.messages_show = []

    # with container_11:
    
    k = 1
    for message_s in st.session_state.messages_show:
        if message_s["role"] == "user":
            avatar_style = str(Avatar.listofAvatar())
            message(message_s["content"], is_user = True, key = str(k) + '_user', avatar_style = avatar_style, seed = "user")
        elif message_s["role"] == "assistant":
            avatar_style = str(Avatar.listofAvatar())
            message(message_s["content"], key = str(k), avatar_style = avatar_style, seed = "assistant", allow_html = True)
        k += 1

    def clear_chat_history():
        st.session_state.messages_show = []
        
    col1, col2 = st.sidebar.columns((0.35,1.75))
    with col2:
        st.button(':green[*New Chat*]', on_click = clear_chat_history)
    
    if prompt := st.chat_input("Hey, there 😊!"):
        
        st.session_state.messages_show.append({"role": "user", "content": prompt})
        
        # with container_11:
        avatar_style = str(Avatar.listofAvatar()) 
        message(prompt, is_user = True, key = str(k) + '_user', avatar_style = avatar_style, seed = "user")

        k += 1
        with st.spinner(":blue[Typing . . .]"): 
            try:
                message_list = st.session_state.messages_show[-15:] if len(st.session_state.messages_show) > 15 else st.session_state.messages_show
                response = ChatModel.GroqFunction(message_list)
                avatar_style = str(Avatar.listofAvatar()) 
                message(response , key = str(k), avatar_style = avatar_style, seed = "assistant", allow_html=True)
            except Exception as e:
                response = Excuses.listofExcuses()
                avatar_style = str(Avatar.listofAvatar()) 
                message(response, key = str(k), avatar_style = avatar_style, seed = "assistant", allow_html=True)
            
        st.session_state.messages_show.append({"role": "assistant", "content": response})
    else:
        # a1, a2 = st.columns((1.55, 2.45))
        # with a2:
        #     st.image("image/flowIQ5-1.png", width = 210)
        st.info("""
        
        :rainbow[**FlowIQ(🗣): Hi, I am FlowIQ & I have a memory. So, I can remember a little of our conversation & that \
        why I get little emotional sometime😊. Also I can talk in any language like bengali, hindi and many more. \
        By the way, english is my first language.**]

        :rainbow[**So, what about you ! Well, let me start first, Hey👋! How's going your day ?**]

        """)
