from iniciativa.app import db


class MasterFlags(db.Model):

    __tablename__ = 'master_flags'
    __bind_key__='datalake'

    id = db.Column(db.Integer,  primary_key=True)
    name = db.Column(db.String(80), nullable=True)
    
    flag = db.Column(db.String(120), nullable=True)
    flagShort = db.Column(db.String(120), nullable=True)

    

    def serialize(self):

        company = {}
        company["id"] = self.id
        company["name"] = self.name
        company["flag"] = self.flag
        company["flagShort"] = self.flagShort
    
        
        return company

    @classmethod
    def create(cls, data):
        model = cls()
        model.name = data.get('name')    
        model.flag = data.get('flag')
    
        return model
