from pymongo import MongoClient
import json
import pandas as pd


def csv_to_json(filename):
    data = pd.read_csv(filename, error_bad_lines=False)
    return data.to_dict('records')


client = MongoClient('mongodb://localhost:27017/')
db = client['youtube']

us_videos_col = db['us_videos']
gb_videos_col = db['gb_videos']

us_category_col = db['us_categories']
gb_category_col = db['gb_categories']

# drop old video data
us_videos_col.drop()
gb_videos_col.drop()

# insert video data from scv tables
us_videos_col.insert_many(csv_to_json('data/USvideos.csv'))
gb_videos_col.insert_many(csv_to_json('data/GBvideos.csv'))

# drop old category data
us_category_col.drop()
gb_category_col.drop()

# insert category data from scv tables
us_category_col.insert_many(json.load(open('data/US_category_id.json'))['items'])
gb_category_col.insert_many(json.load(open('data/GB_category_id.json'))['items'])
