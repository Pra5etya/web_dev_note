# mendeteksi berdasarkan nama mesin

import os
import socket

hostname = socket.gethostname()
print(hostname)

if "prod" in hostname:
    os.environ["FLASK_ENV"] = "production"

else:
    os.environ["FLASK_ENV"] = "development"
