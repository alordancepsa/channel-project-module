import json
from iniciativa.app import db


class RMCFormula(db.Model):

    __tablename__ = 'rmc_formula'
    __bind_key__='datalake'

    id = db.Column(db.Integer,  primary_key=True)
    formula = db.Column(db.String(1024), nullable=True)
    fee = db.Column(db.String(120), nullable=True)
    bussinesUnit = db.Column(db.String(120), nullable=True)

    def serialize(self):

        company = {}
        company["id"] = self.id
        company["fee"] = self.fee
        company["bussinesUnit"] = self.bussinesUnit
        company["fomula"] = json.load(self.formula)

        return company

    @classmethod
    def create(cls, data):
        model = cls()

        model.fee = data.get('fee')
        model.formula = json.dump(data.get('phone'))
        model.bussinesUnit = data.get('bussinesUnit')

        return model

    def update(self, data):

        self.fee = data.get('fee')
        self.formula = json.dump(data.get('formula'))
        self.bussinesUnit = data.get('bussinesUnit')
    
        db.session.commit()

        return self
