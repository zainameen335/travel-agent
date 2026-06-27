import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = ["https://www.googleapis.com/auth/calendar.events"]


def get_calendar_service():
    creds = None

    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file(
            "token.json",
            SCOPES
        )

    if not creds or not creds.valid:

        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())

        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "credentials.json",
                SCOPES
            )

            creds = flow.run_local_server(port=0)

        with open("token.json", "w") as token:
            token.write(creds.to_json())

    service = build(
        "calendar",
        "v3",
        credentials=creds
    )

    return service


def create_calendar_event(destination, dates, travelers, start_date, end_date):
    service = get_calendar_service()

    event = {
        "summary": f"Trip to {destination}",
        "location": destination,
        "description": f"Trip created by AI Travel Agent\nTravelers: {travelers}\nDates: {dates}",

        # temporary hardcoded dates, we will parse real dates next
        "start": {
            "date": start_date,
            "timeZone": "Asia/Karachi",
        },

        "end": {
            "date": end_date,
            "timeZone": "Asia/Karachi",
        },
    }

    created_event = service.events().insert(
        calendarId="primary",
        body=event
    ).execute()

    return created_event.get("htmlLink")