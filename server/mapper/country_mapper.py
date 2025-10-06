import country_pb2

def requestToData(request):
    return {
                "name": request.country.name,
                "code": request.country.code,
                "coordinates": {
                    "latitude": request.country.coordinates.latitude,
                    "longitude": request.country.coordinates.longitude
                },
                "comments": {
                    "food": request.country.comments.food,
                    "activities": request.country.comments.activities,
                    "nature": request.country.comments.nature,
                    "nightlife": request.country.comments.nightlife
                },
                "rating": request.country.rating,
                "visitedAt": request.country.visitedAt
            }   
    
def dataToResponse(data):
    return country_pb2.Country(
                id=str(data["_id"]),
                name=data["name"],
                code=data["code"],
                coordinates=country_pb2.Coordinates(
                    latitude=data["coordinates"]["latitude"],
                    longitude=data["coordinates"]["longitude"]
                ),
                comments=country_pb2.Comments(
                    food=data["comments"]["food"],
                    activities=data["comments"]["activities"],
                    nature=data["comments"]["nature"],
                    nightlife=data["comments"]["nightlife"]
                ),
                rating=data["rating"],
                visitedAt=data["visitedAt"]
            )