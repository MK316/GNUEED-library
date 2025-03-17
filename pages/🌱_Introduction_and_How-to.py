import streamlit as st

def main():
    st.title('English Education Department Library')

    st.write("""
    ## Welcome to Our Library!
    Our Department of English Education has a library dedicated to providing English books for student reading. Below are the methods available to access the books in our library:
    """)

    st.header("How to Use the Library")
    st.write("""
    ### 1. Visit in Person
    - **Direct Selection**: You can visit the library in person and choose the books you want directly from the shelves.

    ### 2. Online Search
    - **Search by ID**: Use this search engine to find the ID of the book you are interested in. After finding the ID, visit the library to locate the book by its specified ID.
    """)

    st.header("Reading and Borrowing Books")
    st.write("""
    - **Reading Onsite**: You are welcome to read the books at the library.
    - **Borrowing Books**: If you wish to take books home, please visit the department office to fill out the borrowing ledger.
    """)

    st.header("Returning Books")
    st.write("""
    - **Book Returns**: When returning books, make sure to check them in with the department assistant to ensure they are properly returned to the library system.
    """)

    st.caption("We hope you enjoy using our library resources to enhance your learning and research!")

if __name__ == "__main__":
    main()
import streamlit as st

st.caption("To be updated")
