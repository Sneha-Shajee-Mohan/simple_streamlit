import streamlit as st
import pandas as pd
from b2sdk.v2 import B2Api
from dotenv import load_dotenv
from utils.b2 import B2
from utils.modeling import *
import os

REMOTE_DATA = 'NPS.ipynbnational_parks.csv'

load_dotenv()


# Function to fetch data from Backblaze B2

    # Initialize B2 API with your account credentials
b2 = B2(endpoint=os.environ['B2_ENDPOINT'],
        key_id=os.environ['B2_KEYID'],
        secret_key=os.environ['B2_APPKEY'])

@st.cache_data  
def get_data():
    # collect data frame of reviews and their sentiment
    b2.set_bucket(os.environ['B2_BUCKETNAME'])
    df = b2.get_df(REMOTE_DATA)
    
    
    return df


st.title('National Parks Data')
    
    # Fetch data from Backblaze B2
df_parks = get_data()

    # Show distribution of parks by states
st.subheader('Distribution of Parks by States')
# Display the dataframe
st.write(df_parks)

   
state_counts = df_parks['states'].value_counts()
st.bar_chart(state_counts)


