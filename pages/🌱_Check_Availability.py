import streamlit as st

    # Link to Google Drive File
    file_url = "https://docs.google.com/spreadsheets/d/1wVjJ0kT3eRXC_-1rZ1CQUTrwwCT6TJC5UUuaIQUsiMM/edit?usp=sharing"  # Replace YOUR_FILE_ID with your actual file ID
    st.markdown(
        f"<a href='{file_url}' target='_blank' style='display: inline-block; text-align: center; "
        f"background-color: #4CAF50; color: white; padding: 10px 20px; "
        f"text-decoration: none; border-radius: 4px; margin-top: 10px;'>"
        f"Status: Check Availability</a>", unsafe_allow_html=True)
