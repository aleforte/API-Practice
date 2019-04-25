# Importing framework
from flask import Flask
import markdown
import os

# Create an instance of Flask
app = Flask(__name__)

@app.route("/")
def index():
    """Present some documentation"""

    with open(os.path.dirname(app.root_path) + '\\README.md', 'r') as markdown_file:
        # Read contents of file
        content = markdown_file.read()

        # Convert to HTML
        return markdown.markdown(content)



