# foodtrucks
## 1. Description
### Functional specifications
This is a full-stack web app that displays all of San Francisco's foodtrucks on a map.
The user can navigate on this map and click on a food truck to see its name, address and menu.

The data of San Francisco's foodtrucks is retrieved from the SF governement's API: 
https://data.sfgov.org/Economy-and-Community/Mobile-Food-Facility-Permit/rqzj-sfat

The app is built with a Django back-end JSON RESTful API and an Ember front-end.
The Django API retrieves the foodtrucks' data from the SF government's API, processes it, stores it, and delivers it to its endpoint. 
The Ember front-end consumes the data from the Django back-end API endpoint and displays it on a map thanks to the Google Maps API.

This project is an answer to this coding challenge:
https://gist.github.com/AlexisMontagne/8b2a2d8794da3979d4b8285f165b1f76


### Technologies used
#### Back-end
- Python 3.8.2
- Django 3.1.3
- Django REST Framework 3.12.2

#### Front-end
- Ember CLI 3.22.0
- Google Maps API 3.41


### Installation & usage
#### Requirements:
You need to have installed:
- Node.js (including npm)
- Python 3 (including pip)

#### Installation instructions:
Open a first terminal:
```
git clone https://github.com/Dorgone/foodtrucks.git
cd ./foodtrucks/backend
pip install -r requirements.txt
```
Create a config.json file in backend/backend/ where you store the SECRET_KEY used in *settings.py*. You can generate a SECRET_KEY here: https://djecrety.ir/.
```
python manage.py migrate
python manage.py runserver
```
You will find the Django API at http://localhost:8000/api/foodtrucks.

Open a second terminal:
```
cd ./foodtrucks/frontend
npm install -g ember-cli
npm install
ember install ember-google-maps
ember install ember-cli-dotenv
```
Create a .env file in frontend/ where you store the GOOGLE_MAPS_API_KEY required in config/environment.js.
```
ember s
```

#### Usage:
Once the two servers are started, you will find the food trucks map at http://localhost:4200/foodtrucks.
You can then navigate and click on the food truck markers to see the related data.



# 2. Technical choices
## Frameworks
**Django** is known to be very scalable, and the Django REST framework implements the essential functionalities of a JSON RESTful API.
Besides, I had already worked on other web projects with Django and Python is a language that I know well.
This is why I chose Django.

I chose **Ember** because it is Upfluence-ready, it is scalable, and there is enough documentation. Like Ruby on Rails, it follows the principle "Convention over Configuration". The code configuration is already mainly structured, which means less time making decisions and more time to code. At last, Ember is also scalable.

## Libraries & apps
### Django:
- *djangorestframework and djangorestframework-jsonapi* - 
"Django REST framework is a powerful and flexible toolkit for building Web APIs."
- *markdown* - 
This adds markdown support for the browsable API.
- *django-cors-headers* - 
This is a Django App that adds Cross-Origin Resource Sharing (CORS) headers to allow in-browser requests to the Django application from other origins.
- *requests* - 
Requests is an HTTP library for Python. I used it to download the DataSF food trucks json file.

### Ember:
- *ember-google-maps* - 
I used this add-on to display a map with the food trucks data points, thanks to the Google Maps API.
- *ember-cli-dotenv* - 
I used this add-on to retrieve the GOOGLE_MAPS_API_KEY in config/environment.js from a .env file.

## Security
- The Django settings.py SECURITY_KEY is stored in a config.json file.
- The ember-google-maps GOOGLE_MAPS_API_KEY is stored in a .env file.

Both files need to be protected in production mode.


# 3. Trade-offs and modifications
This part is about what I did not do and what I would do differently if I were to spend extra time on this project.

## Database
I did not implement a location-based research: the user cannot enter a location or address and get every food truck in a certain radius. 
The user can only navigate visually on the map to find the location he's interested in and the food trucks in the surroundings.

I first implemented a Postgis database, which allowed spatial data fields and distance queries, but it required the GDAL and the GeoDjango libraries, which were really hard to install, and would have made the installation instructions in this README a lot more complicated.

I first used Mapbox instead of Google Maps, but I did not manage to display info windows with data from the food trucks markers. 
Plus it required the Geodjango and GDAL libraries.

Now, the main problem in my database is that it can only store new food trucks, but does not updates the existing food trucks.
For instance, if a food truck with a given (name, address) changes its menu, the database does not take this change into account.
Or if a food truck is deleted from DataSF, the Django database will keep it.
With additional time, I would have worked on creating a better initialization and update of the dataset.


## Testing
Unfortunately, I did not implement any test due to time constraint.
This would have been the major focus if I had more time. I think I would have probably used pytest and ember test.


## Scalability
### In terms of inbound traffic...
Each time a GET is called, the Django API calls initialize_dataset(), which parses the DataSF json file and compares it to the data base.
Obviously, this is resource-consuming and would not scale well with more inbound traffic.

A solution would be to:
- separate the update of the database to DataSF from the view that calls GET
- check if the data base is still up to date after a set interval of time
- update it accordingly

This is related to the issue mentionned in the *Database* part above.

I do not see any major issue in terms of inbound traffic scalability on the client side.

### In terms of data points...
If there were a lot more food trucks (>> 600), the app would also not scale well.
The database update would take even longer. This is the issue that I mentionned right before.

Besides, the Django API serves all food trucks at once, so the map requires some meaningful time to display the markers.
One possible way to improve that would be to:
- query only the food trucks that would be displayed on the map (and not those out of the map display range) = a query by distance
- display the food trucks markers progressively, starting with the closest to the map center


## User experience
Finally, in terms of UX, here are the major updates I could have done to improve the app:
- Allow only one food truck info window opened at once on the map: if a new info window is opened, it closes the others.
- Allow research by location or address to set the map center and display the closest food trucks.
- Allow itinerary research to go to a food truck from current location.



