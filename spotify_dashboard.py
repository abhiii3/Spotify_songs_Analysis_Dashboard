import streamlit as st
import pandas as pd
import plotly.express as px
import streamlit as st

# Custom CSS for background color
st.markdown("""
    <style>
    .stApp {
        background-color: navy blue;  
    }
    </style>
    """, unsafe_allow_html=True)
st.title("🎵 Spotify Songs Analysis Dashboard")
# Display logo
st.image("logo.png.png", width=100)  # Adjust width as needed

# Custom sidebar design
st.sidebar.markdown("""
    <style>
    .css-1d391kg {
        background-color: #191414;  /* Dark background */
        color: white;
        border-radius: 10px;
        padding: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# Custom footer
st.markdown("""
    <div style="background: linear-gradient(to right, #191414, #1DB954); padding: 20px; border-radius: 10px; color: white; text-align: center; margin-top: 20px;">
        <p>© 2024 Spotify Songs Analysis Dashboard</p>
    </div>
    """, unsafe_allow_html=True)


# Load data
st.title("Spotify Songs Analysis Dashboard")
df = pd.read_csv("spotify_songs.csv")  # Update the path if needed

st.header("Dataset Overview")
st.write(df.head())

st.header("Summary Statistics")
st.write(df.describe())

# Select feature for analysis
feature = st.selectbox("Select a feature to analyze", df.select_dtypes(include='number').columns)

st.header(f"Distribution of {feature}")
fig = px.histogram(df, x=feature, nbins=30, title=f"Distribution of {feature}")
st.plotly_chart(fig)

st.header("Top Artists")
top_artists = df['artist'].value_counts().head(10)
st.bar_chart(top_artists)

st.header("Correlation Heatmap")
corr = df.select_dtypes(include='number').corr()
fig2 = px.imshow(corr, text_auto=True, title="Correlation Heatmap")
st.plotly_chart(fig2)

st.header("Scatter Plot")
x_axis = st.selectbox("X-axis", df.select_dtypes(include='number').columns, index=0)
y_axis = st.selectbox("Y-axis", df.select_dtypes(include='number').columns, index=1)
fig3 = px.scatter(df, x=x_axis, y=y_axis, color='artist', title=f"{x_axis} vs {y_axis}")
st.plotly_chart(fig3)

