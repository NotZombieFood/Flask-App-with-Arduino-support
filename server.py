#!/usr/bin/python3
from app import app

import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
print("Tu dirección IP para conectarte a la aplicación es la siguiente")
print(s.getsockname()[0])
s.close()

app.run(debug=True, host='0.0.0.0', port=80)

