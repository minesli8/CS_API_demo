from flask import Flask, render_template, url_for
from flask_restful import abort, Api
from models.sentiment import sentiment_analyzer

app = Flask(__name__)
api = Api(app)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/info')
def info():
    return render_template('info.html')


# # argument parsing
# parser = reqparse.RequestParser()
# # parser.add_argument('query')
# parser.add_argument('words')

# Setup the Api resource routing here
# Route the URL to the resource
api.add_resource(sentiment_analyzer, '/sentiment')


if __name__ == '__main__':
    app.run(debug=True)
