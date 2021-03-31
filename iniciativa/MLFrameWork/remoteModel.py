import requests

class RemoteModel():
    """
    This class implement a call to another backend with the data used to predict
    return the response from this external endpoint
    
    """

    def __init__(self, params):
        self.params = params


    def predict(data):

        return requests.post(self.params["endpoint"], {"body": data} , params["headers"])
    

