# 📚 Book Recommendation System

This project builds a Book Recommendation System using the Book-Crossing Dataset and collaborative filtering with K-Nearest Neighbors (KNN). The model suggests similar books based on user ratings.

---

## 🔧 Features

- Recommends books based on user similarity and preferences  
- Uses KNN for finding nearest neighbors  
- Filters inactive users and rarely-rated books to improve accuracy  
- Extracts book metadata like author, publisher, and image  
- Saves trained models and data structures for deployment  

---

## 📂 Dataset

The data is from the Book-Crossing Dataset and includes:

- Books (`BX-Books.csv`)  
- Users (`BX-Users.csv`)  
- Ratings (`BX-Book-Ratings.csv`)  

---

## 🛠️ Libraries Used

- `pandas`, `numpy` – data processing  
- `scikit-learn` – model building (KNN)  
- `scipy` – sparse matrix construction  
- `pickle` – model and data serialization  

---

## 🚀 How It Works

1. **Load and Clean Data**  
   - Load book, user, and rating datasets  
   - Clean malformed rows and rename columns  
   - Drop unnecessary image URLs and keep only relevant columns  

2. **Filter Active Users & Popular Books**  
   - Keep users who have rated more than 200 books  
   - Keep books that have more than 50 ratings  

3. **Create Book-User Matrix**  
   - Pivot the ratings dataframe to create a matrix of books vs users  
   - Fill missing ratings with zeros  
   - Convert to sparse format to optimize performance  

4. **Train Model**  
   - Use KNN with cosine similarity to identify similar books  
   - Fit model on the book-user matrix  

5. **Get Recommendations**  
   - Input a book name  
   - Return top 5 similar books using KNN neighbors  

---
