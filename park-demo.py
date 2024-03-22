import streamlit as st
import pandas as pd
from b2sdk.v2 import B2Api
from dotenv import load_dotenv
from utils.b2 import B2
import os

load_dotenv()




# Function to fetch data from Backblaze B2
def fetch_data_from_b2():
    # Initialize B2 API with your account credentials
    # b2 = B2Api()
    # b2.authorize_account("02d1b3f7b27a", "005a5b8b23b64bdae6bf3279e22b2c6dcc54fb691c")
    # b2.authorize_account('02d1b3f7b27a','005a5b8b23b64bdae6bf3279e22b2c6dcc54fb691c')
    b2 = B2(endpoint=os.environ['B2_ENDPOINT'],
        key_id=os.environ['B2_KEYID'],
        secret_key=os.environ['B2_APPKEY'])


    # Download the CSV file from B2 bucket
    bucket = b2.get_bucket_by_name("national-park-demo")
    file_info = bucket.download_file_by_name("NPS.ipynbnational_parks.csv")

    # Read the CSV file into a pandas dataframe
    df = pd.read_csv(file_info.content)

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
