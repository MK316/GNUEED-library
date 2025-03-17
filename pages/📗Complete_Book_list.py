import streamlit as st
import pandas as pd

# Load data
df = pd.read_csv('pages/gnueed-booklist.csv', encoding='utf-8')

def main():
    st.title('English Education Library Book Catalog')
    st.write("Welcome to the English Education Library Book Search Tool! This application allows you to explore our collection of books, sorted either by ID or by title.")

    # User choice for sorting
    sort_choice = st.radio("Sort books by:", ('ID', 'Book Title'))

    if sort_choice == 'ID':
        sorted_df = df.sort_values(by='ID')
    else:
        sorted_df = df.sort_values(by='Book_Title')

    # Display the DataFrame with a scrollbar
    st.dataframe(sorted_df, height=300)  # You can adjust the height as needed

if __name__ == "__main__":
    main()
import streamlit as st
