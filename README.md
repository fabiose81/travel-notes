![alt text](https://github.com/fabiose81/travel-notes/blob/master/travel-notes.jpg?raw=true)

### For Python gRPC server and Docker container
    In python folder create a file .env and insert:

    SERVER_PORT=5000
    DATABASE_HOST=travel_database #localhost
    DATABASE_PORT=27017  #7018

    SERVER_CONTAINER_NAME=travel_server
    SERVER_CONTAINER_PORT=5000:5000

    DATABASE_IMAGE=mongo:latest
    DATABASE_CONTAINER_NAME=travel_database
    DATABASE_CONTAINER_PORT=7018:27017
    DATABASE=travelnote

### For Postman test

    1 - Create a gRPC request
    2 - Import country.proto file

#### AddCountry

    {
        "country" : {
                "name": "Italy",
                "code": "IT",
                "coordinates": { "latitude": 41.8719, "longitude": 12.5674 },
                "visitedAt": "2023-04-15",
                "comments": {
                    "food": "Best pizza and pasta I've ever had! Gelato every day was a must.",
                    "activities": "Explored ancient Rome, visited the Colosseum, and took a gondola ride in Venice.",
                    "nature": "Beautiful Tuscan countryside and stunning Amalfi Coast views.",
                    "nightlife": "Great wine bars and lively piazzas in Florence and Rome."
                },
                "rating": 5
                }
    }

#### UpdateCountry
    Same json structure but it must to add the id key

    {
        "country" : {
                "id": "68dff00df541bc68d78e785f"
                "name": "Italy",
                "code": "IT",
                ...
        }
    }

#### GetCountry

    {
        "id": "68dff00df541bc68d78e785f"
    }

#### DeleteCountry

    {
        "id": "68dff00df541bc68d78e785f"
    }