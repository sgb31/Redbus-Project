#pip install psycopg2_binary
#pip install pandas
import pandas as pd
from sqlalchemy import create_engine
import psycopg2


host = "localhost"
port = "5432"
database = "redbusdata"
username = "postgres"
password = "naandhaan"

engine_string = f"postgresql://{username}:{password}@{host}:{port}/{database}"

engine = create_engine(engine_string)

table_name = "redbus"

.to_sql(table_name, engine,if_exists='replace', index=False) 

print("Data successfully pushed to PostgreSQL table!")
