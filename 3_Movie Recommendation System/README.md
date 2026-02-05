# 🎬 Content-Based Movie Recommendation System

A **content-based movie recommendation system** built using the **TMDB 5000 Movies** and **TMDB 5000 Credits** datasets.  
The system recommends movies similar to a given movie based on features such as **genres, keywords, cast, crew, and overview**.

---

## 📌 Project Overview

This project uses **Natural Language Processing (NLP)** and **cosine similarity** to suggest movies that are similar in content.  
Unlike collaborative filtering, this system does **not depend on user ratings** and works purely on movie metadata.

---

## 📂 Dataset

The project uses two datasets from **The Movie Database (TMDB)**:

- `tmdb_5000_movies.csv`
- `tmdb_5000_credits.csv`

### Key Features Used
- Genres  
- Keywords  
- Cast  
- Crew (Director)  
- Movie Overview  

Total movies: **~5000**

---

## 🛠️ Tech Stack

- **Python**
- **Pandas & NumPy** – Data processing
- **Scikit-learn** – Vectorization & similarity calculation
- **NLTK** – Text preprocessing
- **Cosine Similarity**
- **Jupyter Notebook / Python Script**

---

## ⚙️ How It Works

1. **Data Preprocessing**
   - Merge movie and credit datasets
   - Extract relevant fields (genres, cast, crew, etc.)
   - Clean and normalize text data

2. **Feature Engineering**
   - Combine important attributes into a single `tags` column
   - Apply stemming and text cleaning

3. **Vectorization**
   - Convert text data into vectors using **CountVectorizer**

4. **Similarity Calculation**
   - Compute similarity scores using **cosine similarity**

5. **Recommendation**
   - Given a movie title, return the **top 5 most similar movies**

---

## 🚀 Example Output

```text
Input Movie: Avatar

Recommended Movies:
1. John Carter
2. Guardians of the Galaxy
3. The Avengers
4. Star Wars: The Force Awakens
5. Alien

```
## 🧪 Installation & Usage

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/movie-recommendation-system.git
cd movie-recommendation-system
```
### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt

```
### 3️⃣ Run the Project

Open the Jupyter Notebook
OR

Run the Python script:
```bash
python app.py
```
## 📁 Project Structure
```bash
├── data/
│   ├── tmdb_5000_movies.csv
│   └── tmdb_5000_credits.csv
├── notebook/
│   └── movie_recommendation.ipynb
├── app.py
├── requirements.txt
└── README.md
```
## 🔮 Future Improvements

Add a web interface using Streamlit or Flask

Improve recommendations using TF-IDF

Combine with collaborative filtering

Add movie posters using TMDB API

## 📜 License

This project is for educational purposes only.
Dataset credits belong to TMDB.

## 🙌 Acknowledgements

TMDB for the dataset

Scikit-learn and open-source contributors

## 👤 Author

Shraddha Tiwari\
GitHub: [Shraddha6211](https://github.com/Shraddha6211)


