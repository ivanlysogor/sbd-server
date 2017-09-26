import struct
import StringIO
import gzip

class IOTPayload(object):
    """Decompressing payload and preparing JSON"""

    @classmethod
    def decompress(cls, data):
        """Read data and decompress it"""

        out = StringIO.StringIO()
        with gzip.GunzipFile(fileobj=out, mode="w") as f:
          f.write(data)
        cls._value = out.getvalue()
    
    def __init__(self):
        self._value = None

    @property
    def value(self):
        return self._value
