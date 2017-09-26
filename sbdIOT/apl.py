import struct
import StringIO
import gzip

class IOTPayload(object):
    """Decompressing payload"""

    @classmethod
    def decompress(cls, data):
        """Read data and decompress it"""

        out = StringIO.StringIO()
        with gzip.GunzipFile(fileobj=out, mode="w") as f:
          f.write(data)
        payload = cls()
        payload._value = out.getvalue()
        return payload
    
    def __init__(self):
        self._value = None

    @property
    def value(self):
        return self._value
