# Weather-Monitoring
Develop a real-time data processing system to monitor weather conditions and provide summarized insights using rollups and aggregates. The system will utilize data from the OpenWeatherMap API
Overview

This application provides real-time weather updates using APIs and data visualization.

Dependencies

To set up and run the application, download the following dependencies:

Docker/Podman Containers

- Docker for containerization
- Python 3.9
- SQLite3 for database management
- Matplotlib for data visualization
- Schedule for task scheduling
- Requests for API calls
- VS CODE as a editor

Additional Dependencies

- Weather API (e.g., OpenWeatherMap)
  

System Requirements

- Operating System: Windows
- RAM: 4 GB
- Processor: 2 GHz
- Storage: 1 GB

Setup Instructions

Docker Setup

1. Install Docker/Podman on your machine.
2. Clone this repository using `git clone .
3. Navigate to the project directory using cd real-time-weather-app.
4. Build the Docker image using docker build -t weather-app ..
5. Run the Docker container using docker run -p 5000:5000 weather-app.

Non-Docker Setup

1. Install Python 3.9, SQLite3, Matplotlib, Schedule, and Requests.
2. Clone this repository using `git clone .
3. Navigate to the project directory using cd real-time-weather-app.
4. Install the Weather API library using pip install requests.
5. Run the application using python (link unavailable).

Design Choices

Architecture

- Microservices architecture using Docker containers.
- Web server handles API requests.
- Database stores weather data.
- Scheduler runs tasks periodically.

Technology Stack

- Python 3.9 for backend development.
- SQLite3 for database management.
- Matplotlib for data visualization.
- Schedule for task scheduling.
- Requests for API calls.

Run Instructions

Docker

1. Run docker run -p 5000:5000 weather-app.
2. Access the application at http://localhost:5000.



API Documentation

Weather API

- Endpoint: /weather.
- Method: GET.
- Parameters: city, state, country.
- Response: JSON weather data.

Contributing

Pull requests are welcome!


Acknowledgments

- OpenWeatherMap API
- Docker
Troubleshooting

- Check Docker container logs using docker logs -f weather-app.
- Verify API keys and credentials.
- Ensure dependencies are installed correctly.

Future Development

- Implement additional weather APIs.
- Enhance data visualization.
- Improve scalability.
