# Step 1: Import Libraries
import yfinance as yf
import pandas as pd
from sqlalchemy import create_engine
import pymysql

# Step 2: Extract Real-Time Stock Data using yfinance
ticker = 'AAPL'  # You can replace 'AAPL' with any other stock ticker
stock_data = yf.Ticker(ticker)

# Fetch historical stock data (last 1 month as an example)
df = stock_data.history(period='1mo')

# Optional: Add additional financial metrics like moving average
df['SMA_10'] = df['Close'].rolling(window=10).mean()  # 10-day Simple Moving Average

print(df.head())  # To verify the data extraction

# Step 3: Set up SQLAlchemy Engine to connect to your SQL database
username = 'root'  # Your MySQL username
password = 'Sakshiw@01'  # Your MySQL password
database = 'stock_db'  # Your database name

# Specify the correct connection string
try:
    engine = create_engine('mysql+pymysql://root:Sakshiw%4001@127.0.0.1:3306/stock_db')


    
    # Step 4: Load the stock data into a SQL database table
    df.to_sql('stock_prices', con=engine, if_exists='replace', index=False)
    
    print("Data successfully loaded into the SQL database.")
except Exception as e:
    print(f"An error occurred: {e}")
print(df.head())
df.index = pd.to_datetime(df.index)  # Ensure the index is recognized as datetime
df.to_sql('stock_prices', con=engine, if_exists='replace', index=True)
df.reset_index(inplace=True)  # Move the Date index back to a column
df.to_sql('stock_prices', con=engine, if_exists='replace', index=False)

