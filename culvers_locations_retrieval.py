# Standard imports
import requests
import pandas as pd
import time
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from datetime import datetime

# Confidential imports
from config import db_conn_string

# List of US states
us_states = [
    "Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", 
    "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", 
    "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", 
    "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", 
    "New Hampshire", "New Jersey", "New Mexico", "New York", "North Carolina", 
    "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", 
    "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", 
    "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"
]

# Set up the database connection
DATABASE_URL = db_conn_string
engine = create_engine(DATABASE_URL)

# Define a function to retrieve and process data for each state
def retrieve_and_store_state_data(state):
    url = "https://www.culvers.com/api/locator/getLocations"
    params = {
        'location': state,
        'radius': 40233,  # This value covers the entire state
        'limit': 0,
        'layer': 'state'
    }

    try:
        # Retrieve data
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise an error for bad status codes
        
        # Process the data
        data = response.json()
        locations = data.get('data', {}).get('geofences', [])
        
        # Parse the data into a list of dictionaries
        parsed_locations = []
        snapshot_date = datetime.today().date()
        
        for location in locations:
            parsed_location = {
                'location_id': location['_id'],
                'description': location['description'],
                'street': location['metadata'].get('street'),
                'city': location['metadata'].get('city'),
                'state': location['metadata'].get('state'),
                'postal_code': location['metadata'].get('postalCode'),
                'latitude': location['geometryCenter']['coordinates'][1],
                'longitude': location['geometryCenter']['coordinates'][0],
                'open_date': location['metadata'].get('openDate'),
                'is_temporarily_closed': location['metadata'].get('isTemporarilyClosed'),
                'flavor_of_the_day': location['metadata'].get('flavorOfDayName'),
                'snapshot_date': snapshot_date
            }
            parsed_locations.append(parsed_location)

        # Convert to a DataFrame
        df = pd.DataFrame(parsed_locations)

        # Insert into the PostgreSQL table
        df.to_sql('culvers_locations', con=engine, if_exists='append', index=False)
        print(f"Data for {state} successfully inserted.")

    except requests.exceptions.RequestException as e:
        print(f"Request error for {state}: {e}")
    except SQLAlchemyError as e:
        print(f"Database error for {state}: {e}")
    except Exception as e:
        print(f"Unexpected error for {state}: {e}")

# Iterate over the states and retrieve data
for state in us_states:
    retrieve_and_store_state_data(state)
    time.sleep(5)  # Wait for 5 seconds between each state

print("Data retrieval and storage complete.")