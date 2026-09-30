import pandas as pd

df = pd.read_csv("Bike Sales.csv")
print(df.head())
print(df.columns.tolist())
print(df.shape)

Border = "=" * 40

# duplicate removal
df = df.drop_duplicates()

# Missing value check
print(df.isnull().sum())
print("missing value check done")
print(Border)
# ====================================================================

# missing value remove
df = df.dropna()
print("missing value removed")
print(Border)

from urllib.parse import quote_plus
from sqlalchemy import create_engine

password = "Morya@87"
engine = create_engine(
    f"mysql+pymysql://root:{quote_plus(password)}@localhost:3306/bike_sales"
)

with engine.connect() as conn:
    print("MYSQL connection established successfully")
df.to_sql("bike_sales_table", engine, if_exists="replace", index=False)
print("Data loaded successfully to MySQL database")
