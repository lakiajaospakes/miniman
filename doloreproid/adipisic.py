import pandas as pd
from sqlalchemy import create_engine

# Assuming you have a SQLAlchemy engine set up
# Replace 'your_connection_string' with your actual database connection string
engine = create_engine('your_connection_string')

# Define your SQL query
query1 = "SELECT * FROM your_table;"

# Use pd.read_sql to execute the query and read data into a DataFrame
df = pd.read_sql(query1, con=engine)

# Now you can work with the DataFrame 'df'
print(df.head())
