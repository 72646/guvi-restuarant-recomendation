# guvi-restuarant-recomendation
# Swiggy Restaurant Recommendation System

A Python-based restaurant recommendation system that suggests similar restaurants using machine learning techniques. The project uses restaurant attributes such as city, cuisine, rating, and cost to identify restaurants with similar characteristics.

Developed as part of the GUVI Data Science program, this project demonstrates data preprocessing, feature engineering, similarity-based recommendation, and interactive application development using Streamlit.

## Project Overview

Choosing a restaurant can be challenging when there are numerous options available.

This project addresses that problem by developing a content-based restaurant recommendation system inspired by Swiggy.

It analyzes restaurant information and calculates similarity scores to recommend the top 5 restaurants with characteristics similar to the selected restaurant.

## Key Features

- Restaurant data cleaning and preprocessing.
- Handling missing values and duplicate records.
- Conversion of restaurant cost and rating into usable numerical features.
- One-Hot Encoding of categorical features such as city and cuisine.
- Cosine Similarity for identifying similar restaurants.
- Top 5 restaurant recommendations.
- Interactive user interface developed using Streamlit.
- Displays restaurant information, including name, city, cuisine, rating, and cost.

## Technology Stack

| Category | Technologies |
|---|---|
| Programming Language | Python |
| Data Manipulation | Pandas |
| Machine Learning | Scikit-learn |
| Recommendation Algorithm | Cosine Similarity |
| Feature Engineering | One-Hot Encoding |
| Web Application | Streamlit |
| Model Persistence | Pickle |

## Project Workflow

### 1. Data Preprocessing

The original restaurant dataset is cleaned and prepared for further analysis.

Operations include:
- Removing duplicate records.
- Handling missing values.
- Cleaning restaurant ratings.
- Converting restaurant costs into numerical values.
- Preparing categorical and numerical features.

### 2. Feature Engineering

Categorical features are converted into numerical representations using One-Hot Encoding.

The following features are considered:

- City
- Cuisine
- Restaurant Rating
- Restaurant Cost

These features are combined to create a numerical representation of each restaurant.

### 3. Recommendation Engine

Cosine Similarity is used to calculate similarity between restaurant feature vectors.

The system identifies restaurants with similar characteristics and returns the top 5 recommendations.

### 4. Streamlit Application

A Streamlit application provides an interactive interface for accessing the recommendation system.

Users can explore restaurant recommendations and view relevant restaurant information.

##  Project Structure


guvi-restuarant-recomendation/
|
|- app.py                  # Streamlit application
|- preprocessing.py        # Data cleaning and preprocessing
|- recomendation.py        # Feature engineering and recommendation logic
|- encoder.pkl             # Saved encoding object
│
|-- data/
│   |-- swiggy.csv
│
|-- requirements.txt        # Project dependencies
|-- .gitignore              # Git ignored files
|-- README.md               # Project documentation
```




##  Recommendation Technique

**Cosine Similarity**

Cosine Similarity measures the similarity between two numerical feature vectors based on the cosine of the angle between them.

It is used to identify restaurants that share similar characteristics.

A higher similarity score indicates that two restaurants have more similar feature representations.

##  Learning Outcomes

Through this project, I gained practical experience in:

- Data cleaning and preprocessing.
- Handling missing and duplicate data.
- Feature engineering and categorical encoding.
- Understanding similarity-based recommendation systems.
- Implementing machine learning concepts using Scikit-learn.
- Building interactive data science applications using Streamlit.
- Organizing Python projects into reusable modules.

##  Future Improvements

- Introduce user preference-based recommendations.
- Incorporate additional restaurant attributes.
- Improve numerical feature scaling.
- Add interactive filtering options.
- Deploy the application using Streamlit Community Cloud.

##  Author

**Mohamed Ameen**

Integrated M.Tech – Computer Science and Engineering

Vellore Institute of Technology

GitHub: https://github.com/72646
