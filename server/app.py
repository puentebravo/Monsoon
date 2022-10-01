from flask import Flask

def create_app(text_config=None):
    app = Flask(__name__)
    app.url_map.strict_slashes= False

    @app.route("/getWeather")
    def getWeather():
        response_body: dict = {
            "name": "Weather",
            "Temp": "It is 76F and sunny today"
        }

        return response_body

    @app.route("/")
    def home():
        return "<h1> Under development </h1>"

    return app





