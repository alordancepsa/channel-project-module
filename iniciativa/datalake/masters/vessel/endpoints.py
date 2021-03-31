import sys, traceback
from flasgger import swag_from
from flask_restful import Resource, Api
from flask import request
from sqlalchemy import text, asc, desc
from marshmallow import ValidationError

from iniciativa.app import db
from iniciativa.utils import process
from iniciativa.utils.validators import QuerySchema

from . import MastersVessel
from .validators import NewVesselSchema, UpdateVesselSchema

class VesselItem(Resource):
    
    
    @swag_from('swagger/get.yml')
    def get(self, vessel_id):
        vessel = MastersVessel.query.get(vessel_id)
        
        if vessel:
            return vessel.serialize(), 200

        return "NOT_FOUND", 400

    
    @swag_from('swagger/delete.yml')
    def delete(self, vessel_id):
        
        vessel = MastersVessel.query.get(vessel_id)
        
        if not vessel:
            return "NOT_FOUND", 400

        db.session.delete(vessel)
        db.session.commit()

        return "", 200



    @swag_from('swagger/put.yml')
    def put(self, vessel_id):
        
        try:
            vessel = MastersVessel.query.get(vessel_id)

            if not vessel:
                return "NOT_FOUND", 400
            
            newVesselData = UpdateVesselSchema().load(request.json)
            vessel.update(newVesselData)

        except ValidationError as erro:
            return erro.messages, 400
        
        except Exception as er:
            print("Exception in user code:")
            print("-"*60)
            traceback.print_exc(file=sys.stdout)
            print("-"*60)

            return "UKNOW_ERROR", 500


        return vessel.serialize(), 201

class VesselIndex(Resource):

    
    @swag_from('swagger/post.yml')
    def post(self):
        try:
            vesselData = NewVesselSchema().load(request.json)

            newVessel =  MastersVessel.create(vesselData)
             
            db.session.add(newVessel)
            db.session.commit()

        except ValidationError as erro:
            return erro.messages, 400

        except Exception as er:
            print("Exception in user code:")
            print("-"*60)
            traceback.print_exc(file=sys.stdout)
            print("-"*60)

            return "UKNOW_ERROR", 500
        
        return newVessel.serialize(), 201
    

class VesselSearch(Resource):

    @swag_from('swagger/query.yml')
    def post(self):
        """
        Try this query in swagger
        {
            "itemsPerPage": 2,
            "orderby": "id asc",
            "offset": 0,
            "query": [ {
                  "field": "name",
                  "operator": "LIKE",
                  "value": "%com%"
                    },
                "OR",
                [
                  {
                    "field": "imo",
                    "operator": "NEQ",
                    "value": "123"
                  }
                ]
            ]
        }
        """


        try:
            # TODO 1 marshmallow val do it well
                # queryData = QuerySchema().load(request.json)
            queryData = request.json

            itemsPerPage = queryData["itemsPerPage"]
            offset = queryData["offset"]
            orderby = queryData["orderby"] 

            queryParams = {}
            where = process(queryData["query"], queryParams)
            
            items = MastersVessel.query\
                    .filter(text(where))\
                    .params(queryParams)

            countsTotal = items.count()

            items = items.order_by(text(orderby))\
                    .paginate((offset//itemsPerPage)+1, itemsPerPage, error_out=False)\
                    .items

            return {
                    'nextOffset': 0 if offset+itemsPerPage >= countsTotal else offset+itemsPerPage,
                    'metadata': {"countsTotal": countsTotal},
                    'rows': [item.serialize() for item in items]
                   }, 201

        except Exception as e:
            print("Exception in user code:")
            print("-"*60)
            traceback.print_exc(file=sys.stdout)
            print("-"*60)

