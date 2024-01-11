import requests
import json


class GetRequester:

    # initialize method + instance var to accept any URL
    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        URL = self.url

        response = requests.get(URL)

        return response.content

    def load_json(self):
        json_content = json.loads(self.get_response_body())
        # data = json.dumps(json_content, indent=4, sort_keys=True)

        return json_content


get_requester = GetRequester(
    'https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json')
print(get_requester.load_json())
