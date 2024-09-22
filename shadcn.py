import streamlit_shadcn_ui as ui
import streamlit as st

st.header("SARA AI  &nbsp;&nbsp;:brain: :calendar: :zap:")

st.text("No more fretting over upcoming Audits or Course Exams")
st.text("Stay up to date with new revised Standard Operating Procedure")

ui.badges(badge_list=[("Lifesaver Labs", "secondary"), ("Sentosa Fire Station", "secondary"), ("TFTD", "secondary")], class_name="flex gap-2", key="badges1")

import streamlit as st
import streamlit_shadcn_ui as ui


# Create the tabs with two options: 'Page 1' and 'Page 2'
selected_tab = ui.tabs(options=['Page 1', 'Page 2'], default_value='Page 1', key="main_tabs")

# Logic for switching between pages
if selected_tab == 'Page 1':
    st.subheader("This is Page 1")
    st.write("Content for Page 1 goes here.")
    uploaded_file = st.file_uploader("", type="pdf")
    # Add any additional components or content specific to Page 1

elif selected_tab == 'Page 2':
    st.subheader("This is Page 2")
    st.write("Content for Page 2 goes here.")
    # Add any additional components or content specific to Page 2

