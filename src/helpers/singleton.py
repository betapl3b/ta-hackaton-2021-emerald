import threading
from collections import defaultdict


class SingletonPerThread(type):
    _instances = defaultdict(dict)

    def __call__(cls, *args, **kwargs):
        id = str(threading.get_ident())
        if cls not in cls._instances[id]:
            cls._instances[id][cls] = super(SingletonPerThread, cls).__call__(*args, **kwargs)
        return cls._instances[id][cls]
