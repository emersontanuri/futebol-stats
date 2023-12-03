
def generate_auth():
    import json
    import os
    from dotenv import load_dotenv
    load_dotenv()
    
    if not os.path.exists('./auth/google/credentials.json'):
        with open('./auth/google/credentials.json', 'w') as auth_file:
            json.dump(
                {
                    "client_id": os.environ['CLIENT_ID'],
                    "client_secret": os.environ['CLIENT_SECRET'],
                    "refresh_token": os.environ['REFRESH_TOKEN'],
                    "type": "authorized_user"
                }, 
                auth_file
            )