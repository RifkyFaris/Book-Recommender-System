import pickle
import streamlit as st
import numpy as np

# Page config
st.set_page_config(
    page_title="📚 Book Recommender",
    layout="wide",
    initial_sidebar_state="expanded",
)



# Load model and data
model = pickle.load(open('artifacts/model.pkl', 'rb'))
book_names = pickle.load(open('artifacts/book_names.pkl', 'rb'))
final_rating = pickle.load(open('artifacts/final_rating.pkl', 'rb'))
book_pivot = pickle.load(open('artifacts/book_pivot.pkl', 'rb'))

# Custom CSS for modern neumorphic card look
st.markdown("""
    <style>
        .book-card {
            background: #f0f0f3;
            border-radius: 15px;
            box-shadow: 8px 8px 15px #d1d9e6,
                        -8px -8px 15px #ffffff;
            padding: 15px;
            text-align: center;
            transition: all 0.3s ease-in-out;
        }
        .book-card:hover {
            transform: scale(1.02);
        }
        .book-title {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            font-size: 1.1rem;
            margin-top: 10px;
            color: #333;
        }
        .book-image {
            height: 180px;
            width: 120px;
            border-radius: 8px;
            object-fit: cover;
            box-shadow: 0 4px 10px rgba(0,0,0,0.1);
        }
    </style>
""", unsafe_allow_html=True)

# Sidebar
st.sidebar.header("📖 Pick a Book")
selected_book = st.sidebar.selectbox("Choose a book you like:", book_names)

# Recommendation logic
def fetch_posters(suggestions):
    urls = []
    for suggestion_list in suggestions:
        for book_id in suggestion_list:
            book_name = book_pivot.index[book_id]
            idx = np.where(final_rating['title'] == book_name)[0][0]
            urls.append(final_rating.iloc[idx]['image_url'])
    return urls

def recommend_books(book_name):
    book_id = np.where(book_pivot.index == book_name)[0][0]
    distances, suggestions = model.kneighbors(book_pivot.iloc[book_id, :].values.reshape(1, -1), n_neighbors=6)
    poster_urls = fetch_posters(suggestions)
    recommended_books = []
    for suggestion_list in suggestions:
        for book_idx in suggestion_list:
            recommended_books.append(book_pivot.index[book_idx])
    return recommended_books, poster_urls

# Main section
if st.sidebar.button("🎯 Get Recommendations"):
    recommended_books, poster_urls = recommend_books(selected_book)

    st.markdown(f"""
        <div style="text-align: center; padding: 25px 0;">
            <h1 style="color: #4A90E2; font-family: 'Segoe UI', sans-serif;">
                Recommended Books Based on: <em>{selected_book}</em>
            </h1>
        </div>
    """, unsafe_allow_html=True)

    # Display in 2-column layout
    cols = st.columns(2)
    for idx in range(0, 6):  # Skip the first one (it's the input book)
        col = cols[idx % 2]
        with col:
            st.markdown(f"""
                <div class="book-card">
                    <img class="book-image" src="{poster_urls[idx]}" alt="{recommended_books[idx]} cover">
                    <div class="book-title">{recommended_books[idx]}</div>
                </div>
            """, unsafe_allow_html=True)

    st.markdown("<hr>", unsafe_allow_html=True)
    st.success("✨ Try another book from the sidebar for fresh recommendations!")

else:
    st.markdown("""
        <div style="text-align: center; padding: 40px;">
            <h2 style="color:#4A90E2; font-family: 'Segoe UI', sans-serif;">
                Welcome to the Book Recommender System 📘
            </h2>
            <p style="font-size: 1.1rem; color: #444;">
                Select a book from the sidebar and click <strong>“Get Recommendations”</strong> to discover similar reads!
            </p>
        </div>
    """, unsafe_allow_html=True)
