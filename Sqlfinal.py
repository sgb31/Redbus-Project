import streamlit as st
import pandas as pd
import streamlit_pandas as sp
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

connection = psycopg2.connect(
    host="localhost",
    user="postgres",            
    password="naandhaan",
    database="Redbusdata"
)

connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

writer = connection.cursor()

writer.execute('SELECT * FROM public."Redbus"')

database="Redbusdata"
a=writer.fetchall()
df=pd.DataFrame(a)

a=['index','S_no','route_collected','name','type','departure_time','arrival_time','duration','price','seats_available','rating']
df.columns=a

df=df.drop(columns='index',axis=1)

df=df.set_index("S_no")

create_data = {
                "name": "text",
                "type": "multiselect",
                "route-collected": "multiselect"}
 
all_widgets = sp.create_widgets(df, create_data, ignore_columns=["S_no","departure_time","arrival_time","duration","seats_available"])
res = sp.filter_df(df, all_widgets)
col1, col2, col3 = st.columns([1,2,1])
with col2:
    st.title("Red-Bus Details")
st.header("All-Bus")
st.write(df)
st.header("Filter-Bus")
st.write(res)
