import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import altair as alt

# Load the dataset
df = pd.read_csv("/home/sam/python_css2025.py/weather.csv")


# Streamlit Page Title
st.title("Weather Visualization")


# Show the raw dataframe (Optional)
st.subheader("Raw Weather Data")
st.dataframe(df)

# Show summary of the dataframe
st.subheader("Data Summary")
st.write(df.describe())

# Check if the data contains any missing values
st.subheader("Missing Data Check")
st.write(df.isnull().sum())

# Cache the data loading function
@st.cache_data
def load_weather():
    df = pd.read_csv("/home/sam/python_css2025.py/weather.csv")
 
    return df

# Load data
df = load_weather()

# Display DataFrame
st.write("## Weather Data Overview")
st.dataframe(df.head())

# Select columns for visualization
columns = list(df.columns)
selected_x = st.selectbox("Select X-axis", columns, index=0)
selected_y = st.selectbox("Select Y-axis", columns, index=1)

# Plot using Altair
st.write("### Altair Chart")
chart = (
    alt.Chart(df)
    .mark_circle(size=60, opacity=0.6)
    .encode(
        x=selected_x,
        y=selected_y,
        tooltip=[selected_x, selected_y]
    )
).interactive()
st.altair_chart(chart, use_container_width=True)

# Plot using Matplotlib
st.write("### ")
fig, ax = plt.subplots()
ax.scatter(df[selected_x], df[selected_y], alpha=0.6)
ax.set_xlabel(selected_x)
ax.set_ylabel(selected_y)
ax.set_title(f"Scatter Plot: {selected_x} vs {selected_y}")
st.pyplot(fig)

# Correlation Matrix
if st.checkbox("Show Correlation Matrix"):
    st.write("### Correlation Matrix")
    st.dataframe(df.corr())
    fig, ax = plt.subplots()
    cax = ax.matshow(df.corr(), cmap="coolwarm")
    fig.colorbar(cax)
    st.pyplot(fig)


# Plot MinTemp vs MaxTemp
st.subheader("MinTemp vs MaxTemp")
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(df["MinTemp"], label="MinTemp", color='blue', marker='o')
ax.plot(df["MaxTemp"], label="MaxTemp", color='red', marker='o')
ax.set_xlabel("Index (Time or Day)")
ax.set_ylabel("Temperature (°C)")
ax.set_title("MinTemp and MaxTemp over Time")
ax.legend()
st.pyplot(fig)


# Plot Sunshine Duration
st.subheader("Sunshine Duration")
fig, ax = plt.subplots(figsize=(10, 5))
ax.bar(df.index, df["Sunshine"], color='orange')
ax.set_xlabel("Index (Time or Day)")
ax.set_ylabel("Sunshine (hours)")
ax.set_title("Sunshine Duration over Time")
st.pyplot(fig)

# Plot Pressure at 9am vs 3pm
st.subheader("Pressure at 9am vs 3pm")
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(df["Pressure9am"], label="Pressure at 9am", color='purple')
ax.plot(df["Pressure3pm"], label="Pressure at 3pm", color='brown')
ax.set_xlabel("Index (Time or Day)")
ax.set_ylabel("Pressure (hPa)")
ax.set_title("Pressure at 9am vs 3pm")
ax.legend()
st.pyplot(fig)

# Plot Cloud Cover at 9am vs 3pm
st.subheader("Cloud Cover at 9am vs 3pm")
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(df["Cloud9am"], label="Cloud Cover at 9am", color='gray', marker='o')
ax.plot(df["Cloud3pm"], label="Cloud Cover at 3pm", color='lightgray', marker='o')
ax.set_xlabel("Index (Time or Day)")
ax.set_ylabel("Cloud Cover (%)")
ax.set_title("Cloud Cover at 9am vs 3pm")
ax.legend()
st.pyplot(fig)

# Plot Temp at 9am vs 3pm
st.subheader("Temperature at 9am vs 3pm")
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(df["Temp9am"], label="Temperature at 9am", color='cyan', marker='o')
ax.plot(df["Temp3pm"], label="Temperature at 3pm", color='magenta', marker='o')
ax.set_xlabel("Index (Time or Day)")
ax.set_ylabel("Temperature (°C)")
ax.set_title("Temperature at 9am vs 3pm")
ax.legend()
st.pyplot(fig)

# Plot Rainfall Histogram
st.subheader("Rainfall Distribution")
fig, ax = plt.subplots(figsize=(10, 5))
ax.hist(df["Rainfall"].dropna(), bins=20, color='blue', edgecolor='black')
ax.set_xlabel("Rainfall (mm)")
ax.set_ylabel("Frequency")
ax.set_title("Distribution of Rainfall")
st.pyplot(fig)

# Pie Chart for Cloud Cover at 9am
st.subheader("Pie Chart: Cloud Cover at 9am")
cloud_coverage = df["Cloud9am"].value_counts()  # Count occurrences of each cloud cover level
fig, ax = plt.subplots(figsize=(8, 8))
ax.pie(cloud_coverage, labels=cloud_coverage.index, autopct='%1.1f%%', startangle=45, 
          colors = ['#FFB6C1', '#FFDAB9', '#E6E6FA', '#B0E0E6', '#98FB98', '#FAFAD2', '#D8BFD8', '#F5DEB3', '#ADD8E6'])
ax.set_title("Distribution of Cloud Cover at 9am")
st.pyplot(fig)


st.write("- by Paulina Makhubele")




