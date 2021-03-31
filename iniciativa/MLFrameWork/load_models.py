from . import MLModel

def load_app_models(models):

    appModels = {}

    for model in models:
        appModels[model["NAME"]] = MLModel(model)
        
    return appModels
