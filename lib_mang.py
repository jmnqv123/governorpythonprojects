import streamlit as st
import pandas as pd
import os

# File to persist data
DATA_FILE = "library.csv"

# Load or create the data
def load_data():
    if os.path.exists(DATA_FILE):
        return pd.read_csv(DATA_FILE)
    else:
        return pd.DataFrame(columns=["Title", "Author", "Genre"])

# Save data to CSV
def save_data(df):
    df.to_csv(DATA_FILE, index=False)

# App UI
def main():
    st.title("📚 Personal Library Manager")

    df = load_data()

    menu = ["Add Book", "View Library", "Search Books", "Remove Book"]
    choice = st.sidebar.selectbox("Choose Action", menu)

    if choice == "Add Book":
        st.subheader("➕ Add a New Book")
        title = st.text_input("Book Title")
        author = st.text_input("Author")
        genre = st.selectbox("Genre", ["Fiction", "Non-Fiction", "Sci-Fi", "Mystery", "Biography", "Other"])

        if st.button("Add"):
            if title and author:
                new_row = {"Title": title, "Author": author, "Genre": genre}
                df = df.append(new_row, ignore_index=True)
                save_data(df)
                st.success(f"Added '{title}' to your library!")
            else:
                st.warning("Please fill out both title and author.")

    elif choice == "View Library":
        st.subheader("📖 Your Library")
        st.dataframe(df)

    elif choice == "Search Books":
        st.subheader("🔍 Search Library")
        search_term = st.text_input("Enter book title or author")
        if search_term:
            result = df[df.apply(lambda row: search_term.lower() in row.to_string().lower(), axis=1)]
            st.write(f"Found {len(result)} book(s):")
            st.dataframe(result)

    elif choice == "Remove Book":
        st.subheader("❌ Remove Book")
        book_to_remove = st.selectbox("Select a book to remove", df["Title"])
        if st.button("Remove"):
            df = df[df["Title"] != book_to_remove]
            save_data(df)
            st.success(f"Removed '{book_to_remove}' from your library.")

if __name__ == "__main__":
    main()
