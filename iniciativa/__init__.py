import os

from .app import app, api, manager

# add you view by importing you method
from .webapp.tableapp.views import tableapp
from .datalake.masters.company.views import view_get_company



from .datalake.masters.company.endpoints import CompanyItem, CompanyIndex, CompanySearch
from .datalake.masters.flags.endpoints import FlagItem, FlagIndex
# ALL API resource
api.add_resource(CompanyItem, '/masters/company/<int:company_id>/')
api.add_resource(CompanyIndex, '/masters/company/')
api.add_resource(CompanySearch, '/masters/company/search')


api.add_resource(FlagItem, '/masters/flag/<int:id>/')
api.add_resource(FlagIndex, '/masters/flag/')
