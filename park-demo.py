import streamlit as st
import pandas as pd
from b2sdk.v2 import B2Api
from dotenv import load_dotenv
from utils.b2 import B2
from utils.modeling import *
import os

load_dotenv()


# Function to fetch data from Backblaze B2

    # Initialize B2 API with your account credentials
b2 = B2(endpoint=os.environ['B2_ENDPOINT'],
        key_id=os.environ['B2_KEYID'],
        secret_key=os.environ['B2_APPKEY'])
    
def get_data():
    # collect data frame of reviews and their sentiment
    b2.set_bucket(os.environ['B2_BUCKETNAME'])
    df = b2.get_df(df_Parks)

    # average sentiment scores for the whole dataset
    
    
    return df

def main():
    st.title('National Parks Data')
    
    # Fetch data from Backblaze B2
    df_parks = get_data()

    # Display the dataframe
    st.write(df_parks)

    # Show distribution of parks by states
    st.subheader('Distribution of Parks by States')
    state_counts = df_parks['states'].value_counts()
    st.bar_chart(state_counts)

if __name__ == "__main__":
    main()
