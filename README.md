# Auto Class Launcher

Auto Class Launcher is a lightweight desktop tool that automatically opens upcoming online classes using Google Calendar integration.

The application detects scheduled classes, extracts Engageli meeting links, and launches them automatically in a selected Chrome profile.

## Features

* Google Calendar integration
* Automatic Engageli link detection
* Opens classes automatically at the correct time
* Supports specific Chrome profiles/accounts
* Local-only operation
* Lightweight and simple interface

## Privacy

This application only requests read-only access to Google Calendar.

The app:

* does not store passwords
* does not upload calendar data
* does not collect personal information
* does not use external servers

All data remains on the user's device.

## Google Permissions

The application only uses the following Google OAuth scope:

```text
https://www.googleapis.com/auth/calendar.readonly
```

This permission is used solely to read upcoming calendar events required for automatic class launching functionality.

## Installation

### Requirements

* Python 3.10+
* Google Chrome

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run

```bash
python main.py
```

## OAuth Setup

A valid `credentials.json` file from Google Cloud OAuth is required.
The valid `credentials.json` is provided and needed to be downloaded.

## Disclaimer

This project is an independent student/developer utility and is not affiliated with Google, Engageli, or any educational institution.
