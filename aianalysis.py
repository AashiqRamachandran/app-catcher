from openai import OpenAI
import json


class OpenAIAnalysis:
    def __init__(self, api_key: str) -> None:
        self.client = OpenAI(
            api_key=api_key
        )

    def analyse(self, analysis_input: str, full_analysis: bool = False):
        messages = [
            {
                "role": "system",
                "content": "You are a cyber security expert. Your primary expertise lies in email security and "
                           "analysing email meta content. I need"
                           "you to analyse an email metadata JSON and tell me if it comes from a SAAS application "
                           "provider or not."
            },
            {
                "role": "user",
                "content": "Analyse the following email metadata content and tell me if it comes from a SAAS "
                           "application upon the user"
                           "using the saas app (sign on notifications, "
                           "usage reports, login confirmations, registrations, post sign on marketing emails, "
                           "notification alerts etc.) or like a marketing email. Analyse both subject, and source "
                           "emails to get an answer"
                           "\n\n The response should be a valid JSON with the following "
                           "fields\n\n```\nused_by_user: Boolean value indicating if the software that is emailing "
                           "the user was used by the email or not (True for emails that look like - sign on notifications, "
                           "usage reports, login confirmations, registrations, post sign on marketing emails, "
                           "notification alerts etc.)"
                           "```\n\nIf you do not see any of "
                           "the above info, mark it as NA."
            },
            {
                "role": "user",
                "content": analysis_input
            }
        ]
        if full_analysis:
            messages = [
                {
                    "role": "system",
                    "content": "You are a cyber security expert. Your primary expertise lies in email security. I "
                               "need you to analyse an email metadata JSON and tell me if it comes from a SAAS "
                               "application provider or not."
                },
                {
                    "role": "user",
                    "content": "Analyse the following email metadata content and tell me if it comes from a SAAS application or "
                               "not.\n\nThe response should be a valid JSON with the following "
                               "fields\n\n```\ncompany_name: The name of the company sending the email\nsource_email: "
                               "The from email address\ntarget_email: The to email address\n\nused_by_user: Boolean "
                               "value indicating if the software that is emailing the user was used by the email or "
                               "not (True for mails like - sign in notifications, usage reports, login confirmations, "
                               "registrations etc.)```\n\nIf you do not see"
                               "any of the above info, mark it as NA."
                },
                {
                    "role": "user",
                    "content": analysis_input
                }
            ]
        print(messages)
        response = self.client.chat.completions.create(
            model="gpt-4o",
            messages=messages,
            temperature=0,
            max_tokens=4095,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            response_format={"type": "json_object"}
        )
        content = response.choices[0].message.content
        content = json.loads(content)
        response_content = {
            "company_name": content.get("company_name", "NA"),
            "source_email": content.get("source_email", "NA"),
            "target_email": content.get("target_email", "NA"),
            "used_by_user": content.get("used_by_user", "NA"),
            "full_analysis": full_analysis
        }
        return response_content
