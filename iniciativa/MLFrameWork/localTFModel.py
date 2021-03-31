

class LocalTFModel():
    """

    This class implement models load in memory in app instance
    if you model is in other backend use RemoteModel instead

    At app launch, load NN weigth's from  from s3 or readis

    **designed to work with TF models**
    ***for local model with tensor flow or similar us LocalTFModel***
    """

    def load(self, params):
        """
        Mock function like now... install and import tf and just load 
        the model shema from s3 or redis and load the NN weigth

        """
        # import tensorflow from tf
        # self.model = tf.keras.models.model_from_json(params["URL_SHEMA_MODEL"])
        # self.model.load_weigth(params["URL"])
        # 

    def __init__(self, params):

        self.params = params
        self.load(params)



    def predict(data):

        return self.model.predict(data)
    

