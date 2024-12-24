import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time
from datetime import datetime
import base64

# Adding title of app
st.title("My First App")

# Adding simple text
st.write("Here is a simple text")

# Sidebar Customization
st.sidebar.title("User Preferences")

# 1. Add a Theme Selection
theme = st.sidebar.radio("Choose a Theme", ("Light", "Dark"))

if theme == "Light":
    st.write("You selected Light Theme.")
else:
    st.write("You selected Dark Theme.")

# 2. User Info Form (Collect Name and Age)
st.sidebar.subheader("User Information")
name = st.sidebar.text_input("Enter your name:")
age = st.sidebar.slider("Select your age:", 18, 100, 25)

if name:
    st.sidebar.write(f"Hello, {name}!")
    st.sidebar.write(f"You are {age} years old.")

# 3. Allow File Upload in Sidebar (Multiple File Types)
uploaded_file = st.sidebar.file_uploader("Choose a file", type=["csv", "xlsx", "json"])

if uploaded_file is not None:
    # Show file type info
    file_type = uploaded_file.type
    st.sidebar.write(f"Uploaded File Type: {file_type}")

    # Display contents based on file type
    if file_type == "csv":
        df = pd.read_csv(uploaded_file)
        st.write("CSV File Content:")
        st.write(df)
    elif file_type == "xlsx":
        df = pd.read_excel(uploaded_file)
        st.write("Excel File Content:")
        st.write(df)
    elif file_type == "json":
        df = pd.read_json(uploaded_file)
        st.write("JSON File Content:")
        st.write(df)

# User input with a slider
number = st.slider('Pick a number', 0, 100, 10)
st.write(f'You selected: {number}')

# Adding a button
if st.button('Greeting'):
    st.write('Hi, hello there!')
else:
    st.write('Goodbye!')

# Add radio button with options
genre = st.radio("What is your favorite movie genre", ('Comedy', 'Drama', 'Documentary'))
st.write(f'You selected: {genre}')

# Add drop-down list in the sidebar
option1 = st.sidebar.selectbox('How would you like to be contacted?', ('Email', 'Home Phone', 'Mobile Phone'))

# Add your WhatsApp number in the sidebar
st.sidebar.text_input('Enter your WhatsApp Number')

# Add a date input for selecting dates
date_input = st.date_input("Pick a date", min_value=datetime(2020, 1, 1), max_value=datetime(2025, 12, 31))
st.write(f'You selected: {date_input}')

# Create a line plot with dynamic data range
st.subheader("Line Plot Example")

# Slider for dynamic data range adjustment
num_points = st.slider("Select the number of points in the plot", 1, 100, 10)

# Generate data based on the slider input
data = {
    'First Column': np.arange(1, num_points + 1),
    'Second Column': np.random.randint(1, 100, num_points)
}

# Create a DataFrame
df = pd.DataFrame(data)

# Display line chart
st.line_chart(df)

# Checkbox to toggle the display of the plot
show_plot = st.checkbox("Show the plot")
if show_plot:
    st.write(df)
else:
    st.write("Plot is hidden.")

# Display another type of plot (e.g., bar plot)
st.subheader("Bar Plot Example")
st.bar_chart(df['Second Column'])

# Add a message box with input (with a unique key)
message = st.text_area("Leave a message", value="", key="message_1")  # Adding a unique key
if message:
    st.write(f"Your message: {message}")

# Add a button to clear the text input or message (with a unique key for the second text area)
if st.button("Clear Message"):
    st.text_area("Leave a message", value="", key="message_2")  # Unique key for the clear action

# Display an image upload feature
image = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])
if image is not None:
    st.image(image, caption="Uploaded Image.", use_column_width=True)

# Show a progress bar
st.subheader("Progress Bar Example")
progress_bar = st.progress(0)

for i in range(100):
    progress_bar.progress(i + 1)
    time.sleep(0.05)  # Simulate a delay

st.write("Progress bar completed!")

# Allow users to download a CSV of the displayed data
st.subheader("Download CSV")
csv = df.to_csv(index=False)


# Create a download link
def get_csv_download_link(csv_data):
    b64 = base64.b64encode(csv_data.encode()).decode()  # Encoding the CSV data to base64
    return f'<a href="data:file/csv;base64,{b64}" download="data.csv">Download CSV</a>'


st.markdown(get_csv_download_link(csv), unsafe_allow_html=True)

# Display an interactive DataFrame
st.subheader("Interactive DataFrame")

# Create a DataFrame with random values and display it interactively
df_interactive = pd.DataFrame(np.random.randn(10, 3), columns=["Column A", "Column B", "Column C"])
st.write(df_interactive)

# Add a map with markers
st.subheader("Map Example")

# Set up random latitudes and longitudes for demonstration
latitude = np.random.uniform(low=35.0, high=40.0, size=10)
longitude = np.random.uniform(low=-120.0, high=-115.0, size=10)

# Create a DataFrame for the map
map_data = pd.DataFrame({
    'lat': latitude,
    'lon': longitude
})

st.map(map_data)
