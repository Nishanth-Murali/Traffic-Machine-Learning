import os
import requests
from datetime import datetime, timedelta
import json
import urllib
from tqdm import tqdm

url='https://api.miovision.com/intersections'
apiKey = os.getenv('API_KEY')
header = {'Authorization': apiKey, 'accept': 'application/json'}
verify = []


def get_intersections():
    
    request = requests.get(url,headers=header)
    return request.json()


def get_TMC_Data(duration: int = 45,        # miovision stores the last 45 days of data only
                 intersections: list = [], 
                 end_date: datetime = None):
    if not intersections:                 
        intersections = get_intersections()
    if not end_date:
        end_date = datetime.now() - timedelta(hours=2)           # queries are only permitted for data that is at least 2 hours old
    
    return_empty = False         # flag to check if the api call still returns data
    _end_time = end_date 
    _start_time = _end_time - timedelta(day=1)        # the api can provide data for 1 hr max with one call
    total_intersections = len(intersections)
    # breakpoint()
    for intersection in tqdm(intersections):
        _formatted_name = intersection['name'].replace(' ','_')
        try:
            os.mkdir(_formatted_name)
            os.chdir(_formatted_name)
        except:
            print(f"Unable to create dir for intersection: {_formatted_name}")
            continue
        
        for j in tqdm(range(duration)):
            #create request
            params = {'endTime': _end_time.isoformat(), 
                    'startTime': _start_time.isoformat()}
            intersection_url = 'https://api.miovision.com/intersections/{}/tmc?{}'.format(intersection['id'],
                                                                                        urllib.parse.urlencode(params))
            header = {'Authorization': apiKey, 'accept': 'application/json'}
            request = requests.get(intersection_url, headers=header)
            
            #verify responce
            if request.status_code != 200:
                breakpoint()
                raise request.reason
            
            # write to file
            with open(str(_end_time)+'.json', 'w') as outfile:
                json.dump(request.json(), outfile)

            # check if still getting results and update params
            if not request.json():
                verify.append(intersection['names'])
                break
            _end_time = end_date - timedelta(day=j)
            _start_time = _end_time - timedelta(day=1)

        os.chdir('..')

get_TMC_Data()

if verify:
    print(' unable to get the complete data for the follwing intersections, might be duration parma too long')
    print(verify)