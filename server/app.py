import os, sys

sys.path.append(os.path.join(os.path.dirname(__file__), './mapper/'))
sys.path.append(os.path.join(os.path.dirname(__file__), './service/'))

from concurrent import futures
import logging

import grpc
import country_pb2_grpc
import pymongo

from dotenv import load_dotenv
load_dotenv()

import country_service as service

logging.basicConfig(level=logging.INFO)

class Country(country_pb2_grpc.CountryServiceServicer):
    def __init__(self):
        try:
            self.client = pymongo.MongoClient(f"mongodb://{os.environ['DATABASE_HOST']}:{os.environ['DATABASE_PORT']}/")
            self.db = self.client["travelnote"]
            logging.info("✅ Connected to MongoDB")
        except Exception as e:
            logging.error("❌ MongoDB authentication failed:", e)
       
            
    def GetCountry(self, request, context):
        logging.info("Received request for getting country info")
        return service.get(self.db, request.id)
   
    def ListCountries(self, request, context):
        logging.info("Received request for listing countries")
        return service.list(self.db)

    def AddCountry(self, request, context):
        logging.info("Received request for adding country info")
        return service.add(self.db, request)
            
    def UpdateCountry(self, request, context):
        logging.info("Received request for updating country info")
        return service.update(self.db, request)
   
    def DeleteCountry(self, request, context):
        logging.info("Received request for deleting country info")
        return service.delete(self.db, request.id)
      
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    country_pb2_grpc.add_CountryServiceServicer_to_server(Country(), server)
    port = os.environ['SERVER_PORT']

    server.add_insecure_port(f'[::]:{port}')
    server.start()

    logging.info(f"✅ Server started on port {port}")
    server.wait_for_termination()
    
if __name__ == '__main__':
    serve()