import streamlit as st
import pandas as pd
from b2sdk.v2 import B2Api
from dotenv import load_dotenv
from utils.b2 import B2
from utils.modeling import *
import os

REMOTE_DATA = 'NPS.ipynbnational_parks.csv'

load_dotenv()

b2 = B2Api()

b2.authorize_account('02d1b3f7b27a', "005a5b8b23b64bdae6bf3279e22b2c6dcc54fb691c")
