import sys
import os
from registry import app

# Create an instance of Flask
app.run(host='0.0.0.0', port='80', debug=True)
