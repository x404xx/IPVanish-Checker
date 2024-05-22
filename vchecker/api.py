import requests
from rich.traceback import install as traceback_install

traceback_install(theme="fruity")


class InvalidAccount(Exception):
    pass


class VanishChecker:
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.access_token = None
        self.base_headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0",
            "Accept": "*/*",
            "Accept-Language": "en-US,en;q=0.5",
            "Content-Type": "application/x-amz-json-1.1",
            "X-Amz-User-Agent": "aws-amplify/5.0.4 js",
            "Origin": "https://sso.ipvanish.com",
            "DNT": "1",
            "Connection": "keep-alive",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-site",
        }

    def __enter__(self):
        self.session = requests.Session()
        return self

    def __exit__(self, *_):
        self.session.close()

    def _make_request(self, target, json_data):
        headers = {**self.base_headers, "X-Amz-Target": target}
        response = self.session.post(
            "https://idp.sso.ipvanish.com/", headers=headers, json=json_data
        )
        response_json = response.json()
        if not response.ok:
            raise InvalidAccount(
                response_json.get("message", "Error processing request")
            )
        return response_json

    def initiate_auth(self):
        json_data = {
            "AuthFlow": "USER_PASSWORD_AUTH",
            "ClientId": "4ec6gq3ktcm5g5f2p134ot7qi2",
            "AuthParameters": {"USERNAME": self.email, "PASSWORD": self.password},
            "ClientMetadata": {},
        }
        response_json = self._make_request(
            "AWSCognitoIdentityProviderService.InitiateAuth", json_data
        )
        self.access_token = response_json.get("AuthenticationResult", {}).get(
            "AccessToken", ""
        )

    def get_user_info(self):
        json_data = {"AccessToken": self.access_token}
        return self._make_request(
            "AWSCognitoIdentityProviderService.GetUser", json_data
        )
