import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# 1. Load the dataset dynamically from the books.csv file
df = pd.read_csv('books.csv')

# 2. Vectorization (Convert the book descriptions into mathematical numbers)
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(df['description'])

# 3. Compute Similarity Matrix using Cosine Similarity
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# 4. Recommendation Function
def recommend_book(book_title):
    try:
        # Match the book title (case-insensitive)
        idx = df[df['title'].str.lower() == book_title.lower()].index[0]
        
        # Get similarity scores for all books relative to the selected book
        sim_scores = list(enumerate(cosine_sim[idx]))
        
        # Sort the books based on their similarity scores (highest match first)
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

        print(f"📚 Because you checked out '{df['title'].iloc[idx]}', the LMS recommends:")
        
        # Recommend the top 2 closest books (index 0 is the book itself, so we skip it)
        for i in range(1, 3):
            book_idx = sim_scores[i][0]
            score = sim_scores[i][1]
            print(f"👉 {df['title'].iloc[book_idx]} (Match Score: {score*100:.1f}%)")
            
    except IndexError:
        print(f"❌ Book '{book_title}' not found in the library system.")

# Test it out inside your terminal!
if __name__ == '__main__':
    # You can change 'The Hobbit' to 'Deep Work' or 'Dune' to test different genres!
    recommend_book('The Hobbit')