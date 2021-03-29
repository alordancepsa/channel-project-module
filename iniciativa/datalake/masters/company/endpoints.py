from flasgger import swag_from
from flask_restful import Resource, Api
from flask import request
from marshmallow import ValidationError

from iniciativa.app import db
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

    def post(self):

        return {'hello': 'world'}

