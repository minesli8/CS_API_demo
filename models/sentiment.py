from flask_restful import reqparse, Resource
import requests


class sentiment_analyzer(Resource):

    def get(self):
        # argument parsing
        parser = reqparse.RequestParser()
        # parser.add_argument('query')
        parser.add_argument('query')

        args = parser.parse_args()
        user_input = args['query']

        article_url = user_input.strip()

        response = requests.get(article_url)

        content = response.text

        start = content.find('content=')

        partial_content = content[start: start+1000]

        output = {'partial_content': partial_content, 'url': article_url, 'Sentiment': 'Negative'}

        return output