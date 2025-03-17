import streamlit as st
import pandas as pd

# Load data
df = pd.read_csv('pages/gnueed-booklist.csv', encoding='utf-8')

def search_books(category, search_query):
    """Searches books by category and title/author with partial matching."""
    # Filter by category if 'General' or 'Series' is selected
    if category != 'All':
        filtered_df = df[df['Category'] == category]
    else:
        filtered_df = df
    
    # Search by title or author
    if search_query:
        filtered_df = filtered_df[
            (filtered_df['Book_Title'].str.contains(search_query, case=False, na=False)) |
            (filtered_df['Author'].str.contains(search_query, case=False, na=False))
        ]
    
    return filtered_df[['ID', 'Book_Title', 'Author']]

def main():
    st.title('GNU EED Library Book Search Tool')
    st.write("Welcome to the Book Search Tool! Use this application to search for books by category, title, or author name.")
    
    st.subheader("Search Filters")
    category = st.radio("Select Category", ['All', 'General', 'Series'], index=0)
    search_query = st.text_input("Search by Title or Author (Partial matching allowed)")
    st.caption("You can search using partial words from the book title or author's name. There is no need to write the full title.")
    st.subheader("Search Results")
    if st.button('Search'):
        results = search_books(category, search_query)
        if not results.empty:
            st.dataframe(results)
        else:
            st.write("No books found matching the criteria.")

if __name__ == "__main__":
    main()
