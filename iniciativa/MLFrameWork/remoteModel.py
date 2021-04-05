import requests

class RemoteModel():
    """
    This class implement a call to another backend with the data used to predict
    return the response from this external endpoint
    
    """

    def __init__(self, params):
        self.params = params


    def transform(self, data):
        """
        Perform data transformations needed
        """
        return data

    def predict(data):
        
        data = self.transform(data)
        return requests.post(self.params["endpoint"], {"body": data} , params["headers"])
    

