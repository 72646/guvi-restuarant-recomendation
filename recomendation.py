import pandas as pd
from sklearn.preprocessing import OneHotEncoder
import pickle

# Load cleaned dataset
df = pd.read_csv("cleaned_data.csv")

features = df[['city','cuisine','rating','cost']]

encoder = OneHotEncoder(handle_unknown='ignore')

encoded = encoder.fit_transform(features[['city','cuisine']]).toarray()

encoded_df = pd.DataFrame(encoded)

encoded_df['rating'] = df['rating']
encoded_df['cost'] = df['cost']

encoded_df = encoded_df.fillna(0)

# Save encoded dataset
encoded_df.to_csv("encoded_data.csv", index=False)

# Save encoder
with open("encoder.pkl","wb") as f:
    pickle.dump(encoder,f)

print("Encoding completed successfully")