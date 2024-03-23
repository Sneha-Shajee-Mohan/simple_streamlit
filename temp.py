import streamlit as st
import pandas as pd
from b2sdk.v2 import B2Api
from dotenv import load_dotenv
from utils.b2 import B2
from utils.modeling import *
import os

REMOTE_DATA = 'NPS.ipynbnational_parks.csv'

load_dotenv()


def fetch_data_from_b2():
    b2 = B2Api()

    b2.authorize_account("production",'00502d1b3f7b27a0000000001', 'K005Y3TomdGj2uMCd0q8aU7wmuemNQ4')
    buckets = b2.list_buckets()

        # Assuming you know the bucket name
    bucket_name = "national-park-demo"

        # List files within the bucket
    file_names = b2.list_file_names(bucket_name)

        # Download the CSV file from the bucket
    for file_name in file_names:
        if file_name.endswith(".csv"):  # Assuming your file is in CSV format
            file_info = b2.download_file_by_name(bucket_name, file_name)
            df = pd.read_csv(file_info.content)
            return df

def main():
    st.title('National Parks Data')
    
    # Fetch data from Backblaze B2
    df_parks = fetch_data_from_b2()

    # Display the dataframe
    st.write(df_parks)

if __name__ == "__main__":
    main()