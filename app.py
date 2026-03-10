import streamlit as st
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# Load datasets
df = pd.read_csv("cleaned_data.csv")
encoded_df = pd.read_csv("encoded_data.csv")

st.title("Swiggy Restaurant Recommendation System")

restaurant = st.selectbox("Select Restaurant", df['name'].sample(1000))


def recommend(index):

    # vector of selected restaurant
    selected_vector = encoded_df.iloc[index].values.reshape(1, -1)

    # compute similarity only with this vector
    similarity_scores = cosine_similarity(selected_vector, encoded_df)

    scores = list(enumerate(similarity_scores[0]))

    scores = sorted(scores, key=lambda x: x[1], reverse=True)[1:6]

    restaurant_indices = [i[0] for i in scores]

    return df[['name','city','cuisine','rating','cost']].iloc[restaurant_indices]


if st.button("Recommend"):

    index = df[df['name'] == restaurant].index[0]

    results = recommend(index)

    st.write("### Recommended Restaurants")

    st.dataframe(results)