import requests
import base64
import json


class Clearbit:
    def __init__(self, api_key):
        b64_str = base64.b64encode(f"{api_key}:".encode()).decode()
        self.headers = {
            "Authorization": f"Basic {b64_str}"
        }

    def search_company(self, input: str):
        """
        Search for a company by domain/ email. Majorly email 
        :param input: domain or email
        """
        url = f"https://person-stream.clearbit.com/v2/combined/find?email={input}"
        response = requests.get(url, headers=self.headers)
        return {
            "company_name": response.json().get("company", {}).get("name", "NA"),
            "company_domain": response.json().get("company", {}).get("domain", "NA"),
            "company_description": response.json().get("company", {}).get("description", "NA"),
            "company_logo": response.json().get("company", {}).get("logo", "NA")
        }
