import dlt
from dlt.sources.helpers import requests
import os
from dotenv import load_dotenv
import requests
import pandas as pd
import json
from datetime import date
from datetime import datetime
from uuid import uuid4

#loading key
load_dotenv()
key = os.getenv('KEY')

#url
# api call
url = f'https://v6.exchangerate-api.com/v6/{key}/latest/USD'

# Make a request
response = requests.get(url)
data = response.json()


#Transformations part
df = pd.json_normalize(data['conversion_rates'])
df = df.melt().reset_index()
df["index"] += 1 
df['date'] = date.today()
df = df.rename(columns={ 'index':'id','variable': 'currencycode', 'value': 'fxrate'})

# convert api data for dlt format
records = df.to_dict(orient="records")


# Create a dlt pipeline that will load
# Exchange_rate data to Postgresql destination

pipeline = dlt.pipeline(
    pipeline_name="fxrate_pipeline",
    destination="postgres",
    dataset_name="incremental"
)



# Run the pipeline 
load_info = pipeline.run(
        records, 
        write_disposition="merge",
        primary_key=("currencycode", "date"),
        table_name="fxrates")    # 	le rôle de "merge" est : Si une ligne avec la même clé primaire existe, elle sera mise à jour, sinon insérée

print(load_info)