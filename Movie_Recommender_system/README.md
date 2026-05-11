# Content-Based Movie Recommendation System

## Overview
This project is a **Content-Based Movie Recommendation System** built using **Natural Language Processing (NLP)** techniques and similarity-based machine learning.

The system recommends movies similar to a selected movie by analyzing its content features such as:
- Overview
- Genres
- Cast
- Crew

It uses **CountVectorizer** to convert text into numerical features and **Cosine Similarity** to measure similarity between movies.

---

## Problem Statement
With a large number of movies available, users often struggle to find relevant content.  

The goal of this project is to build a system that:
- Understands movie content
- Finds similarities between movies
- Recommends top similar movies to the user

---

## Type of Learning
This is an **Unsupervised Learning** project.

- No target variable is predicted
- The system finds similarity between data points
- Recommendations are based on feature similarity

---

## Project Workflow

### 1. Data Collection
- Dataset containing movie metadata
- Includes information such as title, overview, genres, cast, and crew

---

### 2. Data Preprocessing
- Merged datasets
- Selected relevant columns
- Handled missing values
- Removed duplicates

---

### 3. Feature Engineering
- Extracted important features:
  - Overview
  - Genres
  - Keywords
  - Cast (top 3)
  - Crew (director)
- Combined all features into a single column called **tags**

---

### 4. Text Processing
- Converted text to lowercase
- Removed spaces between names (to preserve meaning)
- Created a clean textual representation for each movie

---

### 5. Vectorization
- Applied **CountVectorizer**
- Converted text data into numerical vectors
- Limited features to top 5000 words

---

### 6. Similarity Calculation
- Computed similarity using **Cosine Similarity**
- Measured similarity between all movie vectors

---

### 7. Recommendation System
- Given a movie, find its closest matches
- Return top 5 most similar movies

---

## Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- NLTK (for text preprocessing)
- Streamlit (for UI)
- Pickle (for model saving)

---

## Repository Structure

```markdown
Movie_Recommendation_System/
│
├── app.py
│
├── movie_recommender.ipynb
├── README.md
```

---

## How It Works

- User selects a movie
- System finds its vector representation
- Computes similarity with all other movies
- Sorts movies based on similarity score
- Returns top 5 recommended movies

---

## Streamlit Application

The project includes a Streamlit web application that allows users to:
- Select a movie from a dropdown
- Get instant recommendations
- View movie posters using API integration

--- 

## Key Concepts Used

- Natural Language Processing (NLP)
- Bag of Words (CountVectorizer)
- Cosine Similarity
- Feature Engineering
- Content-Based Filtering

--- 

## Limitations

- Does not consider user preferences
- Recommendations are based only on content similarity
- Less diversity in recommendations
- Does not use collaborative filtering

---

### Future Improvements

- Use TF-IDF Vectorizer for better weighting
- Implement Collaborative Filtering
- Add user-based recommendations
- Improve UI/UX
- Evaluate recommendation quality

--- 

### Key Learning Outcomes

- Built an end-to-end ML pipeline
- Learned feature engineering for text data
- Understood vectorization techniques
- Applied cosine similarity for recommendations
- Developed and deployed a Streamlit application

