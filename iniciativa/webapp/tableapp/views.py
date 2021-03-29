from flasgger import swag_from
from iniciativa.app import app
from . import TableApp


@app.route('/apptable/<id>/')
@swag_from('apptable.yml')
def tableapp(id):
    rows = TableApp.query.all()
    return {"rows": [user for user in rows]}, 200
