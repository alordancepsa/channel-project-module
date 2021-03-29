from iniciativa.app import db


class TableApp(db.Model):
    __tablename__ = 'app_table_1'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def serialize(self):

        return {
                "username": self.username,
                "emails":[self.email, self.email2]
                }
