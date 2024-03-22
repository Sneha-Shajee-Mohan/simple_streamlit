import streamlit as st
import pandas as pd
from b2sdk.v2 import B2Api
from dotenv import load_dotenv
from utils.b2 import B2
from utils.modeling import *
import os

load_dotenv()


# Function to fetch data from Backblaze B2
def fetch_data_from_b2():
    # Initialize B2 API with your account credentials
    b2 = B2(endpoint=os.environ['B2_ENDPOINT'],
        key_id=os.environ['B2_KEYID'],
        secret_key=os.environ['B2_APPKEY'])
    
    buckets = b2.list_buckets() 
    bucket_name = "NPS.ipynbnational_parks.csv" 
    file_names = b2.list_file_names(bucket_name)
    for file_name in file_names:
        if file_name.endswith(".csv"):  # Assuming your file is in CSV format
            file_info = b2.download_file_by_name(bucket_name, file_name)
            df = pd.read_csv(file_info.content)
            return df

    return df

def main():
    st.title('National Parks Data')
    
    # Fetch data from Backblaze B2
    df_parks = fetch_data_from_b2()

    # Display the dataframe
    st.write(df_parks)

    # Show distribution of parks by states
    st.subheader('Distribution of Parks by States')
    state_counts = df_parks['states'].value_counts()
    st.bar_chart(state_counts)

if __name__ == "__main__":
    main()
