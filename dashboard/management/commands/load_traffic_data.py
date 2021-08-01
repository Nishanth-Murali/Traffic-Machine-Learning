import json
from django.core.management import BaseCommand
from dashboard.models import Data
import pandas as pd
import numpy as np


ALREADY_LOADED_ERROR_MESSAGE = """
If you need to reload the traffic_dashboard data from the JSON file,
first delete the db.sqlite3 file to destroy the database.
Then, run `python manage.py migrate` for a new empty
database with tables"""


class Command(BaseCommand):
    # Show this when the user types help
    help = "Loads data from json into our Data model"

    def handle(self, *args, **options):
        if Data.objects.exists():
            print('Traffic data already loaded...exiting.')
            print(ALREADY_LOADED_ERROR_MESSAGE)
            return
        print("Loading traffic_dashboard data for data visualizations")
        # file='D:/Jobs/Full Time/EPICS Cause no JOB/Traffic Data Analysis/react_traffic_dashboard1/2021-01-31 00-00-00.json'
        # df = pd.read_json(file)
        df = pd.read_json('2020-09-13 00-00-00.json')
        print(df)
        df = df.groupby(['class', 'entrance', 'exit']).resample('15T', on='timestamp').sum().replace(0, np.nan).dropna(axis=0).reset_index()
        for index, row in df.iterrows():
            data = Data()
            data.vehicle_class = row['class']
            data.entrance = row['entrance']
            data.exit = row['exit']
            data.quantity = row['qty']
            data.timestamp = row['timestamp']
            data.save()
