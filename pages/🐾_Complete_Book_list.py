import streamlit as st
import pandas as pd

# Load data
df = pd.read_csv('pages/gnueed-booklist.csv', encoding='utf-8')

def main():
    st.markdown('### 🐳 English Education Library Book Catalog')
    st.caption("This application allows you to explore our collection of books, sorted either by ID, title, or author name.")
    st.markdown("---")
    # User choice for sorting
    sort_choice = st.radio("📌 Sort books by:", ('ID', 'Book Title (alphabetical)', 'Author (alphabetical)'))

    if sort_choice == 'ID':
        sorted_df = df.sort_values(by='ID')
    elif sort_choice == 'Book Title':
        sorted_df = df.sort_values(by='Book_Title')
    else:
        sorted_df = df.sort_values(by='Author')

    # Display the DataFrame with a scrollbar
    st.dataframe(sorted_df, height=300)  # You can adjust the height as needed

    # Link to Google Drive File
    file_url = "https://docs.google.com/spreadsheets/d/1wVjJ0kT3eRXC_-1rZ1CQUTrwwCT6TJC5UUuaIQUsiMM/edit?usp=sharing"  # Replace YOUR_FILE_ID with your actual file ID
    st.markdown(
        f"<a href='{file_url}' target='_blank' style='display: inline-block; text-align: center; "
        f"background-color: #4CAF50; color: white; padding: 10px 20px; "
        f"text-decoration: none; border-radius: 4px; margin-top: 10px;'>"
        f"Status: Check Availability</a>", unsafe_allow_html=True)


if __name__ == "__main__":
    main()

