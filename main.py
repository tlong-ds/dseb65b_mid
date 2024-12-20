import streamlit as st
from Account import User
from Modules import VisualHandler
from streamlit_extras.switch_page_button import switch_page

User.create_user_table() # check if database is created

VisualHandler.initialize_session_state() # create session_state

# main function
def main():
    st.balloons()
    switch_page("Home")
if __name__ == "__main__":
    main()