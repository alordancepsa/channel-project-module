import json
from flasgger import swag_from
from iniciativa.app import app, appModels

from . import MastersCompany


#############################################
## EXAMPLE USAGE FOR A SIMPLE MLFRAMEWORK ##
## now in MLFrameWork folder we defined 3 types of model
## other types cloud be implement
## all models implement the same interface and is transparent for any endpoint
## you just need  tow know with model name you want to use...
###############################################
##############################################

## Using MLFrameWork as easy
@app.route('/masters/views/company/<company_id>/predictSalesLOCAL')
@swag_from('swagger/getML.yml')
def view_predict_salesLocal(company_id):
    """
    Example usage not functional like now
    simple pass data required to predict method
    TODO implement the method you want..
    """

    MODEL_KEY = "MODEL_SALES_PREDICT"

    # TODO GET SOME DATA NEEDED for example given some comapny predict sales???
    company = MastersCompany.query.get(company_id)
    companySales = getCompanyLatestSales()

    return appModels[MODEL_KEY].predict(companySales), 200


## Using MLFrameWork as easy
@app.route('/masters/views/company/<company_id>/predictSalesREMOTE')
@swag_from('swagger/getML.yml')
def view_predict_salesremote(company_id):
    """
    Example usage not functional like now
    simple pass data required to predict method
    TODO implement the method you want..
    """

    MODEL_KEY = "MODEL_REMOTE_SALES_PREDICT"

    # TODO GET SOME DATA NEEDED for example given some comapny predict sales???
    company = MastersCompany.query.get(company_id)
    companySales = getCompanyLatestSales()
    
    return appModels[MODEL_KEY].predict(companySales), 200

## Using MLFrameWork as easy
@app.route('/masters/views/company/<company_id>/predictSalesLOCALTFMODEL')
@swag_from('swagger/getML.yml')
def view_predict_saleslocal_TF(company_id):
    """
    Example usage not functional like now
    simple pass data required to predict method
    TODO implement the method you want..
    """

    MODEL_KEY = "MODEL_LOCAL_SALES_USING_TF_LIKE_MODELS"

    # TODO GET SOME DATA NEEDED for example given some comapny predict sales???
    company = MastersCompany.query.get(company_id)
    companySales = getCompanyLatestSales()
    
    return appModels[MODEL_KEY].predict(companySales), 200


####### FLEETS ENDPOINTS ##########
## se puede hacer en un solo endpoint con un query param y tres if

@app.route('/masters/company/<company_id>/fleets/TP')
@swag_from('swagger/get_fleet.yml')
def view_get_tp_fleets(company_id):
    company = MastersCompany.query.get(company_id)

    return json.dumps([vessel.serialize_simple() for vessel in company.tpFleet]), 200

@app.route('/masters/company/<company_id>/fleets/SO')
@swag_from('swagger/get_fleet.yml')
def view_get_so_fleets(company_id):
    company = MastersCompany.query.get(company_id)

    return json.dumps([vessel.serialize_simple() for vessel in company.soFleet]), 200

@app.route('/masters/company/<company_id>/fleets/CO')
@swag_from('swagger/get_fleet.yml')
def view_get_co_fleets(company_id):
    company = MastersCompany.query.get(company_id)

    return json.dumps([vessel.serialize_simple() for vessel in company.coFleet]), 200

############# END FLEET ENDPOINT ###################
