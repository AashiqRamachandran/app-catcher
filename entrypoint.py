import json
from aianalysis import OpenAIAnalysis
from clearbit import Clearbit
from mailapi import email_entrypoint
import requests

config = json.load(
    open(
        "config.json",
        "r"
    )
)

openai_analysis = OpenAIAnalysis(api_key=config.get("openai_api_key"))
clearbit = Clearbit(config.get("clearbit_api_key"))


def enter():
    emails = email_entrypoint(
        lookback_time=config.get("lookback_time"),
        credentials_path=config.get("gmail_credentials_file")
    )
    for email in emails:
        response = saas_discovery_analysis(
            json.dumps(
                email
            )
        )
        print(response)
        webhook_request = requests.request(
            method=config.get(
                "webhook_method"
            ),
            url=config.get("webhook_url"),
            data=json.dumps(response),
            headers=config.get("webhook_headers")
        )
        print(f"Data sent to {config.get('webhook_url')}, with status {webhook_request.status_code}")


def saas_discovery_analysis(source_data: str):
    source_data = json.loads(source_data)
    source_email = None

    for email_item in source_data.get("payload", {}).get("headers", []):
        if email_item.get("name") == "From":
            source_email = email_item.get("value")

    source_email = source_email[source_email.find("<") + 1:source_email.find(">")]

    ai_analysis = openai_analysis.analyse(
        json.dumps(source_data), full_analysis=False
    )

    used_by_user = ai_analysis["used_by_user"]

    if not used_by_user:
        return {
            "status": True,
            "used_by_user": used_by_user
        }

    clearbit_response = clearbit.search_company(source_email)

    return {
        "status": True,
        "ai_analysis": ai_analysis,
        "company_info": clearbit_response,
        "used_by_user": True
    }


enter()
