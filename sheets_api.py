from __future__ import print_function
import pickle
import os.path
import os 
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request


def get_credentials():

    creds = None
    scope = ['https://www.googleapis.com/auth/spreadsheets']
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow  = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', scope)
            creds = flow.run_local_server(port=0)
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    return creds 


def add_row(credentials, company_name, role, job_type, method, date):

    creds           = credentials
    id              = '1PZglQmVU2Wkye2cjHqGito3Lis5HVxPyNFMa-sC64Gg'
    range           = 'apps!B2:G2'
    value_input_option = 'USER_ENTERED'
    application_row = {
        "majorDimension": "ROWS",
        "values": [
            [
                company_name, 
                role, 
                job_type, 
                method, 
                date, 
            ]
        ]
    }

    service            = build('sheets', 'v4', credentials=creds)

    sheet              = service.spreadsheets()
    request            = sheet.values().append(spreadsheetId=id,
                                    range=range,
                                    valueInputOption=value_input_option,
                                    body=application_row)

    response           = request.execute()


