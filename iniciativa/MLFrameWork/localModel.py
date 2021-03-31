class LocalModel():
    """
    This class implement models load in memory in app instance
    if you model is in other backend use RemoteModel instead

    At app launch, load model from s3 or readis

    **designed to work with sklearn models**
    ***for local model with tensor flow or similar us LocalTFModel***
    """

    def load(self, url):
        """ 
        Mock function like now... 
        implement load load function for example get the picke model form s3 or redis... 
        """
        # from joblib import dump, load
        # return load(url)
        return None
    
    def __init__(self, params):

        self.params = params
        self.model = self.load(params["URL"])


    def predict(data):

        return self.model.predict(data)
