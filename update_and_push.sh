#!/bin/bash

# Activate the virtual environment
source ~/every_culvers/ec_env/bin/activate

# Navigate to the project directory
cd ~/every_culvers

# Pull latest changes from GitHub
git pull --rebase

# Run the data retrieval script
python3 culvers_locations_retrieval.py

# Run the map builder script
python3 culvers_map_builder.py

# Add changes to git
git add culvers_locations_map.html
git commit -m "Daily update: $(date +'%Y-%m-%d')"

# Push the changes to GitHub
git push origin main

# Deactivate the virtual environment
deactivate
