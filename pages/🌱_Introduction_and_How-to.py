import streamlit as st

def main():
    st.markdown('### 🍃 English-Language Books Library (GNU EED)')


    st.write("""
    Welcome to Our Library!
    Our Department of English Education has a library dedicated to providing English books for student reading. Below are the methods available to access the books in our library:
    """)
    st.markdown("---")
    st.markdown("#### 🔸 How to Use the Library")
    st.write("""
    #### 1. Visit in Person
    - **Direct Selection**: You can visit the library in person and choose the books you want directly from the shelves.

    #### 2. Online Search
    - **Search by ID**: Use this search engine to find the ID of the book you are interested in. After finding the ID, visit the library to locate the book by its specified ID.
    - **Check availability**: You can check the availability status of the book you wish to borrow by pressing the button below.
    """)
    st.caption("This Status button can also be found on other pages.")
    # Link to Google Drive File
    file_url = "https://docs.google.com/spreadsheets/d/1wVjJ0kT3eRXC_-1rZ1CQUTrwwCT6TJC5UUuaIQUsiMM/edit?usp=sharing"  # Replace YOUR_FILE_ID with your actual file ID
    st.markdown(
        f"<a href='{file_url}' target='_blank' style='display: inline-block; text-align: center; "
        f"background-color: #4CAF50; color: white; padding: 10px 20px; "
        f"text-decoration: none; border-radius: 4px; margin-top: 10px;'>"
        f"Status: Check Availability</a>", unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("#### 🔸 Reading and Borrowing Books")
    st.write("""
    - **Reading Onsite**: You are welcome to read the books at the library.
    - **Borrowing Books**: If you wish to take books home, please visit the department office to fill out the borrowing ledger.
    """)
    st.markdown("---")
    st.markdown("#### 🔸 Returning Books")
    st.write("""
    - **Book Returns**: When returning books, make sure to check them in with the department assistant to ensure they are properly returned to the library system.
    """)
    st.markdown("---")
    st.caption("We hope you enjoy using our library resources to enhance your learning and research!")

if __name__ == "__main__":
    main()
import streamlit as st

st.caption("Last updated on Mar. 17, 2025")
