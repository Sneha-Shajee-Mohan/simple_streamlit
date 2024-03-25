import streamlit as st
import pandas as pd
from b2sdk.v2 import B2Api
from b2sdk.v2 import DownloadedFile
from dotenv import load_dotenv
from utils.b2 import B2
from utils.modeling import *
import os

REMOTE_DATA = 'https://f005.backblazeb2.com/file/national-park-demo/NPS.ipynbnational_parks.csv'

load_dotenv()


# Function to fetch data from Backblaze B2

    # Initialize B2 API with your account credentials
# b2 = B2(endpoint=os.environ['B2_ENDPOINT'],
#         key_id=os.environ['B2_KEYID'],
#         secret_key=os.environ['B2_APPKEY'])
b2 = B2Api()
b2.authorize_account("production",'00502d1b3f7b27a0000000001', 'K005Y3TomdGj2uMCd0q8aU7wmuemNQ4')
# st.write(b2)
@st.cache_data  
def get_data():
    # collect data frame of reviews and their sentiment
    # b2.set_bucket(os.environ['B2_BUCKETNAME'])
    # df = b2.get_df(REMOTE_DATA)
    
    
    # return df
    bucket = b2.get_bucket_by_name(os.environ['B2_BUCKETNAME'])
    # file_info = bucket.get_file_info_by_name('NPS.ipynbnational_parks.csv')
    file_down = bucket.download_file_by_id('4_z10a2ed515be36f778be2071a_f11770dc54974fd9b_d20240322_m181900_c005_v0501005_t0028_u01711131540363')
    # st.write(file_down)
    path = "/Users/sneha/GitHub/simple_streamlit/file_from_B2.csv"
    file_from_B2 = DownloadedFile.save_to(file_down,"file_from_B2.csv",mode='wb+',allow_seeking=True)
    # Read the CSV file into a pandas dataframe

    df = pd.read_csv(file_from_B2)

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


