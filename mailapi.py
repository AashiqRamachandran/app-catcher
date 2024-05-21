import argparse
import json
import logging
import os

from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def get_google_service(client_secret_file, scopes):
    try:
        flow = InstalledAppFlow.from_client_secrets_file(client_secret_file, scopes)
        creds = flow.run_local_server(port=0)
        service = build('admin', 'directory_v1', credentials=creds)
        return service
    except Exception as e:
        logging.error(f"Failed to get Google service: {e}")
        exit(1)


def get_all_users(service, domain):
    users = []
    try:
        request = service.users().list(domain=domain, maxResults=500, orderBy='email', projection='full')
        while request is not None:
            response = request.execute()
            users.extend(response.get('users', []))
            request = service.users().list_next(previous_request=request, previous_response=response)
    except HttpError as error:
        logging.error(f"HTTP error occurred: {error}")
    except Exception as ex:
        logging.error(f"An error occurred: {ex}")
    return users


def email_entrypoint(client_secret_file, domain):
    scopes = ['https://www.googleapis.com/auth/admin.directory.user']
    service = get_google_service(client_secret_file, scopes)
    users = get_all_users(service, domain)

    if users:
        with open('user_details.json', 'w') as file:
            json.dump(users, file, indent=4)
        logging.info(f"Total users fetched: {len(users)}")
        logging.info("User details saved in 'user_details.json'.")
    else:
        logging.info('No users found.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Fetch and save Google Workspace user details.')
    parser.add_argument('--client_secret', help='Path to client secret JSON file', required=True)
    parser.add_argument('--domain', help='Google Workspace domain', required=True)
    args = parser.parse_args()

    email_entrypoint(args.client_secret, args.domain)
