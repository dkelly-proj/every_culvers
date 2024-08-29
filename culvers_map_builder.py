# Standard imports
import folium
import pandas as pd
from sqlalchemy import create_engine

# Confidential imports
from config import db_conn_string

# Set up the database connection
DATABASE_URL = db_conn_string
engine = create_engine(DATABASE_URL)

# Query the database to get all locations
query = """
SELECT description, street, city, state, latitude, longitude, flavor_of_the_day
FROM culvers_locations
"""
df = pd.read_sql(query, con=engine)

# Create a folium map centered on the USA
m = folium.Map(location=[39.8283, -98.5795], zoom_start=4)  # Central point of the USA

# Add each location as a CircleMarker on the map
for index, row in df.iterrows():
    folium.CircleMarker(
        location=[row['latitude'], row['longitude']],
        radius=3,  # Radius of the circle
        color='#005599',
        fill=True,
        fill_color='#005599',
        fill_opacity=0.7,
        popup=folium.Popup(
            f"{row['description']}<br>{row['street']}, {row['city']}, {row['state']}<br>Flavor of the Day: {row['flavor_of_the_day']}",
            max_width=300),
    ).add_to(m)

# Save the map to an HTML file
m.save("culvers_locations_map.html")

print("Map created and saved as culvers_locations_map.html")