# foodtrucks
## Functional specifications
This is a web full stack app that displays all of San Francisco's foodtrucks on a map.
The user can navigate on the map and click on a foodtruck to see its name, address and menu.

The data of San Francisco's foodtrucks is retrieved from the governement's API : 
https://data.sfgov.org/Economy-and-Community/Mobile-Food-Facility-Permit/rqzj-sfat

The app is built with a Django backend API and an Ember frontend that consumes the data from the Django API.
The Django API retrieves the foodtrucks' data from the SF government's API, processes and stores it, and then delivers it to the frontend. 

## Technologies used
### Backend
Python
Django
Django-rest-framework

### Frontend
JavaScript
Ember JS
Google Maps API