from enum import Enum

from .remoteModel import RemoteModel
from .localModel import LocalModel
from .localTFModel import LocalTFModel

class ModelType(Enum):
    LOCAL_MODEL=1
    REMOTE_MODEL=2
    LOCAL_TF_MODEL=3


class MLModel(LocalModel, RemoteModel, LocalTFModel):

    def __init__(self, params):
        if params["type"] == ModelType.LOCAL_MODEL:
            LocalModel.__init__(self, params)
        elif params["type"] == ModelType.REMOTE_MODEL:
            RemoteModel.__init__(self, params)
        elif params["type"] == ModelType.LOCAL_TF_MODEL:
            LocalTFModel.__init__(self, params)
        else:
            raise RuntimeError('Model Type not IMPLEMENTED') 
