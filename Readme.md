Movie Recommender System 🎬✨
An interactive web application that recommends movies based on user preferences. It provides a list of similar movies and displays their posters using a content-based filtering approach.

🌟 Features
Movie Recommendations: Suggests top 5 movies similar to the user's selected movie.
Poster Display: Fetches and displays movie posters using the OMDB API.
Interactive UI: Simple and intuitive interface for seamless interaction with the recommendation system.

🛠️ Tech Stack
Programming Language: Python
Libraries:
Streamlit: For building the web app.
Pandas: For handling and analyzing the movie data.
Pickle: For loading preprocessed data and similarity matrices.
Requests: For fetching movie poster data from the OMDB API.
Dataset: A preprocessed dataset containing movie titles and metadata.
OMDB API: Used to fetch movie poster URLs.

🚀 How It Works
Data Loading:
Loads a preprocessed dataset of movies and a similarity matrix using Pickle.
Recommendation Engine:
Identifies the most similar movies to the user’s selected movie using a content-based filtering approach (cosine similarity).
Poster Fetching:
Uses the OMDB API to fetch and display movie posters for the recommended movies.
Frontend:
Built with Streamlit for a clean and responsive user interface.

📂 Project Structure
perl
Copy
Edit
movie-recommender-system/
├── movie_dict.pkl          # Pickle file for the movies dataset
├── similarity.pkl          # Pickle file for the similarity matrix
├── app.py                  # Main application script
├── requirements.txt        # Dependencies for the project
└── README.md               # Project description

🖥️ Usage
Clone the repository:
bash
Copy
Edit
git clone https://github.com/yourusername/movie-recommender-system.git
Install dependencies:
bash
Copy
Edit
pip install -r requirements.txt
Run the application:
bash
Copy
Edit
streamlit run app.py
Access the web app at http://localhost:8501.

🛠️ Key Functions
recommend(movie):
Recommends 5 movies similar to the selected movie based on a precomputed similarity matrix.
get_poster(title):
Fetches the movie poster from the OMDB API.

📊 Results
Provides personalized movie recommendations with an engaging visual experience using posters.
Enables users to explore movies and discover new favorites easily.

🤝 Contributions
Contributions are welcome! Feel free to raise issues, submit pull requests, or suggest new features.