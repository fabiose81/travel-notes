import country_mapper as mapper

from bson import ObjectId

import country_pb2

import logging

logging.basicConfig(level=logging.INFO)

def list(db):
    try:
        countries_data = db.countries.find()
        countries = [mapper.dataToResponse(country) for country in countries_data]
        return country_pb2.ListCountriesResponse(
            status=True,
            countries=country_pb2.CountryList(list=countries)
        )
    except Exception as e:
        logging.error("❌ Error occurred while processing request: %s", e)
        return country_pb2.ListCountriesResponse(
            status=False,
            message=str(e)
        )
        
def get(db, id):
    try:
        query = {"_id": ObjectId(id)}
        country_data = db.countries.find_one(query)

        if country_data:
            return country_pb2.GetCountryResponse(
                status=True,
                country=mapper.dataToResponse(country_data)
            )
        else:
            logging.warning("⚠️ Country not found")
            return country_pb2.GetCountryResponse(
                status=False,
                message="Country not found")
    except Exception as e:
        logging.error("❌ Error occurred while processing request: %s", e)
        return country_pb2.GetCountryResponse(
            status=False,
            message=str(e)
        )
        
def add(db, request):
    try:
        country_data = mapper.requestToData(request)
        result = db.countries.insert_one(country_data)
        
        logging.info("✅ Country added successfully")

        return country_pb2.AddCountryResponse(message=
            country_pb2.Message(status=True, message=str(result.inserted_id))
        )
    except Exception as e:
        logging.error("❌ Error occurred while processing request: %s", e)
        return country_pb2.AddCountryResponse(message=
            country_pb2.Message(status=False, message=str(e))
        )

def update(db, request):
    try:
        country_data = mapper.requestToData(request)
        result = db.countries.update_one(
            {"_id": ObjectId(request.country.id)},
            {"$set": country_data}
        )
        if result.matched_count == 1:
            logging.info("✅ Country updated successfully")
            country_data["_id"] = ObjectId(request.country.id)
            return country_pb2.UpdateCountryResponse(
                status=True,
                country=mapper.dataToResponse(country_data)
            )
        else:
            logging.warning("⚠️ Country not found")
            return country_pb2.UpdateCountryResponse(
                status=False,
                message="Country not found")
    except Exception as e:
        logging.error("❌ Error occurred while processing request: %s", e)
        return country_pb2.UpdateCountryResponse(
            status=False,
            message=str(e))
        
def delete(db, id):
    try:
        result = db.countries.delete_one({"_id": ObjectId(id)})
        if result.deleted_count == 1:
            logging.info("✅ Country deleted successfully")
            return country_pb2.DeleteCountryResponse(
                message=country_pb2.Message(status=True, message="Country deleted")
            )
        else:
            logging.warning("⚠️ Country not found")
            return country_pb2.DeleteCountryResponse(
                    message=country_pb2.Message(status=False, message="Country not found")
            )
    except Exception as e:
        logging.error("❌ Error occurred while processing request: %s", e)
        return country_pb2.DeleteCountryResponse(
            message=country_pb2.Message(status=False, message=str(e))
        )