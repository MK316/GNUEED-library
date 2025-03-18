import streamlit as st

def main():
    # Create tabs
    tab1, tab2 = st.tabs(["💙 Introduction", "💜 How to Use"])

    # Content for the Introduction tab
    with tab1:
        st.markdown('### 🍃 English-Language Books Library (GNU EED)')
        st.write("""
        Welcome to Our Library!
        Our Department of English Education has a library dedicated to providing English books for student reading. Below are the methods available to access the books in our library:
        """)
        st.markdown("---")

    # Content for the How to Use tab
    with tab2:
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
        file_url = "https://docs.google.com/spreadsheets/d/1wVjJ0kT3eRXC_-1rZ1CQUTrwwCT6TJC5UUuaIQUsiMM/edit?usp=sharing"
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
        - **Duration**: By default, you can borrow for three weeks and renew once (+2 weeks) for a total of five weeks.
       
        """)
        st.info("❗**Late Return fee**: If you return books late, there is a fee of 500 won per day.")
        st.markdown("---")
        st.markdown("#### 🔸 Returning Books")
        st.write("""
        - **Book Returns**: When returning books, make sure to check them in with the department assistant to ensure they are properly returned to the library system.
        """)
        st.markdown("---")
        st.caption("We hope you enjoy using our library resources to enhance your learning and research!")

if __name__ == "__main__":
    main()

st.caption("Last updated on Mar. 17, 2025")
