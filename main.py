# pip install textual google-auth google-auth-oauthlib google-api-python-client

from textual.app import App, ComposeResult
from textual.containers import Vertical
from textual.widgets import Header, Footer, Button, Static

import os

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build


# =========================
# GOOGLE CONFIG
# =========================
SCOPES = ["https://www.googleapis.com/auth/calendar.readonly"]


# =========================
# GOOGLE LOGIN
# =========================
def connect_google():
    creds = None

    # Load existing token
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file(
            "token.json",
            SCOPES
        )

    # Login if needed
    if not creds or not creds.valid:

        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())

        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "credentials.json",
                SCOPES
            )

            # Opens browser automatically
            creds = flow.run_local_server(port=0)

        # Save token
        with open("token.json", "w") as token:
            token.write(creds.to_json())

    # Build calendar service
    service = build("calendar", "v3", credentials=creds)

    return service


# =========================
# TUI APP
# =========================
class CalendarApp(App):

    CSS = """
    Screen {
        align: center middle;
    }

    #container {
        width: 60;
        height: 20;
        border: round white;
        padding: 1 2;
    }

    Button {
        width: 100%;
        margin-top: 1;
    }

    #status {
        margin-top: 2;
    }
    """

    def compose(self) -> ComposeResult:
        yield Header()

        with Vertical(id="container"):
            yield Static(
                "Auto Class Launcher\n\n"
                "Connect your Google Calendar account.",
                id="title"
            )

            yield Button(
                "Login with Google",
                id="login_btn"
            )

            yield Static(
                "Not Connected",
                id="status"
            )

        yield Footer()

    async def on_button_pressed(self, event: Button.Pressed):

        if event.button.id == "login_btn":

            status = self.query_one("#status", Static)

            status.update("Opening browser for Google login...")

            try:
                service = connect_google()

                # Test calendar access
                calendar = service.calendarList().list().execute()

                count = len(calendar.get("items", []))

                status.update(
                    f"Connected successfully.\n"
                    f"Detected {count} calendar(s)."
                )

            except Exception as e:
                status.update(
                    f"Login failed:\n{e}"
                )


# =========================
# MAIN
# =========================
if __name__ == "__main__":
    CalendarApp().run()