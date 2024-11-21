import streamlit as st
from p_test.mbti_test import test
from p_test.result import display_results
from streamlit_extras.switch_page_button import switch_page
from Modules import VisualHandler, Time

st.set_page_config(
    page_title="Personality Test",
    page_icon="📝",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.title("MBTI Personality Test")
VisualHandler.initial()

# Initialize session states
if 'ptype' not in st.session_state:
    st.session_state['ptype'] = None
if 'stage' not in st.session_state:
    st.session_state['stage'] = 0
if 'completed' not in st.session_state:
    st.session_state['completed'] = False
if 'name' not in st.session_state:
    st.session_state['name'] = None

# Main function to display the test
def display_test():
    placeholder = st.empty()

    # Input the user name
    if st.session_state['name'] == None:
        st.markdown(f'<p class="question-text">Good {pod}. What\'s your name?</p>', unsafe_allow_html=True)
        name_input = st.text_input(f'Enter your name here: ')
        if name_input:
            st.session_state['name'] = name_input 
            st.rerun()  
    else:
        placeholder.markdown(f"""Good {pod}, {st.session_state['name']}! 
                                 Are you ready to take your personality test? <br> 
                                 There are <b>60 questions</b> in this test, 
                                 and you have to answer all of them to identify your personality type. <br>
                                 If you are ready, click <b>Yes</b>. Otherwise, click <b>No</b>. You can still see the test later!
                              """, unsafe_allow_html=True)
        
        if 'clicked' not in st.session_state:
            st.session_state['clicked'] = False

        if not st.session_state.clicked:
            col1, col2 = st.columns(2)
            with col1:
                if st.button('Yes'):
                    st.session_state.stage = 1
                    st.session_state.clicked = True
                    st.rerun()
            with col2:
                if st.button('No'):
                    st.session_state.stage = 2
                    st.session_state.clicked = True
                    st.rerun()
        # Start the test
        if st.session_state.stage == 1:
            placeholder.markdown(f"""
                                 Alright, {st.session_state['name']}. Let's start the test! <br>
                                 """, unsafe_allow_html=True)
            test()
            if st.session_state["completed"]: st.rerun()
            
        # Exit the test
        if st.session_state.stage == 2:
            placeholder.write("If you change your mind, you can reload the page or press this button!")
            st.button('Restart', on_click=reset_app, key="re_entering")
        
        # Display the results
        if st.session_state.stage == 3 and st.session_state["completed"]:
            placeholder.write(f"")
            display_results()
            if st.button("Learn more"):
                switch_page("Personality Types")

display_test()