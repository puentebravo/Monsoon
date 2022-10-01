from flask import Flask
from flask import request
from bots import huntsman

def create_app(text_config=None):
    app = Flask(__name__)
    app.url_map.strict_slashes= False

    @app.route("/api/getStock")
    def getStock():
        huntsman.Hunt(request.json.url)
        

    @app.route("/api/test")
    def testRoute():
        return "Server online and responding to requests."

    return app





