import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
import seaborn as sns

# Display the app title and description
st.write("""
# ALNALYZE
""")

# Load the dataset
df = pd.read_csv("data/movie_final.csv")

# Limit to the top 1000 rows
df = df.head(100)
# info
df.info()
df.drop(df[df['rating_avg'] > 5].index, inplace=True)


# Preview the data
st.write("### Data Preview", df.head(5))

# Select columns for visualization
st.write("### Select Columns for Visualization")


numeric_columns = ['rating_count', 'rating_avg']  # Columns likely to be numeric

columns = st.multiselect("Choose numeric columns to plot (y-axis):", numeric_columns)

# # Check if at least one column is selected
# if columns:
#     # Allow the user to choose an index for the x-axis
#     x_column = st.selectbox("Choose an index column (x-axis):", ['movieId', 'title'], )
    
#     # Prepare the data for plotting
#     df_selected = df.set_index(x_column)[columns]

#     # Display the line chart
#     st.line_chart(df_selected)
# else:
#     st.write("Please select at least one numeric column for the chart.")

genres = df['genres']

fig = plt.figure(figsize=(12,6))
sns.barplot(x=genres.values, y=genres.index, palette='RdGy')
plt.title('Distribution of Genres for Movies and Tv shows according to netflix', fontsize=16)
plt.xlabel('Count',fontsize=14)
plt.ylabel('Genre',fontsize=14)
plt.grid(axis='x')
st.pyplot(fig)

#  genre list graph pie chart 


# Command to run the app
st.write("Run this command to start the app:")
st.code("streamlit run movies.py --server.port 20000")
