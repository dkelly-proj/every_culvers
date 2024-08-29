# Every Culver's Location: Interactive Map

Welcome to the **Every Culver's Location** project, a fun initiative designed to track and display the locations of all Culver's restaurants across the United States.

## Project Overview

This project dynamically retrieves and visualizes the location data for all Culver's restaurants. The interactive map, updated daily, provides a clear and up-to-date view of each location, right down to the street level.

### Key Features:

- **Automated Data Retrieval**: Daily data collection ensures that the map is always up-to-date.
- **Interactive Visualization**: The map allows users to explore each Culver's location, complete with details such as the street address and the flavor of the day.
- **Responsive Design**: The website is fully responsive, providing a seamless experience on both desktop and mobile devices.
- **Cloud-Hosted**: The project is hosted on GitHub Pages, ensuring easy access and minimal downtime.

## Technology Stack

- **Python**: Core programming language used for data retrieval and processing.
- **Folium**: Library used to generate the interactive map.
- **PostgreSQL**: Database used to store location data, with snapshots enabling historical tracking.
- **Heroku**: Platform used for hosting the PostgreSQL database.
- **Cron Jobs & Shell Scripts**: Automation tools for scheduling daily updates and pushing changes from an Ubuntu server.
- **GitHub Pages**: Hosting the front-end for the interactive map.

## How It Works

### Data Collection & Processing

1. **Daily Snapshots**: A Python script is executed daily via a cron job on an Ubuntu server, collecting the latest location data from the Culver's API.
2. **Database Storage**: The data is stored in a PostgreSQL database on Heroku, allowing for historical snapshots and real-time queries without overloading the API.
3. **Map Generation & Deployment**: Another script generates an updated interactive map using Folium and automatically pushes the changes to GitHub Pages via a shell script executed by the cron job.

Feel free to explore the code, and check out the live map [here](https://dkelly-proj.github.io/every_culvers/). If you have any questions or are interested in collaborating on future projects, don't hesitate to reach out.

## License

This project is open-source and available under the [MIT License](LICENSE).
