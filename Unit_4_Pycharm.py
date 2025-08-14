### 1. Sourcing and Loading

# Import the pandas, numpy libraries as pd, and np respectively.

import pandas as pd
import numpy as np

# Load the pyplot collection of functions from matplotlib, as plt

import matplotlib.pyplot as plt

#### 1.2.  Loading the data

# First, make a variable called url_LondonHousePrices, and assign it the following link, enclosed in quotation-marks as a string:
# https://data.london.gov.uk/download/uk-house-price-index/70ac0766-8902-4eb5-aab5-01951aaed773/UK%20House%20price%20index.xls

url_LondonHousePrices = "https://data.london.gov.uk/download/uk-house-price-index/70ac0766-8902-4eb5-aab5-01951aaed773/UK%20House%20price%20index.xls"

# Specify the sheet name in the read_excel() method.

properties = pd.read_excel(url_LondonHousePrices, sheet_name='Average price', index_col= None)

### 2. Cleaning, transforming, and visualizing

#### 2.1. Exploring your data

print(properties.head(), properties.shape(), properties.info())