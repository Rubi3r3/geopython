import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy import inspect
import geopandas as gpd
import matplotlib.pyplot as plt

load_dotenv()


dbname = os.getenv('DB_DATABASE')
user = os.getenv('DB_USER')
password = os.getenv('DB_PASSWORD')
host = os.getenv('DB_HOST')
port = os.getenv('DB_PORT')  

connection_string = f"postgresql://{user}:{password}@{host}/{dbname}"

engine = create_engine(connection_string)

insp = inspect(engine)
table_names = insp.get_table_names()

sorted_table_names = sorted(table_names)

print("Sorted Table Names: ")
for table_name in sorted_table_names:
        print(table_name)

sql= 'SELECT *, shape as geom from mics7_ed'
gdf = gpd.read_postgis(sql, con=engine)
gdf
gdf.plot()
plt.show()

engine.dispose()