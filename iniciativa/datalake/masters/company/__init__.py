from iniciativa.app import db


class MastersCompany(db.Model):

    __tablename__ = 'master_companies'
    __bind_key__='datalake'

    id = db.Column(db.Integer,  primary_key=True)
    name = db.Column(db.String(80), nullable=True)
    phone = db.Column(db.String(120), nullable=True)
    flag = db.Column(db.String(120), nullable=True)

    hiddenfield = db.Column(db.String(120), nullable=True)

    def serialize(self):

        company = {}
        company["id"] = self.id
        company["name"] = self.name
        company["flag"] = self.flag
        company["phone"] = self.phone
        
        return company

    @classmethod
    def create(cls, data):
        model = cls()
        model.name = data.get('name')
        model.phone = data.get('phone')
        model.flag = data.get('flag')
        model.hiddenfield = "somefiled not exposed to api and not serialized"
        return model
