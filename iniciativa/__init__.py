import os

from .app import app, api, manager

# add you view by importing you method
from .webapp.tableapp.views import tableapp
from .datalake.masters.company.views import view_get_tp_fleets
from .datalake.masters.company.views import view_get_so_fleets
from .datalake.masters.company.views import view_get_co_fleets

from .datalake.masters.company.views import view_predict_salesLocal
from .datalake.masters.company.views import view_predict_salesremote
from .datalake.masters.company.views import view_predict_saleslocal_TF


# ALL API resource
from .datalake.masters.company.endpoints import CompanyItem, CompanyIndex, CompanySearch
from .datalake.masters.vessel.endpoints import VesselItem, VesselIndex, VesselSearch

## MASTER COMPANY
api.add_resource(CompanyItem, '/masters/company/<int:company_id>')
api.add_resource(CompanyIndex, '/masters/company')
api.add_resource(CompanySearch, '/masters/company/search')

## MASTER VESSEL
api.add_resource(VesselItem, '/masters/vessel/<int:vessel_id>')
api.add_resource(VesselIndex, '/masters/vessel')
api.add_resource(VesselSearch, '/masters/vessel/search')

