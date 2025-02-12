import os
import requests
import json
print(os.environ)
# These are the credentials passed by the variables of your pipeline to your tasks and in to your env
CLIENT_ID = os.environ['PORT_CLIENT_ID']
CLIENT_SECRET = os.environ['PORT_CLIENT_SECRET']
REPO_NAME = os.environ['PORT_SERVICENAME']
BUILD = os.environ['BUILD_BUILDNUMBER']
PORT_API_URL = os.environ['PORT_API_URL']

credentials = {
    'clientId': CLIENT_ID,
    'clientSecret': CLIENT_SECRET
}
token_response = requests.post(f"{PORT_API_URL}/auth/access_token", json=credentials)
access_token = token_response.json()['accessToken']

headers = {
    'Authorization': f'Bearer {access_token}'
}

entity_json = {
        "identifier": REPO_NAME,
        "properties": {
          "build": BUILD
      }
}

# request url : {API_URL}/blueprints/<blueprint_id>/entities
create_response = requests.post(f'{PORT_API_URL}/blueprints/microservice/entities?upsert=true', json=entity_json, headers=headers)
print(json.dumps(create_response.json(), indent=4))
