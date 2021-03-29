from flasgger import swag_from
from iniciativa.app import app

from . import MastersCompany

@app.route('/masters/views/company/<company_id>')
@swag_from('swagger/get_company.yml')
def view_get_company(company_id):

    company = MastersCompany.query.join(Master)
    
    if company:
        return {company.serialize()}, 200

    return "NOT_FOUND", 400
