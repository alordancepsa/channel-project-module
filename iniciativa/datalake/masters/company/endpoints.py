import sys, traceback
from flasgger import swag_from
from flask_restful import Resource, Api
from flask import request
from sqlalchemy import text, asc, desc
from marshmallow import ValidationError
from iniciativa.app import db
from iniciativa.utils import process
from iniciativa.utils.validators import QuerySchema

from . import MastersCompany
from .validators import NewCompanySchema
# from .validators import CompanyPostPattern

class CompanyItem(Resource):
    
    
    @swag_from('swagger/get_company.yml')
    def get(self, company_id):
        company = MastersCompany.query.get(company_id)
        
        if company:
            return company.serialize(), 200

        return "NOT_FOUND", 400

    
    def delete(self, company_id):
        
        company = MastersCompany.query.get(company_id)
        
        if company:
            db.session.delete(company)
            db.session.commit()

        return "NOT_FOUND", 400

    def put(self, company_id):
        return {'hello': 'world'}

class CompanyIndex(Resource):

    
    @swag_from('swagger/post_company.yml')
    def post(self):
        try:
            companyData = NewCompanySchema().load(request.json)

            newCompany =  MastersCompany.create(companyData)
             
            db.session.add(newCompany)
            db.session.commit()
        except ValidationError as erro:
            return erro.messages, 400
        
        return newCompany.serialize(), 201
    

class CompanySearch(Resource):

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
                    "field": "phone",
                    "operator": "NEQ",
                    "value": "123"
                  },
                  "OR",
                  {
                    "field": "flag",
                    "operator": "EQ",
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
            
            companies = MastersCompany.query\
                    .filter(text(where))\
                    .params(queryParams)

            countsTotal = companies.count()

            companies = companies.order_by(text(orderby))\
                    .paginate((offset//itemsPerPage)+1, itemsPerPage, error_out=False)\
                    .items

            return {
                    'nextOffset': 0 if offset+itemsPerPage >= countsTotal else offset+itemsPerPage,
                    'metadata': {"countsTotal": countsTotal},
                    'rows': [company.serialize() for company in companies]
                   }, 201

        except Exception as e:
            print("Exception in user code:")
            print("-"*60)
            traceback.print_exc(file=sys.stdout)
            print("-"*60)

