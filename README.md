# Ship Route Optimization and Visualization System

A **Flask-based web application** designed to optimize and visualize ship routes between **India and Sri Lanka**, enhancing **fuel efficiency**, **safety**, and **voyage comfort**. It uses **machine learning** and **maritime data** to generate **weather-aware, sea-only paths** displayed on an interactive map.


## Key Features

### Login/Signup System
Secure user authentication for accessing route services.

### Smart Port-to-Port Navigation
Predicts optimal sea routes between major ports:
- Chennai
- Cochin
- Kakinada
- Visakhapatnam
- Colombo
- Kankesanthurai

### ML-Powered Route Prediction
- Decision Tree and Random Forest algorithms.
- Trained on maritime and weather datasets.

### Interactive Route Visualization
- Real-time sea-only paths.
- Powered by **Leaflet.js** and **Folium**.
- Routes intelligently avoid landmass.

### Dynamic Weather Simulation
- Weather-aware routing (e.g., 'rainy', 'cloudy').
- Routes adapt visually based on input conditions.

### Step-by-Step Sailing Instructions
- Easy-to-understand textual instructions for navigation.
- Complements visual map data.


## Technologies Used

### Frontend
- HTML
- CSS
- JavaScript
- Leaflet.js

### Backend
- Python (Flask)
- SQLite

### Machine Learning
- scikit-learn
- pandas
- RandomForest

### Visualization
- Folium
- Leaflet.js

### Authentication
- Flask-SQLAlchemy



