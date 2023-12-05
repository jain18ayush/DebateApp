import streamlit as st
import pandas as pd
import numpy as np

# Simulating a DataFrame with names and scores
np.random.seed(0)  # For reproducible random results
names = ["Alice", "Bob", "Charlie", "Diana", "Ethan",
         "Fiona", "George", "Hannah", "Ian", "Julia"]
scores = np.random.randint(0, 100, len(names))
df = pd.DataFrame({'Name': names, 'Score': scores})

# Sorting the DataFrame by scores in descending order
df_sorted = df.sort_values(by='Score', ascending=False)

# Displaying the leaderboard
st.title("Leaderboard")
st.table(df_sorted)
