from iniciativa.app import db


class MastersVessel(db.Model):

    __tablename__ = 'master_vessels'
    __bind_key__='datalake'

    id = db.Column(db.Integer,  primary_key=True)
    name = db.Column(db.String(80), nullable=True)
    imo = db.Column(db.String(80), nullable=True)

    tp_id = db.Column(db.Integer(), 
                      db.ForeignKey("master_companies.id"), 
                      nullable=True)
    
    so_id = db.Column(db.Integer(), 
                      db.ForeignKey("master_companies.id"), 
                      nullable=True)

    co_id = db.Column(db.Integer(), 
                      db.ForeignKey("master_companies.id"), 
                      nullable=True)

    ### JUST DEFINE RELATION AND LET SqlAchemy create dynamic python objects
    ## see company/views.py accesing to tpFleet / soFleet and coFleet
    tPartyCompany = db.relationship("MastersCompany",
                                    foreign_keys=tp_id,
                                    backref="tpFleet",
                                    lazy='joined')

    sOwnerCompany = db.relationship("MastersCompany",
                                    foreign_keys=so_id,
                                    backref="soFleet",
                                    lazy='joined')

    cOperCompany = db.relationship("MastersCompany",
                                    foreign_keys=co_id,
                                    backref="coFleet",
                                    lazy='joined')


    def serialize_simple(self):
        """
        Simple serializacon method only name and imo
        """
        company = {}
        company["id"] = self.id
        company["name"] = self.name
        company["imo"] = self.imo
        
        return company

    def serialize(self):
        """
        Complet object serialization with companies etc...
        """
        company = {}
        company["id"] = self.id
        company["name"] = self.name
        company["imo"] = self.imo

        company["thirdParty"] = self.tPartyCompany.serialize() if self.tPartyCompany else {} 
        company["shipOwner"] = self.sOwnerCompany.serialize() if self.sOwnerCompany else {} 
        company["comOperator"] = self.cOperCompany.serialize() if self.cOperCompany else {} 

        return company 


    @classmethod
    def create(cls, data):
        model = cls()

        model.name = data.get('name')
        model.imo = data.get('imo')
        model.tp_id = data.get('tp_id', None)
        model.so_id = data.get('so_id', None)
        model.co_id = data.get('co_id', None)

        return model

    def update(self, data):

        self.name = data.get('name')
        self.imo = data.get('imo')
        model.tp_id = data.get('tp_id', None)
        model.so_id = data.get('so_id', None)
        model.co_id = data.get('co_id', None)
    
        db.session.commit()

        return self
